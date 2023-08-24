from django.shortcuts import render

#B0r11xciXTbJAoontU3xcg==xC9VMWbjs3utwyZR
# Create your views here.
def home(request):
    import requests

    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'B0r11xciXTbJAoontU3xcg==xC9VMWbjs3utwyZR'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'home.html')
