"""
Youtube video downloads using python scripts
"""

#Note: pytube latest version might not work
# so i recommend you install pytube3

# import the required library
import pytube

#name a variable that stores the link of the youtube video
url = "https://www.youtube.com/watch?v=GLfUtNUFq5I"

video = pytube.YouTube(url)
youtube = video.streams.first()

# specify the location of where the video will be stored
youtube.download(r"C:\Users\Daniel\Desktop")
