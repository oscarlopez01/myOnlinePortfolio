from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
#constructor    
    def __init__(self, username, password):
    
        self.host='mongodb://'+username+':'+password+'@127.0.0.1:27017/?authMechanism=DEFAULT&authSource=AAC'

        self.client= MongoClient(self.host)

        self.cursor= self.client['AAC']
        self.collection=self.cursor['animals']


#create in crud        
    def create(self, data):
        if data is not None:
            result = self.collection.insert(data) #data should be dictionary form
            return result
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
#read in crud
    def read(self, data):

        if data is not None:
            result = self.collection.find(data,{"_id":False})
            return result
    
#update in crUd       
    def update(self, search, data):

        if search is not None:
            if data is not None:
                myresult = self.collection.update_many(search, data)
                return myresult

        else:
            raise Exception("Document not found")

#delete in crud
    def drop(self, data):

        if data is not None:

            result = self.collection.delete_many(data)
    
            return result

        else:

            raise Exception("Document not found")


class ManageUser(object):
    """ Addd New Users and Activate, or deativate user"""

     def __init__(self, username, password):

        self.host='mongodb://'+username+':'+password+'@127.0.0.1:27017/?authMechanism=DEFAULT&authSource=AAC'

        self.client= MongoClient(self.host)

        self.cursor= self.client['AAC']


    #Create new user and enable active status for the animal database
     def createUser(self, data):

         #test if data is empty
        if data is not None:

            result = self.cursor.createUser(data)
    
            return result

        else:

            raise Exception("No Data was received")       


 #disable user 
     def updateUser(self, data):
    
        if data is not None:

            result = self.cursor.updateUser(data)
    
            return result

        else:

            raise Exception("No Data was received")  

 #drop user 
     def deleteUser(self, data):
    
        if data is not None:

            result = self.cursor.dropUser(data)
    
            return result

        else:

            raise Exception("No Data was received")  


