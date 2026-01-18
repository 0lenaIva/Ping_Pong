from customtkinter import *

class StartWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('350x400')
        self.host = None
        self.port = None

        CTkLabel(self, text='Підключення до сервера', font=('Times New Roman', 25)).pack(pady=35,padx = 15, anchor='w')
        self.entry_host=CTkEntry(self, font=('Times New Roman', 18), placeholder_text='HOST', height=35)
        self.entry_port=CTkEntry(self, font=('Times New Roman', 18), placeholder_text='PORT', height=35)
        self.submit = CTkButton(self,font=('Times New Roman', 18), text='підключитись', height=35,
                                command=self.open_game)
        
        self.entry_host.pack(padx=15, pady=(15,30), fill='x')
        self.entry_port.pack(padx=15, fill='x')
        self.submit.pack(padx=15, fill='x',pady=(100,0) )

    def open_game(self):
        self.host = self.entry_host.get()
        self.port = self.entry_port.get()
        try:
            if self.host:
                self.port = int(self.port)
                self.destroy()
        except:
            self.entry_host.delete(0, END)
            self.entry_port.delete(0, END)



