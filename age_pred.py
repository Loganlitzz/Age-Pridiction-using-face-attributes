# -*- coding: utf-8 -*-
from tensorflow.python.keras import backend as K
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import os
import numpy as np
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
model=load_model('age_out.h5')

def model_predict(img_pth):
  image = cv2.imread(img_pth)
  _,tail = os.path.split(img_pth)
  split_var = tail.split('_')
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image = cv2.resize(image,(256,256))
  image = np.reshape(image,(1,256,256,3))

  out = model.predict(image)
  out = K.eval(out)
  data='PREDICTED AGE : '+str(round(out[0][0]-3))+" - "+str(round(out[0][0]+1))
  return data
        

def select_image():
    # grab a reference to the image panels
    global panelA


    path = filedialog.askopenfilename()
        # ensure a file path was selected
    if len(path) > 0:

        image = cv2.imread(path)
        image=cv2.resize(image,(400,400)) 
        c=model_predict(path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        image = ImageTk.PhotoImage(image)

        if panelA is None :
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=450, pady=10)

        else:
            panelA.configure(image=image)

            panelA.image = image

        Btn1.configure(text=c)


    
root = Tk()
root.state('zoomed')
root['bg']='pink'
panelA = None
outlabel=None


btn = Button(root, text="Select an image",font=("Arial", 15), command=select_image)
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")
Btn1 = Button(root, text="",font=("Arial", 25), bg='blue', fg='yellow')
Btn1.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")
root.mainloop()
