import sys, os
from tokenize import Number
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtGui, QtCore

import pathlib
import tempfile
import json
import shutil
import requests
import threading
import psutil

from MainWindow import Ui_C42_Toollist
from ERROR_MSG import Ui_ERROR_MSG

# Updater

global AktulleVersion
AktulleVersion = ""
JsonURL = 'https://3ddruck-mb.de/UpdateChecker/C42_Toollist_Converter_CheckforUpdate.json'
headersURL = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
paramURL = dict()
DownloadUpdateFileURL = 'https://3ddruck-mb.de/UpdateChecker/Update_C42_Toollist_Converter.zip'
global NeusteVersion
NeusteVersion = ""
pfad_updatepfad = str(pathlib.Path(__file__).parents[0]) + "/C42_Toollist_Converter_CheckforUpdate.json"

TempPath = str(pathlib.Path(tempfile.gettempdir() + "/Materialbestelltung_temp").absolute())
TempPathZIPFILE = str(pathlib.Path(tempfile.gettempdir() + "/Materialbestelltung_temp/Update_C42_Toollist_Converter.zip").absolute())
TempPathEXE = str(pathlib.Path(tempfile.gettempdir() + "/Materialbestelltung_temp/Update_C42_Toollist_Converter.exe").absolute())

from ui_UpdateChecker_MainWindow import Ui_UpdateChecker
from ui_UpdateChecker_Fortschritt import Ui_Fortschritt

# Variablen
    
homePath = os.path.dirname(sys.executable)

homePath = os.path.dirname(__file__) # Ansonsten wird kein Icon angezeigt
logo_Pfad = os.path.join(homePath, 'data\\Icon.png')
logo_ERROR_Pfad = os.path.join(homePath, 'data\\ERROR_ICON.png')

global filepath
global outputpath

filepath = ""
outputpath = ""

# Classes

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_C42_Toollist()
        self.ui.setupUi(self)
        self.setWindowIcon = windowIcon

        self.ui.BTN_Laden.clicked.connect(GetOriginalPath) # Select File

        self.ui.BTN_umwandeln.clicked.connect(Umwandeln) # Select File

        self.show()
    
class ERROR_MSG(QDialog):
    def __init__(self):
        super(ERROR_MSG, self).__init__()
        self.ui = Ui_ERROR_MSG()
        self.ui.setupUi(self)
        self.setWindowIcon = windowERRORIcon

        self.ui.BTN_OK.clicked.connect(self.close) # Select File

# Updatechecker Classes

class UpdateChecker(QMainWindow):
    def __init__(self):
        super(UpdateChecker, self).__init__()
        self.ui = Ui_UpdateChecker()
        self.ui.setupUi(self)
        self.setWindowIcon(windowIcon)

        self.ui.BT_Update.clicked.connect(self.callUpdate)

    def callUpdate(self):
        Fortschritt_UpdateChecker.ui.LBL_Status.setText("Download...")
        Fortschritt_UpdateChecker.ui.progressBar.setValue(0)
        Fortschritt_UpdateChecker.show()
        UpdateChecker.close()
        t1 = Thread_UpdateChecker(1, "t1", "download")
        t1.start()

class Fortschritt_UpdateChecker(QMainWindow):
    def __init__(self):
        super(Fortschritt_UpdateChecker, self).__init__()
        self.ui = Ui_Fortschritt()
        self.ui.setupUi(self)
        self.setWindowIcon(windowIcon)

        self.ui.BT_Clos_ALL.hide()
        self.ui.BT_Clos_ALL.setDisabled(True)

        self.ui.BT_Clos_ALL.clicked.connect(self.closeit)

    def closeEvent(self, event: QtGui.QCloseEvent):
        current_system_pid = os.getpid()

        ThisSystem = psutil.Process(current_system_pid)

        try:
            os.remove(TempPathZIPFILE)
            os.remove(TempPathEXE)
        except:
            pass

        ThisSystem.terminate()

    def closeit(self):
        # Write JsonFile
        with open(pfad_updatepfad, "r") as jsonFile:
            data = json.load(jsonFile)

        data["Programmversion"] = NeusteVersion

        with open(pfad_updatepfad, "w") as jsonFile:
            json.dump(data, jsonFile)
        
        self.close()

class Thread_UpdateChecker(threading.Thread):
    def __init__(self, iD, name, make):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name
        self.make = make

    def download(self):
        response = requests.get(DownloadUpdateFileURL, stream=True, headers=headersURL)

        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte

        prozent = 0

        with open(TempPathZIPFILE, 'wb') as file:
            for data in response.iter_content(block_size):
                prozent = prozent + len(data)
                neuProzent = float(prozent / total_size_in_bytes * 100.00)
                Fortschritt_UpdateChecker.ui.progressBar.setValue(round(neuProzent))
                file.write(data)

        shutil.unpack_archive(TempPathZIPFILE, TempPath)
        os.system(TempPathEXE)
        Fortschritt_UpdateChecker.ui.LBL_Status.setText("Fertig!")

    def run(self):
        if self.make == "download":
            self.download()

# Funktionen

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
    lines = ()
    output = []
    KorrigierenTNummer = 0

    if os.path.exists(outputpath):
        ERROR_MSG.ui.ERRO_MSG.setText("Achtung die Datei wurde bereits umgewandelt!")
        ERROR_MSG.show()
        return

    with open(filepath, 'r+') as f:
        lines = f.readlines()

    my_list = []

    for i in range(len(lines)-1):
        tool_list = []
        if i == 0 or i == len(lines)-1:
            continue
        if ".1" in lines[i][:5] or ".2" in lines[i][:5]:
            KorrigierenTNummer = KorrigierenTNummer + 1
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

        if MainWindow.ui.TOOL_NBR.text().isnumeric():
            if i == 1:
                tool_list.append(my_list[0] + ",") #T
            else:
                Nummer = MainWindow.ui.TOOL_NBR.text()
                Nummer = int(Nummer) + i - KorrigierenTNummer - 2
                tool_list.append(str(Nummer) + ",") #T

        tool_list.append(my_list[1] + ",")#Name

        if i == 1:
            tool_list.append(my_list[2] + ",")#L
            tool_list.append(my_list[3] + ",")#R
            tool_list.append("ACC" + ",")
            tool_list.append("AFC" + ",")
            tool_list.append("AFC-LOAD" + ",")
            tool_list.append("AFC-OVLD1" + ",")
            tool_list.append("AFC-OVLD2" + ",")
        else:
            tool_list.append(str(round(float(my_list[2]),4)) + ",")#L
            tool_list.append(str(round(float(my_list[3]),4)) + ",")#R
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
        if i == 1:
            tool_list.append(my_list[12] + ",")#DOC
        else:
            tool_list.append(my_list[35] + ",")#COMMENT
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
            tool_list.append(my_list[20] + ",")#LBREAK
            tool_list.append(my_list[22] + ",")#LCUTS
        else:
            tool_list.append("" + ",")
            tool_list.append("" + ",")
            tool_list.append(str(float(my_list[20])) + ",")#LBREAK
            tool_list.append(str(0) + ",")#LCUTS

        tool_list.append(my_list[29] + ",")#LIFTOFF
        
        if i == 1:
            tool_list.append(my_list[14] + ",")#LTOL
        else:
            tool_list.append("0" + ",")

        tool_list.append(my_list[6] + ",")#NMAX

        if i == 1:
            tool_list.append("OVRTIME" + ",")
        else:
            tool_list.append("" + ",")

        if i == 1:
            tool_list.append(my_list[30] + ",")#P1
            tool_list.append(my_list[31] + ",")#P2
            tool_list.append(my_list[32] + ",")#P3
            tool_list.append("P4" + ",")
            tool_list.append("P5" + ",")
            tool_list.append("P6" + ",")
            tool_list.append("P7" + ",")
            tool_list.append("P8" + ",")
        else:
            if float(my_list[3]) <= 80.0:
                tool_list.append(str(80) + ",")#R-TOL
            elif float(my_list[3]) >= 80.0:
                tool_list.append(str(80) + ",")#R-TOL
            elif float(my_list[3]) >= 125.0:
                tool_list.append(str(125) + ",")#R-TOL
            
            tool_list.append(my_list[31] + ",")#P2
            tool_list.append(my_list[32] + ",")#P3
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")
            tool_list.append("0" + ",")

            tool_list.append(str(int(round(float(my_list[2]),0)) + 10) + ",") #L-TOL

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
            tool_list.append(my_list[24] + "")#TYP
        else:
            if "MILL" in my_list[24]:
                tool_list.append("0" + "")#TYP
            elif "DRILL" in my_list[24]:
                tool_list.append("1" + "")#TYP
            else:
                tool_list.append("" + "")#TYP

        # tool_list.append(my_list[26] + ",")#CAL-OF1
        # tool_list.append(my_list[27] + ",")#CAL-OF12
        # tool_list.append(my_list[28] + ",")#CAL-ANG

        tool_list = "".join(tool_list)
        tool_list = tool_list + "\n"

        output.append(tool_list) # In liste schreiben

    with open(outputpath , 'w+') as f:
        for item in output:
            f.writelines(item)

# Funktionen Checkfor Update

def CheckVersion_forUpdate():
    global AktulleVersion
    # Installierte Version lesen.
    with open(pfad_updatepfad) as file:
        AktulleVersion = json.load(file)

    AktulleVersion = float(AktulleVersion["Programmversion"])
    UpdateChecker.ui.LBL_aktuelleVersion.setText(str(AktulleVersion))
    print("Aktuelle Version: " + str(AktulleVersion))

    # Neuste Version lesen.

    NeusteVersion = requests.get(url=JsonURL, headers=headersURL, params=paramURL)
    NeusteVersion = NeusteVersion.json()
    NeusteVersion = float(NeusteVersion["Programmversion"])
    UpdateChecker.ui.LBL_verfuegbareVersion.setText(str(NeusteVersion))
    print("Neuste Version: " + str(NeusteVersion))

    if AktulleVersion == NeusteVersion:
        pass
    else:
        UpdateChecker.show() # main window öffnen

# Updatechecker

if os.path.exists(TempPath) == False:
    os.makedirs(TempPath)

# Programm Code

if __name__ == "__main__":
    app= QApplication(sys.argv)
    windowIcon = QIcon(logo_Pfad)
    windowERRORIcon = QIcon(logo_ERROR_Pfad)

    UpdateChecker = UpdateChecker()
    Fortschritt_UpdateChecker = Fortschritt_UpdateChecker()    
    MainWindow = MainWindow()
    ERROR_MSG = ERROR_MSG()

    CheckVersion_forUpdate()

    MainWindow.ui.label_ProgrammVersion.setText("V" + str(AktulleVersion))
    MainWindow.show() # main window öffnen
    sys.exit(app.exec_()) # alles beenden