from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from regis.models import User



class RegisView(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data

        nott = ["username", "phone", "password"]
        s = ''

        for i in nott:
            if i not in data:
                s += f" {i} "

        if s:
            return Response({
                "Error": f" Datada {s}  to`ldirilmagan"

            })

        if len(data['phone']) != 12:
            return Response({"Error": "Telefon raqam  12 tadan iborat bo`lishi kerak !"})

        if not data['phone'].isdigit():
            return Response({"Error": "Raqamlarni sonlarda kiriting"})

        if len(data['password']) < 6:
            return Response({"Error": "Parol juda oddiy"})

        user = User.objects.create_user(
            phone=data['phone'],
            email=data['email'],
            password=data.get('password', ''),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            region=data.get('region', ''),
        )

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,

        })


class LoginView(GenericAPIView):
    def post(self,  requests, *args, **kwargs):
        data = requests.data

        if data is None:
            return Response({
                "error": "data to'ldirilmagan"
            })

        nott = 'email' if 'email' not in data else 'password' if "password" not in data else None
        if nott:
            return Response({
                "Error": f"{nott} to`ldirilmagan"
            })
        user = User.objects.filter(email=data['email']).first()

        if not user:
            return Response({
                "Error": "Bunday foydalanuvchi afsuski yo`q."
            })
        if not user.check_password(data['password']):
            return Response({
                "Error": "Parol xato"
            })

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
            "user": user.format()
        })