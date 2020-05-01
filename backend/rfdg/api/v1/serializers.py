from rest_framework import serializers
from rfdg.models import SFff


class SFffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SFff
        fields = "__all__"
