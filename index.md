## Code Showcase

### There are three artifacts that has played an important role in my education at SNHU.

First lets start with  a code review of this Artifacts:

## Artifact I
##### Code Review



In the course 330 Client Server, there were two final projects in the first Final Project the main objective was to create a CRUD file that would interact with a Mongo DB. Mongo DB is a no SQL database system. It is one of the new trends in technology that many companies are using to improve on the speed and create scalability to a higher level. In a typical relational database system, there are some drawbacks that hinder some of its scalability and development of complex database systems. For instance, relational database the records in a table must conform to having all the fields, if the record needs additional characteristics, you must add them to the table schema, whereas in Mongo DB the table is considered a collection of documents, the record is a Document, and each field or characteristic can be slightly different from one document to another. Simply put, the document could have a field or more different from another document and they can coexist in the same collection. In the relational model the fields of a record must exist for all the records. Moreover, related data in the traditional relational model must be organized in different table, in Mongo the document has all the related tables in the same document, and they could be queried just as well. In Mongo DB the documents are stored in Json style object such as: 
```json
{ “docid”:123,
	   “firstname”:”Oscar”,
   “lastname”:”Lopez”,
   “address”:[
	           {  “type”:”Billing”,
		“street”:”18900 West Park Drive”,
		“street2”:”Suite 4104”,
		“city”:”Miami”,
		“state”:”FL”,
		“zip”:”33189”
	           },
	           {  “type”:”Billing”,
		“street”:”18900 West Park Drive”,
		“street2”:”Suite 4104”,
		“city”:”Miami”,
		“state”:”FL”,
		“zip”:”33189”
	           }
	],
       “phone”:”786-331-7897”
}
```
Once the CRUD Class was finalized, the class was used to build a tool that would allow rescue animal trainers to connect to a national database of animal from shelters all over the USA so that they can locate animals that can be trained for the purpose of performing search and rescue operations. The rescue operations could be in any terrain and location. To enhance this artifact, I have created a class that admin users can create new users for their location. The admin users will be able to create users and modify the status of their users to inactive or delete users.
The class is simple but adds a great functionality, by allowing each location to manage their own list of users.


<video src="https://oscarlopez01.github.io/myOnlinePortfolio/artifacti.png" controls="controls" muted="muted" ></video>


## Artifact II
Code Review
![](CapstoneProject_final-1.mp4)

In the course 330 Client Server, the second final project was to deploy a web interface to the back-end mongo database. The interface was develop using Dash from plotly. Dash is a framework that helps deploy fast web applications using very little code. The framework allows for fast deployment and easy to navigate. Further, it has many built in libraries that makes prototyping an excellent tool. Combine with Jupyter Notebook, makes conceptual applications into real testable interfaces.

In this improvement we are going to take the backend and use the Django framework to recreate the application again. We are going load the elements needed to query the Mongo DB to search for the types of dogs that can be used for search and rescue. Second we are going to load a map reflecting the different coordinate points for each document.


##### Download project here
https://oscarlopez01.github.io/myOnlinePortfolio/cs340_improve.zip


