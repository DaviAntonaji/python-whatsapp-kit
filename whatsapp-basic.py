import pywhatkit as pwk
import datetime

now = datetime.datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M")) + 1


pwk.sendwhatmsg("+5518999999999", "Hello world!", hour, minute)