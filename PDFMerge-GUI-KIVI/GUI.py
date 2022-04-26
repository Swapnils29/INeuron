from tkinter import *
import tkinter
import logging as logg
import os
import PDFMerge


class GUI:
    def __init__(self):
        logg.info('In GUI')
        self.window = Tk()
        self.contents=''
        self.pathdetails=[]
   
    def click(self):
        try:
            self.pathdetails=[]
            enteredtext = self.textbox.get()
            self.contents = os.walk(enteredtext)
            allfiles,allfolders = [],[]
            for paths,folders,files in self.contents:
                allfiles = allfiles + files
                allfolders = allfolders + folders
                
                for file in files:
                    if file.endswith('.pdf'):
                        self.pathdetails.append(paths+'/'+file)
            self.contents = allfiles + allfolders
        except Exception as er:
            logg.exception('Error occured while creating GUI {}'.format())
            raise er


    def show_content(self):
        s = ''
        self.output_window.delete('1.0',tkinter.END)
        for ind,item in enumerate(self.contents):
            s = s + str(ind+1)+ ' - ' + item +'\n'
        self.output_window.insert(tkinter.END,s)


    
    def mergeGUI(self,contents):
        try:
            if len(contents)>0:
                self.merge_window = Text(self.window,width=40,height=1)
                self.merge_window.grid(row=7,column=0,sticky=W)
                self.merge_window.delete('1.0',tkinter.END)
                self.merge_window.insert(tkinter.END,'')
                PDFMerge.merge(contents)
            else:
                self.merge_window = Text(self.window,width=40,height=1)
                self.merge_window.grid(row=7,column=0,sticky=W)
                self.merge_window.insert(tkinter.END,'Multiple PDF files not present')
                self.merge_window.config(state='disabled')
        except Exception as er:
            logg.exception('Exception occured while merging PDF files {}'.format(er))
            raise er


    def create_GUI(self):
        try:
            self.window.title('PDF Merger')
            self.window.configure(background='black')
            picture = PhotoImage(file='1.gif')
            Label(self.window,image=picture,bg='black').grid(row=0,column=0,sticky=W)
            Label(self.window,text='\nEnter the location to search for PDF',bg='black',fg='white',font='none 12 bold').grid(row=2,column=0,sticky=W)
            self.textbox = Entry(self.window,width=28,bg='white')   
            self.textbox.grid(row=3,column=0,sticky=W)
            Button(self.window,text='SUBMIT',width=9,command=lambda:[self.click(),self.show_content()]).grid(row=3,column=1,sticky=W)
            Label(self.window,text='\nContents',bg='black',fg='white',font='none 12 bold').grid(row=4,column=0,sticky=W)
            self.output_window = Text(self.window,width=40,height=6)
            self.output_window.grid(row=5,column=0,sticky=W)
            Button(self.window,text='Merge PDF',width=9,command=lambda:[self.mergeGUI(self.pathdetails)]).grid(row=7,column=1,sticky=W)
            self.window.mainloop()
        except Exception as er:
            logg.exception('Error occured while creating GUI {}'.format())
            raise er



