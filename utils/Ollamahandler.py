import requests
import json

"""参考文档: https://github.com/ollama/ollama/blob/main/docs/api.md """



class OllamaHandler(object):
    def generate_request_streaming():
        url = 'http://localhost:11434/api/generate'
        data = {
        "model": "llava",
        "prompt": "Why is the sky blue?"
        }
        response = requests.post(url, json=data, stream=True)
        # for line in response.iter_lines():
        #     if line:
        #         json_obj = json.loads(line)
        #         print(json_obj)
        return response.iter_lines()
            
OllamaHandler.generate_request_streaming()