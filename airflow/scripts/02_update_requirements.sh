#!/bin/bash

# Define paths
CRAWL_REQUIREMENTS="../../crawl/requirements.txt"
AIRFLOW_REQUIREMENTS="../requirements.txt"
ENV_FILE="../.env"

# Check if requirements.txt in crawl exists
if [ ! -f "$CRAWL_REQUIREMENTS" ]; then
    echo "$CRAWL_REQUIREMENTS does not exist."
    exit 1
fi

# Copy the requirements.txt from crawl to airflow
cp "$CRAWL_REQUIREMENTS" "$AIRFLOW_REQUIREMENTS"

# Check if .env file exists
if [ -f "$ENV_FILE" ]; then
    # Extract AIRFLOW_VERSION from .env file
    AIRFLOW_VERSION=$(grep '^AIRFLOW_VERSION=' "$ENV_FILE" | cut -d'=' -f2)
    
    # Append apache-airflow with version to requirements.txt
    echo "apache-airflow==${AIRFLOW_VERSION}" >> "$AIRFLOW_REQUIREMENTS"
    
    echo "Updated $AIRFLOW_REQUIREMENTS with apache-airflow version ${AIRFLOW_VERSION}."
else
    echo ".env file does not exist."
    exit 1
fi