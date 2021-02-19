import os
import linux_metrics as lm


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


def get_metric():

    message = ''
    warning = ''

    # cpu
    message += 'procs running: %d' % lm.cpu_stat.procs_running() + '\n'
    cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
    message += 'cpu utilization: %.2f%%' % (100 - cpu_pcts['idle']) + '\n'

    # disk
    message += 'disk busy: %s%%' % lm.disk_stat.disk_busy('sda', sample_duration=1) + '\n'
    r, w = lm.disk_stat.disk_reads_writes('sda')
    message += 'disk reads: %s' % r + '\n'
    message += 'disk writes: %s' % w + '\n'

    # memory
    used, total, _, _, _, _ = lm.mem_stat.mem_stats()
    message += 'mem used: %s GB' % str(used / 1024**3)[:5] + '\n'
    message += 'mem total: %s GB' % str(total / 1024**3)[:5] + '\n'

    # network
    rx_bits, tx_bits = lm.net_stat.rx_tx_bits('eth0')
    message += 'net bits received: %s' % rx_bits + '\n'
    message += 'net bits sent: %s' % tx_bits + '\n'

    return message, warning
