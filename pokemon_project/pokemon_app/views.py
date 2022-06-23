from urllib import response
from django.shortcuts import render
import requests as HTTP_Client
import pprint
import random

pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.

def index(request):
    
    id = request.GET.get("id") or random.randrange(1, 875) # This essientially evaulates if there is a query string called 'id'

    API_response = HTTP_Client.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    responseJSON = API_response.json()
    print(API_response)
    # pp.pprint(responseJSON)
    # print(type (responseJSON))
    print(responseJSON['types'][0]["type"]['name'])
    poke_image = responseJSON["sprites"]["front_default"] # This grabs the first random pokemon by number
    poke_type = responseJSON['types'][0]['type']["name"] # This is what the for loop is based of off
    poke_list = []
    poke_list.append(poke_image) # This adds the first image to the array
    API_response = HTTP_Client.get(f"https://pokeapi.co/api/v2/type/{poke_type}")
    responseJSON = API_response.json()
    max_length = len(responseJSON["pokemon"])
    # print(responseJSON["pokemon"][0]['pokemon']['url'])
    for i in range(0, 5): # Grabs five additional URL's for images.
        new_responseJSON = responseJSON["pokemon"][random.randrange(0, max_length)]['pokemon']['url']
        new_response = HTTP_Client.get(new_responseJSON)
        new_responseJSON = new_response.json()
        poke_image = new_responseJSON["sprites"]["front_default"]
        poke_list.append(poke_image) # Adds the final five images
        
        # print(poke_list)
    
        
        
        
    # print(random_num)
    # print(len(responseJSON["pokemon"])) # Pokemon is an array with pokemon of {poke_type}
    

    my_data = {
        "poke_image": poke_image,
        "poke_list": poke_list,
        "hello": "world"  
    }

    return render(request, "index.html", my_data)
