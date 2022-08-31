from rest_framework.serializers import ModelSerializer
from .models import Partner, Advantage, Application, Review


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class AdvantageSerializer(ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'text']
