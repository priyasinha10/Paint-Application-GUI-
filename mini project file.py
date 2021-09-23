#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter 
from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
class Paint():
    def __init__(self,root):
        self.root=root
        self.root.title("Paint app")
        self.root.configure(background="white")
        
        self.pen_color="black"
        self.eraser_color="white"
        

        

        self.color_frame=LabelFrame(self.root,text="Color",font=('elephant',17),bd=5,relief=RAISED,fg='black',bg="white")
        self.color_frame.place(x=0,y=0,width=80,height=318)
        colors=["#ff0000","#FFA500","#008000","#0000FF","#800080","#9400D3","#835C3B","#AFEEEE","#808080","#FFFFFF","#FFC0CB",
                "#800000","#8B008B","#00FFFF","#800000","#808000","#A0522D","#000000","#9ACD32","#FFFF00"]

        i=j=0
        for color in colors:
            Button(self.color_frame,bg=color,bd=3,relief=RIDGE,width=3,
                   command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==10:
                i=0
                j=1
        
         
        self.eraser_button=Button(self.root,text="ERASER",bd=5,bg="white",command=self.eraser,width=9,relief=RAISED)
        self.eraser_button.place(x=0,y=330)

       
        self.clear_button=Button(self.root, text = 'CLEAR',bd=5,bg="white",
                                command=self.new_canvas,width=9,relief=RAISED)
        self.clear_button.place(x=0,y=360)

        
        self.save_button=Button(self.root, text = 'SAVE',bd=5,bg="white",command=self.save_paint,width=9,relief=RAISED)
        self.save_button.place(x=0,y=390)

     
        self.canvas_button=Button(self.root, text = 'CANVAS',bd=5,bg="white",command=self.canvas,width=9,relief=RAISED)
        self.canvas_button.place(x=0,y=420)


        self.pen_size_scale_frame=LabelFrame(self.root,text='Scale',font=('copper black',17,'bold'),bd=5,
                                             bg='white',relief=RIDGE)
        self.pen_size_scale_frame.place(x=0,y=470,width=80,height=200)

        self.pen_size=Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to =0,length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=15)
        
        self.canvas=Canvas(self.root,bg='white',bd=10,relief=GROOVE,width=1250,height=670)
        self.canvas.place(x=90,y=0)
        
        
        
        #bind canvas with mouse
        self.canvas.bind("<B1-Motion>",self.paint) #event,function
        
    def paint(self,event):
        x1,y1=(event.x),(event.y)
        x2,y2=(event.x),(event.y)
        
        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())
        
    def select_color(self,col):
        self.pen_color=col
    
    def eraser(self):
        self.pen_color=self.eraser_color
        
    def canvas(self):
        color=colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color=color[1]
        
        
    def new_canvas(self):
        self.canvas.delete(ALL)

        
    def save_paint(self):
        try:
            filename= filedialog.asksaveasfilename(defaultextension='.png')
            x=self.root.winfo_rootx()+self.canvas.winfo_x()
            y=self.root.winfo_rooty()+self.canvas.winfo_y()
            x1=x+self.canvas.winfo_width()
            y1=y+self.canvas.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo('paint says','image is saved' +str(filename))
        except:
            messagebox.showinfo('paint says','unable to save')
        
        
if __name__=="__main__":
    root=Tk()
    p=Paint(root)
    
root.mainloop()    


# In[ ]:





# In[ ]:




