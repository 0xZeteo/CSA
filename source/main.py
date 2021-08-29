
""" HERE IS THE MAIN PART OF THE APP HANDLING THE SIZE OF THE WINDOW, THE FIRST FRAME TO DISPLAY AND THE MAIN LOOP """

import layout.layout_login as login

import tkinter as tk
from tkinter import messagebox


class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)

        self._frame = None
        self.iconbitmap(default='resources/cyber.ico') # icon of the window

        # set window size and starting position
        self.geometry("1280x768+{}+{}".format(100,20)) 

        self.protocol("WM_DELETE_WINDOW", lambda: Main_App.on_closing(self)) # add confirmation popup for exiting with X

        self.minsize(1280, 768)                # window minimum size
        self.switch_frame(login.Login_Page)    # display login page when first launched

    # destroys current frame and replaces it with a new one
    def switch_frame(self, frame_class): 
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    # displays a confirmation popup and destroys the frame if the user clicks ok
    def on_closing(frame):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit ? Unsaved changes will be lost"):
            frame.destroy()
    #endregion


if __name__ == "__main__":
    app = Main_App()
    app.mainloop()