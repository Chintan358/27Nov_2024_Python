# import calc

# a = calc.add(10,20)
# print(a)

# sq = calc.square(10)
# print(sq)

# import random

# number = random.randint(1000,9999)
# number = random.randrange(1000,9999,2)
# print(number)

# import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.pow(2,2))
# print(math.ceil(2.5))
# print(math.floor(2.5))
# print(round(2.565656,6))

# import calendar

# print(calendar.month(2024,1))

# import os

# os.makedirs("Test")   


# import datetime


# x=datetime.datetime.now()
# print(x)
# print("Today:",x.day)
# print("Current month:",x.month)
# print("Current Year:",x.year)
# print("Current Hrs:",x.hour)
# print("Current Min:",x.minute)
# print("Current Second:",x.second)
# print("Current Microsecond:",x.microsecond)

# import platform


# print(platform.architecture())
# print(platform.platform())
# print(platform.machine())
# print(platform.processor())
# print(platform.python_version())

# import keyword

# x=keyword.kwlist
# print(x)
# print(len(x))

# import requests

# url="https://restcountries.com/v3.1/all"

# req=requests.get(url)

# data=req.json()

# for i in data:
#     print(i['name']['common'])


# import pandas

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)


# import instaloader

# name=input("Enter instagram id:")

# insta=instaloader.Instaloader()

# #insta.download_profile(name,profile_pic_only=True)
# insta.download_profile(name,profile_pic_only=True)

# print("Download Successfully!")

# import pyqrcode
# import sys

# url="https://www.tops-int.com/"

# qr=pyqrcode.create(url)

# qr.png('tops.png')


from pytube import YouTube 

# where to save 
SAVE_PATH = "/home/chintusharma/Downloads" #to_do 

# link of the video to be downloaded 
link = "https://youtube.com/shorts/akL53YfPTfI?si=ju1ohfkBdFSInLNj"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")
