=================================================
Installing PredictionIO with Vagrant (VirtualBox)
=================================================

Vagrant is an open source tool for simplifying the download and setup steps of
a virtual machine (VM) with VirtualBox. It is recommended for a quick
PredictionIO installation in a testing or development environment, as it will
save you from many of the common pitfalls of the installation process.


Installation
------------

To get started, please follow the steps below.


Install VirtualBox
~~~~~~~~~~~~~~~~~~

Download and install VirtualBox. Please refer to
https://www.virtualbox.org/wiki/Downloads.


Install Vagrant
~~~~~~~~~~~~~~~

After VirtualBox is installed, download and install Vagrant. Please refer to
http://docs.vagrantup.com/v2/installation/index.html.


Add precise64 Base Box
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

	$ vagrant box add precise64 http://files.vagrantup.com/precise64.box

This is the Vagrant base box in which PredictionIO will be installed.


Create and Start PredictionIO VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download `the latest release PredictionIO Vagrant project
<https://github.com/PredictionIO/PredictionIO-Vagrant/releases>`_ from
GitHub and unzip the file. The unzipped directory contains the necessary
Vagrantfile and scripts to setup PredictionIO in the VM.

Go to the unzipped directory ``PredictionIO-Vagrant-x.y.z/``
*(x.y.z is the version number)*:

.. code-block:: console

	$ cd PredictionIO-Vagrant-x.y.z/

Run:

.. code-block:: console

	$ vagrant up

.. note::

    The provision script ``pio-x.y.z-vagrant.sh`` is executed automatically
    as VM root user during the process of vagrant up. When you run
    ``vagrant up`` for the *first time*, it will install all necessary
    libraries and setup PredictionIO.

.. note::

    If you encounter error during importing key from *keyserver.ubuntu.com*,
    you may run ``vagrant destroy`` followed by ``vagrant up`` again to have
    a clean retry.

Now you have a PredictionIO Server running!


Create an Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to create an administrator account to manage the newly installed
PredictionIO Server. To do so, you have to ssh to the VM by running

.. code-block:: console

    $ vagrant ssh

then in the VM, run:

.. code-block:: console

    vagrant@precise64$ /opt/PredictionIO/bin/users

Follow the instructions to create an adminstrator account.


Accessing PredictionIO Server VM from the Host Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the administrator account, you can sign in PredictionIO admin panel
through the host machine browser http://localhost:9000.

You can import data into PredictionIO with our REST API/SDK from your host
machine through the API server http://localhost:8000.

In the default Vagrantfile setup, the host ports 8000, 9000, 50030 and
50070 are forwarded to the VM.

* Port 8000 - PredictionIO API server
* Port 9000 - PredictionIO web admin server
* Port 50030 - Hadoop Job tracker
* Port 50070 - Hadoop Namenode


Synced Folders Between the Host Machine and the VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the directory ``/vagrant`` on the VM is synced with the host
machine directory ``PredictionIO-Vagrant-x.y.z/`` so you can easily share
files between the host and the VM.

Please see http://docs.vagrantup.com/v2/synced-folders/index.html for more details.


Shutdown Vagrant & PredictionIO Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To shutdown the VM without deleting any PredictionIO data, execute

.. code-block:: console

    $ vagrant halt

Later you can execute

.. code-block:: console

    $ vagrant up --provision

to bring up the PredictionIO VM again.

.. note::

    If you are running Vagrant 1.3.x or above, you need to specify the
    --provision flag in order to load the provision script for subsequent
    vagrant up. If the --provision flag is not defined, you may need to
    start PredictionIO manually
    (Please see :ref:`vagrant-troubleshooting` at the end).

    If you are using Vagrant 1.2.x or older versions, the
    provision script is loaded even without the --provision flag.

You should see the following console output which indicates the PredictionIO
server is running properly:

.. code-block:: console

    Start PredictionIO ...
    Trying to start admin server... started
    Trying to start API server... started
    Trying to start scheduler server... started

.. note::

    The provision script should start the PredictionIO server. If it fails
    to start, you may try to stop and start PredictionIO manually
    (Please see :ref:`vagrant-troubleshooting` at the end).


You can completely remove the VM and delete all data with

.. code-block:: console

    $ vagrant destroy

.. note::

    The ``vagrant halt``, ``vagrant up`` and ``vagrant destroy`` commands
    should be run inside the directory ``PredictionIO-Vagrant-x.y.z/``.

See http://docs.vagrantup.com/v2/getting-started/teardown.html for more details.


.. _vagrant-troubleshooting:

Troubleshooting
~~~~~~~~~~~~~~~

The vagrant provision script should start PredictionIO server. If you
have problem starting PredictionIO and get the following error when run vagrant up:

.. code-block:: console

    Start PredictionIO ...
    Trying to start admin server... failed (9000 unreachable)

It's probably due to unclean shutdown of PredictionIO server. You may try to manually
stop and then start PredictionIO again and see if it fixes the problem.

To manually stop and start PredictionIO in VM (enter 'y' when it prompts for stopping or starting hadoop):

.. code-block:: console

    $ vagrant ssh
    vagrant@precise64$ /opt/PredictionIO/bin/stop-all.sh
    vagrant@precise64$ /opt/PredictionIO/bin/start-all.sh



