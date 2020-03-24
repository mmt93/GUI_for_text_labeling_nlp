import pandas as pd
import tkinter as tk
from time import sleep
import random
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
os.system('chcp 65001')

temp_category = []

def save_to_file():
    df.to_csv(name,index=False)
    messagebox.showinfo("Saved!", "You fine, your progress has been saved.")

def text_displayed(value):
    result_counter = 0
    text_len = df['text'].last_valid_index()
    cat_len = df['category'].last_valid_index()
    progress_text.set('{}/{}'.format(cat_len,text_len))

    if cat_len is None:
        cat_len = 0

    else:
        result_counter = cat_len + 1

    if text_len == cat_len:
        text.set("Your entire dataset is classified!")
        save_to_file()
    else:
        text.set(df['text'].values[result_counter+1])
        record_category(result_counter, value)
        result_counter += 1

def record_category(result_counter, value):   
    df.loc[result_counter, 'category'] = value

def open_file():
    global df, name

    name = askopenfilename()
    df = pd.read_csv(name)
    
    if df['category'].last_valid_index() is not None:
        last_categorized = (df['category'].last_valid_index() + 1)
    else:
        last_categorized = 0
    
    aux = (str(df['text'].values[last_categorized]))
    text.set(aux)
    return(df)

#Windows Settings
root = tk.Tk()
root.geometry("850x800")
root.configure(background='white')
#root.grid_propagate(False)

#Text Settings
text = tk.StringVar()
open_file()
a = tk.Label(root, textvariable=text, wraplength = 700, font=("Verdana",12), width= 70)
a.grid(column=2, row=3, sticky=tk.S, columnspan=6)
a.configure(background='white')

#Declaring buttons of each category
open_csv = tk.Button(root, text="Open CSV...", command=lambda: open_file())
open_csv.grid(column=1, row=1, sticky=tk.NW)
cat_delivery = tk.Button(root, text="Entregas/Prazos", command=lambda: text_displayed(0))
cat_delivery.grid(column=1, row=2, sticky=tk.S, pady = 2)
cat_cashback = tk.Button(root, text="Cashback", command=lambda: text_displayed(1))
cat_cashback.grid(column=2, row=2, sticky=tk.S, pady = 2)
cat_il_payment = tk.Button(root, text="Cobrança/Pagamento", command=lambda: text_displayed(2))
cat_il_payment.grid(column=3, row=2, sticky=tk.S, pady = 2)
cat_warranty = tk.Button(root, text="Defeito/Garantia", command=lambda: text_displayed(3))
cat_warranty.grid(column=4, row=2, sticky=tk.S, pady = 2)
cat_cancel = tk.Button(root, text="Cancelamento", command=lambda: text_displayed(4))
cat_cancel.grid(column=5, row=2, sticky=tk.S, pady = 2)
cat_calling = tk.Button(root, text="Ligação", command=lambda: text_displayed(5))
cat_calling.grid(column=6, row=2, sticky=tk.S, pady = 2)
cat_others = tk.Button(root, text="Outros", command=lambda: text_displayed(6))
cat_others.grid(column=7, row=2, sticky=tk.S, pady = 2)
save = tk.Button(root, text="save", command=lambda: save_to_file(), bg='green', font=(None,14))
save.grid(column=8, row=1, sticky=tk.SE)

#Progress info
progress_text = tk.StringVar()
progress = tk.Label(root, textvariable=progress_text, wraplength = 800, font=(None,14))
progress.grid(column=2, row=4, sticky=tk.S)
progress.configure(background='white')
#Play
root.mainloop()
