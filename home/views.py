from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home.models import baby_names
import re as re

def home(request):


    template = loader.get_template("myfirst.html")
    name_list=[]
    try:
        file_path = r"C:\Users\Princ\OneDrive\Documents\Projects\python\class\baby2008_46b42cfd9bdffb09354e577e66a1f98a.html"
    
        with open(file_path, "r+") as f:
            content = f.read()
            
    except FileNotFoundError:
        content = "File not found"
    finally:
        print("closing file")
        names = re.findall(r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td",content)
    
    

    for name in names:
        male_names = name[1]
        female_names = name[2]
        name_list.append(male_names)
        name_list.append(female_names)
    
    for name_item in name_list:
        id = 0
        name, created = baby_names.objects.get_or_create(name = name_item) 
        if created:
            print(f"just created  id: {id} , {name} ")
            id+=1
        else:
            print(f"Already exist")
            id+=1
        
                

    database_names = baby_names.objects.all().values()
    return HttpResponse(template.render({'member': database_names}))
# Create your views here.

# Create your views here.
