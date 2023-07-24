from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from API.v1.safo_eshiklar.contact.serializer import CntSerializer
from safo_eshiklar.base.format import format_cnt
from safo_eshiklar.models import Contact


class CntView(GenericAPIView):
    serializer_class = CntSerializer

    def get(self, requests, _id=None, *args, **kwargs):
        if _id:
            cnt = Contact.objects.filter(id=_id).first()
            if not cnt:
                return Response({"Error": "Bunaqa cnt topilmadi"}, status=404)
            else:
                return Response(format_cnt(cnt))


        else:
            all = Contact.objects.all()
            natija = []
            for i in all:
                natija.append(format_cnt(i))

            ctx = {
                "natija": natija
            }
            return Response(ctx)

    def delete(self, requests, _id, *args, **kwargs, ):
        cnt = Contact.objects.filter(id=_id).first()
        if not cnt:
            return Response({"Error": "Bunaqa cnt yogu *****"}, status=400)
        else:
            cnt.delete()

        ctx = {
            "natija": "Aytilgan cnt ochirib tashlandi"
        }
        return Response(ctx)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        cnt = ser.save()

        return Response(format_cnt(cnt))

    def put(self, requests, _id, *args, **kwargs):
        cnt = Contact.objects.filter(id=_id).first()

        if not cnt:
            return Response({"Error": "Yoq narsani qanaq qblb delete qmoqchisa"})

        data = requests.data
        ser = self.get_serializer(data=data, instance=cnt, partial=True)
        ser.is_valid(raise_exceptions=True)
        cnt = ser.save()

        return Response(format_cnt(cnt))









