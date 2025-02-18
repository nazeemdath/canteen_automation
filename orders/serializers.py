from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import Menu

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')  # Make the user field read-only

    class Meta:
        model = Order
        fields = ['user', 'status', 'ordered_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # Automatically set the user to the logged-in user
        order = Order.objects.create(user=self.context['request'].user, **validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
