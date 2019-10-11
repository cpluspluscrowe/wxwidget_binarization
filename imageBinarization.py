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


#plt.imshow(thresh5,'gray')

import wx

def onButton(event):
    print
    "Button pressed."

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(500, 500))
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
        self.refresh_image()
        self.pnl.SetSizer(vbox)
        self.Centre()
        self.Show(True)
    def refresh_image(self):

        bmp = wx.Bitmap("./gray_image.png", wx.BITMAP_TYPE_ANY)

        button = wx.BitmapButton(self.pnl, id=wx.ID_ANY, bitmap=bmp,
                                 size=(300,300))
        button.Bind(wx.EVT_BUTTON, onButton)
        button.SetPosition((100, 175))

    def OnSliderScroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        ret, thresh = cv2.threshold(gray_image, val, 255, cv2.THRESH_BINARY)
        cv2.imwrite('gray_image.png', thresh)
        self.refresh_image()
        #font = self.GetFont()
        #font.SetPointSize(self.sld.GetValue())
        #self.txt.SetFont(font)


ex = wx.App()
Mywin(None, 'Image Binarization')
ex.MainLoop()