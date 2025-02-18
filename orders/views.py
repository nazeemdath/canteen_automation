from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    @action(detail=False, methods=['post'], url_path='place')
    def place_order(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Add the user to the order data
        data = request.data
        data['user'] = request.user.id  # Ensure the user is added to the data
        
        # Serialize the data and save the order
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                "message": "Order placed successfully!",
                "order_id": order.id
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
