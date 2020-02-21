#!/bin/bash

# Exit if not root user
if [[ "${UID}" -ne 0 ]]
then 
  echo 'You are not root! Exited'
  exit 1
fi

# If the user doesn't supply at least one argument, then give them help.

# The first parameter is the user name.
USER_NAME="${1}"
# The rest of the parameters are for the account comments.
USER_NAME="${2}"
# Generate a password.
PASSWORD=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c48)
echo "${PASSWORD}"
# Create the user with the password.
useradd -c "${COMMENT}" -m ${USER_NAME}

# Check to see if the useradd command succeeded.
if [[ "${?}" -ne 0 ]]
then 
  echo 'Acc could not created'
  exit 1
fi

# Set the password.
echo ${PASSWORD} | passwd --stdin ${USER_NAME}  

# Check to see if the passwd command succeeded.
if [[ "${?}" -ne 0 ]]
then 
  echo 'Password could not set'
  exit 1
fi
# Force password change on first login.
passwd -e ${USER_NAME}

# Display the username, password, and the host where the user was created.
echo "${USER_NAME}"
echo "${PASSWORD}"
echo "${HOSTNAME}"


