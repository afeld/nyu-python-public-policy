#!/bin/bash

set -e
set -x


SCHOOL=$1

# remove irrelevant files

git rm -r \
    .github/ \
    nbdime_config.json \
    extras/pandas_crash_course.ipynb \
    extras/terraform/ \
    extras/**/test_*.py

if [ "$SCHOOL" = "nyu" ]; then
    git rm curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL"

./extras/scripts/build.sh

# remove remaining files
git rm -r extras/scripts/

git diff

if [ "$GITHUB_REF_NAME" = "main" ]; then
    # https://lannonbr.com/blog/2019-12-09-git-commit-in-actions/
    # https://github.com/orgs/community/discussions/26560#discussioncomment-3252339
    git config user.name "github-actions[bot]"
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

    # create a fresh branch locally
    git switch -c "$SCHOOL"
    git add .
    git commit -am "CI: render for school"
    git push -f origin "$SCHOOL"
fi
