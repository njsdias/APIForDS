from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import requests                        #to get the hrl that the users sends
import subprocess
import json


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.ImageRecognition          # create a new Database
users = db["Users"]                   # create a new collection



#---->>>> def Section
def UserExist(username):
    if users.find({"Username": username}).count() == 0:
        return False
    else:
        return True

def generateReturnDictionary(status, msg):
    retJson = {
        "status": status,
        "msg": msg
    }
    return retJson

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

def verifyCredentials(username, password):
    if not UserExists(username):
        return generateReturnDictionary(301,"Invalid Username"), True

    correct_pw = verify_pw(username,password)
    if not correct_pw:
        return generateReturnDictionary(302,"Invalid Password"), True

    return None, False
    
    
#---->>>> Class Section   
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


class Classify(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        url = postedData["url"]              # take url

        
        retJson, error = verifyCredentials(username, password)
        if error
            return jsonify(retJson)
    
        # Verify the number of tokens
        num_tokens = countTokens(username)

        tokens = users.find({
            "Username":username
        })[0]["Tokens"]

        if tokens <= 0:
            return jsonify(generateReturnDictionary(303,"Not Enought Tokens!"))

        
        r = requests.get(url)   # Get the Image from URL
        retJson = {}
        # Put the URL image in the file temp.jpg
        with open("temp.jpg","wb") as f:
            f.write(r.content)
            proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg')
            proc.communicate()[0]
            proc.wait()
            with open("text.txt") as g:   # the end results will be saved in text.txt and it 
                retJson = json.load(g)    # will be downloaded as a json file

        # we need modify our classify_image.py to turn it available to save the results in json format.
        # Below are the code modified and you to do this chances in your classify_image.py 
        """
        top_k = predictions.argsort()[-FLAGS.num_top_predictions:][::-1]
        retJson = {}
        for node_id in top_k:
          human_string = node_lookup.id_to_string(node_id)
          score = predictions[node_id]
          retJson[human_string] = score
          print('%s (score = %.5f)' % (human_string, score))
        with open("text.txt") as f:
          json.dump(retJson, f)
        """

        users.update({
            "Username": username,
        },{
           "$set":{
               "Tokens": tokens - 1
           }
        })

        return jsonify(retJson)
        
class Refill(Resource):
    def post(self):
        postedData = request.get_json()        # get information from mongoDB

        username = postedData["username"]      # take username
        password = postedData["admin_pw"]      # take password
        amount = postedData["amount"]   # take refill

        if not UserExists(username):
            return jsonify(generateReturnDictionary(301,"Invalid Username"))

        correct_pw = 'abc123' # Only for demostration. The recommendation is store the pass inside of mongoDb as we do for the user
        if not password == correct_pw:
            return jsonify(generateReturnDictionary(304,"Invalid Admin password"))

       
        users.update({
            "Username": username
        },{
            "$set":{
                "Tokens": amount
            }
        })


        return jsonify(generateReturnDictionary(200,"Refilled Successfully"))


#Api section
api.add_resource(Register,'/register')
api.add_resource(Detect,'/classify')
api.add_resource(Refill,'/refill')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
