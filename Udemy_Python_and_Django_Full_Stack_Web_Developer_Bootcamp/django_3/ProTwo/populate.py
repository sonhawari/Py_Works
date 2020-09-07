import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()


import random
from AppTwo.models import User
from faker import Faker

fakegen= Faker()

def populate(N=5):

    for entry in range(N):

        #crate the fake data for that entry
        fake_email = fakegen.email()
        fake_surname = fakegen.last_name()
        fake_name = fakegen.first_name()


        # create the web page entry

        webpg = User.objects.get_or_create( first_name= fake_name, last_name=fake_surname, Email=fake_email )[0]


if __name__== '__main__':
    print("populating script!")
    populate(20)
    print("populate done")
