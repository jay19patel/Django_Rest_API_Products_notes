from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')

        if api_key == 'jaypatel123':
            try:
                user = User.objects.get(username='jaypatel1911')
                return (user, None)
            except User.DoesNotExist:
                raise AuthenticationFailed('Invalid API key.')
        else:
            raise AuthenticationFailed('Authentication credentials not provided.')

    def authenticate_header(self, request):
        return 'API-Key'
