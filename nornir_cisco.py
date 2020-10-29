from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko import netmiko_send_command
from nornir.core.filter import F


def logging_show_run(task):
    
    cmd = 'show run'
    output = task.run(
        name='show run',
        task=netmiko_send_command,
        command_string=cmd)
    task.run(
        task=write_file,
        name="Write",
        filename=f"output/nornir/{task.host.hostname}.cfg",
        content=output.result,
    )

nr = InitNornir(inventory={"options": {"host_file": f"inventory/nornir/inventory-10.yaml"}},)

nr.run(logging_show_run)
