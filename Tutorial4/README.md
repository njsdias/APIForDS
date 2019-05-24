### Build an API for check the Similarity between two texts - DS API

Resources:

- Register a new user

    - URL: /register
    - Method: POST
    - Parameters : username , password
    - status codes: 
      - 200 ok
      - 301 invalid username

- Detect similarity between two docs: Discount one token for each time the user checks the similarity between two texts.

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
    



