#!/usr/bin/env python  

 """
 http://wiki.wxpython.org/AnotherTutorial
 """
 
import wx

app = wx.App()

frame = wx.Frame(None, -1, 'simple.py')
frame.Show()

frame.SetTitle("Work Timer")

app.MainLoop()

