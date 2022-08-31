from rest_framework.serializers import ModelSerializer
from .models import Partner, Advantage, Application


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
