import googletrans
from googletrans import Translator 
t = Translator()
a = t.translate('Em đẹp quá",src="vi",dest="en')
b = a.text
print(b)