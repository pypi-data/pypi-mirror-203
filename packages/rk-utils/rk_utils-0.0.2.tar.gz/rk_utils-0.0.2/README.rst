.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/rk_utils.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/rk_utils
    .. image:: https://readthedocs.org/projects/rk_utils/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://rk_utils.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/rk_utils/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/rk_utils
    .. image:: https://img.shields.io/pypi/v/rk_utils.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/rk_utils/
    .. image:: https://img.shields.io/conda/vn/conda-forge/rk_utils.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/rk_utils
    .. image:: https://pepy.tech/badge/rk_utils/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/rk_utils
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/rk_utils

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

========
rk_utils
========


    Some useful Python utilities made by RKWS.


A longer description of your project goes here...


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

For developers, extra requirements are in `requirements_dev.txt`::

    cd rk_utils
    pip install -r requirements_dev.txt

This project uses `pre-commit`_, and it is a good idea to update the hooks to
the latest version before installing::

    cd rk_utils
    pre-commit autoupdate
    pre-commit install

.. _pre-commit: https://pre-commit.com/

There are some useful `tox`_ commands that can be used to simplify developing::

    cd rk_utils
    tox  # to run all the tests
    tox -e docs  # to build your documentation
    tox -e build  # to build your package distribution
    tox -e publish  # to test your project uploads correctly in test.pypi.org
    tox -e publish -- --repository pypi  # to release your package to PyPI
    tox -av  # to list all the tasks available

.. _tox: https://tox.readthedocs.io/

Note
====

This project has been set up using PyScaffold 4.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
