# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from datetime import date

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

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Add user
    # password equals to'su'
    user = User(
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
    user.save()

    # Add group. In this model, an organization equals a group.
    group = Group(
        id=1,
        name='organization 1'
    )
    group.save()

    # auth_user_group
    group.user_set.add(user)
    group.save()

    print("'{}' user created.".format(user))