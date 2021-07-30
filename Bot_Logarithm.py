import math
import ctypes
import time
import pandas as pd
import pyautogui as GUI

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

df = pd.read_csv('tuman.csv')

dict = []
harga_reg = 250000

#murid agus
n = len(df)
for j in range(n):
    tem = {}
    tem1 = []
    if not(math.isnan(df.Total_Pertemuan_Agus[j])):
        print(j)
        tem['guru'] = 'Agus'
        tem['nama'] = df['Full name'][j]
        tem['no_telp_ortu'] = df['Parent\'s phone number'][j]
        for i in range(1, int(df.Total_Pertemuan_Agus[j])+1):
            tem1.append(int(df[str(i)][j]))
        tem['tanggal'] = ', '.join(str(e) for e in tem1)
        dict.append(tem)

#murid anton
n = len(df)
for j in range(n):
    tem = {}
    tem1 = []
    if not(math.isnan(df.Total_Pertemuan_Anton[j])):
        print(j)
        tem['guru'] = 'Anton'
        tem['nama'] = df['Full name'][j]
        tem['no_telp_ortu'] = df['Parent\'s phone number'][j]
        for i in range(21, int(df.Total_Pertemuan_Anton[j])+21):
            tem1.append(int(df[str(i)][j]))
        tem['tanggal'] = ', '.join(str(e) for e in tem1)
        dict.append(tem)

#murid yohanes
n = len(df)
for j in range(n):
    tem = {}
    tem1 = []
    if not(math.isnan(df.Total_Pertemuan_yohanes[j])):
        print(j)
        tem['guru'] = 'Yohanes'
        tem['nama'] = df['Full name'][j]
        tem['no_telp_ortu'] = df['Parent\'s phone number'][j]
        for i in range(41, int(df.Total_Pertemuan_yohanes[j])+41):
            tem1.append(int(df[str(i)][j]))
        tem['tanggal'] = ', '.join(str(e) for e in tem1)
        dict.append(tem)
for i in dict:
    if i['nama']:
        pass
print(dict)

#bot starts here
GUI.FAILSAFE = True
GUI.PAUSE = 1

# GUI.press('win')
# GUI.typewrite('WhatsApp')
# GUI.press('enter')
# time.sleep(2)
# user32 = ctypes.WinDLL('user32')
# SW_MAXIMISE = 3
# hWnd = user32.GetForegroundWindow()
# user32.ShowWindow(hWnd, SW_MAXIMISE)
# time.sleep(5)

Mbox('Alert !!!', 'Click Ok when you have successfully logged in to your WhatsApp account', 1)

for i in dict:
    total = len(i['tanggal'].split(', ')) * harga_reg
    text = 'Selamat malam orang tua dari ' + str(i['nama']) + '.' + ' Bulan lalu, ' + str(i['nama']) + ' ada pertemuan dengan ko ' + str(i['guru']) + ' pada tanggal ' + str(i['tanggal']) + '. Total biaya les pada bulan tersebut adalah ' + str(total) + '. Terimakasih.'
    print(text)
    # GUI.click(x=186, y=167)
    # GUI.typewrite(str(i['no_telp_ortu']))
    # GUI.click(x=926, y=973)
    # GUI.typewrite(text)
    # GUI.press('enter')
