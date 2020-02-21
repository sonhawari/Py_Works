#!/bin/bash

# I/O redirection

# Redirect STDOUT to a file
FILE="/tmp/data"
head -n1 /etc/passwd > ${FILE}

# Redirect STDIN to a file
read LINE < ${FILE}
echo "LINE contains: ${LINE}"


# Redirect STDOUT to a file' overwriting the file.
head -n3 /etc/passwd > ${FILE}
echo
echo "Contents of ${FILE}"
cat ${FILE}

# Redirect STDOUT to a file, appending to the file.
echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo
echo "Contents of ${FILE}:"
cat ${FILE}


# Redirect STDIN to a program' using FD 0.
read LINE 0< ${FILE}
echo
echo "LINE contains: ${LINE}"

# Redirect STDOUT to a file using FD1\ overwrite the file.
head -n3 /etc/passwd 1> ${FILE}
echo
echo "Contents of ${FILE}"
cat ${FILE}

# Redirect STDERR to a file using FD2.
ERR_FILE="/tm[/data.err"
head -n /etc/passwd /fakefile 2> ${ERR_FILE}


# Redirect STDERR and STDOUTto a file using FD2.
head -n3 /etc/passwd /fakefile &> ${FILE}
echo
echo "Contents of file ${FILE}:"
cat ${FILE}

# Redirect STDERR and STDOUT to a file with pipe.
echo
head -n3 /etc/passwd /fakefile |& cat -n


# 


#FD0 - Standard Input
#FD1 - Standard Output
#FD2 - Standard Error






















