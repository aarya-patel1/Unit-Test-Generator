with open("../prompts/refine.yaml") as f:
    config = yaml.safe_load(f)

with open("../generated_tests/test_main.cc") as f:
    test_code = f.read()

payload = {
    "model": "llama3",
    "messages": [
        {"role": "system", "content": config["prompt"]},
        {"role": "user", "content": test_code}
    ]
}

response = requests.post("http://localhost:11434/api/chat", json=payload)
content = response.json()['message']['content']

with open("../generated_tests/test_main.cc", "w") as f:
    f.write(content)
