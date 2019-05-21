## Objective

The main objective is improve the app.py builded to do the four elementary operations: add, subtraction, division, multiplication.

Here we are build a MongoDB database to store how many times the user requires an operation. If the same user have more than five requirements the app blocks the access. In other words, an user have a limite of five requirements. For that the user can provide the UserName(User) and the PassWord(PW) to the app controls how many times the app was required by user. This information will be stored in a MongoDB databse.

## MongoDB

The next table mkes the correlations among a Relational DB with a MongoDB. For instance we can see that in a **RBMS** a **Table** is compound by **Rows** and **Colunms**. But in a **MondoDB** a table is a Collection. In MondoDB, **Collections** is compounded by **Documents** and **Fields**. 


![RDMS_MongoDB](https://user-images.githubusercontent.com/37953610/58112126-be7df400-7bea-11e9-9da1-8efb24a95417.png)

![doc_MB](https://user-images.githubusercontent.com/37953610/58112767-0d785900-7bec-11e9-8137-651067eed5fb.png)



The **id** field in the MongoDB means the primary key of the Collection. This primary key is a 12 bytes hexadecimal number which assures the uniqueness of every document and it is build as:

- 4 bytes for the current timestamp
- next 3 bytes for machine id
- next 2 bytes for process if od MongoDB server
- last 3 bytes are simple incremental VALUE

In general, in a Relational DB we have a schema that shows a number of tables and the relashionship between these tables. While in MongoDB, there is no concept of relationship.

**Advantages of  MongoDB over RDBMS**

  1 - Schema Less - MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.
  
  2 - Structure of a single object is clear
  
  3 - No complex joins
  
  4 - Seep query-ability: MongoDB supports dynamic queries on documents using a document based query language that's nearly powerful as SQL (Relational DB).
  
  5 - Tuning
  
  6 - Ease of scale out: MongoDb is easy to scale
  
  7 - Conversion/mapping of application objects to databse objects not neeeded. 
  
  8 - Uses internal memory for storing the (windowed) working set, enabling faster access of data.
  
  **Where to use MongoDB?**
  
   1 - Big Data : sclable and fast
   
   2 - Content Management and Delivery
   
   3 - Mobile and Social Infrastructure
   
   4 - User Data management
   
   5 - Data Hub
   
**Install MongoDb on Ubuntu 18.04 LTS**
   
Go to site and follow the instructions:

   https://websiteforstudents.com/install-mongodb-on-ubuntu-18-04-lts-beta-server/
   
Or simple copy and past in your terminal the next set of commands:

  1 - sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
  
  2 - echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
  
  3 - sudo apt update
  
  4 - sudo apt install -y mongodb-org 
  
  5- Run one of the next commands in according with your objective
  
    - sudo systemctl stop mongod.service
    - sudo systemctl start mongod.service   (for start MongoBD)
    - sudo systemctl enable mongod.service
   
 6 - sudo systemctl status mongod    (to see the status)
 
 ![mongoinst-1](https://user-images.githubusercontent.com/37953610/58115754-ac07b880-7bf2-11e9-963a-6aeed7847b02.png)
 
 7- To run MongoDB type in terminal only: mongo
 
 8 - To see the options: db.help()
 
 9 - To see the status:  db.status()
 
 10- To see the version of MongoDB: db.version()
 
 ![version_mongoDB](https://user-images.githubusercontent.com/37953610/58115875-e8d3af80-7bf2-11e9-93d3-d192c01f2ee7.png)
 
 ## Representation of the same problem in Relational DB and in a MongoDB
 
 **Problem Definition**
 
 Suppose a client needs a database design for his blof/website and see the differences between RDBMS and MongoDB schema design. Website has the following requirements:
 
 - Every post has the unique title, description and url
 
 - Every post can have one or more tags
 
 - Every post has the name of its publisher and total number of likes
 
 - Every post has comments given by users along with their name, message, data-time and likes
 
 - On each post, there can be zero or more comments.
 
 **Relation Database**
 
 ![RDB-Prob1](https://user-images.githubusercontent.com/37953610/58119602-45d36380-7bfb-11e9-81c5-432cc81c9174.png)
 
 **Mongo DB**
 
 ![Mongo-Prob1](https://user-images.githubusercontent.com/37953610/58119629-4ff56200-7bfb-11e9-90f4-af7c3ecc9232.png)
 
 ## First Commands in MongoDB
 
 - _use nameDB_ : Create an non-existence DB or use a existent DB
 
 - _db_ : To check your currently selected database
 
 - _show dbs_ : To check your databases list
 
 **Note:** Your db created only appears on the list after you insert at lesat one document into your created db:
 
      db.movie.insert({"name":"tutorial"})

After you insert a document use _show dbs_ command to see your db in the list. 

**Attention:** As default the MongoDB creates a db named as test. If you didn't create any databse, then collections will be stored in the test database. 

  - _db.dropDatabase()_ : To drop a exisiting database. If you have not selected any database, then it will delete default 'test' database.
  
        use mydb                # use the DatabSe mydb
        db.dropDatabase()       # drop the Dtabase mydb
        show dbs                # check if the Database was dropped 
