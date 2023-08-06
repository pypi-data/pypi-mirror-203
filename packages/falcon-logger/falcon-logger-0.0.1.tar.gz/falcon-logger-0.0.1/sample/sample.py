import argparse
import os
import sys
import time

from falcon_logger.lib.logger import FalconLogger
from sample.normal_logger import NormalLogger
from sample.rsyslog_logger import RsyslogLogger
from sample.stdout_logger import StdoutLogger

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('system')
    parser.add_argument('--numlines', default=100, type=int, required=False)
    args = parser.parse_args()
    # print(args)

    if args.system == 'stdout':
        # ubu: 449 436 517
        # win: 567 530 535
        fl = StdoutLogger()
    elif args.system == 'falcon':
        # ubu: 1239 1073 1064
        # win: 1053 1197 1077
        # 0.250 delay: 776  764 1015
        fl = FalconLogger(os.path.join('out', 'sample_falcon.log'))
    elif args.system == 'normal':
        # ubu: 3694 3903 4262
        # win: 2618 2550 2718
        fl = NormalLogger()
    elif args.system == 'rsyslog':
        # ubu: 3694 3903 4262
        # win: 2618 2550 2718
        fl = RsyslogLogger()
    else:
        print(f'unknown system: {args.system}, choose stdout, falcon, normal')
        sys.exit(1)

    start_time = time.time()
    for i in range(args.numlines):
        fl.debug(f'{i}: test')
    fl.term()
    end_time = time.time()
    elapsed = round((end_time - start_time) * 1_000, 1)
    print(f'{args.system}: total time: {elapsed} ms')
