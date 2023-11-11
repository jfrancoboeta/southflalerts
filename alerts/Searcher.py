#By Juan Franco Boeta
#Libaries to install: BeautifulSoup and mysql connector
from bs4 import BeautifulSoup
from urllib3.util.ssl_ import create_urllib3_context
from requests.adapters import HTTPAdapter
from email.message import EmailMessage
from datetime import datetime
import ssl, smtplib, Settings, re, urllib3, requests, mysql.connector, sys, pytz

log = open('alert_log.txt','a')

#use legacy SSL as this website won't take OpenSSL 3 requests (class by Dhruv97Sharma)
class CustomSslContextHttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
        self.poolmanager = urllib3.PoolManager(ssl_context=ctx)

#check website status before proceding with the rest
weburl = "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_dyn_sched"
session = requests.Session()
session.mount(weburl, CustomSslContextHttpAdapter())
current_date = datetime.now(tz=pytz.timezone("US/Eastern"))
current_date_str = current_date.strftime("%d/%m/%Y %H:%M:%S")
try:
    response = session.get(weburl, timeout=5)
except requests.exceptions.RequestException as error:
    log.write(current_date_str + " - Website is currently down! Error: "+ str(error) + "\n")
    log.close()
    sys.exit()

#send email function
def send_email():
     subject = e_subject
     body = e_body
     email = EmailMessage()
     email["From"] = sender
     email["To"] = receiver
     email["subject"] = subject
     email.set_content(body + """\
<!DOCTYPE html>
    <html>
    <body>

    <h4 style="text-align:center">DISCLAIMER</h4>
    <p style="text-align:center">In no way southflalerts.com is affiliated or related to the University of South Florida or any of its partners. This is a personal project.</p>
    <p style="text-align:center"><a href="https://southflalerts.com/unsubscribe/">unsubscribe to our services</a></p>
    </body>
    </html>
""", subtype = 'html')

     context = ssl.create_default_context()

     with smtplib.SMTP(Settings.smtp_host, Settings.smtp_port) as smtp: #to use SMTPS port 465, change this line to - with smtplib.SMTP_SSL(Settings.smtp_host, Settings.smtp_port, context=context) as smtp:
          smtp.starttls(context=context) #comment this line to disable TLS for SMTPS port 465
          smtp.login(sender, password)
          smtp.sendmail(sender, receiver, email.as_string())

#Connect to MySQL Database
database = mysql.connector.connect(
    host = Settings.host,
    user = Settings.user,
    password = Settings.dbpassword,
    database = Settings.database
)

#Iterate through each row of the database´s table "people" and doing the corresponding action depending on the email/URL used
cursor = database.cursor()
cursor.execute("SELECT * FROM people")
people_list = cursor.fetchall()
for people in people_list:
     current_date = datetime.now(tz=pytz.timezone("US/Eastern"))
     current_date_str = current_date.strftime("%d/%m/%Y %H:%M:%S")
     url = people[0]
     receiver = people[1]
     subscription_id = people[2]
     confirmation_email = people[3]
     sender = Settings.sender
     password = Settings.password
     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

     if(re.fullmatch(email_pattern, receiver) == None): #delete invalid emails from the database
          cursor.execute("DELETE FROM people WHERE id = %s", (subscription_id,))
          database.commit()
          log.write(current_date_str + " - suscriber_id " + str(subscription_id) + " was deleted due to incorrect email formatting\n")
          continue

     if "disp_detail_sched" not in url: #delete invalid URLs from the database and notify user of the mistake
          e_subject = "We couldn't retrieve your class info!"
          e_body = """Sorry, but the URL you provided us won't give the information we need to check for seats available.\nIf you still want to be notified, please subscribe again. You can find a tutorial of which URL you have to look for in our FAQ page (https://southflalerts.com/faq/)"""
          send_email()
          log.write(current_date_str + " - suscriber_id " + str(subscription_id) + " with email " + receiver + " was notified and deleted due to incorrect URL usage\n")
          cursor.execute("DELETE FROM people WHERE id = %s", (subscription_id,))
          database.commit()
          continue

     session = requests.Session()
     session.mount(url, CustomSslContextHttpAdapter())
     try:
          response = session.get(url, timeout=5)
     except requests.exceptions.RequestException as error:
          e_subject = "We couldn't retrieve your class info!"
          e_body = """Sorry, but the URL you provided us won't give the information we need to check for seats available. This could have also been caused by the request being blocked, or the page being down.\nIf you still want to be notified, please try subscribing again. If the issue persists, please contact us at https://southflalerts.com/contact. You can find a tutorial of which URL you have to look for You can find a tutorial of which URL you have to look for in our FAQ page (https://southflalerts.com/faq/)"""
          send_email()
          log.write(current_date_str + " - suscriber_id " + str(subscription_id) + " with email " + receiver + " was notified and deleted due to " + str(error) + "\n")
          cursor.execute("DELETE FROM people WHERE id = %s", (subscription_id,))
          database.commit()
          continue
     page = BeautifulSoup(response.text, "html.parser")

     try:
         body = page.find('body')
         class_info = body.find_all(string = "Detailed Class Information")
         parent2 = class_info[1].parent.parent
         parent3 = class_info[0].parent.parent.parent
         class_details = parent2.contents[2]
         term_and_date = parent3.contents[5].text.strip()
         term = term_and_date.partition('\n')[0]

         seats_list = page.find_all(string = "Seats")
         parent = seats_list[0].parent.parent.parent
         class_capacity = parent.contents[3]
         actual_seats = parent.contents[5]
         available_seats = parent.contents[7]

         #Future waitlist seats implementation
         #waitlist_seats_list = page.find_all(string = "Waitlist Seats")
         #parent1 = waitlist_seats_list[0].parent.parent.parent
         #class_waitlist_capacity = parent1.contents[3]
         #actual_waitlist_seats = parent1.contents[5]
         #available_waitlist_seats = parent1.contents[7]
     except IndexError as error: #Are we checking the correct link?
          e_subject = "We couldn't retrieve your class info!"
          e_body = """Sorry, but the URL you provided us won't give the information we need to check for seats available.\nIf you still want to be notified, please subscribe again. You can find a tutorial of which URL you have to look for in our FAQ page (https://southflalerts.com/faq/)"""
          send_email()
          log.write(current_date_str + " - suscriber_id " + str(subscription_id) + " with email " + receiver + " was notified and deleted due to " + str(error) + ", this might have been caused by the use of a wrong URL\n")
          cursor.execute("DELETE FROM people WHERE id = %s", (subscription_id,))
          database.commit()
          continue

     if confirmation_email == 0: #Send a confirmation email only once
          e_subject = "We got your request!"
          e_body = "Your request to be notified if a seat becomes available for " + class_details.text.strip() + " in the " + term +" semester was received.\nIf you believe this is a mistake, please unsubscribe here: https://southflalerts.com/unsubscribe/"
          send_email()
          log.write(current_date_str + " - An email was sent to " + receiver + " confirming his subscription\n")
          cursor.execute("UPDATE people SET confirmation_email = %s WHERE id = %s", ("1", subscription_id))
          database.commit()

     if ord(available_seats.text[0]) > 48 and ord(available_seats.text[0]) <= 57 and available_seats.text.isdigit() == True: #checking if there are more than 0 seats available, but also check if it is a digit

          e_subject = "A seat has become available for " + class_details.text.strip()
          e_body = available_seats.text.strip() + """ seat(s) available for the class you are following, go register quickly!\nYou have been unsubscribed, if you still want to be notified, please subscribe again"""
          send_email()

          log.write(current_date_str + " - An email was sent to " + receiver + " informing of found seats available\n")

          cursor.execute("DELETE FROM people WHERE id = %s", (subscription_id,))
          database.commit()

log.close()
database.close()
