#imporamos funciones necesaias
from tkinter import *
from tkinter import ttk
#from functools import partial
from pprint import pprint as pp
from ast import literal_eval

# Estos son modulos desarollados por mi
from src.load_ensemble_data import load_ensemble_data
from src.ui import *



def d_print(string):
    if verbose == True:
        print (string)

def evt_stru_select(evt):
    print (evt)


def create_new_protein_tab(tab_parent,uniprot_id):
    tabs_dict[uniprot_id] = ttk.Frame(tab_parent)
    tab_parent.add(tabs_dict[uniprot_id],text=uniprot_id)
    tabs_abiertas.append(uniprot_id)
    secuencia = ensemble_data[uniprot_id]["Sequence"]
    create_scrolable_aa_list(tabs_dict[uniprot_id],secuencia,xx=10,yy=10,alto=50,ancho=780)
    structure_list= literal_eval(ensemble_data[uniprot_id]["PDB_CHAIN_LIST"])

    container,scrollbar,listbox,listbox_dict = create_listbox(tabs_dict[uniprot_id],structure_list,xx=20,yy=300,alto=400,ancho=100)
    listbox.bind('<<ListboxSelect>>',evt_stru_select)
    return listbox


def create_table(root,lista,xx,yy):
    container = Frame(root)
    for i,lines in enumerate(lista):
        for j,item in enumerate(lines):
            Label(container,text=item,font=monospace).grid(row=i,column=j)
    container.place(x=xx,y=yy)
    return container

# MAIN

# create standar windown
verbose = True
window = Tk()
window.title("Visualizador de ensembles")
window.geometry("800x600")
tabs_abiertas= []

#un diccionario para acceder by uniprot_id
tabs_dict = dict()
tab_parent = ttk.Notebook(window)
tab_selector = ttk.Frame(tab_parent)
tab_parent.add(tab_selector,text="Select protein")
tab_parent.pack(expand=1,fill="both")

# Load load_ensemble_data

ensemble_data,protein_labels = load_ensemble_data()

# Carga un dicionario con laa info para el listbox.

protein_list = list(ensemble_data.keys())
container1,scrollbar1,listbox1,listbox_dict1 = create_listbox(tab_selector,protein_list,xx=10,yy=10,ancho=200,alto=580)


#Define el evento de selecionar
def event_protein_select(evt):
    selected_index = evt.widget.curselection()[0]
    uniprot_id = listbox_dict1[selected_index]
    pp(ensemble_data[uniprot_id])

listbox1.bind('<<ListboxSelect>>',event_protein_select)

def click_select_btn():
    selected_index = listbox1.curselection()[0]
    if not is_none(selected_index):
        uniprot_id = listbox_dict1[selected_index]
        if not uniprot_id in tabs_dict:
            create_new_protein_tab(tab_parent,uniprot_id)

button_select =  Button(tab_selector,text="Seleccionar",command=click_select_btn)
button_select.place (x=100,y=200)

tabla_p = [[x,"N/A"] for x in protein_labels]

protein_table = create_table(tab_selector,tabla_p,xx=220,yy=5)

window.mainloop()
