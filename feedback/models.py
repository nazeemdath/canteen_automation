from django.db import models
from users.models import User
from menu.models import FoodItem

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)  # 1 to 5 scale
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name} ({self.rating}★)"