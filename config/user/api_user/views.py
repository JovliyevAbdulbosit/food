from requests import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from .serializers import CostumSerializer


class CostumRegister(GenericAPIView):
    serializer_class = CostumSerializer
    def post(self,request , *args, **kwargs):
        serialize = self.get_serializer(data = request.data)
        serialize.is_valid(raise_exception=True)
        user = serialize.save()
        return Response(
            {"user":CostumSerializer(user,context = self.get_serializer_context()).data,
             "token":Token.objects.get(user = user).key,
             }
        )