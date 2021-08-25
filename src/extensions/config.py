from pydantic import BaseSettings


# class Config(BaseSettings):

class Glances(BaseSettings):
    corgitech_api = "http://localhost:61208/api/3/"
    nas_api = "http://0.0.0.0:61208/api/3/"

    memory_warning = 90
    gpu_warning_temp = 80
    file_sys_warning = 90


class MongoDB(BaseSettings):
    host = "mongodb://i.tech.corgi.plus:27017/"
    base_path = ""

