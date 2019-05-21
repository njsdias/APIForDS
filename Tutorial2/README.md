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
