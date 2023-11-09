import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    fullname: peewee.CharField = peewee.CharField(null=False, default='')
    balance: peewee.FloatField = peewee.Field(default=0)
    regular: peewee.BooleanField = peewee.BooleanField(default=False)


class AuthData(BaseModel):
    login: peewee.CharField = peewee.CharField(default="")
    password: peewee.CharField = peewee.CharField(default="")
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='auth_data_user_id', default=0)


class Staff(BaseModel):
    power_level: peewee.IntegerField = peewee.IntegerField(default=1)
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='staff_data_user_id', default=0)


class Product(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default="")
    price: peewee.FloatField = peewee.FloatField(null=False, default=0)


class UserOrder(BaseModel):
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_order_user_id', default=0)
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='user_order_product_id', default=0)


class Discount(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='discount_product_id', default=0)
    percent: peewee.FloatField = peewee.FloatField(null=False, default=0)
    active: peewee.BooleanField = peewee.BooleanField(default=True)


class Storage(BaseModel):
    address: peewee.CharField = peewee.CharField(null=False, default="")


class UserDiscount(BaseModel):
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_discount_order_user_id', default=0)
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='user_discount_product_id', default=0)
    percent: peewee.FloatField = peewee.FloatField(null=False)


class StorageOrder(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='storage_order_product_id', default=0)
    storage_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Storage, related_name='storage_order_storage_id', default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class ProductInStorage(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='product_in_storage_product_id', default=0)
    storage_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Storage, related_name='product_in_storage_storage_id', default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


db.create_tables([
    User,
    AuthData,
    Staff,
    Product,
    UserOrder,
    Discount,
    Storage,
    StorageOrder,
    ProductInStorage,
    UserDiscount
])
