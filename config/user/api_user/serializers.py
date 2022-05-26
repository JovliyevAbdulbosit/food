from rest_framework import serializers

from config.user.models import User


class CostumSerializer(serializers.ModelSerializer):
    password2 =  serializers.CharField(
        write_only = True,
        style = {'input_type': 'password'}
    )
    class Meta:
        model = User
        fields=["password", "password2", "username","first_name", "last_name","phone" ]
        extra_kwargs ={
            "password":{"write_only":True}
        }
    def save(self , **kwargs):
        user = User(
            username = self.validated_data["username"],
            first_name = self.validated_data["first_name"],
            last_name = self.validated_data["last_name"],
            phone = self.validated_data["phone"],
            password=self.validated_data["password"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2 :
            raise serializers.ValidationError({"error":"pasword error"})

        user.set_password(password)
        user.is_teacher = True
        self.validated_data.pop("password2")

        user.save()
