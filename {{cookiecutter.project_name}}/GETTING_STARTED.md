# Getting Started

Create the GitHub project with a name that matches your directory name
```bash
# change to the root of  your project directory
cd {{cookiecutter.project_slug}}
# initialize git. you'll be prompted for the first commit message
bash scripts/initialize_git.sh
# add the github remote
git remote add origin git@github.com:imprivata-cloud/{{cookiecutter.project_slug}}.git

```