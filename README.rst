wolfe
=====

.. image:: http://badge.kloud51.com/pypi/v/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Version
    
.. image:: http://badge.kloud51.com/pypi/s/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Status

.. image:: http://badge.kloud51.com/pypi/w/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Wheel

.. image:: http://badge.kloud51.com/pypi/l/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI License

.. image:: http://badge.kloud51.com/pypi/f/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Format

.. image:: http://badge.kloud51.com/pypi/p/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Py_versions

.. image:: http://badge.kloud51.com/pypi/d/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Downloads

.. image:: http://badge.kloud51.com/pypi/i/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Implementation

.. image:: http://badge.kloud51.com/pypi/e/wolfe.svg
    :target: https://pypi.python.org/pypi/wolfe
    :alt: PyPI Egg

|image0|

🐺 i am winston wolfe, i solve problems

Demo
----

|image1|

Features
--------

-  Written in Python
-  Uses the stackoverflow api.
-  You need bash for it too work.

Installation
------------

1: `PIP`_
~~~~~~~~~

.. code:: bash

    $ pip install wolfe

2: From Source
~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/h4ck3rk3y/wolfe 
    $ cd wolfe/
    $ python setup.py install

Usage
-----

Ask Mr. Wolfe to record errors, ask politely
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ wolfe on

Ask him to solve the last problem you faced via stackoverflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ wolfe $l

Ask him to solve the last problem you faced via google
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ wolfe $l --google

Tell him his services aren’t needed any more
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ wolfe off

Help
~~~~

.. code:: bash

    $ wolfe --help

Note
~~~~

Mr. Wolfe edits your ``.bashrc`` and stores a copy of the original
``.bashrc`` file in ``~/.bashrc.bak``, every time the ``wolfe on``
command is run.

If your terminal is messed up do ``cp ~/.bashrc.bak ~/.bashrc``

| Mr. Wolfe doesn’t change ``.bashrc`` when the terminal is exited, do
  ``wolfe off``
| to undo the changes to the ``.bashrc`` file.

Contributing
------------

Use the `issue tracker`_ to file bugs or push new features.

License
-------

Open sourced under the **MIT License**

.. _PIP: https://pypi.python.org/pypi/wolfe
.. _issue tracker: https://github.com/h4ck3rk3y/wolfe/issues

.. |image0| image:: http://i.imgur.com/ffMQrWB.png
.. |image1| image:: http://i.imgur.com/L6lXDyG.gif?1
