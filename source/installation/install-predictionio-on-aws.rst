=============================================
Deploying PredictionIO on Amazon Web Services
=============================================

Deploying PredictionIO on Amazon Web Services is extremely easy thanks
to AWS Marketplace. As long as you have access to AWS, you can launch a
ready-to-use PredictionIO Amazon EC2 instance with a single mouse click.


Prerequisites
-------------

* Amazon Web Services account
* Amazon EC2


Deployment
----------

To start using PredictionIO, please follow the steps below.


Access AWS Marketplace
~~~~~~~~~~~~~~~~~~~~~~

Visit PredictionIO product's page on AWS Marketplace using this
`link <https://aws.amazon.com/marketplace/pp/B00ECGJYGE>`_. Sign in with your
AWS account.


Using 1-Click Launch
~~~~~~~~~~~~~~~~~~~~

You should see the following screen after you have logged in.

.. image:: /images/awsm-product.png

Under the big yellow "Continue" botton, select the region where you want to
launch the PredictionIO EC2 instance, then click "Continue".

.. image:: /images/awsm-1click.png

Review your instance's settings before launching. For quick prototyping work,
we recommend using at least the "Standard Medium (m1.medium)" instance type.
For larger loads, use "Standard Large (m1.large)" or "Standard XL (m1.xlarge)".

The default security group, marked by "AutogenByAWSMP", has the following ports
opened to public:

* 22 (SSH)
* 7000 (PredictionIO Scheduler)
* 8000 (PredictionIO API)
* 9000 (PredictionIO Admin Panel)
* 50030 (Hadoop JobTracker)
* 50060 (Hadoop TaskTracker)
* 50070 (HDFS NameNode)
* 50075 (HDFS DataNode)
* 50090 (HDFS SecondaryNameNode)

.. warning::

    HTTP connection to admin panel at port 9000 is not encrypted. Do not use a
    password that you intend to protect your real data.

The default security group is intended only for quick prototyping work with the
least security for convenience. For production use, customize your security
group and protect your ports.

.. note::

    By using SSH dynamic port forwarding, it is possible to securely access
    your PredictionIO EC2 instance with only port 22 opened. Please refer to
    this `tutorial <http://getfoxyproxy.org/sshproxy.html>`_ for more
    information.

When you are done with settings, click the yellow "Accept Terms & Launch with 1-Click"
button.


Adding a User
~~~~~~~~~~~~~

It may take a while until the PredictionIO EC2 instance become ready. Once it
is ready, SSH to the instance and run:

.. code-block:: console

    $ /opt/PredictionIO/bin/users

Follow the on-screen instructions to add a user.


Start Using PredictionIO
------------------------

It may take a few minutes after the EC2 instance has launched for all
PredictionIO components to become ready. When they are ready, you may access
the admin panel at port 9000 and login using the account you have created.
