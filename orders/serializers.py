from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'total_price', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total_price = 0
        for item_data in items_data:
            menu_item = item_data['menu_item']
            quantity = item_data['quantity']
            total_price += menu_item.price * quantity
            OrderItem.objects.create(order=order, **item_data)

        order.total_price = total_price
        order.save()
        return order
