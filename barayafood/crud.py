from sqlalchemy.orm import Session
import models, schemas
import bcrypt

SALT = b'$2b$12$0nFckzktMD0Fb16a8JsNA.'

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# delete semua user
def delete_all_user(db: Session):
    jum_rec = db.query(models.User).delete()
    db.commit()
    return jum_rec

def hashPassword(passwd: str):
    bytePwd = passwd.encode('utf-8')
    pwd_hash = bcrypt.hashpw(bytePwd, SALT)
    return pwd_hash

############  untuk keranjang
def create_cart(db: Session, cart: schemas.Cart):
    db_cart = models.Cart(user_id = cart.user_id, item_id = cart.item_id, quantity = cart.quantity )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def delete_cart_by_id(db: Session, id_cart:int):
    hasil = db.query(models.Cart).filter(models.Cart.id == id_cart).delete()
    db.commit()
    return {"record_dihapus":hasil} 

# ada hapus semua cart berdasarkan user
# asumsikan kalau sudah selesai (sudah sampai ke user), isi cart dikosongkan
def delete_cart_by_userid(db: Session, id_user:int):
    hasil = db.query(models.Cart).filter(models.Cart.user_id == id_user).delete()
    db.commit()
    return {"record_dihapus":hasil} 


def get_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cart).offset(skip).limit(limit).all()

###

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashPassword(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

##==================== item

# ambil semua item
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# ambil item dengan id tertentu
def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


# ambil item yang cocok dengan keyword di deskripsi
def get_item_by_keyword(db: Session, keyword: str):
    #Artikel.Benennung.like("%"+prop+"%")
    return db.query(models.Item).filter(models.Item.description.ilike("%"+keyword+"%")).all()
    #return db.query(models.Item).filter(models.Item.like("%"+keyword+"%")).first()


# tambah item
def create_item(db: Session, item: schemas.ItemBase):
    db_item = models.Item(title=item.title, description = item.description, price = item.price, img_name = item.img_name )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# delete semua item
def delete_all_item(db: Session):
    jum_rec = db.query(models.Item).delete()
    db.commit()
    return jum_rec


# ============
# status
def delete_all_item(db: Session):
    ast_status = session.query(Status).order_by(desc(Status.created_at)).first()










# gagal euy
# def insert_cart(db:Session, cart: schemas.CartBase ):
#     #cart_record = models.Cart(user_id=cart.user_id, item_id=cart.item_id, quantity = cart.quantity)
#     user = db.query(models.User).filter_by(id=cart.user_id).first()
#     # Next, fetch the item from the database
#     item = db.query(models.Item).filter_by(id=cart.item_id).first()
#     # Append the item to the user's cart
#     user.cart.append(item)
#     #db.add(cart_record)
#     db.commit()
#     #db.refresh(cart_record)
#     return user



