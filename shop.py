from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

app = FastAPI()

shop_items = []

class shop(BaseModel):
    c_id : int
    order : str 
    order_itemno : int
    bill : int 
    date : datetime
    completed : bool

@app.post("/shop_items/")
def create_item(shop : shop):
    shop_items.append(shop)
    return shop

@app.get("/shop_items")
def get_shop_item(c_id : int):
    for index, shop in enumerate(shop_items):
        if shop.c_id == c_id:
            return shop_items
        
@app.get("/order_shop_items")
def get_shop_items_by_order(order : str):
    for index in shop_items:
        if index.order == order.lower():
            return shop_items
        else:
            return {"message":"Item not found"}

@app.get("/order_itemno_shop_items")
def get_shop_items_by_order_itemno(order_itemno : int ):
    for index in shop_items:
        if index.order_itemno == order_itemno:
            return shop_items        

@app.get("/bill_shop_items")
def get_shop_items_by_bill(bill : int):
    for index in shop_items:
        if index.bill == bill:
            return shop_items
        
@app.get("/date_shop_items")
def get_shop_items_by_date(date : datetime):
    for index in shop_items:
        if index.date == date:
            return shop_items
        
