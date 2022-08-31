from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Partner, Advantage, Application, Review
from rest_framework import status
from .serializers import PartnerSerializer, AdvantageSerializer, ApplicationSerializer, ReviewsSerializer


@api_view(['GET'])
def getPartners(request):
    partners = Partner.objects.filter(is_published=True)
    serializer = PartnerSerializer(partners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAdvantages(request):
    advantages = Advantage.objects.all()
    serializer = AdvantageSerializer(advantages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createApplications(request):
    if request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getReviews(request):
    reviews = Review.objects.filter(is_published=True)
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)
