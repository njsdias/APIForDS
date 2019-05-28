### Building a Bank API 

Suppose a Bank which have a safe-deposit box with a lot of money and you open different accounts in this Bank. Now we make a deposit in one bank account and you do money transfer between accounts. You can take a loan from the Bank. In this sense it will increase your cash as well your debit. Our API want to ensure the transactions between the accounts are corrected and is no problem.


**Resources**

- Register a new user

    - URL: /register
    - Method: POST
    - Parameters : username , password
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 302 invalid password

- Add: allows you to add money to bank account

    - URL: /add
    - Method: POST
    - Parameters : username , password, amount
    - status codes: 
      - 200 ok : return the similarity between two documents
      - 301 invalid username
      - 302 invalid password
      - 304 negative amount

- Transfer : transfer money between accounts

    - URL: /transfer
    - Method: POST
    - Parameters : username , password, to, amount
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 302 invalid password
      - 303 not enough money
      - 304 negative amount

- CheckBalance : 

    - URL: /balance
    - Method: POST
    - Parameters : username , password
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 302 invalid password
      
- Takeloan : 

    - URL: /takeloan
    - Method: POST
    - Parameters : username , password, amount
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 302 invalid password
      - 304 negative amount
 
- Payloan : 

    - URL: /payloan
    - Method: POST
    - Parameters : username , password, amount
    - status codes: 
      - 200 ok
      - 301 invalid username
      - 302 invalid password
      - 303 not enough money
      - 304 negative amount
    
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *    

## Building a Docker Compose from scratch
    
Inside of the main folder (i.e BankAPI) run the below commands
    
    touch docker-compose.yml
    mkdir web                            # where we develop our API
    mkdir db                             # to store in mongDB informations about the users among of them username and passwords
    touch web/Dockerfile
    touch web/app.py
    touch web/requirements.txt
    touch db/DockerFile
   


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
## Test the API

**To Run**: In the mail foler (TextSimilarity/) run:

    sudo docker-compose build
    sudo docker compose up

**Postman**: To test the API go to Postman

Here we can do a little diferent as usual. We write all entries for all roots (register, classify and register) and we will select one of them to see what happens. For each root only the fields that the root is expected are automatically read.

Now, select Body with option raw and JSON(application/json) and write:

    {
      "username": "user1",
      "password": "secure",
      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Zebra_standing_alone_crop.jpg/250px-Zebra_standing_alone_crop.jpg",
      "amount": 2
    }
    
For url adrress is only to search for a image in your web browser (for instance: zebra) and with right click select _Copy Image Address_.

Now we can select each root. 

- First test Register and for that select POST, and write:

       localhost:5000/register

After click on Send blue bottom you will receive the _"msg": "Successfully registration"_

- Now teste the Classify. Select POST and write:

        localhost:5000/classify
    
Click on Send blue bottom and wait a moment until the result appears:


We can see from the result the category with higher probability is zebra. So, it is what we expected the model do.
   

- For last test Refill. 

For that we need run classify more six times until receive the message _"Not enough tokens"_. After that select POST, and write:

       localhost:5000/refill
       
Now we add more 2 credits for the user and you after three using _/classify_ you will get the same message: _"Not enough tokens"_  .
