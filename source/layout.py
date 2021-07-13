import tkinter as tk
import DATA

class Main_App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Home_Page)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Home_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        irp_button = tk.Button(self, text="Go", command=lambda: master.switch_frame(IRP_Page))
        csm_button = tk.Button(self, text="Go", command=lambda: master.switch_frame(CSM_Page))

        # add 2 text fields

        irp_button.pack()
        csm_button.pack()


class IRP_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        cat1_button = tk.Button(self, text="Technologies and Connection Types", command=lambda: master.switch_frame(IRP_Cat1_Page))
        #cat2_button = tk.Button(self, text="Category 2", command=lambda: master.switch_frame(IRP_Cat2_Page))
        #cat3_button = tk.Button(self, text="Category 3", command=lambda: master.switch_frame(IRP_Cat3_Page))
        #cat4_button = tk.Button(self, text="Category 4", command=lambda: master.switch_frame(IRP_Cat4_Page))
        #cat5_button = tk.Button(self, text="Category 5", command=lambda: master.switch_frame(IRP_Cat5_Page))

        cat1_button.pack()


class IRP_Cat1_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        i = 0
        for key, value in DATA.IRP_Category1.items():
            tempQ = tk.Label(self, text=key).grid(row=i, column=0)
            for j in range(5):
                tempA = tk.Radiobutton(self, text=value[j]).grid(row=i, column=j+1)
            i += 1


class CSM_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        start_button = tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(Home_Page))

        start_button.pack()


if __name__ == "__main__":
    app = Main_App()
    app.mainloop()