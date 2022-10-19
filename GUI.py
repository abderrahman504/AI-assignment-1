import tkinter as tk
from tkinter import *
from tkinter import ttk
import DFS

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
    if count < len(states):
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

def solve(algorithm, intial_state,labels):
    global success_state
    global cost
    global nodes_num
    global depth
    global run_time
    if algorithm == "DFS":
        s, p, d, n, t = DFS.dfs(intial_state)
        success_state.set(str(s))
        cost.set(str(len(p) - 1))
        depth.set(str(d))
        nodes_num.set(str(n))
        run_time.set(str(t) + " ms")
        if s:
            global scrollbar_frame
            for path in p:
                path = str(path)
                if len(path) < 9 : path = "0"+ path
                Label(scrollable_frame, text = path, font = ("Times new roman", 14)).pack()
            update(p, labels, 0)


labels = drawGrid(window)
label1 = Label(window, text = "Enter initail state:", bg = "white" ,font = ("Times new roman", 16, "bold"))
label1.place( x = 15, y = 25)
text = tk.Text(window, width=20, height=1, yscrollcommand=set(), bd=9, font=("helvetica ", 12) )
text.place(x = 180, y = 25)
solve_button = Button(window, text = "Solve", font = ("Times new roman", 16), width = 10,
                      command= lambda : solve("DFS","125340678", labels))
solve_button.place(x = 380, y = 21)
reset_button = Button(window, text = "Reset", font = ("Times new roman", 16), width = 10 )
reset_button.place(x = 520, y = 21)

#Drop List
option = ["BFS", "DFS", "A* Manhatten", "A* Euclidein"]
clicked = tk.StringVar(window)
clicked.set("Choose an Algorithim")
dropMenu = OptionMenu(window, clicked, *option)
dropMenu.place(x= 15, y=80)
dropMenu.config(font = ("Times new roman", 16), width = 55)
algorithm = clicked.get()

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
container = ttk.Frame(window)
label2 = Label(container, text = "solution steps", font = ("Times new roman", 14)).pack()
canvas = tk.Canvas(container, height= 215, width= 345)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame)
canvas.configure(yscrollcommand=scrollbar.set)
container.place(x = 300, y = 138)
container.config(width = 40, height = 40)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#s, p, d, n = algorithm(clicked, "125340678")
#success_state.set(str(s))
#cost.set(str(len(p)))
#depth.set(str(d))
#nodes_num.set(str(n))
window.mainloop()

