from rest_framework import serializers
from .models import User
import re


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            if len(password) > 7:
                if re.search(r'\d', password):
                    if re.search(r'[А-ЯA-Z]', password):
                        user.set_password(password)
                        user.save()
                        return user
                    else:
                        raise serializers.ValidationError({password: "Пароль должен содержать буквы верхнего регистра"})
                else:
                    raise serializers.ValidationError({password: "Пароль должен содержать цифры"})
            else:
                raise serializers.ValidationError({password: "Пароль слишком короткий"})
        else:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
