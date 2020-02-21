#!/bin/bash

# Creates an account on the local system and prompt acc name and passord
read -p "Enter the username to create: " USER_NAME
# Ask for user name
read -p "Enter name of the person: " COMMENT
# Ask for the password
read -p "Select the password: " PASSWORD

# Create user
useradd -c "${COMMENT}" -m ${USER_NAME}

# Set the password
echo ${PASSWORD} | passwd --stdin ${USER_NAME}  

# Force password change on first login
passwd -e ${USER_NAME}


