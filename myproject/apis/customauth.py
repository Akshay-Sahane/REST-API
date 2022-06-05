from rest_framework.authentication import BaseAuthentication

# superuser can change permissions of HR's by adding or removing the groups through admin panel.
# like if there is a user named gokul@123 with group named CRUD then he has all the permissions
# i.e. he can perform crud on emp data. but if superuser removes CRUD group and adds Read group
# to gokul@123 user then he will be only able to see emp details and will not able to perform crud.

# the Read group is created using admin panel which have permission to view employee
# the CRUD group is created using admin panel which have permission to view,add,update,and delete employee

# to check user have read permission or not
class CustomAuthForOnlyView(BaseAuthentication):
    def has_permission(self,request,view):
        if request.user.groups.filter(name='Read').exists():
            return True
        elif request.user.groups.filter(name='CRUD').exists():
            return True
        else:
            return False

# to check user have only CRUD operation permission or not
class CustomAuth(BaseAuthentication):
    def has_permission(self,request,view):
        if request.user.groups.filter(name='CRUD').exists():
            return True
        else:
            return False
    def has_object_permission(self,request,view,obj):
        if request.user.groups.filter(name='CRUD').exists():
            return True
        else:
            return False