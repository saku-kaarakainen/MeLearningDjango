#helper functions here, if needed.

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