import os
import re

gpu_list = os.popen('nvidia-smi').read().split('\n')

# print('\n'.join(gpu_list))

gpu0_info = re.findall('[a-zA-Z0-9]+', gpu_list[9].split('|')[1])
gpu1_info = re.findall('[a-zA-Z0-9]+', gpu_list[13].split('|')[1])

msg = [gpu0_info, gpu1_info]
print(msg)
