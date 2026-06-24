from django.shortcuts import redirect, render
from users.models import User
#usuarios = []
def register(request):
    if request.method == 'post':
        name = request.post.get('name')
        password = request.post.get('password')
        print(name)
        print(password)
        User.objects.create(username=name,nickname=name,password=password)
        #for users in usuarios:
            #if users ['name'] == name:
                #print('Este nombre de usuario ya existe.')
            #else:
                #usuarios.append({'name':name,'password':password})
    return render(request,'users/register.html')
def login():
    pass
# Create your views here.
