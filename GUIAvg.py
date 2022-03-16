import tkinter
import tkinter.messagebox
from turtle import right

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x200')
        self.main_window.title('Label Demo')

        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.test1_frame, 
                                    text="Enter the score for test 1:")
        self.label2 = tkinter.Label(self.test2_frame, 
                                    text="Enter the score for test 2:")
        self.label3 = tkinter.Label(self.test3_frame, 
                                    text="Enter the score for test 3:")    

        self.descr_label = tkinter.Label(self.output_frame,
                                            text="Average:") 
        self.test1 = tkinter.Entry(self.test1_frame,width=10) 
        self.test2 = tkinter.Entry(self.test2_frame,width=10)
        self.test3 = tkinter.Entry(self.test3_frame,width=10)

        self.avg_var = tkinter.StringVar()

        self.avg_label = tkinter.Label(self.output_frame,
                                            textvariable=self.avg_var)

        self.mybutton = tkinter.Button(self.main_window,
                                        text='Average',
                                        command= self.convert)

        self.quit_button = tkinter.Button(self.main_window,
                                            text='Quit',
                                            command=self.main_window.destroy)
        
        self.test1_frame.pack(side='top')
        self.test2_frame.pack(side='top')
        self.test3_frame.pack(side='top')
        self.output_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')
        self.descr_label.pack(side='top')
        self.avg_label.pack(side='right')
        self.quit_button.pack(side='right')
        self.mybutton.pack(side='left')
        self.test1.pack(side='right')
        self.test2.pack(side='right')
        self.test3.pack(side='right')
        

        tkinter.mainloop()

    def convert(self):

        test1 = float(self.test1.get())
        test2 = float(self.test2.get())
        test3 = float(self.test3.get())

        score = round(((test1 + test2 + test3)/3),2)

        self.avg_var.set(score)    

my_gui = MyGUI()                  
        

