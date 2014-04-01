========================================
Installing PredictionIO from Source Code
========================================


Building PredictionIO
---------------------

PredictionIO comes with a convenient build and packaging script.

.. code-block:: sh

    git clone https://github.com/PredictionIO/PredictionIO.git
    cd PredictionIO
    bin/build.sh
    bin/package.sh

After compilation and packaging are completed, a ready-to-run binary package will
be available at ``dist/target/PredictionIO-<version>``. Please follow the
instructions in :doc:`install-predictionio-on-linux` to set up PredictionIO.
