
""" HERE IS THE MAIN PART OF THE APP HANDLING THE SIZE OF THE WINDOW, THE FIRST FRAME TO DISPLAY AND THE MAIN LOOP """

import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_home as home
import layout.layout_login as login
from tkinter import messagebox


class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)

        self._frame = None
        self.iconbitmap(default='resources/cyber.ico') # icon 

        # set window size and starting position relative to screen size
        # self.geometry("1280x768+{}+{}".format(int(self.winfo_screenwidth()/5), int(self.winfo_screenheight()/10-20))) 
        self.geometry("1280x768+{}+{}".format(100,20)) 

        self.protocol("WM_DELETE_WINDOW", lambda: Main_App.on_closing(self)) 

        self.minsize(1280, 768)                # window minimum size
        self.switch_frame(login.Login_Page)    # frame to display on app launch 

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    def on_closing(frame):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit ? Unsaved changes will be lost"):
            frame.destroy()
    #endregion

if __name__ == "__main__":
    app = Main_App()
    app.mainloop()