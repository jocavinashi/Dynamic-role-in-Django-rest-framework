from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group ,Permission
class Role(models.Model):
    role=models.CharField(max_length=50,unique=True)
    groups = models.ManyToManyField(Permission)

    def __str__(self):
        return str(self.role)

    # def ___init__(self, name):
    #     self.name = role

class User(AbstractBaseUser):
    email =models.EmailField(max_length=225,unique=True)
    name =models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    role=models.ForeignKey(Role,on_delete=models.CASCADE,default=0)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username']



    # class Meta:
    #     # default_permissions = ('add',)
    #     permissions = (('can_add_ebooks','Can add ebooks'),('can_hire','Can hire employees'))

    