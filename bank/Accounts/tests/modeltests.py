import sys
sys.path.append('..')
from django.test import TestCase
from models import Accounts


class ModelsTest(TestCase):
    """ 
    test the Accounts model
    """
    Accounts.objects.create(first_name='mike', second_name= 'Murwayi', account_name='mikemurwayi', account_number='420', account_type='fixed', branch_name='thika', phonenumber='0707070707')