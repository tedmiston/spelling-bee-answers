#!/usr/bin/env bash

set -euo pipefail

SRC_DIR=${1}      # source code root directory
LINE_LENGTH=${2}  # max line length
DRY_RUN=${3}      # 1 to use dry run mode; 0 to not

function format {
	echo

	echo '* step 1/2: running black *'
	black --line-length="${LINE_LENGTH}" "${SRC_DIR}"
	echo

	echo '* step 2/2: running isort *'
	isort "${SRC_DIR}"
	echo
}

function format_dry_run {
	echo

	echo '* step 1/2: running black *'
	black --diff --line-length="${LINE_LENGTH}" "${SRC_DIR}"
	echo

	echo '* step 2/2: running isort *'
	isort --diff "${SRC_DIR}"
	echo
}

function main {
	if [ "${DRY_RUN}" ]; then
		format_dry_run;
	else
		format;
	fi
}

main
