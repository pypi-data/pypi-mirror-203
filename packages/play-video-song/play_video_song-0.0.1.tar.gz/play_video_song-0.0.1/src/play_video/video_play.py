from pytube import YouTube
import vlc
import time

video_url = input("enter url link of Youtube video song: ")

def video_play(video_url):
    def video(func):
        def download_play(vname):
            yt = YouTube(video_url)
            yt.streams.filter(res="720p", progressive="True", type="video").first().download('.', vname)
            func(vname)
        return download_play
    return video

@video_play(video_url)
def video_song_play(video_name):
    media_player = vlc.MediaPlayer(video_name)
    media_player.play()
    time.sleep(180)



