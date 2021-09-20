from callbacks import *
import tkinter as tk

class Interface :
    def __init__(self):
        self.createMainWIndow()
        self.createFrames()
        self.genTest()
        self.genPlay()
        self.genScroll()
        self.genPause()
        self.genExit()
        self.genStart()
        #self.genStop()
        self.genValve()
        self.genLumbar()
        self.genBolstersB()
        self.genBolstersC()
        self.genPump()


    def createMainWIndow(self):
        self.window = tk.Tk()
        self.window.geometry("920x680")

    def createFrames(self):
        self.testFrame      = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "testFrame" , bg ="#e9eff5")
        self.playFrame      = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "palyFrame" , bg= "#e9eff5")
        self.scrollFrame    = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "scrollFrame" , bg= "#e9eff5")
        self.startFrame     = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "startFrame" , bg ="#e9eff5")
        self.stopFrame      = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "stopFrame" , bg ="#e9eff5")
        self.pauseFrame     = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "pauseFrame" , bg ="#e9eff5")
        self.exitFrame      = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "exitFrame" , bg ="#e9eff5")
        self.pumpFrame      = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "pumpFrame" , bg ="#e9eff5")
        self.valveFrame     = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "valveFrame" , bg ="#e9eff5")
        self.lumbarFrame    = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "lumbarFrame" , bg ="#e9eff5")
        self.bolstersCFrame = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "bolstersCFrame" , bg ="#e9eff5")
        self.bolstersBFrame = tk.Frame(master = self.window,relief=  tk.GROOVE,borderwidth=5,name = "bolstersBFrame" , bg ="#e9eff5")

    def genPlay(self):
        self.playLabel = tk.Label(master =self.playFrame, text="Play", width = 14 )
        self.playEntry = tk.Entry(master = self.playFrame, bd = 5 ,)
        self.playEntry.insert(0,"b6e997e0-3885-11eb-ad2d-a136ae3f9469-Sieste en Provence")
        self.playEntry_time = tk.Entry(master = self.playFrame, bd = 5 )
        self.playEntry_time.insert(0,"00:00:00:000")
        self.playButton = tk.Button(master = self.playFrame, text="Send",command=lambda:Callbacks.play(self.playEntry.get(), self.playEntry_time.get()))
        self.playLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.playEntry.grid(row =0  ,column = 1 ,padx=(50, 10))
        self.playEntry_time.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.playButton.grid(row =0 ,column = 3 ,padx=(50, 10))

    def genScroll(self):
        self.scrollLabel = tk.Label(master =self.scrollFrame, text="Scroll", width = 14 )
        self.scrollEntry = tk.Entry(master = self.scrollFrame, bd = 5 ,)
        self.scrollEntry.insert(0,"958e4e30-33c4-11eb-99f5-1b08d71845f1-Sieste en Provence")
        self.scrollEntry_time = tk.Entry(master = self.scrollFrame, bd = 5)
        self.scrollEntry_time.insert(0,"00:00:00:000")
        self.scrollButton = tk.Button(master = self.scrollFrame, text="Send",command=lambda:Callbacks.scroll(self.scrollEntry.get(),self.scrollEntry_time.get()))
        self.scrollLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.scrollEntry.grid(row =0  ,column = 1 ,padx=(50, 10))
        self.scrollEntry_time.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.scrollButton.grid(row =0 ,column = 3 ,padx=(50, 10))

    def genStop(self):
        self.stopLabel = tk.Label(master =self.stopFrame, text="Stop", width = 14 )
        self.stopButton = tk.Button(master = self.stopFrame, text="Send",command=lambda:Callbacks.stop())
        self.stopLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.stopButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def genExit(self):
        self.exitLabel = tk.Label(master =self.exitFrame, text="Exit", width = 14 )
        self.exitButton = tk.Button(master = self.exitFrame, text="Send",command=lambda:Callbacks.exit())
        self.exitLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.exitButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def genPause(self):
        self.pauseLabel = tk.Label(master =self.pauseFrame, text="Pause", width = 14 )
        self.pauseButton = tk.Button(master = self.pauseFrame, text="Send",command=lambda:Callbacks.pause())
        self.pauseLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.pauseButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def genStart(self):
        self.startLabel = tk.Label(master =self.startFrame, text="Start", width = 14 )
        self.startButton = tk.Button(master = self.startFrame, text="Send",command=lambda:Callbacks.start())
        self.startLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.startButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def genValve(self):
        self.valveLabel = tk.Label(master =self.valveFrame, text="Valve", width = 14 )
        self.valveEntryNumber = tk.Entry(master = self.valveFrame, bd = 5 )
        self.valveEntryNumber.insert(0,"7")
        self.valveEntryState = tk.Entry(master = self.valveFrame, bd = 5 )
        self.valveEntryState.insert(0,"1")
        self.valveButton = tk.Button(master = self.valveFrame, text="Send",command=lambda:Callbacks.valve(self.valveEntryNumber.get(),self.valveEntryState.get()))
        self.valveLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.valveEntryNumber.grid(row =0  ,column = 1 ,padx=(50, 10))
        self.valveEntryState.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.valveButton.grid(row =0 ,column = 3 ,padx=(50, 10))


    def genLumbar(self):
        self.lumbarLabel = tk.Label(master =self.lumbarFrame, text="Lumbar", width = 14 )
        self.lumbarEntryDirection = tk.Entry(master = self.lumbarFrame, bd = 5 )
        self.lumbarEntryDirection.insert(0,"up")
        self.lumbarEntryState = tk.Entry(master = self.lumbarFrame, bd = 5 )
        self.lumbarEntryState.insert(0,"1")
        self.lumbarButton = tk.Button(master = self.lumbarFrame, text="Send",command=lambda:Callbacks.lumbar( self.lumbarEntryDirection.get(),self.lumbarEntryState.get()))
        self.lumbarLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.lumbarEntryDirection.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.lumbarEntryState.grid(row =0  ,column = 3 ,padx=(50, 10))
        self.lumbarButton.grid(row =0 ,column = 4 ,padx=(50, 10))


    def genBolstersC(self):
        self.bolstersCLabel = tk.Label(master =self.bolstersCFrame, text="bolstersC", width = 14 )
        self.bolstersCEntryDirection = tk.Entry(master = self.bolstersCFrame, bd = 5 )
        self.bolstersCEntryDirection.insert(0,"forward")
        self.bolstersCEntryState = tk.Entry(master = self.bolstersCFrame, bd = 5 )
        self.bolstersCEntryState.insert(0,"1")
        self.bolstersCButton = tk.Button(master = self.bolstersCFrame, text="Send",command=lambda:Callbacks.bolstersC(self.bolstersCEntryDirection.get(),self.bolstersCEntryState.get()))
        self.bolstersCLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.bolstersCEntryDirection.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.bolstersCEntryState.grid(row =0  ,column = 3 ,padx=(50, 10))
        self.bolstersCButton.grid(row =0 ,column = 4 ,padx=(50, 10))


    def genBolstersB(self):
        self.bolstersBLabel = tk.Label(master =self.bolstersBFrame, text="bolstersB", width = 14 )
        self.bolstersBEntryDirection = tk.Entry(master = self.bolstersBFrame, bd = 5 )
        self.bolstersBEntryDirection.insert(0,"rearward")
        self.bolstersBEntryState = tk.Entry(master = self.bolstersBFrame, bd = 5 )
        self.bolstersBEntryState.insert(0,"0")
        self.bolstersBButton = tk.Button(master = self.bolstersBFrame, text="Send",command=lambda:Callbacks.bolstersB(self.bolstersBEntryDirection.get(),self.bolstersBEntryState.get()))
        self.bolstersBLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.bolstersBEntryDirection.grid(row =0  ,column = 2 ,padx=(50, 10))
        self.bolstersBEntryState.grid(row =0  ,column = 3 ,padx=(50, 10))
        self.bolstersBButton.grid(row =0 ,column = 4 ,padx=(50, 10))

    def genPump(self):
        self.pumpLabel = tk.Label(master =self.pumpFrame, text="Pump", width = 14 )
        self.pumpEntry = tk.Entry(master = self.pumpFrame, bd = 5 )
        self.pumpEntry.insert(0,"80")
        self.pumpButton = tk.Button(master = self.pumpFrame, text="Send",command=lambda:Callbacks.pump(self.pumpEntry.get()))
        self.pumpLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.pumpEntry.grid(row =0  ,column = 1 ,padx=(50, 10))
        self.pumpButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def genTest(self):
        self.testLabel = tk.Label(master =self.testFrame, text="Test", width = 14 )
        self.testEntry = tk.Entry(master = self.testFrame, bd = 5 )
        self.testEntry.insert(0,"")
        self.testButton = tk.Button(master = self.testFrame, text="Send",command=lambda:Callbacks.test(self.testEntry.get()))
        self.testLabel.grid(row =0  ,column = 0 ,padx=(50, 10), pady =(20,20))
        self.testEntry.grid(row =0  ,column = 1 ,padx=(50, 10))
        self.testButton.grid(row =0 ,column = 2 ,padx=(50, 10))

    def Play(self):
        self.testFrame.pack(fill=tk.BOTH, expand=True)
        self.startFrame.pack(fill=tk.BOTH, expand=True)
        self.stopFrame.pack(fill=tk.BOTH, expand=True)
        self.playFrame.pack(fill=tk.BOTH, expand=True)
        self.scrollFrame.pack(fill=tk.BOTH, expand=True)
        self.exitFrame.pack(fill=tk.BOTH, expand=True)
        self.pauseFrame.pack(fill=tk.BOTH, expand=True)
        self.pumpFrame.pack(fill=tk.BOTH, expand=True)
        self.valveFrame.pack(fill=tk.BOTH, expand=True)
        self.lumbarFrame.pack(fill=tk.BOTH, expand=True)
        self.bolstersBFrame.pack(fill=tk.BOTH, expand=True)
        self.bolstersCFrame.pack(fill=tk.BOTH, expand=True)
        #self.pneumaticsOnOff.pack(fill=tk.BOTH, expand=True)
        self.window.mainloop()
        

#interface  =Interface()
#interface.Play()





