# cookiecutter-cdk

use this cookiecutter project to create a new project from the template


## Usage

```bash
cookiecutter gh:imprivata-cloud/cookiecutter-cdk
full_name [Nate Marks]: 
email [nmarks@imprivata.com]: 
github_username [imprivata-cloud]: 
# the project name should be hyphenated
# I use the hyphenated project name for teh github project and the project root directory
project_name [cdk-my-project-name]: cdk-example-one
project_slug [cdk_example_one]: 
project_short_description [CDK/Boto3 template is a good starting point]: use example one for all the best things!!11!!

# NOTE the root project directory is hyphenated, but the package and module names use underscores
cd cdk-example-one
tree.
├── app.py
├── cdk_example_one
│ ├── cdk_example_one_stack.py
│ ├── data.py
│ └── __init__.py
├── cdk.json
├── CONTRIBUTE.md
├── GETTING_STARTED.md
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
├── scripts
│ ├── initialize_git.sh
│ └── update_cdk_libs.sh
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        ├── test_cdk_example_one_stack.py
        └── test_data.py

4 directories, 17 files

# initialize the git repo. you'll be prompted for the first commit message
make initialize-git 
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
[[ ! -e .git ]] && bash scripts/initialize_git.sh
configuring repo email: nmarks@imprivata.com
configuring repo name: Nate Marks
Initialized empty Git repository in /home/nmarks/projects/cdk-example-one/.git/
Switched to a new branch 'main'
[main (root-commit) 0f8a2f9] init
 20 files changed, 408 insertions(+)
 create mode 100644 .github/workflows/static-checks.yml
 create mode 100644 .gitignore
 create mode 100644 .python-version
 create mode 100644 CONTRIBUTE.md
 create mode 100644 GETTING_STARTED.md
 create mode 100644 Makefile
 create mode 100644 README.md
 create mode 100644 app.py
 create mode 100644 cdk.json
 create mode 100644 cdk_example_one/__init__.py
 create mode 100644 cdk_example_one/cdk_example_one_stack.py
 create mode 100644 cdk_example_one/data.py
 create mode 100644 pyproject.toml
 create mode 100644 requirements.txt
 create mode 100644 scripts/initialize_git.sh
 create mode 100644 scripts/update_cdk_libs.sh
 create mode 100644 tests/__init__.py
 create mode 100644 tests/unit/__init__.py
 create mode 100644 tests/unit/test_cdk_example_one_stack.py
 create mode 100644 tests/unit/test_data.py

# update aws cdk libs
make update_cdk_libs 
bash scripts/update_cdk_libs.sh

added 1 package, and audited 2 packages in 599ms

found 0 vulnerabilities
make clean-venv
make[1]: Entering directory '/home/nmarks/projects/cdk-example-one'
[[ -e .venv ]] && rm -rf .venv; \
python3 -m venv .venv; \
( \
       . .venv/bin/activate; \
       pip install --upgrade pip; \
       pip install -r requirements.txt; \
    )
Requirement already satisfied: pip in ./.venv/lib/python3.10/site-packages (22.2.1)
Collecting pip
  Using cached pip-23.0-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.2.1
    Uninstalling pip-22.2.1:
      Successfully uninstalled pip-22.2.1
Successfully installed pip-23.0
Collecting constructs<11.0.0,>=10.0.0
  Using cached constructs-10.1.252-py3-none-any.whl (57 kB)
Collecting boto3
  Using cached boto3-1.26.73-py3-none-any.whl (132 kB)
Collecting pytest
  Using cached pytest-7.2.1-py3-none-any.whl (317 kB)
  
...
  
git add --all
git commit -v -a -m 'update cdk'
make static 
( \
       . .venv/bin/activate; \
       git ls-files '*.py' |  xargs black --line-length=79; \
    )
All done! ✨ 🍰 ✨
8 files left unchanged.
( \
       git ls-files '*.sh' |  xargs shellcheck --format=gcc; \
    )
( \
       . .venv/bin/activate; \
       git ls-files '*.py' | xargs pylint --max-line-length=90; \
    )

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "unit" tests/; \
    )
============================================================================================================================== test session starts ===============================================================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0 -- /home/nmarks/projects/cdk-example-one/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/nmarks/projects/cdk-example-one, configfile: pyproject.toml
plugins: typeguard-2.13.3
collected 3 items / 2 deselected / 1 selected                                                                                                                                                                                                                                    

tests/unit/test_data.py::test_data PASSED                                                                                                                                                                                                                                  [100%]

======================================================================================================================== 1 passed, 2 deselected in 4.10s =========================================================================================================================
```
