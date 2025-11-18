from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def indexpage():
    return {"message":"Index Page"} 


@app.get("/about")
def aboutpage():
    return {"message":"About Page"} 



@app.get("/contact")
def contactpage():
    return {"message":"Contact Page"}