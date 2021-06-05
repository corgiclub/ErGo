import os

__all__ = ['nvidia_smi']

"""
    在该文件内定义需要在后台循环执行的系统监控函数
    返回值为
        message: 全部系统状态
        warning: 报警信息
"""


def nvidia_smi():

    #  0123456789012345678901234567890123456789012345678901234567890123456789012345678
    # '| 72%   66C    P2   299W / 300W |   4509MiB / 24265MiB |     98%      Default |'

    text = os.popen('nvidia-smi').read().split('\n')[9]
    fan = text[1:5]
    temp = text[8:10]
    message = f'==== GPU INFO ====\n FAN{fan}, TEMP {temp}\n=================='
    # ==== GPU INFO ====
    #  FAN 72%, TEMP 66
    # ==================
    warning = []
    if fan == 'ERR!':
        warning.append('GPU风扇转速出错')
    if int(temp) > 75:
        warning.append('GPU温度过高 ' + temp + '℃')

    return message, '\n'.join(warning)


