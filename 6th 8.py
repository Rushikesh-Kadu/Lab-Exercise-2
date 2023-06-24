with open('image.png','rb') as f:
    f1=open('image1.png','wb')
    f1.write(f.read())
    print("Image created Successfully")
    f1.close()