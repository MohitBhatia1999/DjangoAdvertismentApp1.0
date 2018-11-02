# DjangoAdvertismentApp1.0

My project is present in the folder Dev/env/myproject and also iam sharing README.txt file which is also in the same folder env.

This project functionalities is designed on Django admin site with the admin 
username-mohit
password-mohitmohit12
The Project contains following module:
1.banner
2.myproject
3.template

1.banner is the application which  contains all the files such as models.pywhere I have made models and activated it, and views.py in which I have written the logical code for the secodn functionality of the task that is the condition in which the price period does not intersect with the booking period in views.py i have written the logical code for it where i have taken loop inside the booking period and price period and checked that no price period is intersecting with the booking period :
if :
it clashes with booking period give httpresponse ("price change clashes with some booking")
else :
continue

2. myproject is the folder name which contains my python package i.e myproject that contains the files settings.py,urls.py and wsgi.py.
in settings.py I have made changes for adding the banner application here in applications installed.

3.template folder which contains check_availability.html ,whenever a priceperiod is added it iterates the database to verify that is there is already a booking in that particular period or not ,and if there is a booking already in that period than it notifies the user to change it else it notify that user is good to go.

##NOTE :
When we run the server going to port and moving forward to  Django Admin Site there you will have 2 options inside the Banner--
1. Booking Period : TO add ,Delete and Change the booking period.
2 Price Period : to add and change the price period. 

check the availability by running the server and typing "http://127.0.0.1:8000/banner/check_availability/" in the browser.
