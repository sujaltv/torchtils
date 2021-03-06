.. Torchtils documentation master file, created by
   sphinx-quickstart on Sat Jun  6 00:51:30 2020. You can adapt this file
   completely to your liking, but it should at least contain the root `toctree`
   directive.

Torchtils
#########

Torchtils is a utility library of implementation of algorithms and research
papers in `PyTorch <https://pytorch.org/>`_.

Installation
------------

* Installing from the `Python Package Index registry <https://pypi.org/project/torchtils/>`_:

  .. code-block:: bash

    pip install torchtils

* Installing from `source <https://github.com/sujaltv/torchtils>`_:

  .. code-block:: bash

    git clone https://github.com/sujaltv/torchtils.git
    cd torchtils
    pip install .

Implementation
---------------

.. toctree::
  :maxdepth: 1

  of

.. toctree::
  :maxdepth: 1

  torchtils.poisson_image_editing

.. toctree::
  :maxdepth: 1

  torchtils.tts_synthesis

Contribution
############

Clone the source:

.. code-block:: bash

  git clone https://github.com/sujaltv/torchtils.git

Instal ``pip`` packages:

.. code-block:: bash

  pip install -r requirements.txt

Building this documentation:

.. code-block:: bash

  pip install sphinx sphinx_theme sphinx-autobuild
  sh build_docs.sh

Note
----

Due to a bug, the build fails to hyperlink documents on search. To fix it, upon
building this documentation, replace ``DOCUMENTATION_OPTIONS.LINK_SUFFIX`` to
``DOCUMENTATION_OPTIONS.FILE_SUFFIX`` in
``docs/_build/html/static/searchtools.js``.

Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`

.. :ref:`search`