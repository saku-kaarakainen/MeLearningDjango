# <project>/<app>/management/commands/seed.py
from distutils.command.upload import upload
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from datetime import date
from files.models import File
from common.utils.helpers import io_helpers

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Deleting data...")
    User.objects.all().delete()
    Group.objects.all().delete()
    File.objects.all().delete()

def add_first_user_and_group():
    # Add group. In this model, an organization equals a group.
    group1 = Group(
        id=1,
        name='organization 1'
    )
    group2 = Group(
        id=2,
        name='organization 2'
    )

    group1.save()
    group2.save()

    # Add user
    # password equals to'su'
    user1 = User(
        id=1,
        password='pbkdf2_sha256$320000$9X6obM0Qq2MAV0oko1Xrvz$e2tHcKL8+2h6bsgIz1rTVruniOF4i9ugRShLSasUZRU=',
        is_superuser=True,
        username='su',
        last_name='User',
        email='super.user@django.org',
        is_staff=True,
        is_active=True,
        date_joined=date.today(),
        first_name='Super',
    )


    #password equals to 'unchained'
    user2 = User(
        id=2,
        password='pbkdf2_sha256$320000$llyXshOYwHQILE5BUbqM8R$KltawciESBQ/3d8ujko4D8EfkfAuNd/eoq8dzQedIdI=',
        is_superuser=False,
        username='django',
        last_name='Unchained',
        email='django@unchained.org',
        is_staff=False,
        is_active=True,
        date_joined=date(2013, 1, 18),
        first_name='Super',
    )   

    user1.save()
    user2.save()   
    
    user1.groups.add(group1) 
    user2.groups.add(group2)

    user1.save()
    user2.save()
    
    print("user/org seeding done.")
    return (
        group1,
        group2, 
        user1,
        user2
    )

def add_seed_files(group1, group2, user1, user2):
    print("adding some files to the database")
    file1 = File(
        id=1,
        group=group1,
        user=user1,
        name='Example file 1',
        filepath='example1.txt',
        uploaded=date(2022, 5, 22),
        download_count=1,
    )

    file2 = File(
        id=2,
        group=group1,
        user=user1,
        name='Example file 2',
        filepath='example2.txt',
        uploaded=date(2009, 1, 9),
        download_count=1,
    )

    # Different user, also belongs in the different organization
    file3 = File(
        id=3,
        group=group2,
        user=user2,
        name='Example file 3',
        filepath='example3.txt',
        uploaded=date(2013, 1, 18),
        download_count=1,
    )

    # also, organization 2
    file4 = File(
        id=4,
        group=group2,
        user=user2,
        name='Example file 3',
        filepath='example4.txt',
        uploaded=date(2015, 7, 30),
        download_count=1,
    )


    file1.save()
    file2.save()
    file3.save()
    file4.save()

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    group1, group2, user1, user2 = add_first_user_and_group()
    add_seed_files(group1, group2, user1, user2)