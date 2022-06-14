terraform {
  required_providers {
    vagrant = {
      source  = "bmatcuk/vagrant"
      version = "4.1.0"
    }
  }
}

provider "vagrant" {}

resource "vagrant_vm" "vagrantbox" {
  env = {
    VAGRANTFILE_HASH = md5(file("./Vagrantfile")),
  }
}
