with open("../prompts/fix_build.yaml") as f:
    config = yaml.safe_load(f)

with open("../generated_tests/test_main.cc") as test_file:
    test_code = test_file.read()

with open("../build_logs/build_output.txt") as log_file:
    logs = log_file.read()

payload = {
    "model": "llama3",
    "messages": [
        {"role": "system", "content": config["prompt"]},
        {"role": "user", "content": f"{test_code}\n\nBuild Logs:\n{logs}"}
    ]
}

response = requests.post("http://localhost:11434/api/chat", json=payload)
content = response.json()['message']['content']

with open("../generated_tests/test_main.cc", "w") as f:
    f.write(content)
