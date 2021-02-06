from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer
from icongen import vectorMeter
from info import cpu
import psutil
  
app = QApplication([]) 
app.setQuitOnLastWindowClosed(False) 
print("initapp") 
# Adding an icon 
icon = QIcon(vectorMeter.foo(50))
print(icon)
# Adding item on the menu bar 
tray = QSystemTrayIcon() 
tray.setIcon(icon) 
tray.setVisible(True) 
print("inittray")
# Creating the options 
menu = QMenu() 
option1 = QAction("Geeks for Geeks") 
option2 = QAction("GFG") 
menu.addAction(option1) 
menu.addAction(option2) 
print("initmenu")
# To quit the app 
quit = QAction("Quit") 
quit.triggered.connect(app.quit) 
menu.addAction(quit) 
  
# Adding options to the System Tray 
tray.setContextMenu(menu) 


# Adding item on the menu bar 
tray2 = QSystemTrayIcon() 
tray2.setIcon(icon) 
tray2.setVisible(True) 
print("inittray")
# Creating the options 
menu2 = QMenu() 
option12 = QAction("Geeks for Geeks") 
option22 = QAction("GFG") 
menu2.addAction(option12) 
menu2.addAction(option22) 
print("initmenu")
# To quit the app 
quit2 = QAction("Quit") 
quit2.triggered.connect(app.quit) 
menu2.addAction(quit2) 
  
# Adding options to the System Tray 
tray2.setContextMenu(menu2) 


print("exec")
i = 0

def updateIcon():
    tray.setIcon(QIcon(vectorMeter.foo(cpu.getNodeN(2), 32)))
    print("CPU USAGE "+ str(cpu.getNodeN(2)), " PSUTIL ", psutil.cpu_percent())

timer = QTimer()
timer.timeout.connect(updateIcon)
timer.start(1000)
app.exec_() 