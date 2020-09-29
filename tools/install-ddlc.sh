#!/bin/sh

echo "Download Doki Doki Literature Club! v1.1.1"
wget -qO ddlc.zip $(curl -qsX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url)
unzip -joq ddlc.zip *.chr -d characters
unzip -joq ddlc.zip *.rpa -d game
unzip -joq ddlc.zip DDLC-1.1.1-pc/game/python-packages/singleton.py -d game/python-packages
rm ddlc.zip
