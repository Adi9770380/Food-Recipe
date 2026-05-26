from django.shortcuts import render,redirect
from .models import  Recipe
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    recipes=Recipe.objects.all()
    search=request.GET.get('search')
    if search:
        recipes=recipes.filter(recipe_name__icontains=search)
    return render(request,'home.html',{'recipes':recipes})
@ login_required
def add_recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
            user=request.user
         )
        return redirect('home')
    return render(request,'add_recipe.html')
@ login_required
def delete_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    if recipe.user!=request.user:
        return redirect('home')
    recipe.delete()
    return redirect('home')
    
@ login_required  
def update_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    if recipe.user!=request.user:
        return redirect('home')
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        if request.FILES.get('recipe_image'):
           recipe.recipe_image = request.FILES.get('recipe_image')
        recipe.recipe_name=recipe_name
        recipe.recipe_description=recipe_description
        recipe.save()
        return redirect('recipe_details', id=recipe.id)

    return render(request, 'update_recipe.html', {'recipe': recipe})
            
        
   
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            messages.info(request,'Password do not match')
            return redirect('signup')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'User already taken')
            return redirect('signup')
        user=User.objects.create(
            username=username,
            email=email,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect('login_page')
         
        
    return render(request,'signup.html')
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('login_page')
        user=authenticate(username=username,password=password)
        if user is None:
              messages.info(request,'Invalid Password')
              return redirect('login_page')
        else:
            auth_login(request,user)
            return redirect('home')
            
        
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')
def recipe_details(request,id):
    recipe=Recipe.objects.get(id=id)
    return render(request,'recipe_details.html',{'recipe':recipe})
    
def logout_page(request):
    auth_logout(request)
    return redirect('login_page')


