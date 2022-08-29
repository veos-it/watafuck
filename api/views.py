from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Partner, Advantage
from .serializers import PartnerSerializer, AdvantageSerializer


@api_view(['GET'])
def getPartners(request):
    partners = Partner.objects.all()
    serializer = PartnerSerializer(partners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAdvantages(request):
    advantages = Advantage.objects.all()
    serializer = AdvantageSerializer(advantages, many=True)
    return Response(serializer.data)