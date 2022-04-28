# Profanity Bot
This is a Discord bot that identifies messages sent to it which contain profanity.


## Requirements
This project uses Docker and Docker Compose. Please install them before continuing.
Also, you must have a Discord bot set up in order to use this program.


## Setup
First, create a ```.env``` file inside the ```profanitybot``` directory.
Then, add the token from your Discord bot to ```DISCORD_TOKEN```, as shown below:
```
DISCORD_TOKEN=[token goes here]
```

Then, run ```docker-compose up -d --build``` to build the image and run the container.


## How to Use
Once the container is running, send a message to the Discord bot. It will only respond
to you if your message contains any profanity.
