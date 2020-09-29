#!/bin/sh

echo "Download Doki Doki Literature Club! v1.1.1"
wget -qO ddlc.zip "$(curl -qsX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url)"
unzip -oq ddlc.zip
cp -afl DDLC-*/* .
rm -rf DDLC-* ddlc.zip
