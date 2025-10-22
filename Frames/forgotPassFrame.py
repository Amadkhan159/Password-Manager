import tkinter as tk
from Frames.resetPassFrame import ResetPassFrame  # No issue here
from Database.MPdatabase import PMPDatabase
from Backend.OTPGenerator import Otp
from Backend.sendMail import SendMail

class ForgotPassFrame(tk.Frame):
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
        self.entryFont = ("Rockwell", 12)

        self.controller = controller
        self.generatedOTP = None  # No OTP at start

        self.configure(bg=self.backgroundColor)

        # Title
        self.titleLabel = tk.Label(self, text="Forgot Password?", bg=self.backgroundColor, fg=self.primaryColor, font=("Rockwell", 22, "bold"))
        self.titleLabel.pack(pady=30)

        # Email Entry
        self.emailLabel = tk.Label(self, text="Enter Registered Email", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.emailLabel.pack(pady=(10, 5))

        self.emailentry = tk.Entry(self, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor, insertbackground=self.secTextColor)
        self.emailentry.pack(ipady=5, pady=10, padx=40, fill='x')
        self.emailentry.place(relx=0.25, rely=0.27, relwidth=0.5, relheight=0.06)

        # Send OTP Button
        self.sendOtpButton = tk.Button(self, text="Send OTP", bg=self.primaryColor, fg=self.secTextColor, font=self.labelFont, command=self.sendOtp)
        self.sendOtpButton.pack(pady=31, ipadx=10, ipady=5)

        # OTP Entry
        self.otpLabel = tk.Label(self, text="Enter OTP", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.otpLabel.pack(pady=(0, 15))

        self.otpentry = tk.Entry(self, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor, insertbackground=self.secTextColor)
        self.otpentry.pack(ipady=5, pady=5, padx=5, fill='x')
        self.otpentry.place(relx=0.35, rely=0.54, relwidth=0.3, relheight=0.06)
        self.otpentry.bind("<Return>", self.verifyOtpShortcut)

        # Verify OTP Button
        self.verifyOtpButton = tk.Button(self, text="Verify OTP", bg=self.primaryColor, fg=self.secTextColor, font=self.labelFont, command=self.checkOTP)
        self.verifyOtpButton.pack(pady=20, ipadx=10, ipady=5)

        # Back Button
        self.backButton = tk.Button(self, text="Back to Login", bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont, command=self.backToLogin)
        self.backButton.pack(pady=10, ipadx=10, ipady=5)

    def sendOtp(self):
        email = self.emailentry.get().strip()
        if not email:
            self.showMessage("Email cannot be empty", self.errorColor)
            return

        pdb = PMPDatabase()
        if not pdb.mailCheck(email):
            self.showMessage("Invalid Email!", self.errorColor)
            return

        # Generate new OTP
        self.generatedOTP = Otp().generateOTP()

        # Send OTP
        mailer = SendMail()
        subject = 'Forgot Password'
        message = f'Your OTP for Password Manager is:\n{self.generatedOTP}'
        mailer.send(email, subject, message)

        self.showMessage("OTP Sent Successfully!", self.successColor)

    def checkOTP(self):
        entered_otp = self.otpentry.get().strip()
        if not self.generatedOTP:
            self.showMessage("Please send OTP first", self.errorColor)
            return

        if entered_otp == self.generatedOTP:
            self.clearFields()
            self.controller.show_frame(ResetPassFrame)
        else:
            self.showMessage("Incorrect OTP!", self.errorColor)

    def verifyOtpShortcut(self, event):
        self.checkOTP()

    def backToLogin(self):
        from Frames.loginFrame import LoginFrame  # <--- LOCAL IMPORT here to fix circular import
        self.clearFields()
        self.controller.show_frame(LoginFrame)

    def clearFields(self):
        self.emailentry.delete(0, 'end')
        self.otpentry.delete(0, 'end')
        self.generatedOTP = None

    def showMessage(self, message, color):
        msg = tk.Label(self, text=message, bg=color, fg=self.priTextColor, font=self.labelFont)
        msg.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.05)
        msg.after(3000, msg.destroy)
