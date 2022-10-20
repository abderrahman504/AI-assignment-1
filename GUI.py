import tkinter as tk
from tkinter import *
from tkinter import ttk
import DFS
import tkinter.scrolledtext as st

window = Tk()
window.geometry('700x650')
window['bg'] = 'white'


def drawGrid(frame):
    labels = []
    for c in range(140, 380, 80):
        for r in range(15, 250, 80):
            label = Label(frame, borderwidth=2, relief="solid")
            label.place(x=r, y=c, width=80, height=80)
            labels.append(label)
    return labels


def update(states, labels, count=0):
    if(reset_flag):
        for i in range(9):
            labels[i].config(text=' ')

    elif count < len(states) and reset_flag==False:
        state = states[count]
        state = str(state)
        if len(state) < 9 :
            state = "0" + state
        for i in range(9):
            if state[i] == '0':
                labels[i].config(text=' ')
            else:
                labels[i].config(text=state[i], font=("Arial", 25))
        window.after(300, update, states, labels, count + 1)






def solve( labels):
    global success_state
    global cost
    global nodes_num
    global depth
    global run_time
    global reset_flag
    reset_flag = False
    algorithm = str(clicked.get())
    intial_state=text.get("1.0","end-1c")
    print(intial_state)
    print(algorithm)
    if algorithm == "DFS":
        s, p, d, n, t = DFS.dfs(intial_state)
        success_state.set(str(s))
        cost.set(str(len(p) - 1))
        depth.set(str(d))
        nodes_num.set(str(n))
        run_time.set(str(t) + " ms")
        if s:
            global scrollable_frame
            i=0

            solutionsteps=""


            for path in p:
                path = str(path)
                if len(path) < 9 : path = "0"+ path

                solutionsteps=solutionsteps+"\n"+path


            text_area = st.ScrolledText(scrollable_frame, width=30, height=8, font=("Times New Roman", 15))

            text_area.grid(column=0, pady=10, padx=10)

            # Inserting Text which is read only
            text_area.insert(tk.INSERT, solutionsteps)

            # Making the text read only
            text_area.configure(state='disabled')





            update(p, labels, 0)


labels = drawGrid(window)
label1 = Label(window, text = "Enter initail state:", bg = "white" ,font = ("Times new roman", 16, "bold"))
label1.place( x = 15, y = 25)
text = tk.Text(window, width=20, height=1, yscrollcommand=set(), bd=9, font=("helvetica ", 12) )
text.place(x = 180, y = 25)

solve_button = Button(window, text = "Solve", font = ("Times new roman", 16), width = 10,
                      command= lambda : solve( labels))
solve_button.place(x = 380, y = 21)
reset_button = Button(window, text = "Reset",command= lambda : reset(), font = ("Times new roman", 16), width = 10 )
reset_button.place(x = 520, y = 21)

#Drop List
option = ["BFS", "DFS", "A* Manhatten", "A* Euclidein"]
clicked = tk.StringVar(window)
clicked.set("Choose an Algorithim")
dropMenu = OptionMenu(window, clicked, *option)
dropMenu.place(x= 15, y=80)
dropMenu.config(font = ("Times new roman", 16), width = 55)


#Results Labels
success_state  = StringVar(window , "")
nodes_num = StringVar(window , "")
depth = StringVar(window , "")
run_time = StringVar(window , "")
cost = StringVar(window , "")

Label(window, text ="Success: ", font = ("Times new roman", 16, "bold"),
      bg = "white").place(x = 15, y =410)
success_label = Label(window, bg = "white",  textvariable = success_state,
                      font = ("Times new roman", 16))
success_label.place(x = 95, y = 410)

Label(window, text = "Cost: ", font = ("Times new roman", 16, "bold"),
      bg = "white").place(x = 15, y = 440)
cost_label = Label(window, bg = "white",  textvariable = cost,
                      font = ("Times new roman", 16))
cost_label.place(x = 70, y = 440)

Label(window, text = "Nodes Expaned: ", font = ("Times new roman", 16, "bold"),
      bg = "white").place(x = 15, y = 470)
node_label = Label(window, bg = "white",  textvariable = nodes_num,
                      font = ("Times new roman", 16))
node_label.place(x = 165, y = 470)

Label(window, text = "Depth: ", font = ("Times new roman", 16, "bold"),
      bg = "white").place(x = 15, y = 500)
depth_label = Label(window, bg = "white",  textvariable = depth,
                      font = ("Times new roman", 16))
depth_label.place(x = 80, y = 500)
Label(window, text = "Runtime: ", font = ("Times new roman", 16, "bold"),
      bg = "white").place(x = 15, y = 530)
time_label = Label(window, bg = "white",  textvariable = run_time,
                      font = ("Times new roman", 16))
time_label.place(x = 105, y = 530)

#Steps Frame
#reset_flag=False
#container = ttk.Frame(window)
#label2 = Label(container, text = "solution steps", font = ("Times new roman", 14)).pack()
#canvas = tk.Canvas(container, height= 215, width= 345)
#scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
#scrollable_frame = ttk.Frame(canvas)


def create_stepslabel():
    global scrollable_frame
    reset_flag = False
    container = ttk.Frame(window)
    label2 = Label(container, text="solution steps", font=("Times new roman", 14)).pack()
    canvas = tk.Canvas(container, height=215, width=345)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame)
    canvas.configure(yscrollcommand=scrollbar.set)
    container.place(x=300, y=138)
    container.config(width=40, height=40)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

create_stepslabel()
def reset():
    success_state.set("")
    nodes_num.set("")
    cost.set("")
    run_time.set("")
    depth.set("")
    text.delete("1.0","end-1c")
    clicked.set("Choose an Algorithim")
    global scrollable_frame
    global reset_flag
    reset_flag=True
    update([],labels,0)
    scrollable_frame.destroy()
    #scrollable_frame = ttk.Frame(canvas)
    create_stepslabel()



#s, p, d, n = algorithm(clicked, "125340678")
#success_state.set(str(s))
#cost.set(str(len(p)))
#depth.set(str(d))
#nodes_num.set(str(n))
window.mainloop()

