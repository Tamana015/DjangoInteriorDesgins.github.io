from django.db import models

class Product(models.Model):
    product_id= models.AutoField
    product_name= models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=200,default='')  
    sub_Category = models.CharField(max_length=200,default='')  
    image = models.ImageField(upload_to= 'shop/images',default=0)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()

    def __str__(Self):
        return Self.product_name


class Contact(models.Model):
    product_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=15,default='')
    region= models.CharField(max_length=30)  
    desc = models.CharField(max_length=500)

    def __str__(Self):
        return Self.first_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class img(models.Model):
    img_id= models.AutoField(primary_key= True)
    img_name= models.CharField(max_length=10)
    img= models.ImageField(upload_to= 'shop/images',default=0)

    def __str__(Self):
        return Self.img_name


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(Self):
        return Self.update_desc[0:7] + "..."