#!/bin/bash

# display what user typed
echo "You executed this command: ${0}"

# display path and file name
echo "You used $(dirname ${0}) as the path to the $(basename ${0}) script"

# display how many paramater after command
NUBER_OF_PARAMETERS="${#}"
echo "You supplied ${NUBER_OF_PARAMETERS} arguments on the command line"

# Make sure at least one argument
if [[ "${NUBER_OF_PARAMETERS}" -lt 1 ]]
then
  echo "Usage: ${0} USER_NAME [USER_NAME]..."
  exit 1
fi

# Generate and display a pass for each parameter
for USER_NAME in "${@}"
do
  PASSWORD=$(date +%s%N | sha256sum | head -c48)
  echo "${USER_NAME}: ${PASSWORD}"
done



















