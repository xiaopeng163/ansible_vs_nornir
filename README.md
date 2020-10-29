# ansible_vs_nornir

## local jinja template

Ansible

```
$ time ansible-playbook - inventory/ansible/inventory-1000/yaml ansible_test.yml
```

Nornir

```
$ time python nornir_test.py 1000
```

## remote cisco cfg backup

Ansible

```
$ time ansible-playbook - inventory/ansible/inventory-30/yaml ansible_cisco.yml
ansible-playbook -i inventory/ansible/inventory-30.yaml ansible_cisco.yml  54.98s user 20.56s system 641% cpu 11.773 total
```

Nornir

```
$ time python nornir_cisco.py
python nornir_cisco.py  0.91s user 0.28s system 33% cpu 3.498 total
```
