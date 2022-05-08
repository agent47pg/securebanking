import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from commonlib.singletonbase import SingletonBase

class Mortgage(SingletonBase):
    def __init__(self):
        #self.interest_rate = super.mortgage_interest_rate
        self.interest_rate = 3

    def set_principal(self,principal = 0):
        self.principal = principal

    def get_monthyly_interest(self):
        self.monthyly_interest = ((self.interest_rate/1200)* self.principal)

    def get_yearly_interest(self):
        self.yearly_interest = ((self.interest_rate/100)* self.principal)



