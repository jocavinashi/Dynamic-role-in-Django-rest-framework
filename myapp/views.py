from rest_framework import permissions
# from django_restframework import ModelViewset
from rest_framework import viewsets
from . import serializers
from . import models
from django.contrib.auth.models import Permission

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()    
    permission_classes =[permissions.IsAdminUser]

    # def perform_create(self,serializer):
    #     mylist=serializer.validated_data['groups']
            
    #     serializer.save(permission=mylist)
        # import pdb; pdb.set_trace()
        
class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()    
    permission_classes =[permissions.IsAdminUser]