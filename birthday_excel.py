import subprocess
import xlrd
import smtplib
k = subprocess.check_output("date")
k = k.split()
date_str = k[2] + "-" + k[1].upper()
book = xlrd.open_workbook("/root/python/proj/OTS_DOB_RPT_test.xls")
first_sheet = book.sheet_by_index(0)
row = 0
name = []
for i in first_sheet.col_values(8):
        if i == date_str:
                name.append(first_sheet.cell(row, 6))
        row = row + 1
#if len(name) > 1:

# subprocess.popen("")
test = ''
for i in name:
 test = test + i + ""

message = "AAJ INKA BIRTHDAY HE : %s " % test
if len(name) > 1:
 sender = 'from@fromdomain.com'
 receivers = ['Amarjeet.S@test.com']
 try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
 except SMTPException:
   print "Error: unable to send email"

