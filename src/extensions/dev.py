import os
import re
import subprocess

# gpu_list = os.popen('nvidia-smi').read().split('\n')
#
# print(gpu_list)
# # print('\n'.join(gpu_list))
# if len(gpu_list) > 2:
#     gpu0_info = re.findall('[a-zA-Z0-9]+', gpu_list[9].split('|')[1])
#     gpu1_info = re.findall('[a-zA-Z0-9]+', gpu_list[13].split('|')[1])
#     msg = [gpu0_info, gpu1_info]
# else:
#     msg = gpu_list[0]


def sh(command, print_msg=True):
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode('unicode_escape').split('\n')
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(">>>", line)
        lines.append(line)
    return lines


msg = sh(['s-tui'])

print(msg)
