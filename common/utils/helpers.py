#helper functions here, if needed.
"""
Provides database related helper methods.
"""
class db_helpers:
  @staticmethod
  def get_organization_by_user_from_the_request(request):
      """
        These errors are raised, because the model treats group as organization.
        The API assumes always that the user belongs always exactly to one group, 
        event though it's possible to add more groups by the model and admin page.
      """

      if(request.user.groups.count() == 0):
        raise Exception("User does not have a group")
              
      if(request.user.groups.count() > 1):
        raise NotImplementedError("The current version does not support multi-group model")
        
      return request.user.groups.all()[0]

"""
Provides file handling related helper methods.
"""
class io_helpers:
  @staticmethod
  def get_upload_folder():
    return '_downloads/'

  @staticmethod
  def save_file_to_disk(file):
      # TODO: Add virus scan 
      with open(io_helpers.get_upload_folder() + file.name, 'wb+') as destination:
          for chunk in file.chunks():
              destination.write(chunk)
  
  @staticmethod
  def get_file_from_disk(filename):
    file = io_helpers.get_upload_folder() + filename
    path = open(file, 'rb')
    return path


  @staticmethod
  def remove_uploaded_file(file):
    # TODO: Remove file
    print("File 'removed' from the system.")


"""
  Simplies ussages of django messages
"""
class message_helpers:
  @staticmethod
  def message(request):
    pass