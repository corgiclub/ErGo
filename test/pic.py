import PIL.Image as Img
import imghdr


_img = Img.open(open('1.gif', 'rb'))
_img_type = imghdr.what(file='1.gif')

print(_img.info['duration'], _img_type)
print(0)
