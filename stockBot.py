import smtplib, datetime, yfinance, sys, time

#Initial Information
sender_email = "mgroholskibot@gmail.com"

if len(sys.argv) == 2:
    password = sys.argv[1]
else:
    exit()


""" emailAmount = input("Please input the amount of emails you would like to enter: ")

try:
    emailAmount = int(emailAmount)
except:
    print("Did not enter an integer amount")

emails = []
for i in range(0,emailAmount):
    email = input("Please input email " + i)
    emails.append(email) """



receiver_email1 = "mattgroholski@yahoo.com"
receiver_email2 = "candersen6416@gmail.com"

currentTime = datetime.datetime.now()

while not (currentTime.hour == "24"):
    if (currentTime.minute == 0 and currentTime.second == 0):
        #gets stock price
        voo = yfinance.Ticker("VOO")
        message = "Subject: VOO Stock Price \n\n The current VOO stock price is: " + str(voo.info["regularMarketPrice"]) + "\n Please let Matthew know if you would like other stocks included in this hourly email."
        with smtplib.SMTP('smtp.gmail.com', 587) as server: 
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email1, message)
            server.sendmail(sender_email, receiver_email2, message)
            print("sent")
            """ for receiver_email in emails:
                server.sendmail(sender_email, receiver_email, message) """
    time.sleep(1)
    currentTime = datetime.datetime.now()

print("Program Ending")



