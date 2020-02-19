#!/bin/bash

# This script displays various info to the screen

# Display "Hello"
echo "Hello"

# Assign a value to a variable
WORD="script"

echo "$WORD"

# Demonstrate single quotes not get expanded

echo '$WORD'

# Combine variable and string

echo "This is a shell $WORD"

# Alternative syntax.

echo "This is a shell ${WORD}"


# Append text to variable

echo "${WORD}ing İS FUN!"

# NOT DO THIS

echo "$WORDing is fun!"
echo "$WORD ing is fun"


# Create new variable

ENDING='ed'

#combine two variables

echo "This is ${WORD}${ENDING}."

# Reassignment

ENDING='ing'

echo "This is ${WORD}${ENDING} ff."



































