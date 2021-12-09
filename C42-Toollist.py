import sys, os
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtCore, QtGui

from MainWindow import Ui_C42_Toollist

# Variablen
    
homePath = os.path.dirname(sys.executable)

homePath = os.path.dirname(__file__) # Ansonsten wird kein Icon angezeigt
logo_Pfad = os.path.join(homePath, 'data\\Icon.png')

global output
global filepath
global outputpath

output = []
filepath = ""
outputpath = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_C42_Toollist()
        self.ui.setupUi(self)

        self.ui.BTN_Laden.clicked.connect(self.GetOriginalPath) # Select File

        self.ui.BTN_umwandeln.clicked.connect(Umwandeln) # Select File

        self.show()
    
    def GetOriginalPath(self):
        global filepath 
        global outputpath

        filepath_original = QFileDialog.getOpenFileName( None, 'Select Werkzeugliste', "", 'Werkzeugliste(*.wzd*)')
        MainWindow.ui.OriginalPath.setText(filepath_original[0]) 

        filepath = filepath_original[0]
        filepath_out = filepath[:-3] + "csv"
        outputpath = filepath_out

        MainWindow.ui.FinalPath.setText(outputpath) 

def Umwandeln():
    global filepath
    global outputpath
    with open(filepath, 'r+') as f:
        lines = f.readlines()

    for i in range(len(lines)-1):
        tool_list = []
        if i == 0 or i == len(lines)-1:
            continue
        if ".1" in lines[i][:5] or ".2" in lines[i][:5]:
            continue

        #  Aufteilen und mit Komma wieder zusammenfügen.
        my_list = lines[i].split() 

        if i == 1:
            my_list.pop(41)
            my_list.pop(38)
            my_list.pop(29)
            my_list.pop(28)
            my_list.pop(11)
            my_list.pop(10)
            my_list.pop(9)
        else:
            my_list.pop(17)
            my_list.pop(16)

        # tool_list.append(my_list[0] + ",")#T
        tool_list.append(my_list[1] + ",")#Name
        tool_list.append(my_list[2] + ",")#L
        tool_list.append(my_list[3] + ",")#R

        if i == 1:
            tool_list.append("ACC" + ",")
            tool_list.append("AFC" + ",")
            tool_list.append("AFC-LOAD" + ",")
            tool_list.append("AFC-OVLD1" + ",")
            tool_list.append("AFC-OVLD2" + ",")
        else:
            tool_list.append("0" + ",")
            tool_list.append("" + ",")
            tool_list.append("" + ",")   
            tool_list.append("" + ",")  
            tool_list.append("" + ",")

        tool_list.append(my_list[23] + ",")#ANGLE
        tool_list.append(my_list[11] + ",")#CUR.TIME
        tool_list.append(my_list[13] + ",")#CUT

        if i == 1:
            tool_list.append("CUTDATA" + ",")
        else:
            tool_list.append("0" + ",")

        tool_list.append(my_list[16] + ",")#DIRECT
        tool_list.append(my_list[5] + ",")#DL
        tool_list.append(my_list[12] + ",")#DOC
        tool_list.append(my_list[7] + ",")#DR
        tool_list.append(my_list[8] + ",")#DR2

        if i == 1:
            tool_list.append("DR2TABLE" + ",")
            tool_list.append("INV-NR" + ",")
        else:
            tool_list.append("" + ",")
            tool_list.append("" + ",")

        if i == 1:
            tool_list.append("KINEMATIC" + ",")#Kinematic
            tool_list.append("LAST_USE" + ",")
        else:
            tool_list.append("" + ",")
            tool_list.append("" + ",")

        tool_list.append(my_list[20] + ",")#LBREAK
        tool_list.append(my_list[22] + ",")#LCUTS
        tool_list.append(my_list[29] + ",")#LIFTOFF
        tool_list.append(my_list[14] + ",")#LTOL
        tool_list.append(my_list[6] + ",")#NMAX

        if i == 1:
            tool_list.append("OVRTIME" + ",")
        else:
            tool_list.append("" + ",")

        tool_list.append(my_list[30] + ",")#P1
        tool_list.append(my_list[31] + ",")#P2
        tool_list.append(my_list[32] + ",")#P3

        if i == 1:
            tool_list.append("P4" + ",")
            tool_list.append("P5" + ",")
            tool_list.append("P6" + ",")
            tool_list.append("P7" + ",")
            tool_list.append("P8" + ",")
        else:
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")

        tool_list.append(my_list[34] + ",")#PITCH
        
        if i == 1:
            tool_list.append(my_list[17] + ",")#PLC
        else:
            tool_list.append("0" + ",")#PLC

        tool_list.append(my_list[25] + ",")#PLC-VAL

        if i == 1:
            tool_list.append("PTYP" + ",")
        else:
            tool_list.append("0" + ",")

        tool_list.append(my_list[4] + ",")#R2

        if i == 1:
            tool_list.append("R2TOL" + ",")
        else:
            tool_list.append("0" + ",")

        tool_list.append(my_list[21] + ",")#RBREAK 

        if i == 1:
            tool_list.append("RT" + ",")
        else:
            tool_list.append("" + ",") 

        tool_list.append(my_list[15] + ",")#RTOL
        tool_list.append(my_list[33] + ",")#T-ANGLE
        tool_list.append(my_list[9] + ",")#TIME1
        tool_list.append(my_list[10] + ",")#TIME2

        if i == 1:
            tool_list.append("TL" + ",")
            tool_list.append("TMAT" + ",")
            tool_list.append("TP_NO" + ",")
        else:
            tool_list.append("" + ",")
            tool_list.append("" + ",")
            tool_list.append("" + ",")

        tool_list.append(my_list[18] + ",")#TT:L-OFFS
        tool_list.append(my_list[19] + ",")#TT:R-OFFS

        if i == 1:
            tool_list.append(my_list[24] + ",")#TYP
        else:
            tool_list.append("0" + ",")#TYP

        # tool_list.append(my_list[26] + ",")#CAL-OF1
        # tool_list.append(my_list[27] + ",")#CAL-OF12
        # tool_list.append(my_list[28] + ",")#CAL-ANG

        tool_list.append(my_list[35] + ",")#COMMENT

        tool_list = "".join(tool_list)
        tool_list = tool_list + "\n"

        output.append(tool_list) # In liste schreiben

    with open(outputpath , 'w+') as f:
        for item in output:
            f.writelines(item)

if __name__ == "__main__":
    app= QApplication(sys.argv)
    windowIcon = QIcon(logo_Pfad)
    MainWindow = MainWindow()

    MainWindow.show() # main window öffnen
    sys.exit(app.exec_()) # alles beenden