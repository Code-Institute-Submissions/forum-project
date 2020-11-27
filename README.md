# Forum Project
This project is a forum made to exchange ideas and opinions. This forum is built in a way that you can shape your topics in anyway you want. Once the framework in categories is defined you can add any topic you want. WIth every topic you can post, read, edit and delete comments. The edit and delete function is (of course) only available for your own comments. 
This website is simple, easy and very straightforward to use with no (commercial) distractions whatsoever.
Moreover, the user is alway notified whether an action is successful or not.

## UX
This site is built for everybody to share their opinions and ideas within an interested community. The forum is presented by category. Within each category you can find several topics and in every topic you'll find the relevant comments.
You can easily navigate through the site.
As a user,:
- I want to be able to easily register an account with clear instructions.
- I want to be able to use CRUD operations on a comment
- I want to be able to create a topic
- I want to be able to see my own created topics
- I want to easily navigate through the site
- I want to be able to change my image
- I dont want to be distracted by anything other than the topic/comments to keep focused
- I want to be able to read previous comments while writing my own comment so it's easy to reply to someone
- I don't want a bright screen shining in my face while trying to read. My eyes are more relaxed when looking at a dark page while trying to read something.

## Features 
- Users don't need to log in to read the content of the page
- Register allow users to make an account and have a profile picture if they want to
- Create Topic allows users to start a topic of their own with any text they like
- Log in allows users to be albe to CRUD on their own comments instead of only read
- Profile shows you the topics you have created and the abillty to change your profile picture
- Homepage by clicking on logo
- Error handler when something goes wrong you dont really see the error but you get redirected to the homepage
- I have dark colors throughout the whole page to make it nicer to read
- Nothing is in place that might distract you from reading and keeping your mind on the topic

### Features left to implement
- Private messages



Technologies Used
- bson==0.5.10
- DateTime==4.3
I used Datetime to get the date and time when a topic or comment is edited/posted and display it to the screen
- dnspython==2.0.0
- Flask==1.1.2
- Flask-PyMongo==2.3.0
- Werkzeug==1.0.1
I used werkzeug to save my passwords to the database which are unable to traceback
- Materialize
- Font awesome

## Testing
### Create topic
	I Filled out the create topic form and submitted it to check if
	- The session user is the author, If the text is displayed correctly
	- and if the topic is registered to the right category selected
	- Date last edited updates if a comment is posted/edited
### Register
I filled out the register page with multiple times with different condition to check:
	- If the username is saved correctly
	- You cannot have duplicate usernames
	- The password is saved "hashed" to the database
	- A correct URL for images displays the image correctly on all sizes
	- Without an URL the default avatar is displayed
	- With a wrong URL an ALT altibrute is in place, if the user submits a wrong URL for an 
	image there won't be an image this displayed, this is considered a user error you can 	fix yourself
### Log  in
	- I checked if the user who logs in is the session user
	- I checked if the comparing hash password works for security
	- I checked if you can log in without any issues

### Log out
	Checked if you are no longer the session user
### Comments
	- if you can write a comment if you are not logged in(you cant)
	-  if the comment is displayed they way a user formats it
	- if the comment will be deleted if you click the garbage can
	- if the comment can be edited
	- if only the author of the comment can edit/delete it
	- if the date updates correctly to time of edit
### Profile
	Checked if you can see your own topics
	If you can change your profile picture
	If your own username is displayed

### Browser Testing
    Checked if everything works on mobile, tablet and pc as intended with the following browsers:
    - Safari
    - Microsoft Edge
    - Firefox
    - Chrome


### Deployment

1 I created a Procfile to tell Heroku which language im using, how to run it and that it's a website
2 I created a requirements.txt with pip freeze to tell heruko which libarys are needed to run my website
3 I set the values from my env.py in the Heroku config vars to connect with my database
4 I logged in with heroku on gitpod and pushed everything to Heroku

## Content
- 154-206, 233-238 : This code was coppied from TravelTim form Code Institute examples
- All other code was written by myself or part of materialize

## Media
The logo was made in paint
The default user avatar is a URL I got from google images
All other media is inserted by the users
Acknowledgements
Code institute support, Thanks to all the Tutors helping me out when I asked them to even though they usually dont give me direct answers it always helps alot