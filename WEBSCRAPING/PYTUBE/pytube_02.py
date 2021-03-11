# https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97


# from pytube import YouTube


# link = input(“Enter the link: “)
# yt = YouTube(link)

# #Title of video
# print(“Title: “,yt.title)
# #Number of views of video
# print(“Number of views: “,yt.views)
# #Length of the video
# print(“Length of video: “,yt.length,”seconds”)
# #Description of video
# print("Description: ",yt.description)
# #Rating
# print("Ratings: ",yt.rating)


# #printing all the available streams
# print(yt.streams)




# # filtering out audio streams
# # print(yt.streams.filter(only_audio=True))
 



# # filtering only video streams
# print(yt.streams.filter(only_video=True))



# # Now, let’s talk about Progressive v/s Dash streams. YouTube uses Dash streams for higher-quality rendering.
# # Progressive streams are limited to 720p and it contains both audio and video codec files while Dash streams have higher quality but only have video codecs.

# # Filter out Progressive Video Stream
# print(yt.streams.filter(progressive=True))


# # get highest resotion for prgressive stream available
# ys = yt.streams.get_highest_resolution()

# # Choosing the video stream by the tag
# ys = yt.streams.get_by_itag('22')



# # download our preferred stream and save it in the current working directory.
# ys.download()

# # donwload to specfic location
# ys.download('location')



# # Eye Candy
# #Starting download
# print("Downloading...")
# ys.download()
# print("Download completed!!")





# FULL SAMPLE
from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")