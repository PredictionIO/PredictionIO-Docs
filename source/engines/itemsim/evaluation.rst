===========================
Item Similarity: Evaluation
===========================

This engine comes with a evaluation metrics for you to compare the performance of algorithms and parameter settings for your specific use cases.
It uses a portion of the collected data to simulate test data. Evaluation is conducted offline.

ItemSim Mean Average Precision
------------------------------

Item Similarity Mean Average Precision (ISMAP@k), developed by PredictionIO, is a modified version of the standard MAP@k.
It evaluates how well an algorithm contributes to a prediction goal when the engine suggests similar items to users based on what they previously liked (or bought, viewed etc).
The higher the score, the better the algorithm is.

