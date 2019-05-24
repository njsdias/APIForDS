## Implementation of an API

Here we are update the API for a new one that is more close to the reality. 

For that we are to define some requirements for our API:

- Registration of a user 0 tokens

- Each user take 10 tokens

- Store a sentence on our database for 1 token

- Retrieve his store sentence on our databse for 1 token

## Chart for the new API

Some explanations.

- For a register user, the user will post him user name and password. The response is 200 ok.

- For store sentence we have three possiblties:

    - the user post a sentences and he still have tokens available for that and the response is: 200 ok
    
    - the user dont have more tokens available to post a sentences and the response is: 301 out of tokens
    
    - the user write a invalid username or password and the response is: 302 invalid username/password

- For retrieve sentence the situation is the same as the "store sentence"

![chart_api](https://user-images.githubusercontent.com/37953610/58331639-7c92bf00-7e31-11e9-8609-900961f28d64.JPG)

For register users we can add additional status code:

- when the user don't give the username

- when user don't give the password

- when the user try to sign in with and user that already exists in our database

## Additional information
   For passwords we are generating a hash code.
   If you know the password we can genetating a hash code.
   If you know the hash we can not generate or know the password associate on it.
   So, when the user give us the same password the same hash will be generated and we will compare the hash and not the password.
   So, we store the hash inside of database.
   To generate a hash code we will use the library Py-BCRYPT
   
           sudo apt install python-pip ->if you don't have the pip installed 
            pip install bcrypt
  
   On requirements.txt file stored in web folder we need add bcrypt to install in our container.
   
   
## Test the API
Save your files: requirements.txt and app.py.

In terminal write:

        sudo docker-compose build
        sudo docker-compose up

Open the postman and select POST

- To test the Register 
    - write: localhost:5000/register
    - select raw and JSON(application/json) and write:
    
            {
                "username": "User1",
                "password": "123xyz"
            }    
    - click in Send blue bottom and check if you receive the message: "You successfully signed up for API"
    
- To test the Store 
    - write: localhost:5000/store
    - select raw and JSON(application/json) and write:
    
           {
                "username": "User1",
                "password": "123xyz",
                "sentence": "This is my first sentence"
            }
     - click in Send blue bottom and check if you receive the message: "Sentence saved successfully"         
        

