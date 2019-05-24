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
