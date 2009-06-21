#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BTNCLOSE, wxID_DIALOG1STATICTEXT1, 
 wxID_DIALOG1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(299, 363), size=wx.Size(414, 190),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(406, 163))
        self.Bind(wx.EVT_KEY_UP, self.OnDialog1KeyUp)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'About Me', name='staticText1', parent=self,
              pos=wx.Point(80, 16), size=wx.Size(112, 24), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Comic Sans MS'))

        self.btnClose = wx.Button(id=wx.ID_CANCEL, label=u'&Close',
              name=u'btnClose', parent=self, pos=wx.Point(288, 120),
              size=wx.Size(75, 23), style=0)
        self.btnClose.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BTNCLOSE)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u" Don Juan did not discuss the mastery of awareness with me until months later. We were at that time in the house where the nagual's party lived.",
              name='staticText2', parent=self, pos=wx.Point(16, 48),
              size=wx.Size(376, 56), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnDialog1KeyUp(self, event):
        char = event.GetRawKeyCode()
        if char in [13, 27, 32]:            # enter, esc, spacebar
            self.OnButton1Button(event)

    def OnButton1Button(self, event):
        self.Close()
