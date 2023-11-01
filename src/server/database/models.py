import peewee
import settings


db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    fullname: peewee.CharField = peewee.CharField(null=False)
    balance: peewee.FloatField = peewee.Field(default=0)
    regular: peewee.BooleanField = peewee.BooleanField(default=False)



class AuthData(BaseModel):
    login: peewee.CharField = peewee.CharField(null=False)
    password: peewee.CharField = peewee.CharField(null=False)
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='auth_data_user_id')


class Staff(BaseModel):
    power_level: peewee.IntegerField = peewee.IntegerField(default=1)
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='staff_data_user_id')


class Product(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False)
    price: peewee.FloatField = peewee.FloatField(null=False)


class UserOrder(BaseModel):
    count: peewee.IntegerField = peewee.IntegerField(null=False)
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_order_user_id')
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='user_order_product_id')


class Discount(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='discount_product_id')
    percent: peewee.FloatField = peewee.FloatField(null=False)
    active: peewee.BooleanField = peewee.BooleanField(default=True)


class Storage(BaseModel):
    address: peewee.CharField = peewee.CharField(null=False)


class UserDiscount(BaseModel):
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_discount_order_user_id')
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='user_discount_product_id')
    percent: peewee.FloatField = peewee.FloatField(null=False)


class StorageOrder(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='storage_order_product_id')
    storage_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Storage, related_name='storage_order_storage_id')
    count: peewee.IntegerField = peewee.IntegerField(null=False)


class ProductInStorage(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='product_in_storage_product_id')
    storage_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Storage, related_name='product_in_storage_storage_id')
    count: peewee.IntegerField = peewee.IntegerField(null=False)


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