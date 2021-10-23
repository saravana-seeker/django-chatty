# Chatty 1.0

Its intent to create for learn about django authentication and authorization management.You can Chat with Available Rooms and You can create Your Own room and chat with your Groups .I am using ajax pattern from https://github.com/tomitokko source to implement the chat room.!

# Setup
### Start a virtual environment
```
virtualenv venv
```

### Initialize the virtualenv
```
source venv/bin/activate
```
### Secret KEY
name the file .env in chatty folder
```
SECRET_KEY='SECRET_KEY'

```
### Install the requirements 
```
pip3 install -r req.txt
```
### Run the server
```
cd django-chatty/chatty
python3 manage.py migrate
python3 manage.py runserver
```
### Create SuperUser
```
python3 manage.py createsuperuser 
```

# Architecture

![chat](https://github.com/saravana-seeker/django-chatty/blob/main/images/login_with_chat.gif)

