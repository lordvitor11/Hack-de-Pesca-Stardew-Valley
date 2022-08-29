import PySimpleGUI as sg;

layout = [[sg.Text("Escolha a vara de pesca que você está utilizando:")],
          [sg.Button("Sair")]];

mainWindow = sg.Window("Hack Stardew Valley", layout);

while (True):
    event, values = mainWindow.read();
    if (event == sg.WIN_CLOSED or event == "Sair"):
        break;

mainWindow.close();
