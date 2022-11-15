
from user_data.models import UserTable
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from user_data.serializers import UserTableSerializer, GetSerializer, AuthTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterAPI(APIView):
    """Api to store the new user details into database"""

    def post(self, request):
        """create user details into database"""
        serializer = UserTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user registration successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAPI(APIView):
    """To get the details of every user present in the database"""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """get the details of users present in database"""
        print("user detail: ", request.user.id)
        query_set = UserTable.objects.filter(id=request.user.id)

        serializer = GetSerializer(query_set, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class LoginAPI(TokenObtainPairView):
    """Api for user to login into website"""
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer
