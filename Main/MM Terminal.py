import yt_dlp
from pytube import Playlist
from tqdm import tqdm

# SECTION - PlayListTest - DoNotShip
TestDrive1 = 'https://www.youtube.com/playlist?list=PLOOt-rtlXnMKO2XF4DCH4l8HyxoUt5TB4'
TestDrive2 = 'https://www.youtube.com/playlist?list=PLOOt-rtlXnMK3fuIy02wmsvRoFi0Ojxn2'
TestDrive3 = 'https://www.youtube.com/playlist?list=PLOOt-rtlXnMIFWHR6T0FB6-ztOeNCAok8'
#!SECTION - PlayListTest - DoNotShip

    # SECTION - config
DEBUG_MODE = True
VERSION = '1.2.5'
FFMPEG_location = None
linkTypeFlag: bool = None
Quality: str = None
# Password = None
# Username = None
playlist_test_link = TestDrive3
format_list = ["best", "bestaudio", "bestvideo", "worst", "worstvideo", "worstaudio",
                "3gp", "aac", "flv", "m4a", "mp3", "mp4", "ogg", "wav", "webm",
                  "360", "480", "720", "1080", "1440", "2160"]
# !SECTION - config


def Get_ydl_opts(ydl_download_dir):
    return {
        'outtmpl': '%(title)s.%(ext)s',
        'paths': {'home': ydl_download_dir, 'temp': "./Mirage's Mixtape/temp files"},
        'verbose': DEBUG_MODE,
        'ffmpeg_location': "./Mirage's Mixtape/ffmpeg-7.0.1-full_build/bin/ffmpeg.exe",
        'format': format_choice,
        #TODO - add a cookie for the whole thing
    }


def Get_playlist_videos(playlist_link):
    Located_playlist = Playlist(playlist_link)
    video_urls = [video for video in Located_playlist.video_urls]
    videos = []
    total_videos = len(video_urls)

    print("\n🚀 | Fetching videos from the playlist...")

    with tqdm(total=total_videos, desc="🎬 Progress", unit="video") as ProgressBar:
        for vid_url in video_urls:
            try:
                YT_loader = yt_dlp.YoutubeDL({'quiet': True})
                whatisthisvariable = YT_loader.extract_info(vid_url, download=True)
                videos.append(vid_url)
                ProgressBar.update(1)
            except Exception as Error:
                print(f"❌ | An error occurred while fetching video : \n {Error}")

    print("\n✅ | Done fetching videos.\n")
    return videos, total_videos


def Download_playlist(video_links, download_dir):
    print("\n   📥 Downloading videos...")
    ydl_opts = Get_ydl_opts(download_dir)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl_opts_loader:
        with tqdm(total=len(video_links), desc="🎬 | Progress", unit="video") as ProgressBar:
            for vid_link in video_links:
                try:
                    ydl_opts_loader.download([vid_link])
                    print(f"\n✅ | Downloaded video: {ydl_opts_loader.extract_info(vid_link, download=False)['title']}")
                except Exception as Error:
                    print(f"❌ | An error occurred while downloading video : \n {Error}")
                ProgressBar.update(1)

    print("\n🎩 | Finished downloading videos.")


def Download_video(video_link, download_dir):
    print("\n📥 Downloading videos...")
    ydl_opts = Get_ydl_opts(download_dir)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl_opts_loader:
        with tqdm(total=len(video_link), desc="🎬 | Progress", unit="data rate?") as ProgressBar:
            try:
                ydl_opts_loader.download([video_link])
                print(f"\n✅ | Downloaded video: {ydl_opts_loader.extract_info(video_link, download=False)['title']}")
            except Exception as Error:
                print(f"❌ | An error occurred while downloading video : \n {Error}")
            ProgressBar.update(1)

    print("\n🎩 | Finished downloading videos.")



if __name__ == "__main__":
    print(f"-=[{'='*40}]=╕")
    print(f"🎹 | Mirage's Mixtape        [Version {VERSION}]\n")

    print("┌=[current available downloaders]=-")
    print("└─── video, playlist")
    
    while True:
        link_type = input("🎹 | Enter the type of video you wish to download : ")
        if link_type.lower() in ["video", "playlist"]: break
        else: print("Invalid Type, maybe dont put a space there?")

    match link_type:
        case "video":
            linkTypeFlag = True
            print("\n\n-=[Before you enter a video, make sure it's at least unlisted or public for it to be able to be accessed]=-")
            video_link = input("🎹 | Enter the YouTube video link: ")

        case "playlist":
            linkTypeFlag = False
            print("\n\n-=[Before you enter a playlist, make sure it's at least unlisted or public for it to be able to be accessed]=-")
            playlist_link = input("🎹 | Enter the YouTube playlist link: ")

    print("\n\n┌=[the download location should look like this]=-")
    print("└──── ./your/path/here")
    download_location = input("🎹 | Enter the directory where you want to store the files : ")

    print("\n\n┌=[current available file formats]=-")
    print("│   ┌ best, bestaudio, bestvideo, worst, worstvideo, worstaudio")
    print("└───┼ resolution : 360, 480, 720, 1080, 1440, 2160")
    print("    └ extention only : 3gp, aac, flv, m4a, mp3, mp4, ogg, wav, webm \n")

    while True:
        format_choice = input("🎛️ | Enter the format you wish to download : ")
        if format_choice.lower() in format_list: break
        else: print("Invalid format, maybe look at the list?")

    if linkTypeFlag == True: Download_video(video_link, download_location)
    else:
        video_links, total_videos = Get_playlist_videos(playlist_link)
        Download_playlist(video_links, download_location)
        print(f"\n🎉 Total videos downloaded: {total_videos}")

    print(f"-=[{'='*40}]=╛")
