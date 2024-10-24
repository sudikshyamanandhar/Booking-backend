from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
def create_booking(request):
    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            # Additional logic for checking availability can be added here
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
