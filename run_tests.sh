#!/bin/bash

# Input parameters:
#   - $1: the path to the *.ini config file, defaults to pytest.ini
# Exported variables in the setup.sh file: HOST_ARTIFACTS, ROOT_VENV, TEST_VENV, COPIED_PROJECT_PATH

PASSED_CONFIG_FILE="$1"

set -Eeuo pipefail
trap cleanup EXIT ERR SIGINT SIGTERM

cleanup() {
  if [ -n "${VIRTUAL_ENV-}" ] && [ "$(type -t deactivate 2>/dev/null)" = "function" ]; then
    echo "Deactivating venv..."
    deactivate
  fi
  if ! [[ "$ORIGINAL_PROJECT_PATH" -ef "$(pwd)" ]]; then
    echo "Returning to the original project path to be able to run the test again with new changes, if there are any"
    cd "$ORIGINAL_PROJECT_PATH"
  fi
}

ORIGINAL_PROJECT_PATH="$(pwd)"
eval source ./setup.sh
if [[ $? -ne 0 ]]; then
  exit 1
fi

DEFAULT_INI_CONFIG_FILE="pytest.ini"
if [[ -z "$PASSED_CONFIG_FILE" ]]; then
  echo "WARNING: no path passed for the project, defaulting to $DEFAULT_INI_CONFIG_FILE"
  INI_CONFIG_FILE="$DEFAULT_INI_CONFIG_FILE"
  if [[ ! -f "$INI_CONFIG_FILE" ]]; then
    echo "ERROR: Default path $DEFAULT_INI_CONFIG_FILE for the repo does not exist"
    exit 1
  fi
elif [[ ! -d "$PASSED_CONFIG_FILE" ]]; then
  echo "ERROR: Provided path '$PASSED_CONFIG_FILE' for the repo does not exist"
  exit 1
else
  INI_CONFIG_FILE="$PASSED_CONFIG_FILE"
  echo "Using $INI_CONFIG_FILE ini config file"
fi

python3 -m pytest -v --tb=short -s --reruns 2 --reruns-delay 2 --ini-config "$INI_CONFIG_FILE" --html=$HOST_ARTIFACTS/test_report_$(date +%Y-%m-%d_%H-%M-%S).html
# Now, let's deactivate venv
deactivate
echo "Returning to the original project path to be able to run the test again with new changes, if there are any"
cd "$ORIGINAL_PROJECT_PATH"
