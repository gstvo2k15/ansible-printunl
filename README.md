# ansible-printunl
Ansible deployment to provision printunl in VirtualBox VMs with Vagrant.

## Verify status of provision machines

`ansible pritunl_servers1 -i hosts.yml -m ansible.builtin.ping`

## Execute deployment for install pritunl and mongodb

`ansible-playbook -i hosts.yml -l pritunl_servers1 pritunl_mongodb.yml`

## Install azure-blob Role:

`ansible-playbook -i hosts.yml backup-restore-playbook.yml --extra-vars "role_action=blob_mount" -l ub22srv02`

## To Run the Backup Role:

`ansible-playbook -i hosts.yml backup-restore-playbook.yml --extra-vars "role_action=backup destination_server=root@ub22srv06" -l ub22srv02`

## To Run the Restore Role:

`ansible-playbook -i hosts.yml backup-restore-playbook.yml --extra-vars "role_action=restore" -l ub22srv06`

## TO-DO (Execute backup/restore via azure pipeline)

```
ansible-printunl/
├── backup-restore-playbook.yml
└── roles/
    ├── backup/
    │   └── tasks/
    │       └── main.yml
    └── restore/
        └── tasks/
            └── main.yml
```