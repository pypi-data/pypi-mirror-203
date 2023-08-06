class Command_function:
    
    def Youtube_Download_video(url,resolution,user_path):
        print(f"Wait untill few seconds.. Your  Downloader is Processing..")
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()
        return_value = stream.download(output_path=user_path)
        if return_value:
            return True
        else:
            return False
        
    def Youtube_Download_video_Resolution(url):
        yt = YouTube(url)
        streams = yt.streams.all()
        resolutions = []
        for stream in streams:
            if 'video/mp4' in str(stream.mime_type):
                return_value = resolutions.append(stream.resolution)
        if resolutions is not None:
            return resolutions
        else:
            return False
    

    def Youtube_Download_Audio(url,user_path,user_filename):
        print(f"Wait untill few seconds.. Your Downloader is Processing..")
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        return_value = audio.download(output_path=user_path, filename=user_filename)
        if return_value:
            return True
        else:
            return False

    # def Other_Downloading_Resources(url):
    #     print(f"Wait untill few seconds.. Your Downloader is Processing..")
    #     ydl_opts = {}
    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         return_value = ydl.download(f"{[url]}")
    #     if return_value:
    #         return True
    #     else:
    #         return False
        
    def Image_Download(url,path,filename):
        print(f"Wait untill few seconds.. Your Downloader is Processing..")
        return_value = urllib.request.urlretrieve(url, path + filename)
        if return_value:
            return True
        else:
            return False
        