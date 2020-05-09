from moviepy.editor import VideoFileClip

# 从视频中提取音频


def get_audio_from_video():
    video = VideoFileClip(r'D:\PycharmProjects\mv.mp4')
    audio = video.audio
    audio.write_audiofile(r'D:\PycharmProjects\test.mp3')
    audio.close()
    video.close()
