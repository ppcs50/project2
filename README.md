# Project 2

Web Programming with Python and JavaScript

## a short write-up
This is a single page web application for chatting.



## each file description

### application.py
This is The main part and server side program file. It has two lists, which is to save each of them separately on the server side.
I made class call Messages to make it clear with those data correlated with messages, such as username, timestamp, and channel name.

index(): Routing index page.

generate_ch(channel_name): It gets channel_name and checks whether the name already exists or not. If not, it generates a channel by appends the name to the channel_list. Then, emit it to JS back.

chat(channel_name): Get a /<channel_name> page and return HTML script to the body. If channel_name is invalid, return Jsonifiied error message.

message(data): When it receives a message from JS side, use this data to append on the message_list, and then announce back to the JS side.


### index.html

When the page is opened, checks localStorage. If localStorage get items 'username' and 'channel_name' together, which is the record of the previous use, it retrieves it and uses it again.
There are a username input box and a log out button. They are dynamically changed by the situation.
It already has the sample channels which is named by three college houses in Harvard University.
When a user selects a channel any of them, it gets channel chatting page and previous record if it remained in the server side, message_list.
Only the data which has the same channel_name attribute will be retrieved.
When a user creates a channel, it checks whether the name has whitespace or not. If there are, it pops up the alert message.

### style.css

Little bit modified version for this application, originally from my previous CSS files.

### env.sh
### requirements.txt
### README.md

## just a comment
Since I always wanted to make an old-school chatting web application, I tried to make something special,
but lack of knowledge and skill, I have barely completed milestones. It was a challenging project for me. I had to feel frustrated every time.
I'm not satisfied with it. I spent every single minute on this project from the beginning even during the weekend, and I couldn't make it.