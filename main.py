import tkinter as tk
from textwrap import wrap


window = tk.Tk()

window.geometry("1500x1000")

window.title("How fast can you type")

text_to_write = 'far far awaybehind the word mountains far from the countries vokalia and consonantiathere live the blind texts\n separated they live in bookmarks grove right at the coast of the semanticsa large language ocean a\n small river named duden flows by their place and supplies it with the necessary regelialia it is a paradisematic countryin which roasted parts of sentences fly into your mouth even the all-powerful pointing has no control about the blind texts it is an almost unorthographic life one day however a small line of blind text by the name of lorem ipsum decided to leave for the far world of grammar the big oxmox advised her not to do sobecause there were thousands of bad commaswild question marks and devious semikolibut the little blind text didn’t listen'

wrapped_text='\n'.join(wrap(text_to_write, width=50))

game_title = tk.Label(text="How  fast can you type\n Press the start button, start typing\n You will have 60 seconds to type as many works accurately\n good luck")
game_title.grid(column=2, row=0)

excerpt_text = tk.Text(window, width=80, height=17)#remember to change column order 

excerpt_text.grid(column=2, row=2) 

excerpt_text.insert(tk.END, wrapped_text)

enter_label = tk.Label(text="Enter here").grid(column=2, row=3)

enter_text = tk.Text(window, width=50, height=5).grid(column=2, row=4) #remember to change column order 

results_label = tk.Label(text="Results").grid(column=4, row=1)

results_text = tk.Text(window, width=50, height=5).grid(column=4, row=3) #remember to change column order 

def start_typing ():
    pass
def get_results ():
    pass

start_button = tk.Button( text ="Start", command = start_typing).grid(column=1, row=0)

results_button = tk.Button(text='Get results', command=get_results).grid(column=4, row=2)

window.mainloop()