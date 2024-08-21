from rest_framework import serializers
from .models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['name', 'country', 'info']

    def validate_name(self, value):
        if value[0].isdigit():
            raise serializers.ValidationError("Первый символ названия марки не должен быть числом!")
        if not all(char.isalnum() or char.isspace() for char in value):
            raise serializers.ValidationError("Название марки должно содержать только буквы, цифры и пробелы!")
        if value.isdigit():
            raise serializers.ValidationError("Название марки не должно состоять только из цифр!")
        if len(value) < 2:
            raise serializers.ValidationError("Название марки слишком короткое!")
        if len(value) > 100:
            raise serializers.ValidationError("Название марки слишком длинное!")
        return value

    def validate_country(self, value):
        valid_countries = ["Korea", "Germany", "Japan"]
        if value not in valid_countries:
            raise serializers.ValidationError("Недопустимая страна производства")
        return value
