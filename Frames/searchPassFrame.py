import tkinter as tk
from Database.PDatabase import siteData
from Backend.passwordGenerator import Pgenerator

class SearchPassFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from Frames.homeFrame import HomeFrame

        # Colors
        self.primaryColor = '#4479ff'
        self.backgroundColor = '#000000'
        self.surface1Color = '#121212'
        self.surface2Color = '#212121'
        self.successColor = '#03dac6'
        self.errorColor = '#cf6679'
        self.priTextColor = '#000000'
        self.secTextColor = '#ffffff'

        # Fonts
        self.entryFont = ("Rockwell", 12)
        self.labelFont = ("Rockwell", 12, "bold")

        # Objects
        self.Gobj = Pgenerator()
        self.Pobj = siteData()

        # Main Frame
        self.searchPassFrame = tk.LabelFrame(self, text="Search Password", bd=5, bg=self.backgroundColor, fg=self.secTextColor)
        self.searchPassFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title
        self.titleLabel = tk.Label(self.searchPassFrame, text="Search Password", bg=self.backgroundColor, fg=self.primaryColor, font=("Rockwell", 18, "bold"))
        self.titleLabel.place(relx=0.25, rely=0.08, relwidth=0.5, relheight=0.1)

        # Search Input
        self.searchLabel = tk.Label(self.searchPassFrame, text="Enter the website name", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.searchLabel.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.05)

        self.siteText = tk.Entry(self.searchPassFrame, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor
                                 , insertbackground=self.secTextColor, relief='flat')
        self.siteText.place(relx=0.1, rely=0.29, relwidth=0.65, relheight=0.05)

        self.searchBtn = tk.Button(self.searchPassFrame, text="Search", bg=self.successColor, fg=self.priTextColor, font=self.labelFont, command=self.searchPass)
        self.searchBtn.place(relx=0.78, rely=0.285, relwidth=0.12, relheight=0.06)

        # Display Info
        self.siteLabel = tk.Label(self.searchPassFrame, text="Website Name", bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont)
        self.siteLabel.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.05)

        self.usernameLabel = tk.Label(self.searchPassFrame, text="Username", bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont)
        self.usernameLabel.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.05)

        self.passLabel = tk.Label(self.searchPassFrame, text="Password", bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont)
        self.passLabel.place(relx=0.1, rely=0.56, relwidth=0.8, relheight=0.05)

        # Action Buttons
        self.copyBtn = tk.Button(self.searchPassFrame, text="Copy Password", bg=self.surface2Color, fg=self.successColor, font=self.labelFont, command=self.copy)
        self.copyBtn.place(relx=0.1, rely=0.66, relwidth=0.35, relheight=0.06)

        self.deleteBtn = tk.Button(self.searchPassFrame, text="Delete Site", bg=self.errorColor, fg=self.priTextColor, font=self.labelFont, command=self.deletePass)
        self.deleteBtn.place(relx=0.55, rely=0.66, relwidth=0.35, relheight=0.06)

        self.homeBtn = tk.Button(self.searchPassFrame, text="Home", bg=self.primaryColor, fg=self.secTextColor, font=self.labelFont, command=lambda: self.goHome(controller, HomeFrame))
        self.homeBtn.place(relx=0.32, rely=0.76, relwidth=0.35, relheight=0.07)

    def searchPass(self):
        returnedData = self.Pobj.searchPass(self.siteText.get())
        if returnedData != "":
            self.siteLabel.config(text=f"Website: {returnedData[0][0]}")
            self.usernameLabel.config(text=f"Username: {returnedData[0][1]}")
            self.passLabel.config(text=f"Password: {returnedData[1]}")
        else:
            invalidLabel = tk.Label(self.searchPassFrame, text="Invalid Site Name", bg=self.errorColor, fg=self.secTextColor, font=self.labelFont)
            invalidLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
            invalidLabel.after(2000, invalidLabel.destroy)

    def copy(self):
        password_text = self.passLabel['text'].split(": ")
        if len(password_text) == 2:
            self.Gobj.c2c(password_text[1])
        self.clearFields()

    def deletePass(self):
        site_text = self.siteLabel['text'].split(": ")
        if len(site_text) == 2:
            self.Pobj.deleteDataTable(site_text[1])
            deleteLabel = tk.Label(self.searchPassFrame, text="Site details deleted", bg=self.successColor, fg=self.priTextColor, font=self.labelFont)
            deleteLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
            deleteLabel.after(2000, deleteLabel.destroy)
        self.clearFields()

    def clearFields(self):
        self.siteText.delete(0, "end")
        self.siteLabel.config(text="Website Name")
        self.usernameLabel.config(text="Username")
        self.passLabel.config(text="Password")

    def goHome(self, controller, HomeFrame):
        self.clearFields()
        controller.show_frame(HomeFrame)
