#!/bin/bash

set -e

# confirm there's exactly one argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 SCHOOL" >&2
  exit 1
fi

SCHOOL=$1
case $SCHOOL in
    nyu)
        REMOVE_TAG=columbia-only
        ;;
    columbia)
        REMOVE_TAG=nyu-only
        ;;
    *)
        echo "Unknown school: $SCHOOL" >&2
        exit 1
        ;;
esac

echo "Rendering notebooks…"
jupyter nbconvert \
    --to notebook --inplace \
    --TagRemovePreprocessor.enabled=True \
    --TagRemovePreprocessor.remove_cell_tags $REMOVE_TAG \
    --Exporter.preprocessors=extras.lib.school.SchoolTemplate \
    --SchoolTemplate.school_id="$SCHOOL" \
    ./*.ipynb

# render additional files
OTHER_FILES=$(git ls-files -- \
    ':!:*.ipynb' ':!:*.py' ':!:*.sh' ':!:*.tf' \
    ':!:.github/workflows/*' \
    ':!:.github/ISSUE_TEMPLATE/new-term.md' \
    ':!:extras/img/*')

for f in $OTHER_FILES; do
    echo "Rendering $f..."
    python -m extras.scripts.school_template --inplace "$f" "$SCHOOL"
done