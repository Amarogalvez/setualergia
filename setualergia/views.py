from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .firebase_service import create_document, get_document, update_document, delete_document, get_all_documents
from .serializers import ItemSerializer

class ItemList(APIView):
    def get(self, request):
        items = get_all_documents("items")
        return Response(items)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            create_document("items", serializer.data['name'], serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):
    def get(self, request, pk):
        item = get_document("items", pk)
        if item:
            return Response(item)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        item = get_document("items", pk)
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            update_document("items", pk, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = get_document("items", pk)
        if item:
            delete_document("items", pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
