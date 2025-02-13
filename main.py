import tkinter as tk
from textwrap import wrap


window = tk.Tk()

window.geometry("1000x1000")

window.title("How fast can you type")

text_to_write = 'far far awaybehind the word mountains far from the countries vokalia and consonantiathere live the blind texts\n separated they live in bookmarks grove right at the coast of the semanticsa large language ocean a\n small river named duden flows by their place and supplies it with the necessary regelialia it is a paradisematic countryin which roasted parts of sentences fly into your mouth even the all-powerful pointing has no control about the blind texts it is an almost unorthographic life one day however a small line of blind text by the name of lorem ipsum decided to leave for the far world of grammar the big oxmox advised her not to do sobecause there were thousands of bad commaswild question marks and devious semikolibut the little blind text didn’t listen'

wrapped_text='\n'.join(wrap(text_to_write, width=50))

frame_1 =tk.Frame(window).grid(column=2, row=1) #title and exerpt 

frame_2 =tk.Frame(window).grid(column=2, row=2) #enter label and text 

frame_3 =tk.Frame(window).grid(column=2, row=3) #results button and results display 


game_title = tk.Label(frame_1,text="How  fast can you type\n Press the start button, start typing\n You will have 60 seconds to type as many works accurately\n good luck")
#game_title.grid(column=1, row=0)
game_title.grid()

excerpt_text = tk.Text(frame_1, width=80, height=17)#remember to change column order 

#excerpt_text.grid(column=1, row=2) 
excerpt_text.grid()


excerpt_text.insert(tk.END, wrapped_text)

enter_label = tk.Label( frame_2,text="Enter here")
#enter_label.grid(column=1, row=3)
enter_label.grid()

enter_text = tk.Text(frame_2, width=50, height=5)
#enter_text.grid(column=1, row=4) #remember to change column order 
enter_text.grid()

def start_typing ():
    pass


start_button = tk.Button(frame_2, text ="Start", command = start_typing)
#start_button.grid(column=0, row=2)
start_button.grid()


def get_results ():
    pass
results_button = tk.Button(frame_3,text='Get results', command=get_results)
#results_button.grid(column=1, row=5)
results_button.grid()

results_text = tk.Text(frame_3, width=50, height=5)
#results_text.grid(column=1, row=6) #remember to change column order 
results_text.grid()




window.mainloop()