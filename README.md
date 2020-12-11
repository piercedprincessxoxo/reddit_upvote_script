Upvote script!
When you run this script it goes through an upvotes up to 20 of the users most recent posts in the last 24 hours.
The number of posts and number of hours can be updated (see below)
The users to upvote need to be added to the script. See instructions for doing this below.


Set up:

Windows
1. Open Command Prompt
2. Check if you have Python installed install it if not
Type 'python -V' into Command Prompt and hit enter (this asks it what version of python is installed)
if it says 'Python some version' youre good to go. If it shows an error youll need to install python

Install Python:
Type Python in command prompt and hit enter. It should open the intaller in the Windows store
or
Go to https://www.python.org/ > Downloads > Windows > Python (latest version) and run the installer.

Instal praw (Reddits Python API)

3. Update the script to work for you. You can open it in Notepad. Youll have to update the following settings:
- Add or remove any users you want to be able to upvote to the groups list. Be careful to type them exactly the way I have it. Ex. names need to be in quotes "like this". Add more groups if you want, with the memebers.
Add more friends if you want.
- replace MY_USERNAME with your reddit username
- replace MY_PASSWORD with your reddit password
- if you want to script to go back farther than a day edit lookback_hours to be the number of hours you want
- If you want the script to upvote more than the users last 20 posts update num_posts to be whatever number you want
- In order to allow the script to run you need to create a reddit developer 'app'. This step is just to get you the authentication information.
	- Log in to reddit them go to https://old.reddit.com/prefs/apps/
	- enter anything for name. Ex upvote_script
	- Select 'script'
	- Enter any description. Ex 'Script to catch up on upvoting my friends posts'
	- enter 'http://localhost:8080' in redirect uri (this is your computer's adress.)
	- click create app
	- copy the public keye and paste into the script to replace MY_PUBLIC_KEY
	- copy the secret key and paste into the script to replace MY_SECRET_KEY

3. Run script
Save the script file somewhere on your computer. Get the full file path. To do this you can right click on it in finder click 'properties' then copy the value next to Location. To run it open Command Prompt and type
'python fullfilepath'
ex 'python C:\users\princess\Documents\upvote_script.py'
This will run the script! It might take a little while. It will print out how many posts it has liked and by who, and let you know when its done!
If you want to know what posts specifically update the script. Where it says verbose = False, change this to True, and it will print out extra info when it runs!
