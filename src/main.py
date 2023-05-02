#!/usr/bin/env python3

import signal
from time import sleep

from utils import config
from rpc_client import TestbedDataAnalysisRPCClient


conf = config.config_from_cmdline()

finished = False


def signal_handler(sig, frame):
    global finished
    finished = True


def exec_rpc_analyze() -> 'dict':
    res = None

    client = TestbedDataAnalysisRPCClient(
        testbedName=conf['testbed'],
        apiAddr=conf['addr'],
        apiPort=conf['port']
    )

    if conf['function'] == 'all':
        res = exec_procedure_analyze_all(client)

    return res


def exec_procedure_analyze_all(client) -> 'dict':
    global finished
    
    res = None
    txOffset = {}

    if conf['intv'] < 1:
        res = client.exec_all_analysis(
            txOffset=txOffset
        )
    else:
        while not finished:
            res = client.exec_all_analysis(
                txOffset=txOffset
            )
            if res['status'] == 200:
                txOffset = res['analyze_clients_delay']
                sleep(conf['intv'])
            else:
                finished = True

    return res


def main():
    res = None

    signal.signal(signal.SIGINT, signal_handler)

    if conf['rpc'] == 'analyze':
        res = exec_rpc_analyze()

    print(res)


if __name__ == '__main__':
    main()
