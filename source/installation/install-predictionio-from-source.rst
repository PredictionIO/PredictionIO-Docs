=====================================
Install PredictionIO from Source Code
=====================================

Building Dependencies
---------------------

MongoDB Connector for Hadoop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PredictionIO depends on the release 1.1.0 of `MongoDB Connector for Hadoop
<https://github.com/mongodb/mongo-hadoop>`_. Unfortunately, it is not currently
published on the Central Repository and must be downloaded and compiled
manually.

.. code-block:: sh

    git clone https://github.com/mongodb/mongo-hadoop.git
    cd mongo-hadoop
    git checkout r1.1.0
    ./sbt publish-local

Building PredictionIO
---------------------

PredictionIO comes with a convenient build and packaging script.

.. code-block:: sh

    git clone https://github.com/PredictionIO/PredictionIO.git
    cd PredictionIO
    bin/build.sh
    bin/package.sh

After compilation and packaging are completed, a ready-to-run binary package will
be available at ``dist/target/PredictionIO-<version>``.
