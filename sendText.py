'''
Meet-SMS - Send SMS easily from MeetSMS
Author: Yunik Maharjan
'''
import requests
import sys
import re
import itertools
import threading
import time

done = False


def main(username, password, message, recipcent): #recipient is list
    global done

    username = username
    message = message
    recipcent = recipcent


    if len(recipcent) > 10:
        print("Sending more than 10 SMS is not supported.")
        exit()
    numbers = None
    ncell = None
    wrongNumber = None
    for j in recipcent:
        j = j.strip()
        # Check for Ncell numbers
        if re.match(r"^\d{10}$", j):
            if(re.match(r'^(980)|(981)|(982)', j)):
                ncell = j if ncell is None else ncell + "," + j
            elif (re.match(r'^(984)|(985)|(986)', j)):
                numbers = j if numbers is None else numbers + "," + j
        else:
            wrongNumber = j if wrongNumber is None else wrongNumber + "," + j


    if numbers is None:
        if ncell is not None:
            ncell_check(ncell)
        if wrongNumber is not None:
            wrongnumber_check(wrongNumber)
        exit()
    if ncell is not None:
        ncell_check(ncell)
    if wrongNumber is not None:
        wrongnumber_check(wrongNumber)
    login_url = "http://www.meet.net.np/meet/action/login"
    sms_url = "http://www.meet.net.np/meet/mod/sms/actions/send.php"
    session_req = requests.session()

    data = {
        "username": username,
        "password": password,

    }

    try:

        messages = {"recipient": numbers,
                    "message": message,
                    "SmsLanguage": "English",
                    "sendbutton": "Send Now"}
    except NameError as e:
        print("Error! {}\nUse the following options:\n -u for username \n -m for message \n -r for receiver's number".format(e))
        exit()

    t = threading.Thread(target=animate)
    t.start()

    resp = session_req.post(login_url, data)
    result = session_req.post(sms_url, messages)
    html_ = str(result.content)
    index_ = re.search("Free SMS Quota", html_)
    done = True
    if index_:
        Quota = html_[index_.start():index_.start() + 46]
        print("\rSuccess\n" + Quota)
    elif re.search("loginform", html_):
        print("\rThe username/password you entered in incorrect")
    else:
        print("Either you're out of Quota or something went wrong.")


def ncell_check(ncell):

    if ncell is not None:
        print(
            "SMS to {} will not be send because Ncell numbers are not supported".format(ncell))


def wrongnumber_check(wrongNumber):

    if wrongNumber is not None:
        print(
            "SMS to {} will not be send because the numbers are incorrect".format(wrongNumber))


def unit_test(text):
    return text


def animate():
    global done
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSending ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()


def text(message, number):
	main("tosendsmsthree@yandex.com", "@ppl3Man", message, number)
