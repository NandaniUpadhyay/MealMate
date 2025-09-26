from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer

@api_view(['GET'])
def get_menu(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def place_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Order placed successfully"})
    return Response(serializer.errors)