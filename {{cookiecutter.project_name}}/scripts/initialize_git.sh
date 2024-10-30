#!/usr/bin/env bash
set -Eeuo pipefail
echo "configuring repo email: {{cookiecutter.email}}"
echo "configuring repo name: {{cookiecutter.full_name}}"

git init .
git checkout -b main
git config user.email "{{cookiecutter.email}}"
git config user.name "{{cookiecutter.full_name}}"

git add --all
git commit -v -a -m 'init'
