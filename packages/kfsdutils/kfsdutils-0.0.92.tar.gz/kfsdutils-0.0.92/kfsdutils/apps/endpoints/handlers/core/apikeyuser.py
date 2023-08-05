#from kfsdutils.apps.core.utils import ConfigUtils

class APIKeyUser:
    is_active = True

    def __init__(self, request, user):
        self.__user = user
        self.__request = request
    
    def getRequest(self):
        return self.__request

    def identifier(self):
        return self.__user.identifier