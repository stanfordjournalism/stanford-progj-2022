#!/bin/bash

# Silence the output of curl and write the results to specified file
curl -s --output banklist.csv https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv

# TODO: create ca_failed_banks.csv
# It must have the same header row as the original file (banklist.csv)
# Check out exercises/bash_drill.md (in this GitHub repo online)
# for pointers on getting the first line of a file
# and redirecting the content to a new file.

# WRITE THE COMMAND(S) HERE

# TODO: Next, filter banklist.csv for just the CA banks
# and APPEND those rows to the new file (ca_failed_banks.csv)
# WARNING: Make sure you append as opposed to overwriting the data!
# Again, you can get pointers in exercises/bash_drill.md (in this GitHub repo online)

# WRITE THE COMMAND HERE

# Some hackery that subtracts 1 from the overall file count of ca_failed_banks.csv
# and then spits out a message with the count on the command line.
ROW_COUNT=`wc -l < ca_failed_banks.csv | xargs` # HACK to strip whitespace
# SUBTRACT THE HEADER ROW FROM FINAL COUNT
NUM_BANKS=$(($ROW_COUNT - 1))
echo "There are ${NUM_BANKS} failed banks in California"

