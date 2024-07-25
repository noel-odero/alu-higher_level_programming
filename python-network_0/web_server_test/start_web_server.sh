#!/bin/bash

# Function to start the server
start_server() {
    python3 "$1" &
    SERVER_PID=$!
    sleep 1  # Give the server a second to start
}

# Function to stop the server
stop_server() {
    kill $SERVER_PID
}

# Function to check the content length
check_content_length() {
    URL=$1
    EXPECTED_LENGTH=$2

    LENGTH=$(curl -s "$URL" -o /dev/null -w '%{size_download}\n')

    if [ "$LENGTH" == "$EXPECTED_LENGTH" ]; then
        echo "Correct output: GET $URL => \"$(curl -s $URL)\""
        echo "[Got]"
        echo "$LENGTH"
        echo "(${#LENGTH} chars long)"
        echo "[Expected]"
        echo "$EXPECTED_LENGTH"
        echo "(${#EXPECTED_LENGTH} chars long)"
    else
        echo "Error: Content length mismatch."
        echo "[Got]"
        echo "$LENGTH"
        echo "(${#LENGTH} chars long)"
        echo "[Expected]"
        echo "$EXPECTED_LENGTH"
        echo "(${#EXPECTED_LENGTH} chars long)"
    fi
}

# Check the first server
start_server web_0.py
check_content_length "http://0.0.0.0:5000" "13"
stop_server

# Check the second server
start_server web_1.py
check_content_length "http://0.0.0.0:5000" "55"
stop_server

