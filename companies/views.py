from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


#lists all  stcoks or create a new one
#stocks/
class StockList(APIView):

    #get is for getting all the data which we need
    #get request will return all the list of the stocks
    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks,many=True)
        return Response(serializer.data)

    #in post reqest we let them create a new stock
    def post(self):
        pass