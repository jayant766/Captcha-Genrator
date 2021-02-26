#generate image captcha
from captcha.image import ImageCaptcha
image = ImageCaptcha()

image_data = image.generate('jayant')
image.write('jayant', 'captcha.png')

#generate audio captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
audio_data = audio.generate('1111')
audio.write('1111', 'audio.wav')