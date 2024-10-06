Vagrant.configure("2") do |config|
  vms = {
    "ub22vm01" => "192.168.1.151",
    "ub22vm02" => "192.168.1.152",
    "ub22vm03" => "192.168.1.153"
  }

  vms.each do |name, ip|
    config.vm.define name do |vm|
      vm.vm.box = "it-gro/ubuntu-22-04-srv-lvm"

      vm.vm.provider "virtualbox" do |vb|
        vb.name = name
        vb.memory = 9200
        vb.cpus = 2
        vb.customize ["modifyvm", :id, "--cpu-execution-cap", "80"]
        vb.gui = false
      end

      vm.vm.network "public_network", ip: ip, bridge: "enp0s31f6"

      vm.vm.synced_folder ".", "/vagrant"

      vm.vm.provision "shell", inline: <<-SHELL
        sudo systemctl disable --now unattended-upgrades

        sudo apt-get update -yqq && sudo apt-get install -yqq ca-certificates curl gnupg
        sudo mkdir -p /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update -yqq && sudo apt-get install -yqq docker.io docker-compose-plugin

        mkdir -p ~/.docker/cli-plugins/
        curl -SL https://github.com/docker/compose/releases/download/v2.29.6/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
        chmod +x ~/.docker/cli-plugins/docker-compose
     
        sudo mkdir -p /news && sudo cp /vagrant/optifact-installer-*.sh /news/
        sudo chmod +x /news/optifact-installer-*.sh
        sudo apt-get install -yqq console-common && sudo localectl set-keymap es && sudo timedatectl set-timezone Europe/Madrid
      SHELL
    
      vm.ssh.insert_key = false
      vm.ssh.username = "vagrant"
      vm.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    end
  end
end
