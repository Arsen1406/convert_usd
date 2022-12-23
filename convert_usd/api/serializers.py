from rest_framework import serializers


class ConvertSerializer(serializers.ModelSerializer):
    result = serializers.IntegerField()

    class Meta:
        fields = ('result',)
