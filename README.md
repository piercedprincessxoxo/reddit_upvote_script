# Reddit Upvote Script
I created this script to help other SWs with promotion on reddit. But it can be repurposed for anyone wanting an easy way to upvote and support their friends.

When you run this script it goes through and upvotes up to 20 of your friends most recent posts in the last 24 hours.
The number of posts and number of hours can be updated (see below)
The users to upvote need to be added to the script. See instructions for doing this below.

This README is meant to help users with no technical knowledge run this script. All you need is a laptop! Feel free to reach out if you have any questions on how to make this work.


## Set up:

#### Install Dependencies
1. Open a cli. For windows this is Command Prompt. For Mac this is terminal.
2. Check if you have Python installed install it if not
Type `python -V` intoypur CLI and hit enter (this asks it what version of python is installed)
if it says 'Python some version' youre good to go. If it shows an error you'll need to install python

3. Install Python:

 For windows: Type `Python` in command prompt and hit enter. It should open Python in the Windows store. Just click install!

 or

 Go to https://www.python.org/ > Downloads > Windows > Python (latest version) and run the installer.

4. Instal praw (Reddits Python API)

 Enter the following in the CLI: `pip install praw` and hit enter
 
 5. Install this script! In your cli enter:
 

#### Update the script with your information

 Update the script to work for you. This means editing the file reddit_upvote_script.py. Click open with > Notepad. (unless you have an IDE then use that) Youll have to update it in a few place. I've includes comments in the file itself to walk you through this!
* Add or remove any users you want to be able to upvote to the groups list. Be careful to type them exactly the way I have it. Ex. names need to be in quotes "like this". Add more groups if you want, with the memebers.
Add more friends if you want. Please leave me in the friends list, this way youll upvote my posts when you run it too. <3
* replace MY_USERNAME with your reddit username
* replace MY_PASSWORD with your reddit password
* if you want to script to go back farther than a day edit lookback_hours to be the number of hours you want
* If you want the script to upvote more than the users last 20 posts update num_posts to be whatever number you want
* In order to allow the script to run you need to create a reddit developer 'app'. This step is just to get you the authentication information to be able to make calls to the Reddit API.
  * Log in to reddit then go to https://old.reddit.com/prefs/apps/
  * enter anything for name. Ex upvote_script
  * Select 'script'
  * Enter any description. Ex 'Script to catch up on upvoting my friends posts'
  * enter 'http://localhost:8080' in redirect uri (this is your computer's adress.)
  * click create app
  * copy the public key and paste into the script to replace MY_PUBLIC_KEY
  * copy the secret key and paste into the script to replace MY_SECRET_KEY

## Run script (once a day or whenever you want to catch up!)
Save the script file somewhere on your computer. Get the full file path. To do this you can right click on it in finder click 'properties' then copy the value next to Location. To run it open Command Prompt and type
`python "fullfilepath"` replace fullfilepath with your filepath!
ex `python "C:\users\princess\Documents\upvote_script.py"`
This will run the script! It might take a little while. It will print out how many posts it has liked, in which group, for which user, and let you know when its done!
If you want to know what posts specifically update the script. Where it says verbose = False, change this to True, and it will print out extra info when it runs!

Thats it! Feel free to reach out to me with any questions. <3

## Troubleshooting errors

prawcore.exceptions.OAuthException: invalid_grant error processing request
- check your log in info

received 401 HTTP response
- Check your client secret & app ID

ModuleNotFoundError: No module named 'praw'
- Did you remeber to download praw?

Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
- Did you install python?
