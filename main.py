import os
import cv2

from modules.optical_flow.horn_schunck import HornSchunck

def show_video(path, write_frames=False, output_dir=None):
  """
  This method shows the video
  """
  w = 10
  h = HornSchunck(w=w, k=5, l = 1)
  # h0 = HornSchunck.read_img('./output/frame_50.png')
  # h1 = HornSchunck.read_img('./output/frame_51.png')

  assert os.path.isfile(path)

  if write_frames:
    assert output_dir is not None and os.path.isdir(output_dir)

  stream = cv2.VideoCapture(path)

  old_frame = None
  new_frame = None

  frame_number = 0

  while True:
    old_frame = new_frame
    status, new_frame = stream.read()
    
    if status is False:
      break

    new_frame = cv2.resize(cv2.flip(new_frame, 90), (480, 200))
    new_frame = HornSchunck.format_img(new_frame)

    if old_frame is None:
      old_frame = new_frame

    a, output = h(old_frame, new_frame, True)
    
    if write_frames is True:
      print(os.path.join(output_dir, f'frame_{frame_number}.png'))
      cv2.imwrite(
        os.path.join(output_dir, f'frame_{frame_number}.png'),
        new_frame
      )
      frame_number += 1

    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break


  stream.release()
  cv2.destroyAllWindows()

# show_video('./input/imm.mov')
# show_video('./input/im.mp4', True, './output')