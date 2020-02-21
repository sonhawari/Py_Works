#!/bin/bash



# Make sure the script is being executed with superuser privileges.
if [[ "${UID}" -ne 0 ]]
then 
  echo 'You are not root! Exited'
  echo 'Exit code: '${?}
  exit 1
fi

echo ${?}

# Get the username (login).

read -p "Enter the username to create: " USER_NAME

# Get the real name (contents for the description field).
read -p "Enter name of the person: " COMMENT

# Get the password.
read -p "Select the password: " PASSWORD

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
























