# How do I get the API \(web\) app in my local computer?

You should now have a copy of this course repository in your  
local computer. The most important thing is to make sure your  
local copy is up to date with our version \(your Python instructors\).

If you are using GitKraken:  
1. Open GitKraken and make sure you are on the master branch of the `shefcodefirst-python-code`
repository (remember this is displayed on the top left corner of the app).
2. Click on the pull icon and you should then see the usual blue pop over saying your version is up to date.  
3. You are ready to go!

If you're using the command line:  
1. Navigate to your local copy of the repository  
2. Make sure your local copy is up to date by typing `git pull`  
3. That's it!

Once you have updated your local repository you should be able to see a `session5` directory \(see below\)

  
![struct](../assets/session5_struct.png)

The first thing we need to do is to make sure that you have the appropriate credentials to access the APIs. We are going to save these in the `config.py` file which will then be accessed by the app to authenticate the user.

## Setting your credentials
Create a new file named `config.py` and enter the following (replacing the 'XXXXX' with your
actual credentials):
```python
import os

# The following updates our config (environment) variables to have these values.

# Twitter API configs
os.environ["twitter_consumer_key"] = "XXXXX"
os.environ["twitter_consumer_secret"] = "XXXXX"
os.environ["twitter_access_token"] = "XXXXX"
os.environ["twitter_access_secret"] = "XXXXX"

# Spotify API configs
os.environ["spotify_client_id"] = "XXXXX"
os.environ["spotify_client_secret"] = "XXXXX"
```

Make sure to save your config file. Also it's super, super important that you **DO NOT add this to GitHub**.

Once you have your credentials we are going to need one more step. Go to your Spotify developers account where you created your app and got your keys. Find the input labelled as **callback uri** and type in : `http://127.0.0.1/5000/callback/`. Make sure to save the changes.

## Running the app

You should now be able to run the app and query all the 3 queries. On your terminal \(command line\) make sure to navigate to the app directory. You can confirm this by typing `ls` in the directory and you should be able to see the `app.py` fil as well as the `helpers, static and templates` directories.

Now you can do your usual `python app.py` open your web browser and navigate to `localhost:5000` and see the web app in action.

## Additional stuff

The three APIs have different levels of authentication:

* The NASA API performs queries using a `DEMO_KEY` meaning that you are not logged in but you can still perform queries
* The Twitter API will log you in using your credentials as we did in the class. Once you click on the Twitter icon it will redirect you to the query page and indicate who you are logged in as
* The Spotify API follows a 5 step authentication method. So once you click on the icon you'll be prompted to the familiar Spotify grant access webpage.
