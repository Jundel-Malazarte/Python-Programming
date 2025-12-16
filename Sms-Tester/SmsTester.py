import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromAddress = prompt("From: ")
toAddress = prompt("To: ").split()
print("Enter message: ")\
    
# Add the form
msg = ("From: %s\r\n To: %s\r\n\r\n" % (fromAddress, ", ".join(toAddress)))
while True: 
    try:
        line = input()
    except EOFError:
        break
    if not line: 
        break
    msg = msg + line
    
    print("Message length is: ", len(msg))
    
    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(fromAddress, toAddress, msg)
    server.quit()