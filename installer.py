import wx
import wx.adv
import asyncio


class wizard(wx.adv.Wizard):

	def __init__(self):
		super().__init__(
			parent=None,
			title='BEE Manipulator Installer',
			bitmap=wx.Bitmap('./icon.png')
		)
		self.SetIcon(wx.Icon('./icon.png'))
		self.Bind(wx.EVT_CLOSE, self.OnClose, self)
		self.Bind(wx.adv.EVT_WIZARD_CANCEL, self.OnCancelButton, self)
		self.Bind(wx.adv.EVT_WIZARD_FINISHED, self.OnFinishedButton, self)

	def Run(self):
		self.RunWizard(pageObj0)
		asyncio.run(self.WaitForFinish())

	async def WaitForFinish(self):
		while self.IsRunning():
			pass
		wx.Exit()

	@staticmethod
	def OnClose(self, event=None):
		wx.Exit()

	def OnCancelButton(self, event=None):
		pass

	def OnFinishedButton(self, event=None):
		pass


class page0(wx.adv.WizardPage):

	def __init__(self):
		super().__init__(
			parent=wx.GetTopLevelWindows()[0]
		)
		sizer = wx.GridSizer(cols=2,hgap=2,vgap=2)
		sizer.Add(
			wx.StaticText(
				parent=self,
				label=
				'''Welcome to the BEE Manipulator installer!\nClick "next" to start the installation''',

			)
		)
		sizer.Add(
			wx.CheckBox(
				parent=self,
				label='Close automatically when finished'
			)
		)
		self.SetSizer(sizer)

	def GetPrev(self):
		return None

	def GetNext(self):
		return pageObj1


class page1(wx.adv.WizardPage):

	def __init__(self):
		super().__init__(
			parent=wx.GetTopLevelWindows()[0]
		)

	def GetPrev(self):
		return pageObj0

	def GetNext(self):
		return pageObj2


class page2(wx.adv.WizardPage):

	def __init__(self):
		super().__init__(
			parent=wx.GetTopLevelWindows()[0]
		)

	def GetPrev(self):
		return pageObj1

	def GetNext(self):
		return None


# app startup code
app = wx.App()
wiz = wizard()
app.SetAppName('BEE Manipulator Installer')
app.SetTopWindow(wiz)
# all page objects
pageObj0 = page0()
pageObj1 = page1()
pageObj2 = page2()
# start installer
wiz.Run()
app.MainLoop()
