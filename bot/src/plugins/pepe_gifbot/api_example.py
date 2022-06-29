import requests
import json
import numpy as np
import tempfile
import os
import time
from moviepy.editor import VideoFileClip

BASE_URL = "http://i.tech.corgi.plus:6670"
API_ROUTE = "api/v1/retrieve"

payload = json.dumps({"text": "Hello there!", "num_resp_gifs": 5})
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", f"{BASE_URL}/{API_ROUTE}", headers=headers, data=payload, proxies=None)
data = json.loads(response.text)
print(f"Request Payload: {payload}")
print(f"Response {response.status_code}: {data}")

random_gif_link = BASE_URL + np.random.choice(data["internal_links"])
print(f"Random GIF Link: {random_gif_link}")

temp_gif_fd, temp_gif_filepath = tempfile.mkstemp(prefix="pepe-gitbot-temp-", suffix=".gif")
os.close(temp_gif_fd) # close the tmp file descriptor

print(temp_gif_fd, type(temp_gif_fd), temp_gif_filepath)
# write GIF
VideoFileClip(random_gif_link).write_gif(temp_gif_filepath)
print(f"Temp GIF File Path: {temp_gif_filepath}")

time.sleep(5) # send file to chat
os.remove(temp_gif_filepath) # remove temp file

