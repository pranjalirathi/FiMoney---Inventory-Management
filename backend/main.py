from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"],  # React dev server URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)


@app.get("/", tags=["Root"], summary="Root Endpoint")
def root():
    return {"message": "Welcome to the FiMoney API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
