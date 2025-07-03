from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

app =  FastAPI()

itms = []

class item(BaseModel):
    id : int 
    name:str
    category: str
    price: int
    date: datetime
    completed : bool



@app.post("/itms/")
def create_item(item : item):
    itms.append(item)
    return item

@app.get("/itms/{id}")
def get_item(item_id :int):
    for index, item in enumerate(itms):
        if item.id == item_id:
            return item

@app.get("/get_by_name_itms")
def get_item_by_name(item_name :str):
    for index in itms:
        if index.name == item_name:
            return itms
        else:
            return {"msg":"no items found"}
    
@app.get("/get_by_category_itms")
def get_item_by_category(item_category :str):
    for index in itms:
        if index.category == item_category:
            return itms
    

@app.get("/get_by_price_itms")
def get_price(item_price :int):
    for index in itms:
        if index.price == item_price:
            return itms

@app.get("/itms")
def get_date(item_date :datetime):
    for index in itms:
        if index.date == item_date:
            return itms
        

@app.get("/itms/")
def get_item():
    return itms

@app.put("/itms/{item_category}")
def update_item(item_category : str, updated_item : item):
    for index, item in enumerate(itms):
        if item.category == item_category:
            itms[index] = updated_item
            return updated_item
    return {"error": "item not found!"}


@app.delete("/itms/{item_category}")
def delete_item(item_category : str):
    for index, item in enumerate(itms):
        if item.category == item_category:
            itms.pop(index)
            return {"message" : "item deleted!"}
