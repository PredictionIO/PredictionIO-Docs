=========================
The Basic of PredictionIO
=========================

To add a predictive feature to your software with PredictionIO, first you need to add your app into PredictionIO Server. Then you choose and create 
an engine according to your prediction needs. You may select an appropriate algorithm for this engine.  Finally, you can retrieve prediction results after a data model is built.

Application
~~~~~~~~~~~

For each web or mobile app, you probably need to create one Application only. All data relating to app will be stored under this Application.

Engine
~~~~~~

In each Application, you can create multiple Engines. Each engine is responsible for one prediction need.
For instance, you may create one engine to recommend news to users and you create another one to help users to discover new friends.

Algorithm
~~~~~~~~~

In each engine, at least one algorithm must be deployed. 





Algorithm Evaluation
---------------------

Each type of engine comes with scientific evaluation metrics for you to evaluate and compare algorithms.  