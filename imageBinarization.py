#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

def convert_color_image_to_grayscale(image):
    """converts a color image to grayscale"""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def show_gray_image(gray_image):
    """ Shows the gray image on the screen"""
    cv2.imshow('gray_image',gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
image = cv2.imread('./image.jpeg')
gray_image = convert_color_image_to_grayscale(image)
cv2.imwrite('gray_image.png',gray_image)

#show_gray_image(gray_image)

# load the gray image
gray_image = cv2.imread("./gray_image.png")
cv2.imwrite("current_image.png", gray_image)

def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a < b:
        return 0
    else:
        return 255


vfunc = np.vectorize(myfunc)


#plt.imshow(thresh5,'gray')

import wx



class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(500, 600))
        self.InitUI()

    def InitUI(self):
        self.pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sld = wx.Slider(self.pnl, value=127, minValue=0, maxValue=255,
                             style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.sld.SetPosition((300, 10))

        vbox.Add(self.sld, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sld.Bind(wx.EVT_SLIDER, self.OnSliderScroll)

        self.txt = wx.StaticText(self.pnl, label='', style=wx.ALIGN_CENTER)
        vbox.Add(self.txt, 1, wx.ALIGN_CENTRE_HORIZONTAL)

        self.fb = wx.Button(self.pnl, wx.ID_ANY, 'Choose Image', (10, 100))

        self.fb.Bind(wx.EVT_BUTTON, self.onButton)
        self.fb.SetPosition((100, 500))
        self.fb.SetBackgroundColour("Dark Grey")

        self.path = "current_image.png"
        self.gray_image = gray_image
        self.refresh_image(gray_image)
        self.pnl.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def onButton(self, event):
        openFileDialog = wx.FileDialog(self.pnl, "Open", "", "",
                                       "Python files (*.png)|*.png",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        openFileDialog.Destroy()
        self.path = openFileDialog.GetPath()
        self.gray_image = cv2.imread(self.path)
        self.refresh_image(self.gray_image)
        print(self.path)

    def refresh_image(self, image):
        cv2.imwrite("temp.png", image)
        bmp = wx.Bitmap("temp.png", wx.BITMAP_TYPE_ANY)
        button = wx.BitmapButton(self.pnl, id=wx.ID_ANY, bitmap=bmp,
                                 size=(300,300))
        button.Bind(wx.EVT_BUTTON, lambda x: x)
        button.SetPosition((100, 175))
        cv2.imwrite("current_image.png", image)

    def OnSliderScroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        thresh = vfunc(self.gray_image, val)
        #ret, thresh = cv2.threshold(gray_image, val, 255, cv2.THRESH_BINARY)
        self.refresh_image(thresh)



ex = wx.App()
Mywin(None, 'Image Binarization')
ex.MainLoop()