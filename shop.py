from fastapi import FastAPI, HTTPException
from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

app = FastAPI()

shop_items = []

class shop(BaseModel):
    c_id : int
    order : str 
    item_no: int
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
def get_shop_items_by_order(order :str):
    a = []
    for index in shop_items:
        if index.order == order.lower():
            a.append(index)
    return a    
        # else:
        #     return {"message":"Item not found"}

@app.get("/item_no_shop_items")
def get_shop_items_by_item_no (item_no:int):
    for index in shop_items:
        if index.item_no == item_no:
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
        

@app.get("/bill_sum")
def get_shop_items_sum(item1:int, item2:int):
    # amount = sum(e.bill for e in shop_items )
    x = 0
    y = 0
    for index in shop_items:
        if index.c_id == item1:
            print(index.c_id,"hello")
            x = index.bill
            
            print("x value is", x)
        if index.c_id == item2:
            y = index.bill

        sum = x+y
    return sum

    # return amount

@app.get("/item_no_sum")
def get_shop_items_sum(item_no1 :int ,item_no2 : int):
    x = 0
    y = 0
    for index in shop_items:
        if index.c_id == item_no1:
            print(index.c_id,"hello")
            x = index.item_no
            
        if index.c_id == item_no2:
            y = index.item_no

        total_item_no = x+y
    return total_item_no

@app.get("/total_item_no")
def get_total_item_no_sum():    
    total_item_no = sum(q.item_no for q in shop_items)
    return total_item_no



