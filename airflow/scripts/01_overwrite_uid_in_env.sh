#!/bin/bash

# Define the path to the .env file
ENV_FILE="../.env"

# Check if the .env file exists
if [ -f "$ENV_FILE" ]; then
    # Get the current UID
    CURRENT_UID=$(id -u)
    
    # Use sed to overwrite AIRFLOW_UID in the .env file
    if grep -q '^AIRFLOW_UID=' "$ENV_FILE"; then
        # If AIRFLOW_UID exists, replace it
        sed -i "s/^AIRFLOW_UID=.*/AIRFLOW_UID=${CURRENT_UID}/" "$ENV_FILE"
    else
        # If AIRFLOW_UID does not exist, add it
        echo "AIRFLOW_UID=${CURRENT_UID}" >> "$ENV_FILE"
    fi
    
    echo "AIRFLOW_UID updated to ${CURRENT_UID} in ${ENV_FILE}."
else
    echo ".env file does not exist."
    exit 1  # Exit with an error code
fi