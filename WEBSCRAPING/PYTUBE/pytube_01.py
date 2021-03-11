# https://medium.com/sage-systems/a-simple-python-script-to-download-youtube-videos-using-pytube-aed3dd9da660
from pytube import YouTube

x = input("Enter the URL of the Youtube Video: ")
print("")
# print("Downloading..........")

yt=YouTube(x)
print("")

print(yt.title)
yt.streams.first().download()

print("")
print("Download Done")