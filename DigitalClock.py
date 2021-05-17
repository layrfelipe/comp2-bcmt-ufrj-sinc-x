from tkinter import *
from threading import Thread
from time import *

class digitalClock:

    # 
    # Constructor.
    #
    # @param clock a label to display the time.
    # @param secs number of seconds for time regressive counting.
    # @param time string for initializing the time. Just leave the default.
    #
    # 
    def __init__ ( self, clock, secs = 0, time='' ):
        self.clock = clock
        self.secs = secs
        self.time = time
        self.running = True # variavel de controle do botao pause

    # 
    # Updates the clock display.
    #
    def tick(self):
        self.clock.config(text=strftime('%H:%M:%S')) # atualiza label do relogio digital (em cima, fundo verde)
        self.clock.after(1000, self.tick)

      # 
      # Starts a count down from the number of seconds set to zero.
      #
    def tickDown(self):
        def setThirty(): # callback function which sets timer to 30 seconds
            self.aEntry.delete(0, "end")
            self.aEntry.insert(0, "30")

        def handle30sec(): # callback function - +30 seconds in timer
            try:
                time = self.aEntry.get()
                # string shown in timer when it reaches 0
                if time == "Time is over":
                    self.aEntry.after(200, setThirty)
                else:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, str(int(time)+30))
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")

        def handleStart(): # recursive callback function - starts count down in timer
            try:
                current = int(self.aEntry.get())
                if current > 0 and self.running == True:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, str(current - 1)) # ticks down
                    self.aEntry.after(1000, handleStart) # recursion
                elif current == 0 and self.running == True:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, "Time is over")
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")
        
        def handlePause(): # callback function - pauses timer
            try:
                if self.running == True:
                    self.running = False
                    current = int(self.aEntry.get())
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, current)
                else:
                    self.running = True
                    handleStart()
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")

        e1Var = StringVar(self.clock.master) # TCL variable interpreted within Tkinter
        e1Var.set(str(self.secs))

        #
        # Creating visual elements with Tkinter widgets like Entries, Buttons and Frames
        self.aEntry = Entry(self.clock.master, font=('times 28', 20, 'bold'), bg="red", textvar=e1Var)
        self.aEntry.pack(fill="both", side="top", expand=1)

        self.bottomFrame = Frame(self.clock.master, bg="white")

        self.startButton = Button(self.bottomFrame, text="Start", command=handleStart)
        self.startButton.pack(fill="both", side="left", expand=1)

        self.plus30Button = Button(self.bottomFrame, text="+30s", command=handle30sec)
        self.plus30Button.pack(fill="both", side="left", expand=1)

        self.pauseButton = Button(self.bottomFrame, text="Pause", command=handlePause)
        self.pauseButton.pack(fill="both", side="left", expand=1)

        self.bottomFrame.pack(fill="both", side="top", expand=1)
        


## Creates a new thread.
class makeThread (Thread):
    ## Constructor.
    #
    #  @param func function to be executed in this thread.
    #
    def __init__ (self,func):
        Thread.__init__(self)
        self.__action = func
        self.debug = False

    ## Obejct destructor.
    #  In Python, destructors are needed much less, because Python has
    #  a garbage collector that handles memory management.
    #  However, there are other resources to be dealt with, such as:        
    #  sockets and database connections to be closed, 
    #  files, buffers and caches to be flushed.
    #
    def __del__ (self):
        if ( self.debug ): print ("Thread end")

    ## Method representing the thread's activity.
    #  This method may be overriden in a subclass.
    #
    def run (self):
        if ( self.debug ): print ("Thread begin")
        self.__action()