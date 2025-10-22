import tkinter as tk
from PIL import Image, ImageTk
from Frames.forgotPassFrame import ForgotPassFrame
from Database.MPdatabase import PMPDatabase

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

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
        self.labelFont = ("Rockwell", 12, "bold")
        self.entryFont = ("Rockwell", 16)

        self.controller = controller

        # Main Frame
        self.loginFrame = tk.Frame(self, bg=self.backgroundColor)
        self.loginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Logo
        try:
            logo_image = Image.open("img/pwm2.png")
            logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logoLabel = tk.Label(self.loginFrame, image=self.logo_photo, bg=self.backgroundColor)
            self.logoLabel.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.2)
        except Exception as e:
            print("Logo Image Error:", e)

        # Title
        self.titleLabel = tk.Label(self.loginFrame, text='Password Manager', bg=self.backgroundColor, fg=self.primaryColor, font=("Rockwell", 22, "bold"))
        self.titleLabel.place(relx=0.25, rely=0.28, relheight=0.08, relwidth=0.5)

        # Password Label
        self.epassLabel = tk.Label(self.loginFrame, text='Enter Master Password', bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.epassLabel.place(relx=0.3, rely=0.4, relheight=0.07, relwidth=0.4)

        # Password Entry
        self.mpassentry = tk.Entry(self.loginFrame, show="*", font=self.entryFont, bg=self.surface1Color, fg=self.primaryColor, insertbackground=self.primaryColor, relief='flat')
        self.mpassentry.place(relx=0.25, rely=0.48, relwidth=0.5, relheight=0.07)
        self.mpassentry.bind("<Return>", self.shortcuts)
        self.mpassentry.delete(0, 'end')

        # Enter Button
        self.mpassenter = tk.Button(self.loginFrame, text="Login", bg=self.primaryColor, fg=self.secTextColor, command=self.checkPass, font=self.labelFont, relief='flat', activebackground=self.surface2Color)
        self.mpassenter.place(relx=0.35, rely=0.58, relwidth=0.3, relheight=0.07)

        # Forgot Password
        self.forgotPass = tk.Button(self.loginFrame, text="Forgot Password?", bg=self.surface2Color, fg=self.secTextColor, command=lambda: controller.show_frame(ForgotPassFrame), font=("Rockwell", 10), relief='flat', activebackground=self.surface1Color)
        self.forgotPass.place(relx=0.4, rely=0.68, relwidth=0.2, relheight=0.05)

    # Shortcut for Enter key 
    def shortcuts(self, event):
        self.checkPass()

    # Check entered password with database
    def checkPass(self):
        mp = self.mpassentry.get()
        pdb = PMPDatabase()
        if pdb.loginCheck(mp):
            confirmLabel = tk.Label(self.loginFrame, text="Login Successful!", font=self.labelFont, bg=self.successColor, fg=self.priTextColor)
            confirmLabel.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.05)
            confirmLabel.after(2000, confirmLabel.destroy)
            self.mpassentry.delete(0, 'end')
            from Frames.homeFrame import HomeFrame
            self.controller.show_frame(HomeFrame)
        else:
            errorLabel = tk.Label(self.loginFrame, text="Wrong Password. Try again.", font=self.labelFont, bg=self.errorColor, fg=self.priTextColor)
            errorLabel.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.05)
            errorLabel.after(2000, errorLabel.destroy)
