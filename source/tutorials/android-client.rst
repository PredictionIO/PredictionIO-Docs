====================================
How to Run the Sample Android Client
====================================

In this tutorial, we will show you how to run the sample Android Client app.
It assumes that you have successfully installed and started PredictionIO
server and Hadoop. It would be better if you have read our quickstart guide
and know how to add an **App** and create an **Item Recommendation Engine**
in the web admin panel, which are just a few easy clicks.

.. note::
   This tutorial assumes that you have already setup an Android development
   environment with Eclipse, preferrably with the latest Juno packages.

1. Obtain the Source
--------------------
You can get the source code of this example by doing:

.. code-block:: console

    $ git clone https://github.com/PredictionIO/PredictionIO-Java-SDK.git

2. Install Apache IvyDE
-----------------------
If you have access to Eclipse Marketplace, installing Apache IvyDE will be
very easy, as shown.

.. image:: /images/android-ivyde.png

If you do not have access to Eclipse Marketplace, follow the instruction at
http://ant.apache.org/ivy/ivyde/download.cgi, and install Apache IvyDE via its
Eclipse update site.

3. Import Android Sample to Eclipse
-----------------------------------
Select **File > Import...** and choose **Android > Existing Android Code Into
Workspace**.

.. image:: /images/android-import.png

Navigate **Root Directory** to the Android sample path as shown above. Leave
everything else as default, and click **Finish**.

4. Resolve Dependencies with IvyDE
----------------------------------
At this point, you should see errors about unresolved types. Right click on
the project folder and select **Configure > Add Ivy dependency management**.

You need to tell Eclipse to consider libraries managed by Ivy. Right click on
the project folder again, and select **Build Path > Add Libraries...**.

Select **IvyDE Managed Dependencies** and proceed to the following screen.

.. image:: /images/android-addlib.png

Leave settings as default values and click **Finish**.

Right click again on the project folder, and select **Ivy > Resolve**. After a
while, type errors should go away.

5. Build Configuration
----------------------
For the final build to include Ivy managed libraries, an additional step is
required. Right click on the project folder and select **Build Path >
Configure Build Path...**.

.. image:: /images/android-buildpath.png

Make sure the entry **ivy.xml** is checked.

6. Run the Sample
-----------------
At this point, you should be able to run the sample in the emulator or on
actual hardware.

The source code is commented and should serve as a basic guideline on how to
use PredictionIO Java SDK in your Android app. Have fun predicting!

.. image:: /images/android-sample.png
