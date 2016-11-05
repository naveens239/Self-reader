from rest_framework import serializers
from pacereader.models import Passage,Subject

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'