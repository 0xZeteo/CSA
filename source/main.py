
""" HERE IS THE MAIN PART OF THE APP HANDLING THE SIZE OF THE WINDOW, THE FIRST FRAME TO DISPLAY AND THE MAIN LOOP """

import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_home as home
import layout.layout_login as login

class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        # set window size and starting position relative to screen size
        self.geometry("800x600+{}+{}".format(int(self.winfo_screenwidth()/5 + 50), int(self.winfo_screenheight()/10 + 20)))              
        self.minsize(400, 300)                # window minimum size
        self.switch_frame(login.Login_Page)   # frame to display on app launch 

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)
    #endregion

if __name__ == "__main__":
    app = Main_App()
    app.mainloop()