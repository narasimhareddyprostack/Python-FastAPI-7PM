from fastapi import FastAPI

app=FastAPI()


'''
usage: Application root Request
Rest API URL: http://localhost:8000/
Method Type : GET
Required Fields: None
Access Type: Public
'''
@app.get("/")
def indexpage():
    return {"message":"Index Page"} 

'''
usage: About Request
Rest API URL: http://localhost:8000/about
Method Type : GET
Required Fields: None
Access Type: Public
'''
@app.get("/about")
def aboutpage():
    return {"message":"About Page"} 


'''
usage: contact page Request
Rest API URL: http://localhost:8000/contact
Method Type : GET
Required Fields: None
Access Type: Public
'''
@app.get("/contact")
def contactpage():
    return {"message":"Contact Page"}