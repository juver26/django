from django.shortcuts import redirect, render
usuarios = []
def register(request):
    if request.method == 'post':
        name = request.post.get('name')
        password = request.post.get('password')
        for users in usuarios:
            if users ['name'] == name:
                print('Este nombre de usuario ya existe.')
            else:
                usuarios.append({'name':name,'password':password})
def login():
    pass
# Create your views here.
