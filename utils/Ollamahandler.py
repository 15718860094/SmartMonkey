import requests
import json
from settings import * 
from ImageHandler import ImageHandler
"""参考文档: https://github.c§om/ollama/ollama/blob/main/docs/api.md """


class OllamaHandler(object):
    def __init__(self, model, prompt) -> None:
        self.url = 'http://localhost:11434/api/generate'
        self.model = model
        self.prompt = prompt
        
    def generate_request_streaming(self):
        data = {
        "model": self.model,
        "prompt": self.prompt
        }
        response = requests.post(self.url, json=data, stream=True)
        # for line in response.iter_lines():
        #     if line:
        #         json_obj = json.loads(line)
        #         print(json_obj)
        return response.iter_lines()
    
    def request_with_images(self, image_path):
        data = {
        "model": self.model,
        "prompt": self.prompt,
        "stream": False,
        "images": [ImageHandler().encode_image_base64(image_path)]
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url, data=json.dumps(data), headers=headers)            
        logging.info(response.json()['response'])
        
