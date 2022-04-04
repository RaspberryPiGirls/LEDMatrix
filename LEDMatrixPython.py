import board
import time
import neopixel
from PIL import Image
from adafruit_pixel_framebuf import PixelFramebuffer

pixel_pin = board.D18
pixel_width = 16
pixel_height = 48
num_pixels =  768

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.2,
    auto_write=False,
)

text = "Raspberry Pi Girls"
icon_emoji = Image.open("Emoji.png")
icon_covid = Image.open("Covid.png")
icon_bk = Image.open("bk.png")

while True:
    pixel_framebuf = PixelFramebuffer(
         pixels,
         pixel_width,
         pixel_height,
         reverse_x= True,
         orientation=1,
         rotation=1)

    for i in range(6 * len(text) + pixel_width-1):
        pixel_framebuf.fill(0x000000)
        if  (i % 32) == 0:
            linecolor1 = 0x0000FF
            linecolor2 = 0xFFFF00
            linecolor3 = 0x00FFFF
            linecolor4 = 0xFF4500
        elif (i % 32) == 8:
            linecolor1 = 0xFF4500
            linecolor2 = 0x0000FF
            linecolor3 = 0xFFFF00
            linecolor4 = 0x00FFFF
        elif (i % 32) == 16:
            linecolor1 = 0x00FFFF
            linecolor2 = 0xFF4500
            linecolor3 = 0x0000FF
            linecolor4 = 0xFFFF00
        elif (i % 32) == 24:
            linecolor1 = 0xFFFF00
            linecolor2 = 0x00FFFF
            linecolor3 = 0xFF4500
            linecolor4 = 0x0000FF
        pixel_framebuf.line(0, 0, pixel_height-1, 0, linecolor1)
        pixel_framebuf.line(0, pixel_width-1, pixel_height - 1, pixel_width-1, linecolor3)
        #pixel_framebuf.line(0, 0, 0,0, 0xFFFFFF)
        #pixel_framebuf.line(0, pixel_height-1, 0,pixel_height-1, 0xFFFFFF)
        #pixel_framebuf.line(pixel_width-1, 0, pixel_width-1, 0, 0xFFFFFF)
        #pixel_framebuf.line(pixel_width-1, pixel_height-1, pixel_width-1, pixel_height-1, 0xFFFFFF)
        pixel_framebuf.text(text, pixel_width - i , 4, 0xb400ff)
        pixel_framebuf.line(0, 1, 0, pixel_width-2, linecolor4)
        pixel_framebuf.line(pixel_height - 1, 1, pixel_height - 1, pixel_width-2, linecolor2)
        pixel_framebuf.display()
        time.sleep(0.05)

    pixel_framebuf = PixelFramebuffer(
      pixels,
      pixel_width,
      pixel_height,
      reverse_x = True)
    image = Image.new("RGBA", (pixel_width, pixel_height))

    image.alpha_composite(icon_bk)
    pixel_framebuf.image(image.convert("RGB"))
    pixel_framebuf.rect(0, 0, pixel_width, pixel_height, 0xFFFFFF)
    pixel_framebuf.display()

    image.alpha_composite(icon_covid)
    pixel_framebuf.image(image.convert("RGB"))
    pixel_framebuf.display() 
    time.sleep(6)

    image.alpha_composite(icon_bk)
    pixel_framebuf.image(image.convert("RGB"))
    pixel_framebuf.display()

    image.alpha_composite(icon_emoji)
    pixel_framebuf.image(image.convert("RGB"))
    pixel_framebuf.display() 
    time.sleep(4)

    image.alpha_composite(icon_bk)
    pixel_framebuf.image(image.convert("RGB"))
    pixel_framebuf.display()
