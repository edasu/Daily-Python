#If ISS is close my current position 
#and its currently dark
#then send me a email to look up
#run this code every 60 seconds

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'erqwrqwer@gmail.com'
MY_PASSWORD = '12345'

MY_LAT = 40.507351 #your latitude
MY_LONG = -0.127758 #your longitute

#get() will get the data from the end point
#end point goes in argument called 'url'
#Then we will capture the data in new variable called reponse
def iss_is_overhead():
    response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    response.raise_for_status() #will raise an HTTPError if the HTTP request returned an unsuccessful status code.
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    #will look to positions within +5 or -5 degrees of ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
       return True


#in order to get specific piece of data we set parametters pyhton dict to pass over 
def is_night():
    paramaters= {
        'lat': MY_LAT,
        'lng': MY_LONG,
        #disables the formating
        'formatted': 0,
    }

    response = requests.get(url ='https://api.sunrise-sunset.org/json', params=paramaters )
    response.raise_for_status()
    data = response.json()

    #spliting the string in order to get specific hours that we will compare
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    now = datetime.now().hour 
    #print(type(now))

    if now>= sunset or now<=sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject: Look Up\n\nThe ISS is aboue you, see it'
        )
