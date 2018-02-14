# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial32"
  # config.vm.network "forwarded_port", guest: 8080, host: 8080
  # config.vm.network "forwarded_port", guest: 8081, host: 8081
  # config.vm.network "forwarded_port", guest: 8082, host: 8082

  config.vm.provision "shell" do |s|
    s.inline = "apt-get update && apt-get install -y python"
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
  end
end
