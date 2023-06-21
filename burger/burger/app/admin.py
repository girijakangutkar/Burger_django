from django.contrib import admin

# Register your models here.
from .models import MenuItem, Category, OrderModel, UserProfileInfo
#from app.models import UserProfileInfo


admin.site.register(UserProfileInfo)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
