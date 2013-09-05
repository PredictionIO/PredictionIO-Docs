==============================================
Install PredictionIO with Vagrant (VirtualBox)
==============================================

Vagrant is an open source tool for simplifying the download and setup steps of a virtual machine (VM) with VirtualBox.
It is recommended for a quick PredictionIO installation in a testing or development environment, as it will save you from many of the common pitfalls of the installation process.

Installation
------------

To get started, please follow the steps below.

Install VirtualBox
~~~~~~~~~~~~~~~~~~

Download and install VirtualBox. Please refer to https://www.virtualbox.org/wiki/Downloads. 

Install Vagrant
~~~~~~~~~~~~~~~

After VirtualBox is installed, download and install Vagrant. Please refer to http://docs.vagrantup.com/v2/installation/index.html. 

Create PredictionIO VM
~~~~~~~~~~~~~~~~~~~~~~

Download PredictionIO Vagrant project.

    $ git clone https://github.com/PredictionIO/PredictionIO-Vagrant.git

Create PredictionIO Precise64 box.

    $ vagrant box add precise64 http://files.vagrantup.com/precise64.box

Start PredictionIO Server
~~~~~~~~~~~~~~~~~~~~~~~~~

    $ vagrant up

Vagrant will bring up the VM and setup the PredictionIO. Now you have a PredictionIO Server running!

Create an Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to create an administrator account to manage the newly installed PredictionIO Server. To do so, you have to ssh to the VM by running

    $ vagrant ssh

then in the VM, run:

    $ /opt/PredictionIO/bin/user


Accessing PredictionIO Server VM from the Host Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the administrator account, you can sign in PredictionIO admin panel through the host machine browser http://localhost:9000.

You can import data into PredictionIO with our REST API/SDK from your host machine through the API server http://localhost:8000 

In the default Vagrantfile setup, the ports 8000, 9000, 50030 and 50070 are forwarded from VM to the host machine.

* Port 8000 - PredictionIO API server
* Port 9000 - PredictionIO web admin server
* Port 50030 - Hadoop Job tracker
* Port 50070 - Hadoop Namenode


Shutdown Vagrant & PredictionIO Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To shutdown the VM without deleting any PredictionIO data, execute 

    $ vagrant halt

Later you can execute

    $ vagrant up 

again to bring up the PredictionIO VM.

You can completely remove the VM and delete all data with

    $ vagrant destroy

See http://docs.vagrantup.com/v2/getting-started/teardown.html for more details.
