from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Contact
from .serializers import ContactSerializer

# Create Contact
class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Contact
class ContactDeleteView(APIView):
    def delete(self, request, id):
        contact = get_object_or_404(Contact, id=id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data="Contact deleted successfully.")
        