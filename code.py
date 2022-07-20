from PIL import image
me = Image.open('') #your image
bg = Image.open('') #background
bg.paste(me,(0,0),me)
me.show()
bg.save('')
