from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working perfectly"}
products = [
    {"id": 1, "name": "Notebook", "price": 499, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Water Bottle", "price": 299, "category": "Home", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 99, "category": "Stationery", "in_stock": True}
]

# GET all products
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

# POST product
@app.post("/products")
def add_product(name: str, price: int, category: str, in_stock: bool):
    for p in products:
        if p["name"].lower() == name.lower():
            raise HTTPException(status_code=400, detail="Product already exists")

    new_product = {
        "id": len(products) + 1,
        "name": name,
        "price": price,
        "category": category,
        "in_stock": in_stock
    }
    products.append(new_product)
    return {"message": "Product added", "product": new_product}

# PUT update product
@app.put("/products/{product_id}")
def update_product(product_id: int, price: int = None, in_stock: bool = None):
    for p in products:
        if p["id"] == product_id:
            if price is not None:
                p["price"] = price
            if in_stock is not None:
                p["in_stock"] = in_stock
            return {"message": "Product updated", "product": p}

    raise HTTPException(status_code=404, detail="Product not found")

# DELETE product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return {"message": f"Product '{p['name']}' deleted"}

    raise HTTPException(status_code=404, detail="Product not found")