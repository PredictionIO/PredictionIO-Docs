===================
Predictive Modeling
===================

Predictive modeling is a process by which a model is built (or trained) to predict future or unknown outcome. 
The accuracy and the performance of the model is determined by the algorithm you select as well as the parameter settings of this algorithm.

Every engine manages a predictive model independently in PredictionIO. In another word, there is one deployed algorithm running in each engine.

.. note::
  
    Depends on the implementation of the engine type, the system can train the model with the collected data in batch mode or in real-time.
    
     
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


Choose an Algorithm
-------------------

Algorithms can rely on very different assumptions and theories. There is no one-size-fit-all solution that is suitable for every prediction problem.
To improve prediction accuracy for your specific case, you may need to evaluate various combination of algorithms and parameter settings.
To learn more about it, read :doc:`optimization`.