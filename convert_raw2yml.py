#!/usr/bin/env python3
import os
import yaml

if __name__ == "__main__":
    registers = []
    with open('data.txt', 'r') as fd:
        for line in fd.readlines():
            line = line.strip()
            tokens = line.split(' ')
            name = ' '.join(tokens[2:-6]).strip('.')
            unit = tokens[-6]
            addr_hi = int(tokens[-5], 16)
            addr_lo = int(tokens[-4], 16)
            addr = addr_hi << 8 | addr_lo
            register = {
                'name': name,
                'unit_of_measurement': unit,
                'slave': 1,
                'address': addr,
                'input_type': 'input',
                'data_type': 'float32',
                'precision': 2,
                'count': 2
            }
            registers.append(register)
            print("[{}] {} ({})".format(addr, name, unit))
    yaml.dump(registers, open('sdm630_addresses.yaml', 'w'), default_flow_style=False)
