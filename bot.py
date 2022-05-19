import smtplib, sys, time

#Initial Information
sender_email = "mgroholskibot@gmail.com"

if len(sys.argv) == 2:
    password = sys.argv[1]
    print(password)
else:
    print(len(sys.argv))
    exit()


emailAmount = input("Please input the amount of emails you would like to enter: ")

try:
    emailAmount = int(emailAmount)
except:
    print("Did not enter an integer amount")

emails = []

for i in range(0,emailAmount):
        email = input("Please input email " + str(i + 1) + ": ")
        emails.append(email)

subject = input("Input Subject Line: ")
body = input("Input Body: ")

message = "Subject: " + subject + " \n\n " + body
with smtplib.SMTP('smtp.gmail.com', 587) as server: 
    server.starttls()
    server.login(sender_email, password)
    for receiver_email in emails:
        server.sendmail(sender_email, receiver_email, message)
    


print("Program Ending")



