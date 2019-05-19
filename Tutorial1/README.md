### Information of the Files

- add.py: it is the basics of the api with the JSON file that is used to send information between server/servers

- add2.py: it contains a basic API that do the four elementary math operations: add, subtraction, multiply and divided. In this file the important we two important things:
    - how we can send error messages to guide the user
    - how we can pass a value to the API


### Important Notes

When we access to a normal page 

- The Browser sends the request to the google.com and the google.com sends a response back whcih is the index.html that is the google structure.

- Browsers only communicate using only text. all communication between server/servers or server/browser all communication on internt can only be done only with text (even when we send a image or video it is a text). Because the internet is based in the protocol TCP thats only support text

When we send a image the information that is send is text that are numbers that represent RGB for each pixel which is in the image.

- JSON is one format that is used to send organize texts between server/servers or server/browser

This is a simple strucute of JSON file (file-> value). The last line dont have commma

{

  "field1": "abc",
  
  "field2": "def",
  
  "field3": 4,
  
  "array": [1,2,3,4, "abc"],
  
  "array of objects"
  
}


**JSON Files**
When we send arrays of objects we can send a array with objects that contais other objects, that is another JSON:

- array [objects(objects)]

{

  "field1": "abc",
  
  "field2": "def",
  
  "field3": 4,
  
  "array": [1,2,3,4, "abc"],
  
  "array of objects":[
    
    {
      "field1_of object_1": 1
    },
    
    {
      "field2_of object_2": "this is a string"
    }
    
  ]
  
  "array of nested arrays": [
    
    {
    
       "nested array": [
       
          {
          
           "field1":1
           
           "name": "Olchenback"
      
          } #End first object of first nested array
          
       ] # End first nested array
    
    } # End the objects inside array of nested arrays
   
    
    
  ] #End array Nested array
     
  
} #end JSON FILE


**Array of nested arrays**

This is the output of the first exmaple of JSON files

![json_example](https://user-images.githubusercontent.com/37953610/57933258-b2c1c300-78b4-11e9-9275-0772e6e6c225.png)

**Install Postman**

- sudo wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz

- sudo tar -xzf postman.tar.gz -C /opt

- sudo rm postman.tar.gz

- sudo ln -s /opt/Postman/Postman /usr/bin/postman

- run postman type in terminal: postman

## Error chart for app2.py

![error_chart](https://user-images.githubusercontent.com/37953610/57983413-7d021300-7a49-11e9-918b-2748b2c2929b.png)



