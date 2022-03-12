from rest_framework import serializers
from .models import MusicalWork
from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['contributor']


class MWMetaSerializer(serializers.ModelSerializer):
    # musical_works = serializers.RelatedField(many=True, read_only=True)
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = MusicalWork
        depth = 1
        fields = ['id', 'iswc', 'title', 'contributors']
