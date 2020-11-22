import linux_metrics as lm


def get_metric() -> str:
    # cpu
    ret = ''
    ret += 'procs running: %d' % lm.cpu_stat.procs_running() + '\n'
    cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
    ret += 'cpu utilization: %.2f%%' % (100 - cpu_pcts['idle']) + '\n'
    # ret += 'load average: %.2f%%' % (lm.cpu_stat.load_avg()) + '\n'
    # disk
    ret += 'disk busy: %s%%' % lm.disk_stat.disk_busy(
        'sdb', sample_duration=1) + '\n'
    r, w = lm.disk_stat.disk_reads_writes('sdb')
    ret += 'disk reads: %s' % r + '\n'

    ret += 'disk writes: %s' % w + '\n'
    # memory
    used, total, _, _, _, _ = lm.mem_stat.mem_stats()
    ret += 'mem used: %s GB' % str(used / 1024**3)[:5] + '\n'
    ret += 'mem total: %s GB' % str(total / 1024**3)[:5] + '\n'
    # network
    rx_bits, tx_bits = lm.net_stat.rx_tx_bits('eth0')
    ret += 'net bits received: %s' % rx_bits + '\n'
    ret += 'net bits sent: %s' % tx_bits + '\n'
    return ret


if __name__ == '__main__':
    print(get_metric())
