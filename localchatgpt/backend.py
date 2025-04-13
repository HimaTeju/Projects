# backend.py

import requests

OLLAMA_BASE_URL = "http://localhost:11434"  # Default Ollama endpoint
MODEL_NAME = "llama3.2:latest"  # Use `ollama list` to see available models

def get_llama_response(prompt, temperature=0.7, max_tokens=512):
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "temperature": temperature,
        "num_predict": max_tokens,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        response_data = response.json()
        return response_data.get("response", "Sorry, no response from the model.").strip()

    except requests.exceptions.RequestException as e:
        return f"Error communicating with LLaMA (Ollama): {e}"
