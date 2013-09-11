================================
Item Similarity: Engine Settings
================================

You can specify the following settings on the web admin panel.

* Item Types Settings
  
  * Selected Item Types
  
    If you have more than one type of item data in your app, you can limit an engine to access certain type(s) of items. 
    This feature is useful especially when you want different engines to handle the similarity estimation of different types of items.
    
* Recommendation Preferences

    * Freshness
      
      Specify whether the engine should give priority to newer items in its top N ranking. A value of 0 to 10. 10 means you prefer newer items the most. 
      
    * Serendipity
    
      Specify whether the engine should try to surprise users with unexpected suggestion. 
      Currently it is achieved by adding randomness to the top N list. This feature is useful when a discovery experience is more important than accuracy.  
      A value of 0 to 10. 10 means you prefer pleasant surprise the most.
      
* Prediction Goal

  Define the goal you want to achieve through suggesting similar items. Some algorithms may try to maximize this goal.