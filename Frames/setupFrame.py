import tkinter as tk
from tkinter.constants import LEFT
from Database.MPdatabase import PMPDatabase
from Backend.OTPGenerator import Otp
from Backend.sendMail import SendMail

class SetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Color Scheme (more professional tones)
        self.primaryColor = '#3f51b5'  # Subtle blue
        self.backgroundColor = '#1e1e1e'  # Dark background for better contrast
        self.surface1Color = '#2c2c2c'  # Light gray background for input fields
        self.surface2Color = '#333333'  # Slightly darker gray for buttons
        self.successColor = '#4caf50'  # Green for success
        self.errorColor = '#f44336'  # Red for error messages
        self.priTextColor = '#ffffff'  # White text color for visibility
        self.secTextColor = '#e0e0e0'  # Lighter gray text color

        # Fonts (Modern font family for better readability)
        self.entryFont = ("Segoe UI", 12)
        self.labelFont = ("Segoe UI", 12, "bold")

        self.controller = controller
        otpObj = Otp()
        self.generatedOTP = otpObj.generateOTP()

        # Main Frame (Add padding and rounded corners for professional design)
        self.setupFrame = tk.LabelFrame(self, text="Setup Your Account", bg=self.backgroundColor, fg=self.secTextColor, font=("Segoe UI", 14, "bold"))
        self.setupFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title Label
        self.titleLabel = tk.Label(self.setupFrame, text='Account Setup', bg=self.backgroundColor, fg=self.primaryColor, font=("Segoe UI", 22, "bold"))
        self.titleLabel.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.7, anchor="center")

        # Email Entry Section (Maintained professional width)
        self.emailLabel = tk.Label(self.setupFrame, text="Email Address", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.emailLabel.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.07)
        self.emailentry = tk.Entry(self.setupFrame, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor, relief="flat")
        self.emailentry.place(relx=0.25, rely=0.27, relwidth=0.5, relheight=0.06)
        self.emailentry.delete(0, 'end')

        # Send OTP Button with Hover Effects
        self.sendOtpButton = tk.Button(self.setupFrame, text="Send OTP", command=self.sendOtp, bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont, relief="flat")
        self.sendOtpButton.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.08)
        self.sendOtpButton.bind("<Enter>", lambda e: self.on_button_hover(self.sendOtpButton))
        self.sendOtpButton.bind("<Leave>", lambda e: self.on_button_leave(self.sendOtpButton))

        # OTP Entry Section (Smaller width set)
        self.otpLabel = tk.Label(self.setupFrame, text="Enter OTP", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.otpLabel.place(relx=0.25, rely=0.47, relwidth=0.5, relheight=0.07)
        self.otpentry = tk.Entry(self.setupFrame, width=10, font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor, relief="flat")  # Smaller width (10)
        self.otpentry.place(relx=0.35, rely=0.54, relwidth=0.3, relheight=0.06)  # Reduced relative width
        self.otpentry.delete(0, 'end')

        # Verify OTP Button
        self.otpEnterButton = tk.Button(self.setupFrame, text="Verify OTP", command=lambda: [self.checkOTP()], bg=self.surface2Color, fg=self.secTextColor, font=self.labelFont, relief="flat")
        self.otpEnterButton.place(relx=0.40, rely=0.63, relwidth=0.20, relheight=0.08)
        self.otpEnterButton.bind("<Enter>", lambda e: self.on_button_hover(self.otpEnterButton))
        self.otpEnterButton.bind("<Leave>", lambda e: self.on_button_leave(self.otpEnterButton))

        # Password Entry Section
        self.passLabel = tk.Label(self.setupFrame, text="Password", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.passLabel.place(relx=0.25, rely=0.75, relwidth=0.5, relheight=0.07)
        self.passentry = tk.Entry(self.setupFrame, show="*", font=self.entryFont, bg=self.surface1Color, fg=self.secTextColor, relief="flat")
        self.passentry.place(relx=0.25, rely=0.82, relwidth=0.5, relheight=0.06)
        self.passentry.delete(0, 'end')

        # Enter Button
        self.enterButton = tk.Button(self.setupFrame, text="Enter", bg=self.primaryColor, fg=self.secTextColor, font=self.labelFont, relief="flat", command=lambda: [self.insertPass(self.checkOTP())])
        self.enterButton.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.08)
        self.enterButton.bind("<Enter>", lambda e: self.on_button_hover(self.enterButton))
        self.enterButton.bind("<Leave>", lambda e: self.on_button_leave(self.enterButton))

        # Status Label (for error/success messages)
        self.statusLabel = tk.Label(self.setupFrame, text="", bg=self.backgroundColor, fg=self.secTextColor, font=self.labelFont)
        self.statusLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)

    def on_button_hover(self, button):
        button.config(bg="#303f9f")  # Darker shade on hover

    def on_button_leave(self, button):
        button.config(bg=self.surface2Color)  # Reset to original color

    def insertPass(self, otpStatus):
        from Frames.loginFrame import LoginFrame
        try:
            db = PMPDatabase()
            em = self.emailentry.get()
            mp = self.passentry.get()
            if otpStatus:
                db.insertIntoTable(mp, em)
                self.updateStatus("Account Setup Successful!", self.successColor)
                self.controller.show_frame(LoginFrame)
            else:
                self.updateStatus("OTP Incorrect! Try again.", self.errorColor)
                self.clearFields()

        except Exception as e:
            self.updateStatus(f"Database Error: {str(e)}", self.errorColor)
            self.clearFields()

    def updateStatus(self, message, bgColor):
        self.statusLabel.config(text=message, bg=bgColor)
        self.statusLabel.after(2000, self.clearStatus)

    def clearStatus(self):
        self.statusLabel.config(text="", bg=self.backgroundColor)

    def clearFields(self):
        self.emailentry.delete(0, 'end')
        self.passentry.delete(0, 'end')
        self.otpentry.delete(0, 'end')

    def checkOTP(self):
        enteredOTP = self.otpentry.get()
        if enteredOTP == self.generatedOTP:
            self.updateStatus("OTP Verified Successfully!", self.successColor)
            return True
        else:
            self.updateStatus("Incorrect OTP. Try again.", self.errorColor)
            return False

    def sendOtp(self):
        try:
            mail = SendMail()
            subject = 'OTP Verification'
            message = f"Your OTP for Password Manager is: {self.generatedOTP}"
            mail.send(self.emailentry.get(), subject, message)
            self.updateStatus("OTP Sent to Email!", self.successColor)
        except Exception as e:
            self.updateStatus(f"Error in Sending OTP: {str(e)}", self.errorColor)
