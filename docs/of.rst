Optical flow
------------

Consider two successive image frames :math:`\mathcal{I}_t` and
:math:`\mathcal{I}_{t+1}` captured with moving light source over
time. The velocity of the light source, assuming that the intensity of the
source remains constant, can be computed by differentiating the image over time.
That is,

.. math::
  \mathbf{v} = \mathcal{I}_t = \frac{d\mathcal{I}}{dt} =
    \begin{bmatrix}
      \frac{\partial{\mathcal{I}}}{\partial{x}}\cdot\frac{\partial{x}}
      {\partial{t}}\\
      \frac{\partial{\mathcal{I}}}{\partial{y}}\cdot\frac{\partial{y}}
      {\partial{t}}
    \end{bmatrix}
    = \begin{bmatrix}v_x\\ v_y,\end{bmatrix}

where, for any pixel location :math:`(i, j)`,

.. math::
  v_x(i, j) = \mathcal{I}_{t + 1}(i, j) - \mathcal{I}_t(i-1, j) \\
  v_y(i, j) = \mathcal{I}_{t + 1}(i, j) - \mathcal{I}_t(i, j-1)

For a given frame :math:`\mathcal{I}`, let its partial, spatial differentials be
:math:`\mathcal{I}_x = \frac{\partial\mathcal{I}}{\partial{x}}` and
:math:`\mathcal{I}_y = \frac{\partial\mathcal{I}}{\partial{y}}`. More precisely,
for a given pixel :math:`(i, j)`,

.. math::
  \mathcal{I}_x(i, j) = \mathcal{I}(i+1, j) - \mathcal{I}(i-1, j)\\
  \mathcal{I}_y(i, j) = \mathcal{I}(i, j+1) - \mathcal{I}(i, j-1)

Given this setup, it can be noted that

.. math::
  \mathcal{I}(x + v_xdt, y + v_ydt, t + dt) = \mathcal{I}(x, y, t)

This decomposes into its subcomponents with Taylor Series expansion as

.. math::
  \mathcal{I}(x, y, t) + \mathcal{I}_xv_xdt + \mathcal{I}_yv_ydt + \mathcal{I}_t
  dt + \rm{higher~order~terms} &= \mathcal{I}(x, y, t)\\
  \mathcal{I}(x, y, t) + \mathcal{I}_xv_xdt + \mathcal{I}_yv_ydt + \mathcal{I}_t
  dt &\approx \mathcal{I}(x, y, t)\\
  \mathcal{I}_xv_x + \mathcal{I}_yv_y + \mathcal{I}_t &= 0\\
  \nabla\mathcal{I}^\top\mathbf{v} + \mathcal{I}_t &= 0\\

where :math:`\nabla\mathcal{I} = \begin{bmatrix}\mathcal{I}_x\\\mathcal{I}_y
\end{bmatrix}`. However, the resulting equation, :math:`\nabla\mathcal{I}^\top
\mathbf{v} + \mathcal{I}_t = 0`, known as *optical flow constraint equation*, is
that of two unknown variables :math:`v_x` and :math:`v_y` and hence cannot be
solved. This is know as the *aperture problem*.


Methods
=======

.. toctree::
  :maxdepth: 1

  optical_flow