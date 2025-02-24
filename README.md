# ansible-printunl
Ansible deployment to provision printunl in VirtualBox VMs with Vagrant in Ubuntu 22.04 servers with blue/green strategy.

## Example usage

- Deploy to blue servers (impar numbers):

    `ansible-playbook main.yml -i hosts.yml --limit pritunl_blue_servers`
