import os

class ReportFile:
    
     def PrepareReport(obj):
       # fHandler = OpenFile()
        fname = "ShabanaReport.txt"
        open(fname, "+w")
        fHandler = os.open(fname, os.O_RDWR)
        s = obj.name + '\n' + str(obj.age)
        line = str.encode(s)
        os.write(fHandler, line)
        os.system('notepad.exe' + ' ' +   fname)