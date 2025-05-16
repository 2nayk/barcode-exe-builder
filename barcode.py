# test
import keyboard
import time
import pyperclip
import pyautogui

buffer = ""

def on_key(event):
    global buffer
    if event.name == 'enter':
        if len(buffer) >= 9:
            trimmed = buffer[8:]  # 先頭から8文字を除いた部分を抽出
            pyperclip.copy(trimmed)
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')
        buffer = ""
    elif len(event.name) == 1:
        buffer += event.name
    elif event.name == 'space':
        buffer += ' '

keyboard.on_press(on_key)
print("バーコード読み取り待機中。ESCを3回押すと終了します。")
keyboard.add_hotkey('esc, esc, esc', lambda: exit())
keyboard.wait()
