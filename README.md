# Django_Rest_API_Products_notes


## Data we need in api
- Product Id
- Product Name
- Product Company
- Product Quantity
- Product Price
- Product Image
- Product Category
- Product Description

```js
{
        "id": "njsproduct_1",
        "name": "Iphone 13",
        "company": "apple",
        "quantity":5
        "price": 80000,
        "image": "img.jpg",
        "category":"Phones",
        "description": "falanu Dheknu",
        "featured": true
    },

```
## Create Virtual Enivronment 
```py
python -m venv envname
#  Activate =>  envname/Scripts/Activate 
```
## Django Project
```py
# Install Django in env
django-admin startproject projectname
#  Run Django =>
# cd  projectname
# python manage.py runserver
```
# Rest Framework (APIs)

## Basic Setup
- create django app
```py python manage.py startapp API ``` 
- install djangorestframework
- create model first whitch data we need to manage at here

```py
# model.py
class Products(models.Model):
    id=models.CharField(max_length=50,default=generate_custom_id, editable=False, unique=True,primary_key=True)
    name=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='Products')
    category=models.ForeignKey(Categoty,on_delete=models.CASCADE)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
- create model and migrate them using 

```py
python manage.py makemigrations appname
python manage.py migrate 
```
- create superuse 
```py python manage.py createsuperuser```

## Serializers
- A serializer in Django is a component that allows you to convert complex data types, such as Django model instances, into Python data types (e.g., dictionaries, JSON) that can be easily rendered into different formats, such as JSON, XML, or HTML. It also provides deserialization, allowing parsed data to be converted back into complex types after first validating the incoming data.

```py
# serializer.py
from rest_framework import serializers
from .models import Products

class MyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name','company','quantity','price','image','category','description']  


# view.py
@api_view(['GET']) # as well POST and all Methods 
def HomeAPI(request):
    products = Products.objects.all()
    serializer = MyProductsSerializer(products, many=True)
    print(serializer)
    
    data = {
                'status_code': 200,  # Example status code
                'message': 'Success',  # Example message
                'data': serializer.data
            }
    return Response(data)
```
- simple get method are done by easly like this .
- if need pass the id in url then use <str:id> at the end of url
```py path('getone/<str:id>/', views.GetOneAPI, name="GetOneAPI") ,  ````
- Accsess the id directly at veies file => def functionname(request,id) 

## API authenication for Post Methos
- add this configation at setting.py

- if we need custom authenictaion file for costom api key
- authenication configations in setting.py file
```py
#  Need to add config in setting.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',# Api key mate
        'rest_framework.authentication.BasicAuthentication',#login mate
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

```
#### Costom (Custom API key) 
```py
# costom authenictaion .py
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')

        if api_key == 'jaypatel123':
            try:
                user = User.objects.get(username='jaypatel1911')
                return (user, None)
            except User.DoesNotExist:
                raise AuthenticationFailed('Invalid API key.')
        else:
            raise AuthenticationFailed('Authentication credentials not provided.')

    def authenticate_header(self, request):
        return 'API-Key'
```

#### Automatic 

- if inbuild authenication  (notwork well)
```py
# view.py
from rest_framework.authentication import TokenAuthentication
@authentication_classes([TokenAuthentication])

```
#### Costom (user password)
```py
from rest_framework.authentication import BasicAuthentication
@authentication_classes([BasicAuthentication])
```
# Create Data Entery Point  App  (HTML Page)

```py
python manage.py startapp APP_API
```
- create urls.py file and add url for our HomePage  and other APIs

```py
# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage, name="HomePage")  
]

```


```py
# Views.py
from django.shortcuts import render
def HomePage(request):
    context={}
    return render(request,"HomePage.html",context)
```
- if we use html file then we need to use templates folder in our project,so create Templates folder in stor_API folder
- create simple home page for test in Templates folder
- before use of templates we need to configrate folder name in setting.py => TEMPLATES => 'DIRS': ["Templates"]
- For access our new app we need to add app in setting.py => INSTALLED_APP=> 'APP_API.apps.AppApiConfig',
- access those app urls using project urls.py ,so we need to add app url in project url=> path('', include('APP_API.urls'))


## Create Dash Bord For Our Product adding System
- need to load static file to access css and other images file => {% load static %}

- Need to add into setting.py for  static files and upload files
```py
STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR, 'static']
STATIC_ROOT = 'staticfiles'

MEDIA_DIR = [BASE_DIR , 'media']
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Authentication (Login/Registration)
- first login the admin and then use interface.
- for authentication we use  auth in views.py
```py
from django.contrib import auth
from django.contrib.auth.decorators import login_required
```
- create pages like home , login ,registration pages
-  create login logout and resisttaion system using auth inbuild feature of django
- if use are not authenticate then using decorater we redirect to login page => 
```py @login_required(login_url='/Login') ```

## Create Products Model
- first create Page for adding data 
- geting all product data on views.py
- create models for save data in data base

- use costome id function to genrtate id
- if we upload some image or file then we need to configarte path of media folder 
- set  patten in main project url
```py 
# Project urls.py

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

```py
# model.py

class Products(models.Model):
    id=models.CharField(max_length=50,default=generate_custom_id, editable=False, unique=True,primary_key=True)
    name=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='Products')
    category=models.ForeignKey(Categoty,on_delete=models.CASCADE)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
- after creating perfect model then migrate the  modelusing => makemigratetions and migrate command 
- check the all functionality are done using admin pannel
- Now connect out html page with model

## Connect Model with View using form
- we need to connect our model with view becouse we are adding data using our html page
- create our html page and get all data in view
- create form.py 
```py
# forms.py
from django import forms
from .models import Products

class MyProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
```
- and get form in our view file and pass in context and get all form fild access at html page
- all done and setup to uplaod data using html temples 

- also we create custome page for getting data without form like login and registration page

