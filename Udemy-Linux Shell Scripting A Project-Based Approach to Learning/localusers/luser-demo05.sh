#!/bin/bash

# This generates list of random passwords.

# A RANDOM password
PASSWORD="${RANDOM}"
echo "${PASSWORD}"

# Three random numbers together

PASSWORD="${RANDOM}${RANDOM}${RANDOM}"
echo "${PASSWORD}"

# use current datetime as basis for password
PASSWORD=$(date +%s%N)
echo "${PASSWORD}"

# Other pass
PASSWORD=$(date +%s%N | sha256sum | head -c32)
echo "${PASSWORD}"

# other2
PASSWORD=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c48)
echo "${PASSWORD}"

# Other 3
SPECIAL_CHARACTER=$(echo '!@#$%^&*()_+=' | fold -w1 | shuf | head -c1)
echo "${PASSWORD}${SPECIAL_CHARACTER}"












