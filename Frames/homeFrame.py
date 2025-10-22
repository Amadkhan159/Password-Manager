import tkinter as tk
from tkinter import scrolledtext
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame
from Database.PDatabase import siteData

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        from Frames.loginFrame import LoginFrame
        tk.Frame.__init__(self, parent)

        # Colors
        self.primaryColor = '#4479ff'
        self.backgroundColor = '#121212'
        self.surface1Color = '#1e1e1e'
        self.surface2Color = '#2a2a2a'
        self.successColor = '#03dac6'
        self.errorColor = '#cf6679'
        self.priTextColor = '#ffffff'
        self.secTextColor = '#b0b0b0'

        # Fonts
        self.titleFont = ("Rockwell", 22, "bold")
        self.labelFont = ("Rockwell", 14)
        self.buttonFont = ("Rockwell", 13, "bold")

        self.configure(bg=self.backgroundColor)

        # Home Title
        self.titleLabel = tk.Label(self, text="🏠 Home", bg=self.backgroundColor, fg=self.primaryColor, font=self.titleFont)
        self.titleLabel.place(relx=0.05, rely=0.02)

        # Logout and Refresh
        self.logoutBtn = tk.Button(self, text="⎋ Logout", font=self.buttonFont, bg=self.errorColor, fg=self.priTextColor,
                                   bd=0, activebackground="#ff4b5c", command=lambda: controller.show_frame(LoginFrame))
        self.logoutBtn.place(relx=0.83, rely=0.025, relwidth=0.12, relheight=0.06)

        self.refreshBtn = tk.Button(self, text="⟳ Refresh", font=self.buttonFont, bg=self.successColor, fg=self.priTextColor,
                                    bd=0, activebackground="#04f9d9", command=self.insertScrolledText)
        self.refreshBtn.place(relx=0.68, rely=0.025, relwidth=0.12, relheight=0.06)

        # Data Frame
        self.dataFrame = tk.Frame(self, bg=self.surface2Color, bd=5)
        self.dataFrame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.7)

        self.viewData = scrolledtext.ScrolledText(self.dataFrame, font=self.labelFont,
                                                  bg=self.surface1Color, fg=self.priTextColor,
                                                  insertbackground=self.priTextColor, wrap='word', bd=2, relief='flat')
        self.viewData.place(relwidth=1, relheight=1)

        # Bottom Buttons
        self.newPassBtn = tk.Button(self, text="➕ Add New Password", bg=self.primaryColor, fg=self.priTextColor,
                                    font=self.buttonFont, bd=0, activebackground="#5b93ff",
                                    command=lambda: controller.show_frame(AddPassFrame))
        self.newPassBtn.place(relx=0.18, rely=0.84, relwidth=0.28, relheight=0.09)

        self.searchPassBtn = tk.Button(self, text="🔎 Retrieve Password", bg=self.primaryColor, fg=self.priTextColor,
                                       font=self.buttonFont, bd=0, activebackground="#5b93ff",
                                       command=lambda: controller.show_frame(SearchPassFrame))
        self.searchPassBtn.place(relx=0.54, rely=0.84, relwidth=0.28, relheight=0.09)

        # Load data
        self.insertScrolledText()

    def insertScrolledText(self):
        self.viewData.config(state='normal')
        self.viewData.delete(1.0, 'end')

        VObj = siteData()
        allPass = VObj.viewData()

        heading = f"{'Site Name':<30}{'|':^5}{'Username':<30}\n"
        heading += "-" * 70 + "\n"
        self.viewData.insert('insert', heading, 'head')

        for d in allPass:
            info = f"{d[0]:<30}{'|':^5}{d[1]:<30}\n"
            info += "-" * 70 + "\n"
            self.viewData.insert('insert', info, 'data')

        self.viewData.tag_config('head', background=self.primaryColor, foreground=self.priTextColor,
                                 font=("Rockwell", 15, "bold"))
        self.viewData.tag_config('data', foreground=self.secTextColor, font=self.labelFont)

        self.viewData.config(state='disabled')
