from googletrans import Translator
import clipboard, time
import tkinter as tk
import keyboard as kb

while True:
    try:
        kb.wait(hotkey='ctrl+c', suppress=False, trigger_on_release=False)
        time.sleep(.1)
        #finding bold text
        bold_text = clipboard.paste()
        #translating
        translator = Translator()
        new_text = translator.translate(bold_text, dest='en')
        print(f'{bold_text} got translated to {new_text.text}')
        #printing message
        root = tk.Tk()
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=8, width=50)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.insert(tk.END, new_text.text)
        tk.mainloop()
    except:
        break
