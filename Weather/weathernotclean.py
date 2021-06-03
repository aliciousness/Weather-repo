import json
import requests
from datetime import datetime
import boto3
import urllib3 #for slack
def lambda_handler(event, context):
    
                    
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Philadelphia&appid=033d27df08ec34a0b35c514fafa67a34&units=imperial')
    w = weather.json()

    main_temp = weather.json()["main"]['temp']
    sys = weather.json()['sys']
    sunrise_sys = sys["sunrise"]
    sunset_sys = sys["sunset"]
    
    location = weather.json()['name']
    sunrise = str(datetime.fromtimestamp(sunrise_sys))
    sunset = str(datetime.fromtimestamp(sunset_sys))
   
    http=urllib3.PoolManager()
    data={"text":f"sunrise: {sunrise} / sunset {sunset} / location: {location} / temp: {main_temp}F "}
    r = http.request("POST",
                    "https://hooks.slack.com/services/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",
                    body = json.dumps(data),
                    headers = {"content-Type": "application/json"})
    # to send to slack channel from lambda function
    # has to run data as text nothing else and only a string 

    return {
        'statusCode': 200,
        'temp': main_temp,
        'location': location,
        'sunrise': sunrise,
        'sunset': sunset
        
    }