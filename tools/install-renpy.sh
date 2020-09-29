#!/bin/sh

RENPY_VERSION='6.99.12.4'

echo "Download Ren'Py SDK v$RENPY_VERSION"
wget -q -O sdk.tar.bz2 https://www.renpy.org/dl/$RENPY_VERSION/renpy-$RENPY_VERSION-sdk.tar.bz2

echo "Extract Ren'Py SDK v$RENPY_VERSION"
tar -xf sdk.tar.bz2
rm sdk.tar.bz2
mv renpy-6.99.12.4-sdk sdk

echo "Apply Extract Dialogue patch to Ren'Py"
wget -q -O sdk/renpy/translation/dialogue.py https://raw.githubusercontent.com/proudust/renpy/dialogue-patch/renpy/translation/dialogue.py
