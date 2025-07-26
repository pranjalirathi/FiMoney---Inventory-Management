from fastapi import FastAPI

from database import engine
from models.user import User
from models.product import Product

from routers import auth, users, products

User.metadata.create_all(bind=engine)
Product.metadata.create_all(bind=engine)


app = FastAPI(
    title="FiMoney API",
    description="A Financial Money Management API with Authentication",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def root():
    return {"message": "Welcome to the FiMoney API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
