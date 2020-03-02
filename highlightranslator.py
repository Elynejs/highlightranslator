from googletrans import Translator
import clipboard, time
import tkinter as tk
import keyboard as kb

while True:
    try:
        #kb.wait(hotkey='ctrl+c', suppress=False, trigger_on_release=False)
        key = kb.read_hotkey()
        if (key == 'ctrl+c'):
            time.sleep(.1)
            #finding bold text
            bold_text = clipboard.paste()
            #translating
            translator = Translator()
            new_text = translator.translate(bold_text, dest='en')
            print(f'{bold_text} got translated to {new_text.text}')
            #printing message
            root = tk.Tk()
            T = tk.Text(root)
            T.pack()
            T.insert(tk.END, new_text.text)
            tk.mainloop()
    except:
        break
