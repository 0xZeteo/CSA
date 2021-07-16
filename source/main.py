
""" HERE IS THE MAIN PART OF THE APP HANDLING THE SIZE OF THE WINDOW, THE FIRST FRAME TO DISPLAY AND THE MAIN LOOP """

import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_home as home

class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("900x700")              # window size
        self.minsize(900, 700)                # window minimum size
        self.maxsize(900, 700)                # window maximum size
        self.switch_frame(home.Home_Page)  # frame to display on app launch 

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    #endregion

if __name__ == "__main__":
    app = Main_App()
    app.mainloop()