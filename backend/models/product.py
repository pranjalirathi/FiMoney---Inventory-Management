from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    type = Column(String(50), nullable=False)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    image_url = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    
    
    # Foreign key to user who created the product
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationship
    creator = relationship("User", back_populates="products")
