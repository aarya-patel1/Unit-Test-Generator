import requests, yaml, os, json

# Load prompt
with open("../prompts/initial.yaml") as f:
    config = yaml.safe_load(f)

# Read the C++ file
# ✅ CORRECT
src_file = "../../orgChartApi/main.cc"

with open(src_file, 'r') as f:
    code = f.read()

# Build the payload
payload = {
    "model": "llama3",
    "messages": [
        {"role": "system", "content": config["prompt"]},
        {"role": "user", "content": code}
    ],
    "stream": True
}

# Make the request to Ollama with streaming support
response = requests.post("http://localhost:11434/api/chat", json=payload, stream=True)

# Handle NDJSON streaming output
output_chunks = []
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode('utf-8'))
        if 'message' in data and 'content' in data['message']:
            output_chunks.append(data['message']['content'])

content = ''.join(output_chunks)

# Save the result to a file
output_path = "../generated_tests/test_main.cc"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Test file generated at: {output_path}")
