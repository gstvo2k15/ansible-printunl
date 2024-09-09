# Vagrantfile para un entorno de 3 nodos con Ubuntu 22.04
Vagrant.configure("2") do |config|

  # Configuración global para que todas las VMs utilicen Ubuntu 22.04
  config.vm.box = "ubuntu/jammy64"  # Ubuntu 22.04

  # Nodo 1
  config.vm.define "node1" do |node1|
    node1.vm.hostname = "labnode1"
    node1.vm.network "public_network", ip: "192.168.1.131", bridge: "enp0s3"  # Ajusta el nombre del adaptador de red
    node1.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
  end

  # Nodo 2
  config.vm.define "node2" do |node2|
    node2.vm.hostname = "labnode2"
    node2.vm.network "public_network", ip: "192.168.1.132", bridge: "enp0s3"  # Ajusta el nombre del adaptador de red
    node2.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
  end

  # Nodo 3
  config.vm.define "node3" do |node3|
    node3.vm.hostname = "labnode3"
    node3.vm.network "public_network", ip: "192.168.1.133", bridge: "enp0s3"  # Ajusta el nombre del adaptador de red
    node3.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
  end

  # Configuración para habilitar SSH desde fuera de la VM
  config.ssh.insert_key = false
end
