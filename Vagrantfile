Vagrant.configure("2") do |config|
  
  # Configuración global para todas las VMs
  config.vm.box = "ubuntu/jammy64"  # Ubuntu 22.04

  # Nodo 1
  config.vm.define "node1" do |node1|
    node1.vm.hostname = "labnode1"
    
    # Solo adaptador puente
    node1.vm.network "public_network", ip: "192.168.1.131", bridge: "enx3c18a0d4bb07"

    # Configuración del proveedor VirtualBox
    node1.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2

      # Crear un controlador SATA para el disco adicional
      vb.customize ['storagectl', :id, '--name', 'SATA Controller', '--add', 'sata', '--controller', 'IntelAHCI']

      # Crear un disco adicional de 10GB para LVM (usando una ruta absoluta)
      vb.customize ['createhd', '--filename', '/home/kloud/Documents/Repos/ansible-printunl/labnode1_disk.vdi', '--size', 10240]

      # Adjuntar el disco al controlador SATA
      vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', '/home/kloud/Documents/Repos/ansible-printunl/labnode1_disk.vdi']
    end

    # Aprovisionamiento para LVM
    node1.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y lvm2
      echo -e "n\np\n1\n\n\nw" | sudo fdisk /dev/sdb
      sudo pvcreate /dev/sdb1
      sudo vgcreate vg_data /dev/sdb1
      sudo lvcreate -L 5G -n lv_data vg_data
      sudo mkfs.ext4 /dev/vg_data/lv_data
      sudo mkdir -p /mnt/data
      sudo mount /dev/vg_data/lv_data /mnt/data
      echo '/dev/vg_data/lv_data /mnt/data ext4 defaults 0 0' | sudo tee -a /etc/fstab
    SHELL
  end

  # Nodo 2 (misma configuración)
  config.vm.define "node2" do |node2|
    node2.vm.hostname = "labnode2"
    
    # Solo adaptador puente
    node2.vm.network "public_network", ip: "192.168.1.132", bridge: "enx3c18a0d4bb07"

    node2.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2

      # Crear un controlador SATA para el disco adicional
      vb.customize ['storagectl', :id, '--name', 'SATA Controller', '--add', 'sata', '--controller', 'IntelAHCI']

      # Crear un disco adicional de 10GB para LVM (usando una ruta absoluta)
      vb.customize ['createhd', '--filename', '/home/kloud/Documents/Repos/ansible-printunl/labnode2_disk.vdi', '--size', 10240]

      # Adjuntar el disco al controlador SATA
      vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', '/home/kloud/Documents/Repos/ansible-printunl/labnode2_disk.vdi']
    end

    node2.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y lvm2
      echo -e "n\np\n1\n\n\nw" | sudo fdisk /dev/sdb
      sudo pvcreate /dev/sdb1
      sudo vgcreate vg_data /dev/sdb1
      sudo lvcreate -L 5G -n lv_data vg_data
      sudo mkfs.ext4 /dev/vg_data/lv_data
      sudo mkdir -p /mnt/data
      sudo mount /dev/vg_data/lv_data /mnt/data
      echo '/dev/vg_data/lv_data /mnt/data ext4 defaults 0 0' | sudo tee -a /etc/fstab
    SHELL
  end

  # Nodo 3 (misma configuración)
  config.vm.define "node3" do |node3|
    node3.vm.hostname = "labnode3"
    
    # Solo adaptador puente
    node3.vm.network "public_network", ip: "192.168.1.133", bridge: "enx3c18a0d4bb07"

    node3.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2

      # Crear un controlador SATA para el disco adicional
      vb.customize ['storagectl', :id, '--name', 'SATA Controller', '--add', 'sata', '--controller', 'IntelAHCI']

      # Crear un disco adicional de 10GB para LVM (usando una ruta absoluta)
      vb.customize ['createhd', '--filename', '/home/kloud/Documents/Repos/ansible-printunl/labnode3_disk.vdi', '--size', 10240]

      # Adjuntar el disco al controlador SATA
      vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', '/home/kloud/Documents/Repos/ansible-printunl/labnode3_disk.vdi']
    end

    node3.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y lvm2
      echo -e "n\np\n1\n\n\nw" | sudo fdisk /dev/sdb
      sudo pvcreate /dev/sdb1
      sudo vgcreate vg_data /dev/sdb1
      sudo lvcreate -L 5G -n lv_data vg_data
      sudo mkfs.ext4 /dev/vg_data/lv_data
      sudo mkdir -p /mnt/data
      sudo mount /dev/vg_data/lv_data /mnt/data
      echo '/dev/vg_data/lv_data /mnt/data ext4 defaults 0 0' | sudo tee -a /etc/fstab
    SHELL
  end

end
