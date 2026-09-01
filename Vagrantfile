Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.hostname = "scenario4"

  config.vm.network "forwarded_port",
    guest: 5000,
    host: 8085,
    auto_correct: true

  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    set -e

    apt-get update
    apt-get install -y docker.io docker-compose

    systemctl enable docker
    systemctl start docker

    cd /vagrant
    docker-compose up -d --build
  SHELL
end