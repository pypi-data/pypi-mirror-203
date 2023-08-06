# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['readonly']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'readonly',
    'version': '0.1.2',
    'description': 'Make any module attributes read only.',
    'long_description': '=========\nreadonly\n=========\n\n.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg\n   :target: https://github.com/wiseaidev/readonly/blob/main/LICENSE\n   :alt: License\n\n.. image:: https://img.shields.io/pypi/v/readonly.svg\n   :target: https://pypi.org/project/readonly/\n   :alt: pypi version\n\n.. image:: https://img.shields.io/github/repo-size/wiseaidev/readonly\n   :target: https://github.com/wiseaidev/readonly/\n   :alt: Repo Size\n\n.. image:: https://circleci.com/gh/wiseaidev/readonly/tree/main.svg?style=svg\n   :target: https://circleci.com/gh/wiseaidev/readonly/tree/main\n   :alt: Circle ci Build Status\n\n**readonly** is a simple package to make any given module attributes into read only mode. \n\n🛠️ Requirements\n---------------\n\n**readonly** requires Python 3.9 or above.\n\nTo install Python 3.9, I recommend using `pyenv`_.\n\n.. code-block:: bash\n\n   # install pyenv\n   git clone https://github.com/pyenv/pyenv ~/.pyenv\n\n   # setup pyenv (you should also put these three lines in .bashrc or similar)\n   # if you are using zsh\n   cat << EOF >> ~/.zshrc\n   # pyenv config\n   export PATH="${HOME}/.pyenv/bin:${PATH}"\n   export PYENV_ROOT="${HOME}/.pyenv"\n   eval "$(pyenv init -)"\n   EOF\n\n   # or if you using the default bash shell, do this instead:\n   cat << EOF >> ~/.bashrc\n   # pyenv config\n   export PATH="${HOME}/.pyenv/bin:${PATH}"\n   export PYENV_ROOT="${HOME}/.pyenv"\n   eval "$(pyenv init -)"\n   EOF\n   # Close and open a new shell session\n   # install Python 3.9.10\n   pyenv install 3.9.10\n\n   # make it available globally\n   pyenv global system 3.9.10\n\n\nTo manage the Python 3.9 virtualenv, I recommend using `poetry`_.\n\n.. code-block:: bash\n\n   # install poetry\n   curl -sSL https://install.python-poetry.org | python3 -\n   poetry --version\n   Poetry version 1.1.13\n\n   # Having the python executable in your PATH, you can use it:\n   poetry env use 3.9.10\n\n   # However, you are most likely to get the following issue:\n   Creating virtualenv readonly-dxc671ba-py3.9 in ~/.cache/pypoetry/virtualenvs\n\n   ModuleNotFoundError\n\n   No module named \'virtualenv.seed.via_app_data\'\n\n   at <frozen importlib._bootstrap>:973 in _find_and_load_unlocked\n\n   # To resolve it, you need to reinstall virtualenv through pip\n   sudo apt remove --purge python3-virtualenv virtualenv\n   python3 -m pip install -U virtualenv\n\n   # Now, you can just use the minor Python version in this case:\n   poetry env use 3.9.10\n   Using virtualenv: ~/.cache/pypoetry/virtualenvs/readonly-dxc671ba-py3.9\n\n\n🚨 Installation\n---------------\n\nWith :code:`pip`:\n\n.. code-block:: console\n\n   python3.9 -m pip install readonly\n\n\n🚸 Usage\n--------\n\n.. code-block:: python3\n\n   >>> from readonly import readonly\n   >>> import math\n   >>> math = readonly(math)\n\n   # raises AttributeError\n   >>> math.pi = 3.0\n\n🎉 Credits\n----------\n\nThe following projects were used to build and test :code:`readonly`.\n\n- `python`_\n- `poetry`_\n- `pytest`_\n- `flake8`_\n- `coverage`_\n- `rstcheck`_\n- `mypy`_\n- `pytestcov`_\n- `tox`_\n- `isort`_\n- `black`_\n- `precommit`_\n\n\n👋 Contribute\n-------------\n\nIf you are looking for a way to contribute to the project, please refer to the `Guideline`_.\n\n📝 License\n----------\n\nThis program and the accompanying materials are made available under the terms and conditions of the `GNU GENERAL PUBLIC LICENSE`_.\n\n.. _GNU GENERAL PUBLIC LICENSE: http://www.gnu.org/licenses/\n.. _readonly: https://pypi.org/project/readonly/\n.. _Marco Sulla: https://github.com/Marco-Sulla\n.. _Guideline: https://github.com/wiseaidev/readonly/blob/main/CONTRIBUTING.rst\n.. _pyenv: https://github.com/pyenv/pyenv\n.. _poetry: https://github.com/python-poetry/poetry\n.. _pipx: https://github.com/pypa/pipx\n.. _python: https://www.python.org/\n.. _pytest: https://docs.pytest.org/en/7.1.x/\n.. _flake8: https://flake8.pycqa.org/en/latest/\n.. _coverage: https://coverage.readthedocs.io/en/6.3.2/\n.. _rstcheck: https://pypi.org/project/rstcheck/\n.. _mypy: https://mypy.readthedocs.io/en/stable/\n.. _pytestcov: https://pytest-cov.readthedocs.io/en/latest/\n.. _tox: https://tox.wiki/en/latest/\n.. _isort: https://github.com/PyCQA/isort\n.. _black: https://black.readthedocs.io/en/stable/\n.. _precommit: https://pre-commit.com/\n',
    'author': 'Mahmoud Harmouch',
    'author_email': 'business@wiseai.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wiseaidev/readonly',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
