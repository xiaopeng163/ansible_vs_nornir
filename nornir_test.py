import sys

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_jinja2.plugins.tasks import template_file

def generate(task):
    template = task.run(
        task=template_file,
        name="Render",
        template="nornir-base.j2",
        path="templates",
    )
    task.run(
        task=write_file,
        name="Write",
        filename=f"output/nornir/{task.host}.cfg",
        content=template.result,
    )


def main(inventory_size):
    nornir = InitNornir(
        inventory={"options": {"host_file": f"inventory/nornir/inventory-{inventory_size}.yaml"}},
        dry_run=False,
    )
    nornir.run(task=generate)
    # result = nornir.run(task=generate)
    # print_result(result)


if __name__ == "__main__":
    inventory_size = int(sys.argv[1])
    main(inventory_size)
