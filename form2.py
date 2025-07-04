from fastapi import FastAPI, HTTPException, Form
from typing import List, Optional

from pydantic import BaseModel , Field ,EmailStr, ValidationError

app = FastAPI()

forms = []

class Valid_form(BaseModel):
    id: int
    # name: str=Field(min_length=3, max_length=20)
    name:str
    email: EmailStr

# form = Form(id = 1, name = "Mayank" , email = "mayank@emaple.com")
# print(form) 

# try:
#     invalid_user = Form(id=2, name="Al", email="invalid-email")
# except ValidationError as e:
#     print(e)

@app.post("/form")
def create_from(form:Valid_form):
    print(len(form.name),"length of form is ")
    if len(form.name) < 3:
        return {"msg":"name length is too short"}
    elif len(form.name) > 20:
        return {"msg":"name is tooo large"}
    else:
        return form

@app.get("/form/{id}")
def get_form(form_id : int):
    for index, form in enumerate(forms):
        if form.id == form_id:
            return forms 