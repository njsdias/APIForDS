### Build an API for check the Similarity between two texts - DS API

Resources:

- Register a new user

    - URL: /register
    - Method: POST
    - Parameters : username , password
    - status codes: 
      - 200 ok
      - 301 invalid username

- Detect similarity between two docs: Take off one token for each time always the user checks the similarity between two texts.

    - URL: /detect
    - Method: POST
    - Parameters : username , password, text1, text2
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
        
Since we need to compare the text among two documents we will use spacy python library. Spacy have your own moddels and it use a model already trained for NLP: en-core_web_sm-2.0.0.tar.gz. The website for download the model can be found searching in web by: spacy download models, or download it directly from github: 

    https://github/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz

After downloaded the previous file put it on folder /web .

**NOTE**: We prefere do not install spacy models from pip install because the server can breack any point , and for that we can prefere have the models locally available.




