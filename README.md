# DjangoTutorial
Me learning django

## how to run this
>python manage.py migrate # first time only
>python manage.py runserver


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
  -> [verb] upload
  -> [verb] download(organization_id???)
  -> [verb] login (use django use model for auth)
  -> [verb] logout 
  -> GET files(organization_id) # query: {path}/files?organization_id=3

  -> GET files/{user_id} # query: {path}/files/{user_id}
    -> returns: [{
      uploaded,
      downloaded,
      blob
    }, ...]

#### database
  - migrations by manual scripts

  dbo.organizations
    .id

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

