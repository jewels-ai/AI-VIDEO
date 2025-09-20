from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
import os

def create_video(image_path, ad_text, music_path="sample_music/background.mp3", output_path="outputs/videos/output.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    clip = ImageClip(image_path).set_duration(5)

    txt_clip = TextClip(ad_text, fontsize=40, color='white', font='Arial-Bold',
                        method='caption', size=(clip.w*0.9, None))
    txt_clip = txt_clip.set_position('bottom').set_duration(5)

    video = CompositeVideoClip([clip, txt_clip])

    if music_path:
        audio = AudioFileClip(music_path).subclip(0, video.duration)
        video = video.set_audio(audio)

    video.write_videofile(output_path, fps=24)
    return output_path
