#!/usr/bin/env python3

import argparse
import json
import time
from threading import Thread
from time import sleep

import solaredge_modbus

def Reading(x):
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument("host", type=str, help="Modbus TCP address")
    # argparser.add_argument("port", type=int, help="Modbus TCP port")
    # argparser.add_argument("--timeout", type=int, default=1, help="Connection timeout")
    # argparser.add_argument("--unit", type=int, default=1, help="Modbus device address")
    # argparser.add_argument("--json", action="store_true", default=False, help="Output as JSON")
    # args = argparser.parse_args()
    hostINV = "192.168.100.{}".format(x)
    inverter = solaredge_modbus.Inverter(
        host= hostINV,
        port=502,
        timeout=1,
        unit=1
    )

    values = {}
    values = inverter.read_all()
    f.write("--------------------- {} --------------------\n".format(hostINV))
    for i in values:
        f.write("- {} : {}\n".format(i, values[i]))


if __name__ == "__main__":
    start_time = time.time()
    x_ls =list(range(89))
    thread_list = []
    f = open("res.txt", "a")
    Reading(23)
    # for x in range(0,90):
    #     thread = Thread(target=Reading, args=(100+x,))
    #     thread_list.append(thread)
    # for thread in thread_list:
    #     thread.start()
    # for thread in thread_list:
    #     thread.join()
    f.close()
    print("--- %s seconds ---" % (time.time() - start_time))
