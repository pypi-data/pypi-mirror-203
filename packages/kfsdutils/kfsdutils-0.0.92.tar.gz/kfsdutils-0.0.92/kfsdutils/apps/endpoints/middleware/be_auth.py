from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication

from kfsdutils.apps.endpoints.handlers.core.apikeyuser import APIKeyUser


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("Calling ApiKeyAuthentication")
        if request.path == "/doc/schema/":
            return None
        
        api_key = request.headers.get('X-APIKey')
        if not api_key:
            raise AuthenticationFailed('API key was not passed in header!')
        
        #client_obj = self.getAPIKey(api_key)
        #apiKeyUser = APIKeyUser(request, client_obj)
        return (None, api_key)
    
    def getAPIKey(self, apiKey):
        # try:
        #     clientObj = Client.objects.get(api_key=apiKey)
        #     return clientObj.get_child()
        # except Client.DoesNotExist:
        #     raise AuthenticationFailed('\'{}\' is not a valid API key.'.format(apiKey))

        pass

        
