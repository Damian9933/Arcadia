import PySimpleGUI as sg
import random
sg.theme("DarkPurple1")

layout_principal = [
    [sg.Text("Bienvenido a Arcadia")],
    [sg.Stretch(),sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'),sg.Stretch()],
    [sg.Stretch(), sg.Button("Iniciar",size = (7, 2),button_color = ("black", "#F80DD1")), sg.Stretch()]
]
window_principal = sg.Window("Arcadia", layout_principal)

layout = [  
            [sg.Stretch(), sg.Text("Haga click para jugar "), sg.Stretch()],
            [sg.Stretch(), sg.Button("Piedra - papel - tijera", size = (40, 3),button_color = ("black", "#F80DD1")), sg.Stretch()],
            [sg.Stretch(), sg.Button("Exit", size = (40, 3),button_color = ("black", "#F8340D")), sg.Stretch()]
            ]
window = sg.Window("Arcadia", layout)

reinicio = False
usuario = 0 
imagenes = ["piedra.png", "papel.png", "tijera.png"]

layout2 = [
            [sg.Button(key = "-USUARIO-", image_filename = imagenes[0]), 
            sg.Button("Jugar!", size = (12, 5),button_color = ("black", "#F80DD1"), key = "-JUGAR-"), 
            sg.Image(key = "-COMPUTADORA-", size = (180, 140))]
            ]
Window = sg.Window("Piedra - Papel - Tijera", layout2)

while True:
    event, values = window_principal.read(timeout=100)
    window_principal['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
    
    if event == sg.WIN_CLOSED:
        break 
    
    if event == "Iniciar":
        window_principal.close()
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        
        if event == "Piedra - papel - tijera":
            while True:
                event, values = Window.read()
            
                if event == sg.WIN_CLOSED:
                    break
            
                # Control del boton del jugador 
                if event == "-USUARIO-":
                    if not reinicio:
                        usuario = (usuario + 1) % 3  
                        Window["-USUARIO-"].update(image_filename = imagenes[usuario])
                        
                # Control del boton Jugar!
                if event == "-JUGAR-":
                    
                    # Si no dice reinicio juega la computadora
                    if not reinicio:
                        computadora = random.randint(0, 2)
                        Window["-COMPUTADORA-"].update(filename = imagenes[computadora])
                        Window["-JUGAR-"].update("Reiniciar")
                        
                        # resultados
                        if usuario == computadora: # Empate
                            Window["-JUGAR-"].update(button_color = ("black", "yellow"))
                            
                        elif usuario == 0: # El jugador tiene piedra 
                            if computadora == 1: # La computadora tiene papel
                                Window["-JUGAR-"].update(button_color = ("black", "red"))
                            elif computadora == 2: # La computadora tiene tijera
                                Window["-JUGAR-"].update(button_color = ("black", "green"))
                
                        elif usuario == 1: # El jugador tiene papel 
                                    if computadora == 0: # La computadora tiene piedra
                                        Window["-JUGAR-"].update(button_color = ("black", "green"))
                                    elif computadora == 2: # La computadora tiene tijera
                                        Window["-JUGAR-"].update(button_color = ("black", "red"))
                                        
                        elif usuario == 2: # El jugador tiene tijera
                                    if computadora == 0: # La computadora tiene piedra
                                        Window["-JUGAR-"].update(button_color = ("black", "red"))
                                    elif computadora == 1: # La computadora tiene papel
                                        Window["-JUGAR-"].update(button_color = ("black", "green"))
                                        
                    # si dice reinicio se va a reiniciar el juego 
                    else:
                        Window["-JUGAR-"].update("JUGAR!", button_color = ("black","#F80DD1"))
                        Window["-USUARIO-"].update(image_filename = imagenes[0])
                        Window["-COMPUTADORA-"].update(filename = None)
                        
                    # Se intercambia el valor reinicio
                    reinicio = not reinicio 

window.close()
Window.close() 

sg.popup("Gracias por jugar!", button_color = ("black", "#F80DD1"), text_color = "white")