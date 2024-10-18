import PySimpleGUI as sg
sg.theme("DarkGrey9") 
window = sg.Window(title="Latihan pertama", layout=[
    [sg.Text("NPM      : 2210010472 ")],
    [sg.Text("Nama     : Muhammad Malik Akbar ")],
    [sg.Text("Kelas     : 5N Regular Banjarmasin ")],
    [sg.Text("Matkul    : Pemograman Visual 3 ")],
    
    ],size=(400,200))
window()
window.close()