import requests

api_key ='django-insecure-1ze!ypg3f580gn@cw*occfv$v4yz714b%=6!3wdi0^q_xuue5o' # Yahan apni real key daal
city = "Delhi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    print(f"Delhi ka temperature: {temp - 273.15:.2f}°C")
else:
    print(f"API call fail ho gaya, bro! Status Code: {response.status_code}")
    print(f"Error Message: {response.text}")