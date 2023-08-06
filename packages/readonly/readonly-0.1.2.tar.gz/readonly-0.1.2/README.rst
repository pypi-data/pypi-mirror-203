=========
readonly
=========

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://github.com/wiseaidev/readonly/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/pypi/v/readonly.svg
   :target: https://pypi.org/project/readonly/
   :alt: pypi version

.. image:: https://img.shields.io/github/repo-size/wiseaidev/readonly
   :target: https://github.com/wiseaidev/readonly/
   :alt: Repo Size

.. image:: https://circleci.com/gh/wiseaidev/readonly/tree/main.svg?style=svg
   :target: https://circleci.com/gh/wiseaidev/readonly/tree/main
   :alt: Circle ci Build Status

**readonly** is a simple package to make any given module attributes into read only mode. 

🛠️ Requirements
---------------

**readonly** requires Python 3.9 or above.

To install Python 3.9, I recommend using `pyenv`_.

.. code-block:: bash

   # install pyenv
   git clone https://github.com/pyenv/pyenv ~/.pyenv

   # setup pyenv (you should also put these three lines in .bashrc or similar)
   # if you are using zsh
   cat << EOF >> ~/.zshrc
   # pyenv config
   export PATH="${HOME}/.pyenv/bin:${PATH}"
   export PYENV_ROOT="${HOME}/.pyenv"
   eval "$(pyenv init -)"
   EOF

   # or if you using the default bash shell, do this instead:
   cat << EOF >> ~/.bashrc
   # pyenv config
   export PATH="${HOME}/.pyenv/bin:${PATH}"
   export PYENV_ROOT="${HOME}/.pyenv"
   eval "$(pyenv init -)"
   EOF
   # Close and open a new shell session
   # install Python 3.9.10
   pyenv install 3.9.10

   # make it available globally
   pyenv global system 3.9.10


To manage the Python 3.9 virtualenv, I recommend using `poetry`_.

.. code-block:: bash

   # install poetry
   curl -sSL https://install.python-poetry.org | python3 -
   poetry --version
   Poetry version 1.1.13

   # Having the python executable in your PATH, you can use it:
   poetry env use 3.9.10

   # However, you are most likely to get the following issue:
   Creating virtualenv readonly-dxc671ba-py3.9 in ~/.cache/pypoetry/virtualenvs

   ModuleNotFoundError

   No module named 'virtualenv.seed.via_app_data'

   at <frozen importlib._bootstrap>:973 in _find_and_load_unlocked

   # To resolve it, you need to reinstall virtualenv through pip
   sudo apt remove --purge python3-virtualenv virtualenv
   python3 -m pip install -U virtualenv

   # Now, you can just use the minor Python version in this case:
   poetry env use 3.9.10
   Using virtualenv: ~/.cache/pypoetry/virtualenvs/readonly-dxc671ba-py3.9


🚨 Installation
---------------

With :code:`pip`:

.. code-block:: console

   python3.9 -m pip install readonly


🚸 Usage
--------

.. code-block:: python3

   >>> from readonly import readonly
   >>> import math
   >>> math = readonly(math)

   # raises AttributeError
   >>> math.pi = 3.0

🎉 Credits
----------

The following projects were used to build and test :code:`readonly`.

- `python`_
- `poetry`_
- `pytest`_
- `flake8`_
- `coverage`_
- `rstcheck`_
- `mypy`_
- `pytestcov`_
- `tox`_
- `isort`_
- `black`_
- `precommit`_


👋 Contribute
-------------

If you are looking for a way to contribute to the project, please refer to the `Guideline`_.

📝 License
----------

This program and the accompanying materials are made available under the terms and conditions of the `GNU GENERAL PUBLIC LICENSE`_.

.. _GNU GENERAL PUBLIC LICENSE: http://www.gnu.org/licenses/
.. _readonly: https://pypi.org/project/readonly/
.. _Marco Sulla: https://github.com/Marco-Sulla
.. _Guideline: https://github.com/wiseaidev/readonly/blob/main/CONTRIBUTING.rst
.. _pyenv: https://github.com/pyenv/pyenv
.. _poetry: https://github.com/python-poetry/poetry
.. _pipx: https://github.com/pypa/pipx
.. _python: https://www.python.org/
.. _pytest: https://docs.pytest.org/en/7.1.x/
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _coverage: https://coverage.readthedocs.io/en/6.3.2/
.. _rstcheck: https://pypi.org/project/rstcheck/
.. _mypy: https://mypy.readthedocs.io/en/stable/
.. _pytestcov: https://pytest-cov.readthedocs.io/en/latest/
.. _tox: https://tox.wiki/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _black: https://black.readthedocs.io/en/stable/
.. _precommit: https://pre-commit.com/
