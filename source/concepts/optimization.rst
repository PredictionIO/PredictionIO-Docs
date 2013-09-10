=====================
Accuracy Optimization
=====================

Prediction accuracy of an engine is affected by a number of factors, such as:
* the quality and quantity of data collected
* algorithm
* algorithm parameter settings

PredictionIO provides evaluation tools for you to select better algorithm and optimize parameter settings. 

Evaluation 
----------

To choose between two algorithms and/or two sets of parameter settings within an engine, you need to evaluate how good they are objectively.
One of the best approaches is to create two engines to do an A/B test on their performance based on your prediction goal.
While this method is reliable, it requires you to conduct the experiment in production (or online) environment.
An alternative approach is to conduct a simulated (or offline) test using existing data. You assign a portion of the existing data as unseen test data and evaluate the prediction accuracy using some scientific metrics.
PredictionIO comes with offline evaluation tools for you to evaluate algorithms and parameter settings easily.   


Evaluation Metrics
-------------------

One or more metrics is provided in each engine type.

First, you add the algorithms (and parameter settings) you want to compare in the web admin panel.
Then you can run a simulated evaluation with a specified metrics on these algorithms using your existing data. 
A number score will be assigned to each algorithm based on their performance on a metric-specified prediction goal.
In most cases, the higher the score, the better the algorithm is.

.. note::
  
    Offline evaluation is a computationally expensive process. Depends on your data size and other factors, it can take a very long time.
    