Horn-Schunck
===================

A global method for *Determining Optical Flow* was proposed by Berthold Horn and
Brian Schunck [HS81]_. The Horn-Schunck method of optical
flow detection begins with the fact that optical flow cannot be computed
locally. It further makes the assumption that optical flow is smooth. This
assumption can be summed up symbolically as :math:`\int{\int{\Vert\nabla{v_x}
\Vert^2 + \Vert\nabla{v_x}\Vert^2}} dx dy = 0`. However, this ideal case many
not be realistic; any deviation from the sum's vanishing is treated as spatial
error, :math:`e_s`:

.. math::
  e_s = \int{\int{\Vert\nabla{v_x} \Vert^2 + \Vert\nabla{v_x}\Vert^2}} dx dy

Similarly, any violation of the optical flow constraint is treated as chromatic
error, :math:`e_c`:

.. math::
  e_c = \int{\int{\left(\nabla{\mathcal{I}}^\top\mathbf{v} +
    \mathcal{I}_t\right)^2}} dx dy

The total error, :math:`e`, is the sum of the two:

.. math::
  e &= e_s + \lambda e_c\\
    &= \int{\int{\Vert\nabla{v_x} \Vert^2 + \Vert\nabla{v_x}\Vert^2}} +
      \lambda\left(\nabla{\mathcal{I}}^\top\mathbf{v} + \mathcal{I}_t\right)^2
      dx dy\\
    &= \sum_{i}{\sum_{j}{\Vert\nabla{v_x}(i,j) \Vert^2 + \Vert\nabla{v_x}(i, j)
      \Vert^2}} +\lambda\left(\nabla{\mathcal{I}}^\top(i, j)\mathbf{v}(i, j) +
      \mathcal{I}_t(i, j)\right)^2

The goal is to minimise this error:

.. math::
  \DeclareMathOperator*{\argmin}{arg\,min}
  E = \argmin{e}

Hence, we differentiate :math:`E` and set it to :math:`0`.

.. math::
  \frac{dE}{\partial{v_x}\partial{v_y}} &= 0\\
  \frac{\partial{E}}{\partial{v_x}} = 0, \frac{\partial{E}}{\partial{v_y}} &=
  0\\
  2\left(\mathcal{I}_xv_x(i,j) + \mathcal{I}_yv_y(i,j) + \mathcal{I}_t\right)
  \mathcal{I}_x + 2\lambda\left(v_x(i,j) - \bar{v}_x(i,j)\right) &= 0,\\
  2\left(\mathcal{I}_xv_x(i,j) + \mathcal{I}_yv_y(i,j) + \mathcal{I}_t\right)
  \mathcal{I}_y + 2\lambda\left(v_y(i,j) - \bar{v}_y(i,j)\right) &= 0\\

where :math:`\bar{v}_x` and :math:`\bar{v}_y` are local averages of :math:`v_x`
and :math:`v_y`, respectively. Therefore,

.. math::
  \left(\lambda + \mathcal{I}_x^2\right)v_x + \mathcal{I}_x\mathcal{I}_yv_y &=
  \lambda\bar{v}_x - \mathcal{I}_x\mathcal{I}_t\\
  \mathcal{I}_x\mathcal{I}_yv_x + \left(\lambda + \mathcal{I}_y^2\right)v_y &=
  \lambda\bar{v}_y - \mathcal{I}_y\mathcal{I}_t

Iteratively,

.. math::
  v_x^{m + 1} &= \bar{v}_x^m - \left[\frac{\mathcal{I}_x\bar{v}_x^m + \mathcal{I}_y\bar{v}_y^m + \mathcal{I}_t}{\lambda+\mathcal{I}_x^2 + \mathcal{I}_y^2}\right]\mathcal{I}_x\\
  v_y^{m + 1} &= \bar{v}_y^m - \left[\frac{\mathcal{I}_x\bar{v}_x^m + \mathcal{I}_y\bar{v}_y^m + \mathcal{I}_t}{\lambda+\mathcal{I}_x^2 + \mathcal{I}_y^2}\right]\mathcal{I}_y

Thus,

.. math::
  \mathbf{v}^{m+1} = \mathbf{v}^m - \alpha(\nabla\mathcal{I})

Implementation
--------------

.. automodule:: modules.optical_flow.horn_schunck
  :members:
  :undoc-members:
  :show-inheritance:

Lucas-Kanade
===================

.. automodule:: modules.optical_flow.lucas_kanade
  :members:
  :undoc-members:
  :show-inheritance:

References
==========

.. [HS81]  Berthold K. P. Horn and Brian G. Rhunck: "*Determining Optical
    Flow*", 1981