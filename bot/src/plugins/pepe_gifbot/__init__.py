import httpx
import os
import numpy as np
import tempfile
from pathlib import Path
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from moviepy.editor import VideoFileClip

from src.extensions import coolperm


BASE_URL = "http://i.tech.corgi.plus:6670"
API_ROUTE = "api/v1/retrieve"
header = {'Content-Type': 'application/json'}

pepe = on_regex(r'^pepe.*', priority=50, block=False)

@pepe.handle(parameterless=[coolperm('.pepe')])
async def _(event: Event):
    sender = int(event.get_user_id())
    message = ' '.join(event.get_plaintext().split()[1:])
    data = {
        "text": message,
        "num_resp_gifs": 5
    }
    async with httpx.AsyncClient(proxies=None, headers=header) as cli:
        resp = await cli.post(url=f"{BASE_URL}/{API_ROUTE}", json=data)
        reps_json = resp.json()
        chosen_gif_url = BASE_URL + np.random.choice(reps_json['internal_links'])
        normalized_text = reps_json['normalized_text']
    
    # Create a random file for the GIF
    temp_gif_fd, temp_gif_filepath = tempfile.mkstemp(prefix="pepe-gitbot-temp-", suffix=".gif")
    os.close(temp_gif_fd) # close the tmp file descriptor
    temp_gif_filepath = Path(temp_gif_filepath)
    VideoFileClip(chosen_gif_url).write_gif(temp_gif_filepath)

    msg = Message([
        # MessageSegment.reply(id_=sender),
        # MessageSegment.text(f"Normalized Text: {normalized_text}"),
        MessageSegment.image(file=temp_gif_filepath)
    ])

    await pepe.finish(msg)
    os.remove(temp_gif_filepath) # remove temp file
