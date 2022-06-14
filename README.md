# DjangoTutorial
Me learning django

## how to run this
`too long, didn't read:`
># NOTE: This is made with VS code and windows
>python manage.py makemigrations  # step 1, only once
>python manage.py migrate         # step 2, only once
>python manage.py seed            # step 3, only once
>python manage.py runserver       # to run the server

### Initialize - Migrations
First, run:
>python manage.py makemigrations
>python manage.py migrate

### Initialize first user
Then you can run the following script.
>python manage.py seed

It will create an user with the following information.
The credentials are not very secure, but the app is easier test with this user.
The seed is found from `org/managemenet/commands/seed.py`
> user = User(
>   id=1,
>   password='pbkdf2_sha256$320000$9X6obM0Qq2MAV0oko1Xrvz$e2tHcKL8+2h6bsgIz1rTVruniOF4i9ugRShLSasUZRU=' # equals to'su',
>   is_superuser=True,
>   username='su',
>   last_name='User',
>   email='super.user@django.org',
>   is_staff=True,
>   is_active=True,
>   date_joined=date.today(),
>   first_name='Super'
> )

And the user will belong in the group. In this project an organization equals a group
>group = Group(
> id=1,
> name='organization 1'
>)

The script also adds some files in the database for testing.

### finally run the app
>python manage.py runserver

As the app will say, the dev-server will be ran at
`http://127.0.0.1:8000/`


## Specification
Please write a web application that provides a REST API for logged-in users to upload and download any kind of files.
The users must be able to login and logout. Use either token or session authentication (hint: use the user model and authentication mechanism provided by django). 
Each user and file must belong to an organization. Once uploaded, the file must belong to the same organization as the user who uploaded it.
There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script.
Users should see and be able to download any of the uploaded files from any organization. Write an endpoint for listing all the files that belong to one organization, and an endpoint for listing all the file downloads done by one user. Include timestamps when the file was uploaded and when the user downloaded a file.
Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization). Include the number of downloads when listing files and organizations.
Use Django and Django REST Framework (https://www.django-rest-framework.org/). You can use a database of your choice.

### Notes from the specification
 - Even though the specs is saying about REST framework, this is technically done with plain Django. It's just because I misread the specs. 
    -> I added Django REST to installed apps, so i guess you can say it's used here *insert 'its something' meme*
 - organization file upload count is not stored in the database but just calculated in the endpoint.
 - UI is implemented but it doesn't have separate UI nor even endpoint for fetching data from other organizations. You can download files of other organizations if you know their file id...
