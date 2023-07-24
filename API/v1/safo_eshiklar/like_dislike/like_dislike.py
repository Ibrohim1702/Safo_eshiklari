from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from safo_eshiklar.models import Products, Likes


class LikeView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        if 'product_id' not in data or 'status' not in data:
            return Response({"error": "data to'lliq emas"})

        pro = Products.objects.filter(pk=data['product_id']).first()
        if not pro:
            return Response({'error': "bunaqa product yo'"})

        likes = Likes.objects.get_or_create(product=pro)[0]

        if 'like' in data and 'dislike' in data:
            return Response({"error": "xato data"})

        like = likes.like
        dislike = likes.dislike

        if 'dislike' in data and data['dislike']:
            like = False
            dislike = True

        if 'like' in data and data['like']:
            like = True
            dislike = False

        likes.like = like
        likes.dislike = dislike
        likes.save()

        return Response({
            "tog'ri": likes.res()
        })


class DisLikeView(GenericAPIView):

    def post(self, requests):
        data = requests.data
        if 'product_id' not in data or 'status' not in data:
            return Response({'error': "data tto'llimas"})

        pro = Products.objects.filter(pk=data['product_id']).first()
        if not pro:
            return Response({'error': "bunaqa product yo'"})

        likes = Likes.objects.get_or_create(product=pro)[0]
        if data['status'] == 'like':
            likes.like = not likes.like
            likes.dislike = False
        if data['status'] == 'dislike':
            likes.like = False
            likes.dislike = not likes.dislike  # bazadagini teskarisiga alamshtiradi like->dis, dis->like
        likes.save()

        liked = Likes.objects.filter(like=True).count()
        dis = Likes.objects.filter(dislike=True).count()

        return Response({
            "tog'ri": likes.res(),
            "likes": liked,
            "dis": dis

        })