from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

item_list = [
    {"id": 1, "name": "PC"},
    {"id": 2, "name": "Keyboard"},
    {"id": 3, "name": "Mouse"},
    {"id": 4, "name": "Mousepad"},
    {"id": 5, "name": "Monitor"},
]


@app.get("/")
def read_root():
    return {"message": "Hello, World"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(gt=0)):
    for item in item_list:
        id = item.get("id")
        if id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
