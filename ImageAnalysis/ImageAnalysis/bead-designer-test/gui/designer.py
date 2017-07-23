"""
designer.py
"""
import warnings
warnings.filterwarnings("ignore")
import os
import sys
import wx
import wx
import beadgui

#Some constants
#BEAD_RADIUS = 1.75*mm
#BEAD_THICKNESS = 1*mm
#BOARD_SPACING = 4.85*mm
#BOARD_BORDER = 4*mm

#Some notes
#A4 60x43 = 2580
#A3 86x60 = 5160
#A2 86x120 = 10,320
#MARQUEE A4+A4 = 120x43


# Implementing Designer
class BeadDesignDesigner( beadgui.Designer ):
  def __init__( self, parent ):
    beadgui.Designer.__init__( self, parent )
    self.addPDFWindow()

  def addPDFWindow(self):
    from wx.lib.pdfwin import PDFWindow
    self.pdf = PDFWindow(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
    self.previewPane.Add(self.pdf, proportion=1, flag=wx.EXPAND)
    self.pdf.Raise()    
    self.SetSize((780,620))
    self.loadPDF()

  def loadPDF(self, pdf="C:\\code\\pil\\images\\title.pdf"):    
    self.pdf.LoadFile(pdf)
    self.pdf.setView('FitB')
    #self.pdf.Show()    
    
#==========================================================================================
# Handlers for Designer events.
  def onImageSelect(self, event):
    pass
  
  def onAbout(self, event):
    info = wx.AboutDialogInfo()
    info.SetIcon(wx.Icon('C:\\code\\pil\\images\\jon.png', wx.BITMAP_TYPE_PNG))
    info.SetName('Bead Pattern Designer')
    info.SetVersion('1.0')
    info.SetDescription("A simple utility to generate patterns for HAMA beads")
    info.SetCopyright('(C) 2011 Jon Wilson')
    info.SetWebSite('https://sites.google.com/site/degenatrons/')
    info.AddDeveloper('Jon Wilson')
    wx.AboutBox(info)
        

  def onGenerate( self, event ):
    # TODO: Implement onGenerate
    pass

  def onImage( self, event ):
    # TODO: Implement onImage
    pass

  def onView( self, event ):
    # TODO: Implement onView
    pass

  def onLoadImage( self, event ):
    # TODO: Implement onLoadImage
    pass

  def onExit( self, event ):
    # TODO: Implement onExit
    pass

  
def main():
  app = wx.App(False)
  BeadDesignDesigner(None).Show()
  app.MainLoop()
  app.Destroy()

if __name__ == "__main__":
  main()  