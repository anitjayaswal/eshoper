from django.db import models

# Create your models here.

class mobiles(models.Model):
     task_id = models.AutoField(primary_key=True)
     product_id = models.CharField(max_length=100)
     title = models.CharField(max_length=100)
     target_link = models.TextField()
     selling_price = models.IntegerField()
     category   = models.CharField(max_length=100)
     image_link  =models.CharField(max_length=100)
     sort_image_link = models.CharField(max_length=100)
     mrp = models.IntegerField()
     pro_link = models.CharField(max_length=255,unique=True)
     brand   = models.CharField(max_length=100)
     model_name= models.CharField(max_length=200)
     target = models.CharField(max_length=100)
     seller = models.CharField(max_length=100)
     description = models.TextField()
     product_spec =models.TextField()
     release_date = models.CharField(max_length=100)
     date = models.CharField(max_length=100)
     status = models.CharField(max_length=100)
     image_status = models.CharField(max_length=10,default='NO')
     discount = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=200,unique=True)
    user_password = models.CharField(max_length=100)

    

