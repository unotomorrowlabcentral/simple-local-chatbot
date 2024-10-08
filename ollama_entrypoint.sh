#!/bin/bash

set -e

ollama serve &
sleep 5

echo "Waiting for Ollama to start..."
while ! ollama list &>/dev/null; do
  sleep 1
done

echo "ollama started successfully"

echo "pulling llama3.2 model..."
if ollama pull llama3.2; then
  echo "llama3.2 successfully pulled"
else
  echo "failed to pull llama 3.2 model"
  exit 1
fi

# keep the container running
tail -f /dev/null
