import constant,time
 
main_temp = constant.WEATHER["main"]["temp"]
sunrise = time.ctime(constant.WEATHER["sys"]["sunrise"])
sunset = time.ctime(constant.WEATHER["sys"]["sunset"])
location = constant.WEATHER["name"]
  
 
print(f"sunrise{sunrise}")