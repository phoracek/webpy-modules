web.py modules
=============

Optional extensions for web.py framework.

Install
-------

Use pip:

::
    
    pip install web.py-modules

or do it manualy:

::

    wget http://pypi.python.org/packages/source/p/pip/web.py-modules-0.1.tar.gz
    tar -zxvf web.py-modules-0.1.tar.gz
    cd web.py-modules-0.1
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

Auth
````
Auth module handles basic requirements for users and access rights management. 
