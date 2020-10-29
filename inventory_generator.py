import sys

import yaml
from faker import Faker


def main(num_hosts):
    fake = Faker()

    inventory = {}
    location = {}

    for index in range(num_hosts):
        prefix = f'r{index+1}'
        hostname = f"{prefix}.cisco.com"
        host = {}
        host["ansible_user"] = "cisco"
        host["ansible_password"] = "C1sc0!23"
        host['ansible_connection'] = 'network_cli'
        host['ansible_network_os'] = 'ios'
        host["loopback0"] = fake.ipv4()
        host["asn"] = 65538
        inventory[hostname] = host

    ansible = {}
    ansible["all"] = {}
    ansible["all"]["hosts"] = inventory

    with open(f"inventory/ansible/inventory-{num_hosts}.yaml", "w") as fobj:
        yaml.dump(ansible, fobj, default_flow_style=False)

    nornir = {}
    for host in inventory:
        nornir[host] = {}
        nornir[host]["hostname"] = host
        nornir[host]["username"] = inventory[host]["ansible_user"]
        nornir[host]["password"] = inventory[host]["ansible_password"]
        nornir[host]["platform"] = inventory[host]["ansible_network_os"]
        nornir[host]["data"] = {}
        nornir[host]["data"]["loopback0"] = inventory[host]["loopback0"]
        nornir[host]["data"]["asn"] = inventory[host]["asn"]
    with open(f"inventory/nornir/inventory-{num_hosts}.yaml", "w") as fobj:
        yaml.dump(nornir, fobj, default_flow_style=False)


if __name__ == "__main__":
    inventory_size = int(sys.argv[1])
    main(inventory_size)
