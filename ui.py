from tkinter import *
from tkinter import ttk
from functools import partial
from pprint import pprint as pp


def is_none(variable):
    if type(variable)==type(None):
        return True
    else:
        return False

def create_scrolable_vertical(root,lista=[],xx=0,yy=0,ancho=200,alto=300):
    container = ttk.Frame(root)
    canvas = Canvas(container,width=ancho,height=alto)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    for index,items in enumerate(lista):
        ttk.Label(scrollable_frame, text=str(index) + " Sample scrolling label").pack()

    container.place(x=xx,y=yy)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return [container,canvas,scrollbar,scrollable_frame]


#esto crea la lista de aminoacidos
def create_scrolable_aa_list(root,lista=[],xx=10,yy=10,ancho=5800,alto=200):
    container = ttk.Frame(root)
    canvas = Canvas(container,width=ancho,height=alto,bg="#aaaaff")
    scrollbar = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)


    def click_aa(index):
        print ("clicked aa",index)
        pass

    for index,items in enumerate(lista):
        x = Button(scrollable_frame,text=items,padx=5,pady=3,font=('Liberatarion Mono',9),command=partial(click_aa,index))
        x.pack(side="left")

    #fija el cotainer en las cordenadas xx yy
    container.place(x=xx,y=yy)
    canvas.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="bottom", fill="x" )

    return [container,canvas,scrollbar,scrollable_frame]




def onselect(evt):
    print ("Hi",evt)
    #print (dir(evt))
    pp(dir(evt.widget))

def create_listbox(root,list = ["Example 1","Example2"],xx=0,yy=0,ancho=200,alto=300):
    container = ttk.Frame(root)
    sample_listbox = Listbox(container,exportselection=0)
    listbox_dict = dict()
    for index,element in enumerate(list):
        #protein_dict[index] = [uniprot_id,ensemble_data[uniprot_id]["Sequence"]]
        listbox_dict[index] = element
        sample_listbox.insert(index,element)
    scrollable_frame =""# ttk.Frame(sample_listbox)
    #canvas = Canvas(container,width=ancho,height=alto)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=sample_listbox.yview)

    """
    scrollable_frame.bind(
        "<Configure>",
        lambda e:  sample_listbox.configure(
            scrollregion=sample_listbox.bbox("all")
        )
    )
    """
    #canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    sample_listbox.configure(yscrollcommand=scrollbar.set)


    scrollbar.pack(side="right", fill="y")
    sample_listbox.pack(fill="y")
    container.place(x=xx,y=yy)

    return container,scrollbar,sample_listbox,listbox_dict








#https://blog.tecladocode.com/tkinter-scrollable-frames/
#https://stackoverflow.com/questions/45122244/having-frames-next-to-each-other-in-tkinter
"""
root = Tk()
root.title("Root papa")
root.configure(bg="grey80")
root.geometry("800x600")

vertical_scroll = create_scrolable_vertical(root,list=list(range(0,50)),xx=10,yy=10)

vertical_scroll2 = create_listbox(root,list=list(range(0,25)),xx=250,yy=10)

root.mainloop()
"""
