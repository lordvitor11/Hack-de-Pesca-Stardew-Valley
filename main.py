import keyboard;
# from pynput.keyboard import Key, Listener;
# import time;
import PySimpleGUI as sg;
import pyautogui as pg;

# def setLanguage(lang):
#     global language, layout2;
#     language = langList[lang];

#     if (language == "pt-br"):
#         layout2 = [[sg.Text("Escolha a vara de pesca que você está utilizando:")],
#                    [sg.Combo(["Vara de treinamento", "Vara de bambu", "Vara de fibra de vidro", "Vara de irídio"], default_value="Vara de bambu")],
#                    [sg.Button("Sair")]];
#     elif (language == "pt"):
#         layout2 = [[sg.Text("Escolha a cana de pesca que está a usar:")],
#                    [sg.Combo(["Vara de treinamento", "Vara de bambu", "Vara de fibra de vidro", "Vara de irídio"], default_value="Vara de bambu")],
#                    [sg.Button("Sai")]];
#     elif (language == "en"):
#         layout2 = [[sg.Text("Choose the fishing rod you are using:")],
#                    [sg.Combo(["Training rod", "Bamboo pole", "Fiberglass rod", "Iridium rod"], default_value="Bamboo Pole")],
#                    [sg.Button("Exit")]];

# language = "";

# langList = {"Português do Brasil":"pt-br", "Português de Portugal":"pt", "English":"en"};

# Language layout
# layout1 = [[sg.Text("Select your language:")],
#            [sg.Combo(["Português do Brasil", "Português de Portugal", "English"], default_value="English", key="comboLang")],
#            [sg.Button("Confirm")]];

# layout2 = [];

# # Layout manager
# layout = [[sg.Column(layout1, key="COL1")],
#           [sg.Column(layout2, key="COL2", visible=False)]];

keys = []
def show(key):
    global keys;
    keys.append(key);
    print(keys)
    if (len(keys) == 3):
        del keys[0];
    else:
        if (keys[0] == Key.ctrl and keys[1] == "j"):
            pg.mouseDown(button=left, duration=2);
            # time.sleep(2);
            # pg.mouseUp();

layout = [[sg.Text("Choose the fishing rod you are using:")],
          #[sg.Combo(["Training rod", "Bamboo pole", "Fiberglass rod", "Iridium rod"], default_value="Bamboo Pole")],
          [sg.Button("Exit")]];

mainWindow = sg.Window("Hack Stardew Valley", layout);

# layout = 1;

while (True):
    event, values = mainWindow.read();
    if (event == sg.WIN_CLOSED or event == "Sair"):
        break;

    while (True):
        if (keyboard.is_pressed("q")):
            print("a")

    # with Listener(on_press = show) as listener:
    #     listener.join();
    
    # if (event == "Confirm"):
    #     setLanguage(values["comboLang"]);
    #     mainWindow[f"COL{layout}"].update(visible=False);
    #     layout += 1;
    #     mainWindow[f"COL{layout}"].update(visible=True);

mainWindow.close();
