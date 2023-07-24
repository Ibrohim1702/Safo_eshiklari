from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from safo_eshiklar.base.format import basketFormat
from safo_eshiklar.models import Basket, Products


class BasketView(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data

        if "product_id" not in data:
            return Response({
                "Error": "product_id berilmagan"
            })

        prod = Products.objects.filter(pk=data['product_id']).first()

        if prod:
            baskett = Basket.objects.get_or_create(
                user=requests.user,
                product=prod,
            )[0]

            baskett.quantity = data.get('quantity', baskett.quantity)
            baskett.save()

            return Response({
                "result": basketFormat(baskett)
            })

        else:
            return Response({
                "Error": "Noto'gri product_id berilgan"
            })