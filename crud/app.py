from fastapi import FastAPI

app=FastAPI()

""" Create
-------------
usage:create new employee 
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type:POST
Required Fields:eid,ename,esal
Access Type:Public """

@app.post("/emp/create")
def create_newemployee():
    return {"message":"New Employee Created"}


"""
Read
----
usage:fetch all employees  
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type:GET
Required Fields:None
Access Type:Public
"""
@app.get("/emp/read")
def get_Employees():
    return {"messge":"Fetching all employees"}



@app.get("/")
def index_page():
    return {"message":"Index Page"}