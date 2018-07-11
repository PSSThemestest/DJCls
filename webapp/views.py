# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from .serializers import *

def index(request):
    products = Product.objects.all()
    return render(request, 'webapp/home.html', {})

class CategView(viewsets.ModelViewSet):
    queryset = Categ.objects.all()
    serializer_class = CategSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserProductView(viewsets.ModelViewSet):
    serializer_class = UserProductSerializer
    def get_queryset(self):
        author_id = self.kwargs['author_id']
        products = Product.objects.filter(author=author_id)
        return products

class TradeView(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class ProductTradeView(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        trades = Trade.objects.filter(desired_product=product_id)
        return trades
