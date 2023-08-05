========
Overview
========

Client library for IdealSpot's Geodata API.

* Free software: Apache Software License 2.0

Installation
============

::

    pip install idealgeo

You can also install the in-development version with::

    pip install https://gitlab.com/jbwinters/python-idealgeo/-/archive/main/python-idealgeo-main.zip


Documentation
=============


https://python-idealgeo.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
