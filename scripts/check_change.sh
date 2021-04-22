#!/bin/bash

set -e
set -x


echo "Setting up..."
SOURCE=$1
PRE="tmp/$SOURCE"
POST=${PRE//\./.nbconvert.}
FINAL=${PRE//\./.final.}

mkdir -p tmp
python scripts/diffable.py < "$SOURCE" > "$PRE"

cp "$PRE" "$POST"
./scripts/update.sh "$POST"

python scripts/diffable.py < "$POST" > "$FINAL"

echo "Comparing output..."
DIFF=$(nbdiff "$PRE" "$FINAL")
echo "$DIFF"
[ -z "$DIFF" ] || exit 1
