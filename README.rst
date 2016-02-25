wolfe
=====

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

    $ git clone https://github.com/Zephrys/wolfe
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
.. _issue tracker: https://github.com/h4ck3rk3y/wolfe

.. |image0| image:: http://i.imgur.com/ffMQrWB.png
.. |image1| image:: http://i.imgur.com/L6lXDyG.gif?1