import datetime
import sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from commonlib.loadStdConfig import GlobalBase

class SecureAuth(GlobalBase):
    """A function to validate user credentails and set initial setup upon successful authentication"""
    def __init__(self):
        super().__init__()
        pass

    def login(self,username, password):
        try:
            self.__username = username
            self.__password = password
        except:
            self.__logger.error("Username and Password shouldn't be null")
            raise Exception("Username and Password shouldn't be null")

        if password == "passwd":
            currentDT = datetime.datetime.now()
            self.__session_start_time = currentDT.strftime("%Y%m%d%H%M%S")
        else:
            self.__logger.error("Invalid username / password")
            raise Exception("Invalid username / password")
        self.__mapUserDetails()

    def __mapUserDetails(self):
        """
        map user details to the object after successful authentication
        """
        self.__name = 'user_name'
        self.__email  = 'email'
        self.__mobile = 'mobile'
        self.__logger.info("Mapped user details to the object")

    def isActive(self):
        #current time - self.last_login > 10:
        #   return false
        #return true

        self.isActive = 'True'

if __name__ == "__main__":
    SA = SecureAuth('pgoupal','passwd')



