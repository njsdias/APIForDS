from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

# initialize the application
app = Flask(__name__)
api = Api(app)

# connect to mongoDb to database
client = MongoClient("mongodb://db:27017")
db = client.BankAPI                   # create a new Database
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

    correct_pw = verifyPw(username,password)
    if not correct_pw:
        return generateReturnDictionary(302,"Invalid Password"), True

    return None, False

def cashWithUser(username):
    cash = users.find({
        "Username": username
    })[0]["Own"]
    return cash

def debtWithUser(username):
    debt = users.find({
        "Username": username
    })[0]["Debt"]
    return debt
   

def updateAccount(username,balance):
    users.update({
        "Username": username
    },{
        "$set": {
            "Own":balance
        }
    })


def updateDebt(username,balance):
    users.update({
        "Username": username
    },{
        "$set": {
            "Debt": balance
        }
    })



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

        # Store in mongoDB the username, the password and the credits for tokens
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Own": 0,                   #how much money the user have
            "Debt": 0
        })
        
        retJson = {
            "status": 200,
            "msg": "Successfully registration"
        }
        return jsonify(retJson)


class Add(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        money = postedData["amount"]        # take amount

        
        retJson, error = verifyCredentials(username, password)

        if error
            return jsonify(retJson)
        
        if money <= 0:
            return jsonify(generateReturnDictionary(304,"The money entered must be >0."))

        #if money is greater >0
        cash = cashWithUser(username)               # this is the cash that user have 
        money -= 1                                  # for each transaction take 1 from user
        bank_cash = cashWithUser("BANK")            # verify the money in the BANK
        updateAccount("BANK", bank_cash + 1 )       # update account of the BANK adding 1 of the user
        updateAccount(username, cash + money )      # update user's account subtracting 1 

        return jsonify(generateReturnDictionary(200,"amount added successfully to account."))

class Transfer(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        to       = postedData["to"]
        money    = postedData["amount"]     # take amount

        retJson, error = verifyCredentials(username, password)

        if error:
            return jsonify(retJson)

        cash = cashWithUser(username)
        if cash <= 0:
            return jsonify(generateReturnDictionary(304,"You are out of the money, please add or take a loan."))

        if not USerExist(to):
            return jsonify(generateReturnDictionary(301,"Receiver username is invalid."))

        cash_from = cashWithUser(username)
        cash_to   = cashWithUser(to)
        bank_cash = cashWithUSer("BANK")

        updateAccount("BANK", bank_cash +1)
        updateAccount(to, cash_to + money -1)
        updateAccount(username, cash_from - money)

        return jsonify(generateReturnDictionary(200,"Amount transfer successfully."))
        

class Balance(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password

        retJson, error = verifyCredentials(username, password)

        if error:
            return jsonify(retJson)

        #Using projection in JSON
        retJson = users.find({
            "Username": username
        },{
            "Password":0,                 # I don't see the password
            "_id": 0                      # I don't see the password 
        })[0]                             # Display all rest information of the user
        
        return jsonify(retJson)

class TakeLoan(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        money    = postedData["amount"]   

        retJson, error = verifyCredentials(username, password)
        
        if error:
            return jsonify(retJson)

        cash   = cashWithUser(username)
        debt   = debtWithUser(username)
        updateAccount(username, cash+money)
        updateDebt(username, debt+money) 

        return jsonify(generateReturnDictionary(200,"Loan added to your account"))


class PayLoan(Resource):
    def post(self):
        postedData = request.get_json()     # get information from mongoDB

        username = postedData["username"]   # take username
        password = postedData["password"]   # take password
        money    = postedData["amount"]   

        retJson, error = verifyCredentials(username, password)
        
        if error:
            return jsonify(retJson)

        cash   = cashWithUser(username)

        if cash < money:
            return jsonify(generateReturnDictionary(303,"Not enough cash in your account."))
        
        debt   = debtWithUser(username)

        updateAccount(username, cash - money)
        updateDebt(username, debt - money) 

        return jsonify(generateReturnDictionary(200,"You've successfully paid your loan."))


#Api section
api.add_resource(Register,'/register')
api.add_resource(Add,'/add')
api.add_resource(Transfer,'/transfer')
api.add_resource(Balance,'/balance')
api.add_resource(TakeLoan,'/takeloan')
api.add_resource(PayLoan,'/payloan')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
