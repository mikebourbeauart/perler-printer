# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Designer
###########################################################################

class Designer ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bead Pattern Generator v1.0", pos = wx.DefaultPosition, size = wx.Size( 780,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 600,400 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetMinSize( wx.Size( 300,-1 ) )
		self.m_panel3.SetMaxSize( wx.Size( 300,-1 ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Image File" ), wx.VERTICAL )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.gif; *.jpg; *.jpeg; *.png", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer2.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4.Add( sbSizer2, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Bead Options" ), wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cb_hama = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_hama.SetValue(True) 
		bSizer8.Add( self.m_cb_hama, 0, wx.ALL, 5 )
		
		self.m_cb_perler = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Perler", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_cb_perler, 0, wx.ALL, 5 )
		
		self.m_cb_nabbi = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Nabbi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_cb_nabbi, 0, wx.ALL, 5 )
		
		self.m_cb_hobby = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"PictureBeads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_cb_hobby, 0, wx.ALL, 5 )
		
		sbSizer21.Add( bSizer8, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cb_standard = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Standard Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_standard.SetValue(True) 
		bSizer9.Add( self.m_cb_standard, 0, wx.ALL, 5 )
		
		self.m_cb_metal = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Metalic Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_metal, 0, wx.ALL, 5 )
		
		self.m_cb_glitter = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Glitter Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_glitter, 0, wx.ALL, 5 )
		
		self.m_cb_neon = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Neon Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_neon, 0, wx.ALL, 5 )
		
		self.m_cb_trans = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Translucent Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_trans, 0, wx.ALL, 5 )
		
		self.m_cb_flour = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Include Flourescent Beads", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_flour, 0, wx.ALL, 5 )
		
		self.m_cb_glow = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Glow in the Dark", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_cb_glow, 0, wx.ALL, 5 )
		
		sbSizer21.Add( bSizer9, 3, wx.EXPAND, 5 )
		
		bSizer4.Add( sbSizer21, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_generate = wx.Button( self.m_panel3, wx.ID_ANY, u"Generate Design", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_generate, 0, 0, 5 )
		
		bSizer4.Add( bSizer13, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		bSizer3.Add( self.m_panel3, 0, wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Design View" ), wx.VERTICAL )
		
		self.previewPane = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1.Add( self.previewPane, 1, wx.EXPAND, 5 )
		
		bSizer5.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_radioBtn3 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"Design View", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn3.SetValue( True ) 
		bSizer11.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( self.m_panel2, wx.ID_ANY, u"Materials View", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		bSizer11.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		bSizer5.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer3.Add( self.m_panel2, 1, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Load Image from File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Generate Design", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu4, u"Generate" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Design View", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Materials View", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem5 )
		
		self.m_menubar1.Append( self.m_menu5, u"View" ) 
		
		self.m_menu6 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.AppendItem( self.m_menuItem6 )
		
		self.m_menubar1.Append( self.m_menu6, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.onImageSelect )
		self.m_generate.Bind( wx.EVT_BUTTON, self.onGenerate )
		self.Bind( wx.EVT_MENU, self.onLoadImage, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.onGenerate, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.onAbout, id = self.m_menuItem6.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onImageSelect( self, event ):
		event.Skip()
	
	def onGenerate( self, event ):
		event.Skip()
	
	def onLoadImage( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	
	
	def onAbout( self, event ):
		event.Skip()
	

