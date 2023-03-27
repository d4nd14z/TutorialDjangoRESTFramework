from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

class RegisterView(APIView):

    def post(self, request):
        print('Registrando usuarios...') 
        return Response(status=status.HTTP_200_OK, data='Todo OK !!!')
