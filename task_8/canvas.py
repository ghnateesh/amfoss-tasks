from PIL import Image
import pytesseract
i=Image.open('canvas.png')
s=pytesseract.image_to_string(i,lang='eng')
k=s.find('+') or s.find('-') or s.find('*') or s.find('/')
a=s[0:k]
b=s[k+1:len(s)+1]
a=int(a)
b=int(b)
if s[k]=='+':
	print(a+b)
if s[k]=='-':
	print(a-b)
if s[k]=='*':
	print(a*b)
if s[k]=='/':
	print(a/b)