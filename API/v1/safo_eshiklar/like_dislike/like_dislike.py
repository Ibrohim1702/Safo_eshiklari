from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from safo_eshiklar.models import Products, Likes



class Dislike_LikeView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data
        print("saaaa")

        if 'product_id' not in data or 'status' not in data:
            return Response({"error": "data to'lliq emas"})

        pro = Products.objects.filter(product_id=str(data['product_id'])).first()
        print(pro)
        if not pro:
            return Response({'error': "bunaqa product yo'"})

        likes = Likes.objects.get_or_create(product=pro)[0]

        like = likes.like
        dislike = likes.dislike

        if data['status'] == 'dislike':
            like = False
            dislike = True

        if data['status'] == 'like':
            like = True
            dislike = False

        likes.like = like
        likes.dislike = dislike
        likes.save()

        return Response({
            "tog'ri": likes.res()
        })


