from rest_framework import serializers


class employee_serializer(serializers.Serializer):
    deptno = serializers.IntegerField()
