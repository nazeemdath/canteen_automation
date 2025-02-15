from rest_framework import viewsets
from .models import Menu
from .serializers import MenuSerializer

# Unified ViewSet for all Menu operations
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
