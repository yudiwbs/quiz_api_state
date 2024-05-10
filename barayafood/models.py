from database import BaseDB
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Nullable, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy import Table
from sqlalchemy import DateTime


#import List


# cart adalah hubungan many to many
# Cart = Table(
#     "cart",
#     BaseDB.metadata,
#     Column("user_id", ForeignKey("users.id")),
#     Column("item_id", ForeignKey("items.id")),
#     Column("quantity",Integer, nullable=False)
# )

class Item(BaseDB):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer,nullable=False)
    img_name = Column(String)  # nanti diambil pake API
    

class User(BaseDB):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# masih gagal pengaturan foreign_key nya, todo kalau sempat
class Cart(BaseDB):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    

class Status(BaseDB):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status  = Column(String, nullable=False) # urutan: keranjang_kosong, belum_bayar, 
    #bayar, (pesanan_diterima atau pesanan_batal), pesanaan_diantar, pesanan_selesai
    timestamp = Column(DateTime, nullable=False, server_default=func.now(),index=True)
    
