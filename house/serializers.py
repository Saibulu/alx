from rest_framework import serializers

from . models import Company, students, Teams, pricings



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class pricingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = pricings
        fields = '__all__'




