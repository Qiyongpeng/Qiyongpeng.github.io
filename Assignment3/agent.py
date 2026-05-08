import requests

url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

headers = {
    "Authorization": "Bearer sk-ffda8b7341034732981a66e30e0cab8a",
    "Content-Type": "application/json"
}

data = {
    "model": "qwen-turbo",
    "input": {
        "messages": [
            {
                "role": "user",
                "content": "Explain matrix multiplication"
            }
        ]
    },
    "parameters": {
        "result_format": "message"
    }
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

print("AI Response:")
print(result["output"]["choices"][0]["message"]["content"])