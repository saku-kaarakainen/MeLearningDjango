# DjangoTutorial
Me learning django

## how to run this
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


### finally run the app
>python manage.py runserver

As the app will say, the dev-server will be ran at
`http://127.0.0.1:8000/`



> # log in with the user
>user: django
>email bd983f53-13e3-46c9-882d-aa178961dbde@mailinator.com (you can check the emails at: https://www.mailinator.com/v4/public/inboxes.jsp?to=bd983f53-13e3-46c9-882d-aa178961dbde)
>password: unchained

## To debug (on vs code)
>to actiavte environment, on mac, run source ./venv/bin/activate on windows, run .\venv\Scripts\activate.bat [if it doesn't work, try to put your absolute path]
Thanks to: https://stackoverflow.com/questions/68425824/virtualenv-for-django-in-vs-code-not-working-what-am-i-doing-wrong

## Specification
Please write a web application that provides a REST API for logged-in users to upload and download any kind of files.
The users must be able to login and logout. Use either token or session authentication (hint: use the user model and authentication mechanism provided by django). 
Each user and file must belong to an organization. Once uploaded, the file must belong to the same organization as the user who uploaded it.
There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script.
Users should see and be able to download any of the uploaded files from any organization. Write an endpoint for listing all the files that belong to one organization, and an endpoint for listing all the file downloads done by one user. Include timestamps when the file was uploaded and when the user downloaded a file.
Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization). Include the number of downloads when listing files and organizations.
Use Django and Django REST Framework (https://www.django-rest-framework.org/). You can use a database of your choice.


### breakdown
  - Please write a web application that provides a REST API 
    -- for logged-in users to upload and download any kind of files.
  - The users must be able to login and logout. 
    -- Use either token or session authentication
    -- hint: use the user model and authentication mechanism provided by django. 
  - Each user and file must belong to an organization.
  - Once uploaded, the file must belong to the same organization as the user who uploaded it.
  - There is no need to implement CRUD endpoints for users or organizations, 
    -- those can be created by running a script. 
      -> since wording is "can be", won't be implemented yet.
  - Users should see and be able to download any of the uploaded files from any organization.
  - Write an endpoint for listing all the files that belong to one organization, 
    - and an endpoint for listing all the file downloads done by one user. 
    - Include timestamps when the file was uploaded and when the user downloaded a file.
  - Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization). 
    - Include the number of downloads when listing files and organizations.
  - Use Django and Django REST Framework (https://www.django-rest-framework.org/).
  - You can use a database of your choice.

#### REST API 

  # gets the list of files by the organisation id
  GET files ?organizationId={int}

  # downloads a file. 
  # returns list { uploaded, downloadedCount, blob }
  GET files/{file_id}

  # uploads a file. returns 201 
  -> POST files/upload 

  # *(done)* logs the user in 
  GET accounts/login

  #  *(done)* logs the user out
  GET accounts/logout


#### database
  - migrations by manual scripts

  dbo.organizations
    .id
    .name

  dbo.users
    .id
    .organization_id
    .username
    .password
    .email
    .first_name
    .last_name

  dbo.files
    .id
    .organization_id
    .blob
    .uploaded
    .downloadCount

