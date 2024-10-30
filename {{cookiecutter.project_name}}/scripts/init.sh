#!/usr/bin/env bash
set -Eeuoxv pipefail
# shellcheck disable=SC1083
go mod init github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
git init .
# shellcheck disable=SC1083
git config user.name "{{ cookiecutter.github_username }}"
# shellcheck disable=SC1083
git config user.email "{{ cookiecutter.email }}"
git add -A
git commit -am 'initial'
git branch -m main
