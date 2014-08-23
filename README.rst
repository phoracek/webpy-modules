web.py modules
==============

Optional extensions for web.py framework.

Install
-------

Use pip:

::

    pip install web.py-modules

or do it manualy:

::

    wget https://github.com/PetrHoracek/webpy-modules/archive/v0.1.tar.gz
    tar -zxvf web.py-modules-v0.1.tar.gz
    cd web.py-modules-v0.1
    python setup.py install

or just download package and paste ``webmod`` folder into your project.


Usage
-----

This package contains independent modules which you can import to your project.
Of course it's dependent on web.py package.

.. code:: python

    import webmod
    from webmod import modulename, othermodulename


You can find details in docs.

- ``auth`` - handles basic requirements for users and access rights management.
