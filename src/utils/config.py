from argparse import ArgumentParser


def config_from_cmdline():
    config = {}

    parser = ArgumentParser()
    parser.add_argument('-a', '--addr', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=5000)
    parser.add_argument('-i', '--intv', type=float, default=0)  # seconds
    parser.add_argument('-t', '--testbed', type=str, required=True)
    parser.add_argument('-r', '--rpc', type=str, default='analyze')
    parser.add_argument('-g', '--args', type=str, default='all')

    args = parser.parse_args()
    config['addr'] = args.addr
    config['port'] = args.port
    config['intv'] = args.intv
    config['testbed'] = args.testbed
    config['rpc'] = args.rpc
    config['args'] = args.args.split(',')

    return config
