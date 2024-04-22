import pyautogui
import random
import time
import threading
import keyboard
import sys
import tkinter as tk
import os

pyautogui.FAILSAFE = False
center_x, center_y = 100, 100
offset_range = 200  
caminho_da_pasta_principal = 'farme'
nomes_das_pastas = next(os.walk(caminho_da_pasta_principal))[1]
pause_thread = threading.Event()  

def start_harvesting():
    global procurar
    procurar = 'sim'
    start_button.config(state=tk.DISABLED)
    pause_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.NORMAL)
    harvest_thread = threading.Thread(target=harvest_loop)
    harvest_thread.start()

def pause_harvesting():
    if pause_thread.is_set():
        pause_thread.clear() 
        pause_button.config(text="Pausar Coleta")
    else:
        pause_thread.set() 
        pause_button.config(text="Continuar Coleta")

def stop_harvesting():
    global procurar
    procurar = 'sim'
    start_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.DISABLED)
    sys.exit()  

def move_to_left():
    pyautogui.moveTo(center_x, center_y, duration=0.1)

def harvest_loop():

    while procurar == 'sim':
        try:
            if pause_thread.is_set():
                time.sleep(1)  
                continue

            fecharloot = pyautogui.locateCenterOnScreen('combate/fecharloot.png', confidence=0.8)
            if fecharloot: 
                    pyautogui.click(fecharloot.x, fecharloot.y)

            inicioCombate = pyautogui.locateCenterOnScreen('combate/inicioCombate.png', confidence=0.8)
            if inicioCombate: 
                inicio = pyautogui.locateCenterOnScreen('combate/inicio.png', confidence=0.8)
                if inicio: 
                    pyautogui.click(inicio.x, inicio.y)
                    time.sleep(2)

                    pronto = pyautogui.locateCenterOnScreen('combate/pronto.png', confidence=0.8)
                    if pronto: 
                        pyautogui.click(pronto.x, pronto.y)

            estouEmCombate = pyautogui.locateCenterOnScreen('combate/estouEmCombate.png', confidence=0.8)
            if estouEmCombate: 
                imgMeuTurno = pyautogui.locateCenterOnScreen('combate/meuturno.png', confidence=0.8)

                if imgMeuTurno: 
                    selecionaSkillRange = pyautogui.locateCenterOnScreen('combate/skillrange.png', confidence=0.8)
                    if selecionaSkillRange :
                        pyautogui.click(selecionaSkillRange.x, selecionaSkillRange.y)
                        time.sleep(1)

                        move_to_left()

                        for num in range(1, 9):
                            img_path = f'combate/personagempe{num}.png'
                            cliclaChar = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)

                            if cliclaChar:
                                pyautogui.click(cliclaChar.x, cliclaChar.y)
                                time.sleep(1)

                                move_to_left()

                    selecionaSkillDano = pyautogui.locateCenterOnScreen('combate/skilldano.png', confidence=0.8)
                    if selecionaSkillDano:
                        pyautogui.click(selecionaSkillDano.x, selecionaSkillDano.y)
                        time.sleep(1)

                        move_to_left()

                        for num in range(1, 9):
                            img_path = f'combate/personagempe{num}.png'  
                            cliclaChar = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)

                            if cliclaChar:
                                pyautogui.click(cliclaChar.x, cliclaChar.y)
                                time.sleep(1)

                                move_to_left()            

                    selecionaSkill1 = pyautogui.locateCenterOnScreen('combate/skill1.png', confidence=0.8)
                    if selecionaSkill1: 
                        pyautogui.click(selecionaSkill1.x, selecionaSkill1.y)
                        time.sleep(1)

                        move_to_left()
                        
                        for num in range(1, 24):
                            img_path = f'combate/boss{num}.png'
                            clicaBoss = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)

                            if clicaBoss:
                                pyautogui.click(clicaBoss.x, clicaBoss.y)
                                time.sleep(1)

                                move_to_left()

                    selecionaSkill2 = pyautogui.locateCenterOnScreen('combate/skill2.png', confidence=0.8)
                    if selecionaSkill2: 
                        pyautogui.click(selecionaSkill2.x, selecionaSkill2.y)
                        time.sleep(1)

                        move_to_left()
                        for num in range(1, 24):
                            img_path = f'combate/boss{num}.png'  
                            clicaBoss = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
                            if clicaBoss:
                                pyautogui.click(clicaBoss.x, clicaBoss.y)
                                time.sleep(1)

                                move_to_left()                                 
            else:                        
                for nome_pasta in nomes_das_pastas:
                    caminho_da_subpasta = os.path.join(caminho_da_pasta_principal, nome_pasta)
                    
                    for nome_arquivo in os.listdir(caminho_da_subpasta):
                        img_path = os.path.join(caminho_da_subpasta, nome_arquivo)
                        img = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
                        if img:
                            pyautogui.click(img.x, img.y)
                            time.sleep(1)

                
        except:
            time.sleep(1)
            print("ENCERRANDO PROGRAMA")
            sys.exit()

root = tk.Tk()
root.title("BOT-AUTO-FARM-DOFUS")

intro_label = tk.Label(root, text="BOT AUTO FARM DOFUS")
intro_label.pack()

start_button = tk.Button(root, text="Iniciar Coleta", command=start_harvesting)
start_button.pack()

pause_button = tk.Button(root, text="Pausar Coleta", command=pause_harvesting, state=tk.DISABLED)
pause_button.pack()

stop_button = tk.Button(root, text="Encerrar Script", command=stop_harvesting, state=tk.DISABLED)
stop_button.pack()

attention_label = tk.Label(root, text="Atenção: a pausa só se conclui após o script finalizar a sua rota")
attention_label.pack()

root.mainloop()
