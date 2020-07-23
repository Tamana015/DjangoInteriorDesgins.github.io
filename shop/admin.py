from django.contrib import admin
from .models import Product,img,Contact,Orders,OrderUpdate

# Register your models here.
admin.site.register(Product)
admin.site.register(img)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
