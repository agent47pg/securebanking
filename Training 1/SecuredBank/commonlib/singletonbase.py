#import yaml
from os.path import dirname, join, abspath

class SingletonBase(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(class_, *args, **kwargs):
        config_file = abspath(join(dirname(__file__), '../config/config.yml'))
        with open(config_file,'r') as file:
            config = yaml.safe_load(file)

        self.credit_card_interest_rate = config['credit_card']['interest_rate']
        self.mortgage_interest_rate = config['mortgage']['interest_rate']
        self.banking_interest_rate = config['banking']['interest_rate']

