import tkinter as tk
from Database.PDatabase import siteData
from Backend.passwordGenerator import Pgenerator

class AddPassFrame(tk.Frame):
    def __init__(self, parent, controller):
        from Frames.homeFrame import HomeFrame
        tk.Frame.__init__(self, parent)

        # Fonts
        self.titleFont = ("Rockwell", 16, "bold")
        self.labelFont = ("Rockwell", 13)
        self.buttonFont = ("Rockwell", 13, "bold")
        self.entryFont = ("Rockwell", 13)

        # Colors
        self.primaryColor = '#4479ff'
        self.backgroundColor = '#000000'
        self.surface1Color = '#121212'
        self.surface2Color = '#212121'
        self.successColor = '#03dac6'
        self.errorColor = '#cf6679'
        self.priTextColor = '#000000'
        self.secTextColor = '#ffffff'

        self.configure(bg=self.backgroundColor)

        self.sd = siteData()

        # Outer Frame
        self.addPassFrame = tk.LabelFrame(self, text="Add New Password", bd=5,
                                          bg=self.backgroundColor, fg=self.secTextColor, font=self.titleFont)
        self.addPassFrame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.94)

        # Title
        self.titleLabel = tk.Label(self.addPassFrame, text="➕ Add New Password", bg=self.backgroundColor,
                                   fg=self.primaryColor, font=self.titleFont)
        self.titleLabel.place(relx=0.22, rely=0.05, relwidth=0.56, relheight=0.1)

        # Site Name
        self.siteLabel = tk.Label(self.addPassFrame, text='Website Name', bg=self.backgroundColor,
                                  fg=self.secTextColor, font=self.labelFont)
        self.siteLabel.place(relx=0.15, rely=0.18, relwidth=0.7, relheight=0.06)
        self.siteText = tk.Entry(self.addPassFrame, font=self.entryFont, bg=self.surface1Color,
                                 fg=self.secTextColor, insertbackground=self.secTextColor, relief='flat')
        self.siteText.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.06)

        # Username / Email
        self.usernameLabel = tk.Label(self.addPassFrame, text='Username or Email', bg=self.backgroundColor,
                                      fg=self.secTextColor, font=self.labelFont)
        self.usernameLabel.place(relx=0.15, rely=0.34, relwidth=0.7, relheight=0.06)
        self.usernameText = tk.Entry(self.addPassFrame, font=self.entryFont, bg=self.surface1Color,
                                     fg=self.secTextColor, insertbackground=self.secTextColor, relief='flat')
        self.usernameText.place(relx=0.15, rely=0.41, relwidth=0.7, relheight=0.06)

        # Password
        self.passLabel = tk.Label(self.addPassFrame, text='Password', bg=self.backgroundColor,
                                  fg=self.secTextColor, font=self.labelFont)
        self.passLabel.place(relx=0.15, rely=0.50, relwidth=0.7, relheight=0.06)
        self.passText = tk.Entry(self.addPassFrame, font=self.entryFont, bg=self.surface1Color,
                                 fg=self.secTextColor, insertbackground=self.secTextColor, relief='flat')
        self.passText.place(relx=0.15, rely=0.57, relwidth=0.7, relheight=0.06)

        # Buttons
        self.pwGenBtn = tk.Button(self.addPassFrame, text="⚡ Generate Password", font=self.buttonFont,
                                  command=self.generatePass, bg=self.surface2Color, fg=self.secTextColor,
                                  activebackground="#333333", activeforeground=self.successColor, bd=0)
        self.pwGenBtn.place(relx=0.15, rely=0.68, relwidth=0.32, relheight=0.08)

        self.saveBtn = tk.Button(self.addPassFrame, text="💾 Save Password", font=self.buttonFont,
                                 command=self.savePass, bg=self.surface2Color, fg=self.successColor,
                                 activebackground="#333333", activeforeground=self.successColor, bd=0)
        self.saveBtn.place(relx=0.53, rely=0.68, relwidth=0.32, relheight=0.08)

        self.homeBtn = tk.Button(self.addPassFrame, text="🏠 Home", font=self.buttonFont,
                                 command=lambda: self.goHome(controller), bg=self.primaryColor, fg=self.secTextColor,
                                 activebackground="#5b93ff", activeforeground=self.priTextColor, bd=0)
        self.homeBtn.place(relx=0.32, rely=0.80, relwidth=0.36, relheight=0.08)

    def generatePass(self):
        gp = Pgenerator()
        p = gp.generatePass()
        self.passText.delete(0, 'end')
        self.passText.insert(0, p)

    def savePass(self):
        self.sd.insertDataTable(self.siteText.get(), self.usernameText.get(), self.passText.get())
        self.siteText.delete(0, 'end')
        self.usernameText.delete(0, 'end')
        self.passText.delete(0, 'end')

        # Smooth Success Message
        saveLabel = tk.Label(self.addPassFrame, text="✅ Password saved successfully!", bg=self.successColor,
                             fg=self.priTextColor, font=("Rockwell", 14, "bold"))
        saveLabel.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.05)
        saveLabel.after(2000, saveLabel.destroy)

        

    def goHome(self, controller):
        from Frames.homeFrame import HomeFrame
        self.siteText.delete(0, 'end')
        self.usernameText.delete(0, 'end')
        self.passText.delete(0, 'end')
        controller.show_frame(HomeFrame)
