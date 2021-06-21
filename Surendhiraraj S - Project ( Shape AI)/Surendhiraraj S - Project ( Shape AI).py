import requests

api_key=str(input("Enter your API KEY: "))
place=input("Enter your City name: ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()


temperature_of_city=((api_data['main']['temp'])-273.15)
weather_description=api_data['weather'][0]['description']
humidity_of_city=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']

print("*****************************************************")
print("Weather report for the location of {}".format(place.upper()))
print("*****************************************************")

r=open('report.txt','a')

temp=str(temperature_of_city)
wd=str(weather_description)
h=str(humidity_of_city)
ws=str(wind_speed)
print("The fetched data's are uploaed to the file named report.txt")
r.write("Current temprature is: ")
r.write(temp+"deg in C \n")
r.write("Current weather_description is: ")
r.write(wd+"\n")
r.write("Current humidity is: ")
r.write(h+"% \n")
r.write("Current wind_speed is: ")
r.write(ws+"kmph \n")
print("Printing completed , Check out the file report.txt in this same location")

r.close()
