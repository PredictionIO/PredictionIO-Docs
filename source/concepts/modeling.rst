===================
Predictive Modeling
===================

Predictive modeling is a process by which a model is built to predict future or unknown outcome. 
The accuracy and the performance of the model is determined by the algorithm you select as well as the parameter settings of this algorithm.
In PredictionIO, each engine manages a model independently.

Algorithm
---------

Algorithm is sometimes called 'learning algorithm' in Machine Learning. It determines how your system learns to predict from data. 
Each type of engine in PredictionIO comes with different built-in algorithms available for use.
An algorithm is deployed with default parameters when you create a new engine. You can deploy another one to fit your needs.
 
Algorithm Parameter
-------------------

Some algorithms require you to specify parameter values. (They are sometimes referred to as hyperparameters in academic disciplines.) 
Parameters adjust how an algorithm learns. For instance, a regularization parameter tries to ensure that the model does not overfit its data. 
Some algorithms provide an automatic tuning feature to help you find better parameter settings. This feature requires a lot of computational resources though.

Evaluation 
----------

To choose between two algorithms and/or two sets of parameter settings, you need to evaluate how good they are objectively.
One of the best approaches is to create two engines to do an A/B test on their performance based on your prediction goal.
While this method is reliable, it requires you to conduct the experiment in production (or online) environment.
An alternative approach is to conduct a simulated (or offline) test using existing data. You assign a portion of the existing data as unseen test data and evaluate the prediction accuracy using some scientific metrics.
PredictionIO comes with offline evaluation tools for you to evaluate algorithms and parameter settings easily.   