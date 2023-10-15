from pytube import YouTube
from pytube.exceptions import VideoUnavailable


class ModelActions():
    def __init__(self):
        self.yt = None

    def GetInfoFromURL(self, url_link):
        self.yt = YouTube(url_link)

    def GetStream(self, selectedTag):
        return self.yt.streams.get_by_itag(itag = selectedTag)