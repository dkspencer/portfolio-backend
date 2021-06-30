from rest_framework import serializers


class ExceptionSerializer(serializers.Serializer):
    class NestedErrorSerializer(serializers.Serializer):
        non_field_errors = serializers.ListField(child=serializers.CharField())

        class Meta:
            ref_name = None

    status_code = serializers.IntegerField()
    errors = NestedErrorSerializer()

    class Meta:
        ref_name = None
