from rest_framework import serializers, status
from rest_framework.response import Response
# important one
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer

# Class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class ArticleListCreateView(APIView):
    # response to GET request
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    # response to POST request
    def post(self, request):
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    # take instance of an article and return
    def get_object(self, pk):
      article_instance = get_object_or_404(Article, pk=pk)
      return article_instance
    
    # and response to client GET method by returning captured article above
    def get(self, request, pk):
      # get_object is our method defined above
      article = self.get_object(pk=pk)
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
    
    # response to put request by comparing two data, one of them coming from client
    # one of them from our db(we understand which data come from by pk parameter)
    # if data comes as expected, then we save serializer and return updated data to client
    # else we return 400 BAD request response
    def put(self, request, pk):
      article = self.get_object(pk=pk)
      # here our Article Serializer compare our instance and coming data from client
      serializer = ArticleSerializer(article, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      # we also add errors coming from our serializer
      # for example if client try to update field with wrong data structure
      # such as pub_date : false, then client will take this response
      # {
      #   "pub_date": [
      #     "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
      #   ]
      # } 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # response to delete request as name suggested,
    # run our get_object method and capture related data
    # then delete and return 204 status
    def delete(self, request, pk):
      article = self.get_object(pk=pk)
      article.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)





# FUNCTION METHOD
# GET ve POST request beklediğimizi belirtiyoruz
"""@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    
    if request.method == 'GET':
      articles = Article.objects.filter(is_active=True) # burada nesnelerden oluşan bir query set var
      # if we dont assing many=True then django throw exception AttributeError
      # Got AttributeError when attempting to get a value for field `author` on serializer `ArticleSerializer`.
      # The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
      # Original exception text was: 'QuerySet' object has no attribute 'author'.
      # so let's assing many=True
      # if we sent more than one instance then we should provide many=True
      serializer = ArticleSerializer(articles, many=True) # query set veriyoruz
      return Response(serializer.data)
    
    elif request.method == 'POST':
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
      return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, pk):
    try:
      article_instance = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      return Response(
        {
          'errors':{
            'code': 404,
            'message': f'Not found an article with this number of {pk} id',
          }
        },
        status=status.HTTP_404_NOT_FOUND
      )
    if request.method == 'GET':
      # now we dont need to many=True, due to given one instance not more
      serializer = ArticleSerializer(article_instance)
      return Response(serializer.data)
      
    elif request.method == 'PUT':
      # data is coming from client with modified inside request object
      serializer = ArticleSerializer(article_instance, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK)
      return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      article_instance.delete()
      return Response(
         {
          'process':{
            'code': 204,
            'message': f'The article with number of {pk} id has been deleted.',
          }
        },
        status=status.HTTP_204_NO_CONTENT
      )"""


