import cv2
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch import Tensor
from torchvision import transforms
from matplotlib import pyplot as plt


class HornSchunck(nn.Module):
    """The `HornSchunck` class encapsulates utility and implementation methods
    for optical flow detection with the Horn-Schunck method.

    :param k: Number of iterations until optimisation (default 5)
    :type k: int?
    
    :param alpha: Tuning factor (default 10)
    :type alpha: int?
    
    :param w: Averaging window size (default 10)
    :type w: int?
    """

    transformer = transforms.Compose([
        transforms.ToTensor()
    ])

    def __init__(self, k=5, alpha=10, w=10):       
        super(HornSchunck, self).__init__()
        self.k = k
        self.alpha = alpha
        self.w = w

        self.dx = nn.Conv2d(1, 1, (1,3), 1,  bias=False)
        self.dx.weight = nn.Parameter(Tensor([[[[-1, 0, 1]]]]), False)
        
        self.dy = nn.Conv2d(1, 1, (3,1), 1, bias=False)
        self.dy.weight = nn.Parameter(Tensor([[[[-1], [0], [1]]]]), False)

        h = nn.Conv2d(1, 1, (1, 2), 1, bias=False)
        h.weight = nn.Parameter(Tensor([[[[-1, 1]]]]))
        self.velocity_x0 = nn.Sequential(nn.ReplicationPad2d((1, 0, 0, 0)), h)
        self.velocity_x1 = nn.Sequential(nn.ReplicationPad2d((0, 1, 0, 0)), h)

        v = nn.Conv2d(1, 1, (2, 1), 1, bias=False)
        v.weight = nn.Parameter(Tensor([[[[-1], [1]]]]))
        self.velocity_y0 = nn.Sequential(nn.ReplicationPad2d((0, 0, 1, 0)), v)
        self.velocity_y1 = nn.Sequential(nn.ReplicationPad2d((0, 0, 0, 1)), v)
    
    def forward(self, x, y, verbose=False):
        """Sample forward summary

        Args:
            x (torch.Tensor): Image frame at `t`
            y (torch.Tensor): Image frame at time `t + 1`
            verbose (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """        

        assert x is not None and y is not None
        assert x.shape == y.shape
        
        Ix = self.dx(F.pad(x, (1, 1, 0, 0), mode='constant', value=0))
        Iy = self.dy(F.pad(y, (0, 0, 1, 1), mode='constant', value=0))

        a = F.pad(x, (0, 1, 0, 0), mode='constant', value=0)
        b = F.pad(y, (1, 0, 0, 0), mode='constant', value=0)
        vx = (a - b)[:,:,:,:-1]
        
        c = F.pad(x, (0, 0, 0, 1), mode='constant', value=0)
        d = F.pad(y, (0, 0, 1, 0), mode='constant', value=0)
        vy = (c - d)[:,:,:-1,:]


        Ixy = self.alpha + torch.square(Ix) + torch.square(Iy)
        It = y - x

        for _ in range(self.k):
            vx = (1/4) * (\
                torch.square(self.velocity_x0(vx)) +\
                torch.square(self.velocity_x1(vx)) +\
                torch.square(self.velocity_y0(vx)) +\
                torch.square(self.velocity_y1(vx))
            )

            
            vy = (1/4) * (\
                torch.square(self.velocity_y0(vy)) +\
                torch.square(self.velocity_y1(vy)) +\
                torch.square(self.velocity_x0(vy)) +\
                torch.square(self.velocity_x1(vy))
            )

            coeff = Ix * vx + Iy * vy + It
            coeff = coeff / Ixy

            vx = vx - coeff * Ix
            vy = vy - coeff * Iy
        
        w = self.w
        vx = nn.MaxPool2d((w, w), (w, w))(vx)
        vy = nn.MaxPool2d((w, w), (w, w))(vy)

        v = torch.cat([vx, vy], 1)

        frame = None
        if verbose is True:
          frame = self.show_output(x, v)
        
        return v, frame
    
    @staticmethod
    def read_img(img_path):
        frame = cv2.imread(img_path)
        return HornSchunck.format_img(frame)
    
    @staticmethod
    def format_img(frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = HornSchunck.transformer(image)
        image = image[None]
        return image

    def show_output(self, img, a):
        """Display a sample output

        :param img: The image on which to display optical flow
        :type img: torch.Tensor
        """        

        a = a.detach().squeeze().permute((1, 2, 0))

        r, c, _ = a.shape
        w = self.w

        img = img.squeeze().numpy()
        for i in range(r):
            for j in range(c):
                cv2.arrowedLine(img, (j * w + w // 2, i * w + w // 2),
                    (j * w + a[i][j][0] * w + w // 2,
                        i * w + a[i][j][1] * w + w // 2), (0,0,255), 2)

        return img
