## Implementation APP

First we need to download image file for MongoDB. For that we go to DockerHub to get the image of MongoDB.

- search for mongodb in https://hub.docker.com

Second open the terminal and inside of _db_ folder run the command: 

    touch Dockerfile

Using atom to edit the Dockerfile we need to specifiy the mongodb image. For that type:
  
    FROM mongo: 3.6.12

Now we need to define our _db_ service in _docker-compose.yml_ file as we did before for _web_ service

        db:
          build: ./db
          
But remember our _web_ service will depends of _db_ service because the _web_ wil use _db_ to store information. So, we need to add a link that coonect _web_ service to _db_ service. At the end your _docker-compose.yml_ file need to be equal to:

      version: '3'
      services:
        web:
          build: ./web
          ports:
            - "5000:5000"
          links:
            - db
        db:
          build: ./db

Since _web_ service depends of _db_ service the _db_ service is build in first and after that _web_ service is built.

Now we need to build a communication among _web_ and _db_ in our app.py. For that we need a library named as _pymongo_. So this library needs to be installed. And for that in file _requirements.txt_ add:

      pymongo
      
Now we need to build the project. In terminal run:

      sudo docker-compose build
