      
import boto3,json,requests
 
 
CITY = "Philadelphia"
API_TOKEN = "033d27df08ec34a0b35c514fafa67a34"
 
WEATHER = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'.format(CITY,API_TOKEN)).json()