from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser, IsParentUser, IsTeacherUser

from .serializers import UserRegistrationSerializer, UserLoginSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)



class UserLoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,) 

#     def get(self, request):
#         content = {'message': 'Hello, World! You are authenticated.'}
#         return Response(content)

#Dummy View
# class AdminAPIView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         content = {'message': 'Hello Admin, Welcome!'}
#         return Response(content)

# class ParentAPIView(APIView):
#     permission_classes = [IsParentUser]

#     def get(self, request):
#         content = {'message': 'Hello Parent, Welcome!'}
#         return Response(content)

# class TeacherAPIView(APIView):
#     permission_classes = [IsTeacherUser]

#     def get(self, request):
#         content = {'message': 'Hello Teacher, Welcome!'}
#         return Response(content)