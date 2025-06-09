from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    if request.method=='POST':
        city = request.POST.get('city')
        url1 = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key=fe714c15cc3041939a0dae4cc4211042"

        response1 = requests.get(url1)
        data1 = response1.json()
        
        latitude = data1['results'][0]['geometry']['lat']
        longitude =data1['results'][0]['geometry']['lng']




        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=1b274b6a8139a5eeae5571f298f7258e&units=metric"

        response = requests.get(url)
        data = response.json()
        context = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')




