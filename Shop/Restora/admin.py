from django.contrib import admin

# Register your models here.
from .models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'phone', 'category')
    # fieldsets = (
    #     (None, {
    #         'fields': ('book','imprint', 'id')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back')
    #     }),
    # )
class DishesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'cookingTime', 'category')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'dateOfBirthday')
    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'unit', 'pricePerUnit', 'expiration')  
    
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('dishe', 'product', 'amount', 'unit')  
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'adress', 'price', 'payment', 'delivery')  
    list_filter = ('id', 'date')
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity')
   
class TablesAdmin(admin.ModelAdmin):
    list_display = ('number', 'numberOfSeats', 'availability')
    
class AvailabilitysAdmin(admin.ModelAdmin):
    list_display = ('table', 'beginning', 'end')    
    
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('provider', 'product', 'quantity', 'unit', 'total', 'status') 



# class UsersInline(admin.TabularInline):
#      model = Users
      
class AdministratorsAdmin(admin.ModelAdmin):
    list_select_related = ('user',)
    list_display = ('user', 'email', 'level')
    
    def email(self, obj):
        return obj.user.email  # Обращаемся к полю email связанной модели Users

    email.short_description = 'Email'
    #inlines = [UsersInline]
         
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(CategoriesFood)
admin.site.register(Dishes, DishesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Tables, TablesAdmin)
admin.site.register(Availabilitys, AvailabilitysAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Administrators, AdministratorsAdmin)
