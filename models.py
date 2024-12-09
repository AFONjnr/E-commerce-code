import pydantic
from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
# from tortoise import Tortoise


# Tortoise.init(
#     {
#         "connections": {"default": "sqlite://db.sqlite3"},
#         "apps": {
#             "models": {
#                 "models": ["models", "aerich.models"], 
#                 "default_connection": "default",
#             },
#         },
#     }
# )


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200,null = False, unique = True)
    password = fields.CharField(max_length=100, null=False)
    Is_verified = fields.BooleanField(default=False)
    join_data = fields.DatetimeField(default=datetime.utcnow)



class Business(Model):
        id = fields.IntField(pk = True, index = True)
        Business_name = fields.CharField(max_length=20, null = False, unique = True)
        city = fields.CharField(max_length=100, null = False, default = "unspecified")
        region = fields.CharField(max_length=100, null=False, default= "unspecified")
        Business_description = fields.TextField(null = True)
        logo = fields.CharField(max_length=200, null=False, default= "default.jpg")
        owner = fields.ForeignKeyField("models.User", related_name="Business")



class Product(Model):
        id = fields.IntField(pk= True, index = True)
        name = fields.CharField(max_length = 100, null = False, index = True)
        category = fields.CharField(max_length= 30, index = True)
        original_price = fields.DecimalField(max_digits = 12, decimal_places = 2)
        new_price = fields.DecimalField(max_digits=12, decimal_places = 2)
        percentage_discount = fields.IntField()
        offer_expiration_date = fields.DateField(default = datetime.utcnow)
        product_image = fields.CharField(max_length = 200, null = False, default="productDefault.jpg")
        Business = fields.ForeignKeyField("models.Business", related_name = "products")



user_pydantic = pydantic_model_creator(User, name = "user", exclude = ("is_verified" , ))
user_pydanticIn = pydantic_model_creator(User, name = "userIN", exclude_readonly=True)
user_pydanticout = pydantic_model_creator(User, name = "userout", exclude=("password", ))

business_pydantic = pydantic_model_creator(Business, name = "business")
business_pydanticin = pydantic_model_creator(Business, name = "businessin", exclude_readonly=True)

product_pydantic = pydantic_model_creator(Product, name="product")
product_pydanticIn = pydantic_model_creator(Product, name="productIn", exclude=("percentage_discount", "id"))














