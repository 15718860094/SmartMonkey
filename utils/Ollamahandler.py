import requests
import json
from ImageHandler import ImageHandler
"""参考文档: https://github.c§om/ollama/ollama/blob/main/docs/api.md """
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


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
        "images": [ImageHandler(image_path).encode_image_base64()]
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url, data=json.dumps(data), headers=headers)            
        logging.debug(response.json()['response'])
        
