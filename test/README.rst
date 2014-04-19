# web.py modules unit tests

## Setup

All databases expect a database with name ``webpy`` with username ``scott`` and password ``tiger``.

## Running all tests

To run all tests:

::

    $ python test/alltests.py

## Running individual tests

To run all tests in a file:

::

    $ python test/auth.py

To run all tests in a class:

::

    $ python test/auth.py AuthTest

To run a single test:

::

    $ python test/auth.py AuthTest.testLogin
