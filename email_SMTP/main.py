#Import libraries
from email.message import EmailMessage
import ssl
import smtplib

#Define email parameters
sender_email = 'kyawzinlattrafiq@gmail.com'
gmail_app_generated_password = 'xwsofdpxuzloqxcb'
receiver_email = 'mr.rafiq111187@gmail.com'

subject = 'Use my program to decrypt this ciphertext'
body = """
I have used RSA encryption and below is the ciphertext.
guw2JgrPfckRrRK/Hn5IQK4sNZdIsgxtV5IC3GxgFuQ4VR6wPp+bFEvDiGgEnP0YyvhyUeuWGOweDtXEyrVG15xNOPDEmzt5MyuAt1GENrYKYgJqz0J+lFSiybrPk/sZUHVGNH86d/CacaOpKPaFSBTG4k/8Em5S4yDwxUsuydHAKi2bt+wvU38XwBgxxS2b/y03dzDwGCZW0rYlOJDSSrRw6KJ9dKd0uFaxFilGXXq6uH/QzZPF2CvKunZkG5oE+TFUV1w+qAYI9nC5vxA8ll/xgb4a0bAnwHB5AqF2oJT09lUwqFo3qpmt7nTX/nxXScHQeRdY4Z/qtS6+DmFeCw==
And this is the digital signature:
Or47p8W8LyrDl7PXX6kKsj3oZymZRudvdbXrfV8XReSUKR1nlz0ygRzpK9EpzKwKDtB28VBFoBNJcGiFhux9siZkrtJ5vKQeqhpKiKw8A5RRzx9XTYcX5l04eOomcecXwb1gA4613c49JDYMUQJYXU7bffv6O+P9OPeCJ5ltn/IYkYCLlrRcRE1pIR0wGrt4Hmr2VfTiES/M+Cv8UgtDuqBwu+yQpr5dn+6YfFvRe/ZodWWpIjWtUN3IHtbMuWbZ0MMBqfGFMRsfuLSY+kNALNmFS59uVpsamYqx3RsiuE1310BTN34pnoJjJu1W7W3uVm4mkIWWT//3bMgGhW85Xw==

"""

em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['Subject'] = subject
em.set_content(body)

#Create a secure SSL context
context = ssl.create_default_context()

#Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, gmail_app_generated_password)
        server.sendmail(sender_email, receiver_email, em.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)

