import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Emailer:
    def __init__(self, login, password, *, smtp_server='smtp.gmail.com', smtp_port=587, imap_server='imap.gmail.com'):
        self.__login = login
        self.__password = password
        self.__smtp_server = smtp_server
        self.__smtp_port = smtp_port
        self.__imap_server = imap_server

    def send(self, subject, message, recipients):
        # send message
        email_message = MIMEMultipart()
        email_message['From'] = self.__login
        email_message['To'] = ', '.join(recipients)
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message))

        smtp_connection = smtplib.SMTP(self.__smtp_server, self.__smtp_port)
        # identify ourselves to smtp gmail client
        smtp_connection.ehlo()
        # secure our email with tls encryption
        smtp_connection.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_connection.ehlo()

        smtp_connection.login(self.__login, self.__password)
        smtp_connection.sendmail(self.__login,
                                 smtp_connection,
                                 email_message.as_string())
        smtp_connection.quit()
        # send end

    def receive(self, folder='inbox', header=None):
        content_type = '(RFC822)'

        imap_connection = imaplib.IMAP4_SSL(self.__imap_server)
        imap_connection.login(self.__login, self.__password)
        imap_connection.list()
        imap_connection.select(folder)

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = imap_connection.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = imap_connection.uid('fetch', latest_email_uid, content_type)
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        imap_connection.logout()

        return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    emailer = Emailer(login, password)
    emailer.send('Subject', 'Message', ['vasya@email.com', 'petya@email.com'])
    print(emailer.receive())
