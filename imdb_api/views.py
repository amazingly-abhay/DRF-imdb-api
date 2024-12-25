from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# def list_view(request):
#     movielist=WatchList.objects.all()
#     serializer=WatchListSerializer(movielist,many=True)
#     data=serializer.data
#     return JsonResponse(data,safe=False)


# def detail_view(request,pk):
#     movie=WatchList.objects.get(pk=pk)
#     serializer=WatchListSerializer(movie)
#     data=serializer.data
#     return JsonResponse(data)

# # CBVs 
# class ListView(APIView):
#     def get(self,request):
#         list=WatchList.objects.all()
#         serializer=WatchListSerializer(list,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class ListDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         movie=self.get_object(pk)
#         serializer=WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         movie=self.get_object(pk)
#         serializer=WatchListSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self,request,pk):
#         movie=self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# mixins
from rest_framework import mixins,generics

class ListView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class ListDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



@api_view(['GET','POST'])
def platform_list(request):
    if request.method=="GET":
        platformlist=StreamingPlatform.objects.all()
        serialized=StreamingPlatformSerializer(platformlist,many=True)
        data=serialized.data
        return Response(data,status=status.HTTP_200_OK)
    
    if request.method=="POST":
        data=request.data
        serialized=StreamingPlatformSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def platform_view(request,pk):
    try:
        platform=StreamingPlatform.objects.get(pk=pk)
    except StreamingPlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serialized=StreamingPlatformSerializer(platform)
        data=serialized.data
        return Response(data)
    
    if request.method=="PUT":
        serialized=StreamingPlatformSerializer(platform,data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

