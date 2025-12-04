#!/bin/bash

# Build the Docker image
docker build -t raghulm/groq-chatapp:v1.0.0 .

# Run the container
# Replace "your key here" with your actual Groq API key or use environment variable
docker run -p 8501:8501 \
  -e GROQ_API_KEY="${GROQ_API_KEY:-your key here}" \
  raghulm/groq-chatapp:v1.0.0
