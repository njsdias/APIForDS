from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.Similarity     # create a new Database
users = db["Users"]        # create a new collection




def UserExist(username):
    if users.find({"Username": username}).count() == 0:
        return False
    else:
        return True
        
def verifyPw(username,password):  
    if not UserExist(username):
        return False

    # For the specific user find the password
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    #Compare the password
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

#To return the tokens of the users    
def countTokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens
    
    

class Register(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password

        # Check if the user does already exists
        if UserExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        # Encrypt password
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # Input in mongoDB the username, the password and the credits for tokens
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Tokens": 6
        })
        
        retJson = {
            "status": 200,
            "msg": "Successfully registration"
        }
        return jsonify(retJson)

class Detect(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        text1 = postedData["text1"]         # take the first string text
        text2 = postedData["text2"]         # take the second string text

        # Verify the user existence
        if not UserExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        # Verify the user password
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302,
                "msg": "Invalid Passowrd"
            }
            return jsonify(retJson)
        

        # Verify the number of tokens
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 303,
                "msg": "Not enough tokens. Please,refill!!"
            }
            return jsonify(retJson)

        # Calculate the edit distance between text1, text2
        nlp = scpay.load('en_core_web_sm')

        text1 = nlp(text1)
        text2 = nlp(text2)

        # Compare the two texts by evaluate the ratio. Closest to 1 more similare are the two files
        ratio = text1.similarity(text2)
        retJson = {
            "status": 200,
            "similarity": ratio,
            "msg": "similarity score calculated sucessfully"
        }
        return jsonify(retJson)

        # After compare texts we need subtract one token from the user
        current_tokens = countTokens(username)
        users.update({
            "Username": username,
        },{
           "$set":{
               "Tokens": current_tokens - 1
           }
        })

        return jsonify(retJson)


class Refill(Resource):
    def post(self):
        postedData = request.get_json()        # get information from mongoDB

        username = postedData["username"]      # take username
        password = postedData["admin_pw"]      # take password
        refill_amount = postedData["refill"]   # take password

        if not UserExists(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        correct_pw = 'abc123' # Only for demostration. The recommendation is store the pass inside of mongoDb as we do for the user
        if not password == correct_pw:
            retJson = {
                "status": 304,
                "msg": "Invalid admin Password"
            }
            return jsonify(retJson)

        #Make the refill
        users.update({
            "Username": username
        },{
            "$set":{
                "Tokens": refill_amount
            }
        })

        retJson = {
            "status": 200
            "msg": "Refilled successfully"
        }
        return jsonify(retJson)
    

#Api section
api.add_resource(Register,'/register')
api.add_resource(Detect,'/detect')
api.add_resource(Refill,'/refill')

if __name__ == "__main__":
    app.run(host='0.0.0.0')


        










        
        

