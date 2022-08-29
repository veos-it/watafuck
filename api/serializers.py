from rest_framework.serializers import ModelSerializer
from .models import Partner, Advantage


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class AdvantageSerializer(ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'
