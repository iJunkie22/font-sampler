#Boa:Frame:Frame1

import wx
import sys
import os
import wx.lib.filebrowsebutton
import AboutDialog
import font_list_generator
class Options:
    pass

# ------------------------ private library ---------------
#from library import *
def directory_chooser_dialog(title, default):
    dialog = wx.DirDialog(None, title, default)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetPath()
    else:
        return default

def msgbox(msg, title=''):
    wx.MessageBox(msg)

def get_samples_dir():
    return os.path.join(get_mydocuments_dir(), 'Font-Samples')

def get_mydocuments_dir():

    if sys.platform in ['darwin', 'mac']:
        from Carbon import Folder, Folders
        folderref = Folder.FSFindFolder(Folders.kUserDomain,
            Folders.kDocumentsFolderType, False)
        mydocs = folderref.as_pathname()
        
    elif 'win' in sys.platform:
        from win32com.shell import shell
        df = shell.SHGetDesktopFolder()
        pidl = df.ParseDisplayName(0, None, "::{450d8fba-ad25-11d0-98a8-0800361b1103}")[1]
        mydocs = shell.SHGetPathFromIDList(pidl)
        
    elif 'linux' in sys.platform:
        mydocs = '~/Desktop'
    
    else:
        mydocs = os.path.abspath('.')  #cur dir
    
    return mydocs
    
def get_fonts_dir():
    if sys.platform in ['darwin', 'mac']:
        return ''
        
    elif 'win' in sys.platform:
        return os.environ['windir'] + '\\' + 'Fonts'
        
    elif 'linux' in sys.platform:
        return '/usr/share/fonts/truetype'
    
    else:
        return os.path.abspath('.')  #cur dir
    
# ------------------------ private library ---------------

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BACK_COLOR_PICKER, wxID_FRAME1BTNDIRPICKER, 
 wxID_FRAME1BTNEXIT, wxID_FRAME1BTNOUTPUTDIR, wxID_FRAME1BUTTON1, 
 wxID_FRAME1FONT_SIZE, wxID_FRAME1FORE_COLOR_PICKER, wxID_FRAME1PANEL1, 
 wxID_FRAME1SPLIT_HEIGHT, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1TXTDIRFONTDIR, wxID_FRAME1TXTOUTPUTDIR, wxID_FRAME1TXTSAMPLE, 
] = [wx.NewId() for _init_ctrls in range(21)]

[wxID_FRAME1MENU1ITEMS0, wxID_FRAME1MENU1ITEMS1, wxID_FRAME1MENU1ITEMS2, 
 wxID_FRAME1MENU1ITEMS4, wxID_FRAME1MENU1ITEMS5, wxID_FRAME1MENU1ITEMS6, 
 wxID_FRAME1MENU1ITEMS7, wxID_FRAME1MENU1ITEMS8, 
] = [wx.NewId() for _init_coll_menu1_Items in range(8)]

[wxID_FRAME1EDITMENUSITEMS0, wxID_FRAME1EDITMENUSITEMS1, 
 wxID_FRAME1EDITMENUSITEMS2, wxID_FRAME1EDITMENUSITEMS4, 
 wxID_FRAME1EDITMENUSITEMS5, 
] = [wx.NewId() for _init_coll_editmenus_Items in range(5)]

[wxID_FRAME1FILEMENUSITEMS_EXIT, wxID_FRAME1FILEMENUSITEM_OPEN, 
 wxID_FRAME1FILEMENUSITEM_SAVE, wxID_FRAME1FILEMENUSITEM_SAVE_AS, 
] = [wx.NewId() for _init_coll_filemenus_Items in range(4)]

[wxID_FRAME1HELPMENUSITEM_ABOUT, wxID_FRAME1HELPMENUSITEM_HELP_CONTENTS, 
] = [wx.NewId() for _init_coll_helpmenus_Items in range(2)]

[wxID_FRAME1EDITMENUS_WTFITEMS1, wxID_FRAME1EDITMENUS_WTFITEMS2, 
 wxID_FRAME1EDITMENUS_WTFITEMS4, wxID_FRAME1EDITMENUS_WTFITEMS5, 
 wxID_FRAME1EDITMENUS_WTFITEM_DO_THIS, 
] = [wx.NewId() for _init_coll_editmenus_wtf_Items in range(5)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.filemenus, title=u'&File')
        parent.Append(menu=self.editmenus_wtf, title=u'&Edit')
        parent.Append(menu=self.helpmenus, title=u'&Help')

    def _init_coll_filemenus_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1FILEMENUSITEM_OPEN,
              kind=wx.ITEM_NORMAL, text=u'&Open')
        parent.Append(help='', id=wxID_FRAME1FILEMENUSITEM_SAVE,
              kind=wx.ITEM_NORMAL, text=u'&Save')
        parent.Append(help='', id=wxID_FRAME1FILEMENUSITEM_SAVE_AS,
              kind=wx.ITEM_NORMAL, text=u'Save &As...')
        parent.AppendSeparator()
        parent.Append(help=u'', id=wxID_FRAME1FILEMENUSITEMS_EXIT,
              kind=wx.ITEM_NORMAL, text=u'E&xit')
        self.Bind(wx.EVT_MENU, self.OnFilemenusItems_exitMenu,
              id=wxID_FRAME1FILEMENUSITEMS_EXIT)

    def _init_coll_helpmenus_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'', id=wxID_FRAME1HELPMENUSITEM_HELP_CONTENTS,
              kind=wx.ITEM_NORMAL, text=u'&Help contents')
        parent.AppendSeparator()
        parent.Append(help=u'', id=wxID_FRAME1HELPMENUSITEM_ABOUT,
              kind=wx.ITEM_NORMAL, text=u'&About')
        self.Bind(wx.EVT_MENU, self.OnHelpmenusItem_aboutMenu,
              id=wxID_FRAME1HELPMENUSITEM_ABOUT)

    def _init_coll_editmenus_wtf_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1EDITMENUS_WTFITEM_DO_THIS,
              kind=wx.ITEM_NORMAL, text=u'Do this')
        parent.Append(help='', id=wxID_FRAME1EDITMENUS_WTFITEMS1,
              kind=wx.ITEM_NORMAL, text=u'Do That...')
        parent.Append(help='', id=wxID_FRAME1EDITMENUS_WTFITEMS2,
              kind=wx.ITEM_NORMAL, text=u'Etc.')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_FRAME1EDITMENUS_WTFITEMS4,
              kind=wx.ITEM_NORMAL, text='Items4')
        parent.Append(help='', id=wxID_FRAME1EDITMENUS_WTFITEMS5,
              kind=wx.ITEM_NORMAL, text='Items5')
        self.Bind(wx.EVT_MENU, self.OnEditmenus_wtfItem_do_thisMenu,
              id=wxID_FRAME1EDITMENUS_WTFITEM_DO_THIS)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(3)

        parent.SetStatusText(number=0, text=u'Ready')
        parent.SetStatusText(number=1, text=u'Font count')
        parent.SetStatusText(number=2, text=u'\xa9 Shula')

        parent.SetStatusWidths([-1, -2, -1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.editmenus_wtf = wx.Menu(title=u'')

        self.filemenus = wx.Menu(title=u'&File')

        self.helpmenus = wx.Menu(title=u'&Help')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_editmenus_wtf_Items(self.editmenus_wtf)
        self._init_coll_filemenus_Items(self.filemenus)
        self._init_coll_helpmenus_Items(self.helpmenus)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(446, 273), size=wx.Size(333, 413),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Generate Font Samples')
        self._init_utils()
        self.SetClientSize(wx.Size(325, 386))
        self.SetStatusBarPane(1)
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetStatusText(u'zorba')
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(325, 347),
              style=wx.TAB_TRAVERSAL)

        self.txtDirFontdir = wx.TextCtrl(id=wxID_FRAME1TXTDIRFONTDIR,
              name=u'txtDirFontdir', parent=self.panel1, pos=wx.Point(96, 16),
              size=wx.Size(184, 21), style=0, value=u'C:\\WINDOWS\\Fonts')

        self.btnDirPicker = wx.Button(id=wxID_FRAME1BTNDIRPICKER, label=u'...',
              name=u'btnDirPicker', parent=self.panel1, pos=wx.Point(280, 16),
              size=wx.Size(27, 23), style=0)
        self.btnDirPicker.Bind(wx.EVT_BUTTON, self.OnBtnDirPickerButton,
              id=wxID_FRAME1BTNDIRPICKER)

        self.back_color_picker = wx.ColourPickerCtrl(col=wx.Colour(253, 255,
              185), id=wxID_FRAME1BACK_COLOR_PICKER, name=u'back_color_picker',
              parent=self.panel1, pos=wx.Point(96, 56), size=wx.Size(72, 20),
              style=wx.CLRP_DEFAULT_STYLE)
        self.back_color_picker.SetToolTipString(u'zzzz in Pixels)')

        self.fore_color_picker = wx.ColourPickerCtrl(col=wx.Colour(0, 0, 64),
              id=wxID_FRAME1FORE_COLOR_PICKER, name=u'fore_color_picker',
              parent=self.panel1, pos=wx.Point(96, 88), size=wx.Size(64, 24),
              style=wx.CLRP_DEFAULT_STYLE)

        self.split_height = wx.TextCtrl(id=wxID_FRAME1SPLIT_HEIGHT,
              name=u'split_height', parent=self.panel1, pos=wx.Point(96, 128),
              size=wx.Size(40, 21), style=0, value=u'600')

        self.font_size = wx.TextCtrl(id=wxID_FRAME1FONT_SIZE, name=u'font_size',
              parent=self.panel1, pos=wx.Point(96, 160), size=wx.Size(40, 21),
              style=0, value=u'22')

        self.txtSample = wx.TextCtrl(id=wxID_FRAME1TXTSAMPLE, name=u'txtSample',
              parent=self.panel1, pos=wx.Point(96, 192), size=wx.Size(216, 21),
              style=0,
              value=u'\u05d0\u05b8\u05dc\u05b6\u05e9\u05d9\u05d5\u05e3 \u05e4\u05bc\u05b5\u05e8\u05b4\u05e7 1234 %^&*$')

        self.button1 = wx.Button(id=wx.ID_OK, label=u'&Generate Samples',
              name='button1', parent=self.panel1, pos=wx.Point(24, 280),
              size=wx.Size(168, 56), style=0)
        self.button1.SetToolTipString(u'button1')
        self.button1.SetHelpText(u'')
        self.button1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wx.ID_OK)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Font (*.ttf) containing folder', name='staticText2',
              parent=self.panel1, pos=wx.Point(8, 16), size=wx.Size(88, 32),
              style=0)
        self.staticText2.SetToolTipString(u'Height of each result image (in Pixels)')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Text Color', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(50, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Background Color', name='staticText3', parent=self.panel1,
              pos=wx.Point(8, 56), size=wx.Size(84, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Split to (pixels)', name='staticText4',
              parent=self.panel1, pos=wx.Point(16, 128), size=wx.Size(71, 13),
              style=0)
        self.staticText4.SetToolTipString(u'Height of each result image (in Pixels)')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Font Size (pixels)', name='staticText5',
              parent=self.panel1, pos=wx.Point(8, 160), size=wx.Size(82, 13),
              style=0)
        self.staticText5.SetToolTipString(u'Height of each result image (in Pixels)')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Sample text', name='staticText6', parent=self.panel1,
              pos=wx.Point(32, 192), size=wx.Size(57, 13), style=0)

        self.btnExit = wx.Button(id=wx.ID_CANCEL, label=u'&Close',
              name=u'btnExit', parent=self.panel1, pos=wx.Point(224, 280),
              size=wx.Size(75, 56), style=0)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExitButton, id=wx.ID_CANCEL)

        self.btnOutputDir = wx.Button(id=wxID_FRAME1BTNOUTPUTDIR, label=u'...',
              name=u'btnOutputDir', parent=self.panel1, pos=wx.Point(280, 224),
              size=wx.Size(27, 23), style=0)
        self.btnOutputDir.Bind(wx.EVT_BUTTON, self.OnBtnDirPickerButton,
              id=wxID_FRAME1BTNOUTPUTDIR)

        self.txtOutputDir = wx.TextCtrl(id=wxID_FRAME1TXTOUTPUTDIR,
              name=u'txtOutputDir', parent=self.panel1, pos=wx.Point(96, 224),
              size=wx.Size(176, 21), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Create samples in', name='staticText7',
              parent=self.panel1, pos=wx.Point(8, 224), size=wx.Size(88, 16),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.txtOutputDir.Value = get_samples_dir()
        self.txtDirFontdir.Value = get_fonts_dir()
        
    def OnMenu1Items6Menu(self, event):
        event.Skip()

    def OnFilemenusItems_exitMenu(self, event):
        self.Close()

    def OnHelpmenusItem_aboutMenu(self, event):
        #msgbox('Welcome to Boa Constructor 0.6.x\nThis template was created by Shula')
        dlg = AboutDialog.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy() 
        
        
    def OnEditmenus_wtfItem_do_thisMenu(self, event):
        d = directory_chooser_dialog('ahalan', 'd:\\shahar')
        wx.MessageBox(d)
        msgbox('done')

    def OnBtnDirPickerButton(self, event):
        self.txtDirFontdir.Value = directory_chooser_dialog('folder with *.ttf files', self.txtDirFontdir.Value )

    def OnButton1Button(self, event):
        print self.fore_color_picker.Colour
        options = Options()
        options.fore = self.fore_color_picker.Colour
        options.background = self.back_color_picker.Colour
        options.height = int(self.split_height.Value)
        options.fontdir = self.txtDirFontdir.Value
        options.size = int(self.font_size.Value)
        options.sample = self.txtSample.Value
        options.outputdir = self.txtOutputDir.Value
        font_count = font_list_generator.generate_font_image(options)
        self.set_status(0, 'done')
        self.set_status(1, '%d fonts listed' % font_count)
        print 'done.'
        
    def OnBtnExitButton(self, event):
        self.Close()

    def set_status(self, field_num, text):
        self.statusBar1.SetStatusText(text, field_num)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
