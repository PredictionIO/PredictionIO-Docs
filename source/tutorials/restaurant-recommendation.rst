===============================================
How to Build a Restaurant Recommendation Engine
===============================================

In this tutorial, we are building a unique recommendation engine on PredictionIO for a restaurant discovery app.
Sign into PredictionIO web admin panel using the administrator account you have created during installation.
Then follow these 5 steps:

Step 1: Add your App
--------------------

In the Applications page, add a new app by giving it a name, e.g. 'My Restaurant App', and click **Create**.

Step 2:  Obtain an App Key
--------------------------

Click **Develop** on 'My Restaurant App', and you will find the App Key.
This is the information you need when you integrate your app with PredictionIO SDKs later.

Step 3:  Create the Engine
--------------------------
Click **Add an Engine**. You will see the available engine types of PredictionIO.
In this example, we want to use 'Item Recommendation Engine' which can predict user preferences for items.
In our case, restaurants are the items.

Give your new engine a name, e.g. 'restaurant-rec', and click **Create**.

Now you have a working recommendation engine. You can start using it right away! 
If you can spare another minute with us, see how you can fine-tune this engine in 'Adjust Prediction Settings' (Step 4). Otherwise, skip to 'Start Using the Engine' (Step 5).

Step 4: Adjust Prediction Settings  (Optional)
----------------------------------------------

After your first engine is created, you will arrive at the Prediction Settings page.

1. Item Types Settings

    Here, you can define which types of items, i.e. Item Types, this engine should handle.

    With our example, we may assign a single item type 'restaurant' to all restaurants. But other item types such as 'cafe', 'bar', 'fast-food', 'casual' and 'fine-dining' may be assigned to individual restaurants.  

    If you want to this engine to only handle 'fast-food' and 'casual' types of restaurants, you should add 'fast-food' and 'casual' in the Item Types Settings area.

    By default, an Item Recommendation Engine would "Include ALL item types".

2. Recommendation Preferences

    Recommendation preferences of different applications vary. For a newsfeed application or a group buying site, it is more desirable to recommend new items to users; for our example of restaurant discovery app, you may not always need to recommend the newest restaurants.  You can fine-tune this engine in the Recommendation Preferences area.

3. Recommendation Goal

    You can adjust what to optimize with this engine in this area.

Step 5: Start Using the Engine
------------------------------

Ruby SDK is used in examples below.

    client = PredictionIO::Client.new(<appkey>)

1. Import your Data

    Import your users, items and behaviors data into 'My Restaurant App' through the API key that you have obtained:

    Add User

        client.acreate_user(<username>)

    Add Item (restaurant)
    
        client.acreate_item(<itemname>, <array_of_item_types>)
    
    Add Behavior

        client.auser_rate_item(<username>, <itemname>, <rating_from_1_to_5>)
    
    .. note::
    
      * Item Recommendation Engine uses previous user behavior data to predict users' future preferences. 
    
      * The data you import into 'My Restaurant App' will be shared among all engines you create.


2. Retrieve Prediction

    Item Recommendation Engine is trained/re-trained with new data every hour. 
    
    To predict top N restaurants that a user may like:
    
        client.get_itemrec_top_n(<enginename>, <username>, <N>)
    
    Item Recommendation Engine also supports location-based and item validity scenario.
    

Extra Step: Select and Tune Algorithms
--------------------------------------

An **Algorithms** tab can be found next to the **Prediction Settings** tab.
This is the place where you can fine-tune the underlying algorithm of the engine.
