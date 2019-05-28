### Build an API for Image Recognition - DS API

This API uses Machine Learning for Image Recognition using TensorFlow using a trained model named as Inceptionv3.
The user sends the image to the API and the Machine Learning classifies the image as:

- Person
- Vegetable
- Famouse Person
- Animal
- Transport: cars, airplane, trains, etc.

**Resources**

- Register a new user

    - URL: /register
    - Method: POST
    - Parameters : username , password
    - status codes: 
      - 200 ok
      - 301 invalid username

- Classify: root for classify the image

    - URL: /detect
    - Method: POST
    - Parameters : username , password, image url (image from the internet)
    - status codes: 
      - 200 ok : return the similarity between two documents
      - 301 invalid username
      - 302 invalid password
      - 303 out of tokens

- Refill : allows the admin of the site to add tokens to the users

    - URL: /refill
    - Method: POST
    - Parameters : username , adm_pw, refill_amount
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 304 invalid admin password
    
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *    

## Building a Docker Compose from scratch
    
Inside of the main folder (i.e Tutorial4) run the below commands
    
    touch docker-compose.yml
    mkdir web                            # where we develop our API
    mkdir db                             # to store in mongDB informations about the users among of them username and passwords
        
Inside of folder \Tutorial4\db create a new file:
   
    touch Dockerfile
   
Inside of folder \Tutorial4\web create a new file:

    touch requirements.txt   
    touch Dockerfile
        
**Tensorflow**
For to classify the image using inceptionv3 we to create a new file with the name _classify_image.py_ with the contect that you will find in the Tensorflow repo:
    
    https://github.com/tensorflow/models/blob/master/tutorials/image/imagenet/classify_image.py
   
Inside of this file we need to find the localization of the model. And download the model from there (84.8 MB):

    DATA_URL = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'



* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
## Test the API

**To Run**: In the mail foler (TextSimilarity/) run:

    sudo docker-compose build
    sudo docker compose up

**Postman**: To test the API go to Postman

- Register: Select POST

       localhost:5000/register

select raw and JSON(application/json) and write:

    {
      "username": "test",
      "password": "secure",
      "url":
      "amount"
    }
click in SEND blue bottom and check if you receive the message: "Sentence saved successfully"

- Classify: Select POST

        localhost:5000/classify
    
select raw and JSON(application/json) and write:

    {
      "username": "User1",
      "password": "123",
      "text1": "This is a cute dog",
      "test2": "Wow. The dog is so cute!"
    }
   
click in Send blue bottom and check if you receive similarity ratio. if you send it for more six times you will get the satus error message: "Not enough tokens. Please,refill!!"

- Refill: Select POST

       localhost:5000/refill

select raw and JSON(application/json) and write:

    {
      "username": "User1",
      "password": "abc123",
      "refill": 4
    }

We can check if you can get similarity for four more time. Click in SEND blue bottom and check if you receive the message: "Sentence saved successfully" following the procedure _Detect_.
