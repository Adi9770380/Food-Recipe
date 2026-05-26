from django.urls import path
from .views import *
urlpatterns = [
         path('',home,name="home"),
         path('add-recipe/',add_recipe,name='add_recipe'),
         path('update-recipe/<int:id>/',update_recipe,name='update_recipe'),
         path('delete-recipe/<int:id>/',delete_recipe,name='delete_recipe'),
         path('signup/',signup,name='signup'),
         path('login_page/',login_page,name='login_page'),
         path('logout_page/',logout_page,name='logout_page'),
         path('about/',about,name='about'),
         path('recipe_details/<int:id>/', recipe_details, name='recipe_details')
        
    
]