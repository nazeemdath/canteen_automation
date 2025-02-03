from django.contrib import admin
from .models import User, Menu, Order, Payment, Feedback

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Feedback)