#!/usr/bin/env python3
import json
import subprocess

def get_azure_vms():
    # Azure CLI command to list VMs
    result = subprocess.check_output([
        "az", "vm", "list", "-d", "--query", "[].{name:name, public_ip:publicIps}", "-o", "json"
    ])
    return json.loads(result)

def main():
    vms = get_azure_vms()
    inventory = {"_meta": {"hostvars": {}}}
    inventory["azure_vms"] = []

    for vm in vms:
        name = vm["name"]
        public_ip = vm.get("public_ip")
        if public_ip:
            inventory["azure_vms"].append(name)
            inventory["_meta"]["hostvars"][name] = {"ansible_host": public_ip}

    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    main()
