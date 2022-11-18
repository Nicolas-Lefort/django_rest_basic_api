# Django Rest Framework Basic API

A Web API allows communication between computers through internet.
They are typically used to decouple Back and Front end in web development.
Developers use Web APIs to query for a specific set of data from a server. 
A Client send requests in the form of an HTTP request or URL and a response message in JSONformat is sent back.
A REST API is a set of HTTP-based standards that control how different applications communicate with one another.
 
There are 4 basic methods, which are also referred to as CRUD operations: 
POST: Create a record.
GET: Read a record.
PUT: Update a record.
DELETE: Delete a record.

On python, you can build API with the help of FastAPI, Django Rest Framework of Flask.

DRF (Django Rest Framework) allows you to build an API in many different ways, from decorators till ModelViewSet.
In this folder, we set a basic API using the following:

- api_view        from rest_framework.decorators
- APIView         from rest_framework.views  
- GenericAPIView  from rest_framework.generics  
- ViewSet         from rest_framework.viewsets  
- ModelViewSet    from rest_framework.viewsets  



