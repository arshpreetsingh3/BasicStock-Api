from rest_framework import serializers
#serialize just means taking a model and converting it to data which can be saved on hard drive etc
from .models import Stock
#were converting something to json based on a model (Stock) in this case
#whenever we send this json response it knows to include ticker,open,close,volume
class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        #fields = ('ticker','volume')#fields which we want to send in return 
        #whenever we make a request we just send info about ticker and volume
        fields = '__all__'
