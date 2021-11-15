from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    result = None
    if request.method == "POST":
        r = requests.post("https://api.deepai.org/api/summarization", 
        data ={
            'text': request.POST["res"],
            }, 
        headers={'api-key': '2788e9aa-b304-4ee1-8e60-2ce735da77f2'})
        result = r.json()['output']
        print(result)
        # re = result.replace("\n", " ")
       
    
  
    
    context = {"re": result}
    return render(request, "index.html", context)



def about(request):


    return render(request, "about.html")



def privacy(request):


    return render(request, "privacy.html")
