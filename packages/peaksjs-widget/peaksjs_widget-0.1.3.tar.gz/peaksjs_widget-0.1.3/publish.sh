#!/bin/bash
# do tbump <> BEFORE THIS SCRIPT

rm dist/peaksjs*

yarn build:prod
yarn publish
pyproject-build .
twine upload dist/peaksjs* -u k-tonal
