#!/bin/bash

#

# Display first theree parameters

echo "Parameter 1: ${1}"
echo "Parameter 1: ${2}"
echo "Parameter 1: ${3}"
echo

# Loop through all the positional parameters

while [[ "${#}" -gt 0 ]]
do
  echo "Number of parameters is ${#}"
  echo "Parameter 1: ${1}"
  echo "Parameter 1: ${2}"
  echo "Parameter 1: ${3}"
  echo
  shift
done































