from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /users returns list of all users | /users/me returns currently logged in user


    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super(UserViewSet, self).get_object()

class MyLoginView(LoginView):

    """
    Login user and return the REST Token
    if the credentials are valid and authenticated.
    Accept the following POST parameters: email, password
    Return the REST Framework Token Object's key.
    """
class MyRegisterView(RegisterView):

    """
    Register new user and return the REST Token
    if the credentials are valid and authenticated.
    Accept the following POST parameters: username, email, password
    Return the REST Framework Token Object's key.
    """
