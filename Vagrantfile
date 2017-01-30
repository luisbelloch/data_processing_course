Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial32"
  config.vm.provision "file", source: "local_setup.sh", destination: "~/spark_setup.sh"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 8081, host: 8081
  config.vm.network "forwarded_port", guest: 8082, host: 8082
end

