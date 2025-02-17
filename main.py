import tkinter as tk
from textwrap import wrap


window = tk.Tk()

window.geometry("1200x1000")

window.title("How fast can you type")

text_to_write = 'the european languages are members of the same family their separate existence is a myth for science  music  sport  etc  europe uses the same vocabulary the languages only differ in their grammar  their pronunciation and their \nmost common words everyone realizes why a new common language would be desirable  one could refuse to pay expensive translators to achieve this  it would be necessary to have uniform grammar  pronunciation and more common words if several languages coalesce  the grammar of the resulting language is more simple and regular than that of the individual languages the new common language will be more simple and regular than the existing european languages it will be as simple as occidental in fact  it will be occidental to an english person  it will seem like simplified english  as a sceptical cambridge friend of mine told me what occidental is the european languages are members of the same family their separate existence is a myth for science  music  sport  etc  europe uses the same vocabulary the languages only differ in their grammar  their pronunciation and their most common words everyone realizes why a new common language would be desirable  one could refuse to pay expensive translators '

wrapped_text='\n'.join(wrap(text_to_write, width=50))


game_title = tk.Label(text="How  fast can you type\n Press the start button, start typing\n You will have 60 seconds to type as many works accurately\n good luck",
bg="turquoise")

game_title.grid(column=1, row=0, pady=10)


excerpt_text = tk.Text(window, width=80, height=26)

excerpt_text.grid(column=1, row=2, pady=10, padx=50) 


excerpt_text.insert(tk.END, wrapped_text)
excerpt_text.config(state="disabled")

enter_label = tk.Label( window,text="Enter here", bg="yellow")
enter_label.grid(column=1, row=5,pady=10)


enter_text = tk.Text(window, width=80, height=5)
enter_text.grid(column=1, row=6, pady=10) 

def start_typing ():
    pass


start_button = tk.Button(window, text ="Start", command = start_typing , bg="Yellow")
start_button.grid(column=1, row=4, pady=10)

def get_results ():
    grab_entered_text = enter_text.get('1.0', 'end')
    grab_exerpt_text = excerpt_text.get('1.0', 'end')

    exerpt_list = list(grab_exerpt_text.split())
    entered_list = list(grab_entered_text.split())

    excerpt_text_length = len(exerpt_list)
    entered_text_length = len(entered_list)

    words_captured =[]
    count = 0 

    if len(entered_list) == len(exerpt_list):
        for x in entered_list:
            index_x = entered_list.index(x)
            if exerpt_list[index_x] == x:
                words_captured.append(x) # remove this or the count 
                count += 1
            print (x)
        print(count)
        print(words_captured)
       
        
    elif len(entered_list) < len(exerpt_list):
        sample_exerpt_list = exerpt_list[0:len(entered_list)]
        for x in entered_list:
            index_x = entered_list.index(x)
            if sample_exerpt_list[index_x] == x:
                words_captured.append(x) # remove this or the count 
                count += 1
            print (x)
        print(count)
        print(words_captured)
    

    elif len(entered_list) > len(exerpt_list):
        sample_entered_list = entered_list[0:len(exerpt_list)]
        for x in sample_entered_list:
            index_x = sample_entered_list.index(x)
            if exerpt_list[index_x] == x:
                words_captured.append(x) # remove this or the count 
                count += 1
            print (x)
        print(count)
        print(words_captured)


    else:
        print ("Invalid submission") 
     

    results_label = tk.Label(window, text=f"You've managed to type {count} words accurately in 1 miniute")
    results_label.grid(column=2, row=3)
    return results_label  


   
results_button = tk.Button(window,text='Get results', command=get_results, bg="green")
results_button.grid(column=2, row=2)



window.mainloop()