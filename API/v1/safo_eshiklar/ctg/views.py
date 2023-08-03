from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from safo_eshiklar.base.format import format_ctg
from safo_eshiklar.models import Category
from API.v1.safo_eshiklar.ctg.serializer import CtgSerializer

class CtgView(GenericAPIView):

    serializer_class = CtgSerializer

    def get(self, requests, _id=None, *args, **kwargs):
        if _id:
            ctg = Category.objects.filter(id=_id).first()
            if not ctg:
                return Response({"Error": "Bunaqa ctg topilmadi"}, status=404)
            else:
                return Response(format_ctg(ctg))


        else:
            all = Category.objects.all()
            natija =  []
            for i in all:
                natija.append(format_ctg(i))

            ctx = {
                "natija": natija
            }
            return Response(ctx)


    def delete(self, requests, _id, *args, **kwargs,):
        ctg = Category.objects.filter(id=_id).first()
        if not ctg():
            return Response({"Error": "Bunaqa ctg yogu *****"}, status=400)
        else:
            ctg.delete()

        ctx = {
            "natija": "Aytilgan ctg ochirib tashlandi"
        }
        return Response(ctx)


    def post(self, requests, *args, **kwargs):
        data = requests.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception = True)
        ctg  = ser.save()

        return Response(format_ctg(ctg))

    def put(self, requests, _id, *args, **kwargs):
        ctg = Category.objects.filter(id=_id).first()

        if not ctg:
            return Response({"Error": "Yoq narsani qanaq qblb delete qmoqchisa" } )


        data = requests.data
        ser = self.get_serializer(data=data, instance=ctg, partial= True)
        ser.is_valid(raise_exceptions = True)
        ctg = ser.save()


        return Response(format_ctg(ctg) )