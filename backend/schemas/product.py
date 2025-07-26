from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    type: str = Field(min_length=1, max_length=50)
    sku: str = Field(min_length=1, max_length=50)
    image_url: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    quantity: int = Field(ge=0)
    price: float = Field(gt=0)

class ProductCreate(ProductBase):
    pass

class ProductCreateResponse(BaseModel):
    product_id: int
    message: str

class ProductQuantityUpdate(BaseModel):
    quantity: int = Field(ge=0)

class ProductResponse(ProductBase):
    id: int
    created_by: int
    
    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int
    page: int
    size: int
    total_pages: int
