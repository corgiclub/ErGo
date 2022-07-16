from pydantic import BaseSettings


# class Config(BaseSettings):

class Glances(BaseSettings):
    corgitech_api = "http://172.17.0.1:61208/api/3/"
    nas_api = "http://172.17.0.1:61208/api/3/"

    memory_warning = 90
    gpu_warning_temp = 80
    cpu_warning_temp = 90
    file_sys_warning = 90


class MongoDB(BaseSettings):
    host = "mongodb://i.tech.corgi.plus:27017/"
    base_path = "/mnt/0/base/"

    retry_times = 3
    wait_time = 0.5

