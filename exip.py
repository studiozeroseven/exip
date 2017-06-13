import urllib, json
import smtplib

email = "ian@EMAIL_ADDRESS.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login( email , "CHANGE_ME_PASSWORD")
print "Logging to server..."


data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
ip = data["ip"]
print "Current IP: " + ip

file_loc = "C:\Users\ischwartz\ownCloud\exip\exip-data.txt" # LINUX SERVER= /saved/scripts/exip
print "Locating file..."
print "Comparing IPs..."
exipR = open(file_loc,"r")
exipRead = exipR.read()
exipR.close()

if ip != exipRead:
        print "Same IP, no change recorded"
else:
        print "Changed IP: " + ip
        exipO = open(file_loc,"w")
        exipO.write(ip)
        exipO.close()
        msg = "\n Changed ip: " + ip  # The \n separates the message from the headers
        server.sendmail( email, email , msg)
