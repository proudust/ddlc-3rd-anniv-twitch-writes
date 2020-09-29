BUILD_NAME := $(subst $() ,_,$(shell grep -oP '(?<=define build.name = ").+(?=")' game/options.rpy))
VERSION := $(shell git describe --tags)
ARTIFACT_NAME := $(BUILD_NAME)-$(VERSION).zip
ARTIFACT_PATH := dists/$(ARTIFACT_NAME)

RENPY := SDL_AUDIODRIVER=dummy sdk/renpy.sh
DDLC_FILES := game/audio.rpa game/fonts.rpa game/images.rpa game/scripts.rpa game/python-packages/singleton.py

all: build

install: sdk $(DDLC_FILES) ## Install Ren'Py SDK
sdk:
	@./tools/install-renpy.sh
$(DDLC_FILES):
	@./tools/install-ddlc.sh

run-linux: sdk $(DDLC_FILES) ## Run game on Linux version
	@$(RENPY) .
run-windows: sdk $(DDLC_FILES) ## Run game on Windows version
	@./DDLC.exe

build: dists/$(BUILD_NAME)-$(VERSION).zip ## Build and package mods (Default)
$(ARTIFACT_PATH): install
	@$(RENPY) sdk/launcher distribute . --package "$(VERSION)"
	@echo '::set-env name=ARTIFACT_NAME::$(ARTIFACT_NAME)'
	@echo '::set-env name=ARTIFACT_PATH::$(ARTIFACT_PATH)'
	@echo '::set-env name=BUILD_NAME::$(BUILD_NAME)'
	@echo '::set-env name=VERSION::$(VERSION)'

dialogue: dialogue.tab ## Extract dialogue
dialogue.tab: install
	@$(RENPY) . dialogue --strings --escape
	@sed -i "s|$(shell pwd)|game|" dialogue.tab

check: dialogue.tab ## Check translation
	@python3 ./tools/check_translate.py

clean: ## Remove artifacts
	-rm -rf dists/
	-find game -name '*.rpyc' | xargs rm
	-rm README.txt
	-rm errors.txt log.txt traceback.txt project.json
	-rm dialogue.tab
	-rm error_report.tab

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: \
	all \
	install \
	run-linux \
	run-windows \
	build \
	dialogue \
	check \
	clean \
	help
