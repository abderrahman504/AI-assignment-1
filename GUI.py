import tkinter as tk
from tkinter import *
from tkinter import ttk
import DFS
import tkinter.scrolledtext as st
import bfs
window = Tk()
window.geometry('700x650')
window['bg'] = 'white'


def drawGrid(frame):
    """
    used to draw grid of 9 cells
    :param frame: fram name to draw the grid on it
    :return: arraylist of labels -label to each cell in grid-
    """
    labels = []
    for c in range(140, 380, 80):
        for r in range(15, 250, 80):
            label = Label(frame, borderwidth=2, relief="solid")
            label.place(x=r, y=c, width=80, height=80)
            labels.append(label)
    return labels


def update(states, labels, count=0):
    """
    function used to show moves visulaization

    :param states: arraylist of moves
    :param labels: arraylist of label cells
    :param count:
    :return:
    """
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
def getinversions(initial_state):
    """
    function used to count inversion num of the initail state

    :param initial_state:  input which user entered
    :return: number of inversions
    """
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if int(initial_state[i])!=0 and int(initial_state[j])!=0 and int(initial_state[i]) > int(initial_state[j]):

                inv_count =inv_count+1
    print(inv_count)
    return inv_count


def check_solvability(input):
    """
    check if the input is solvable or not
    :param input: initail stete the user entered
    :return: true or false
    """
    inversions = getinversions((input))

    # return true if inversion count is even.
    return (inversions % 2 == 0)





def solve( labels):
    """
    function to call the right algorithm which the user chose
    :param labels: labels of grid dells
    :return:
    """
    global success_state
    global cost
    global nodes_num
    global depth
    global run_time
    global reset_flag
    reset_flag = False
    algorithm = str(clicked.get())
    intial_state=text.get("1.0","end-1c")

    if(check_solvability(intial_state)==False):
        success_state.set("Your input isn't Solvable")
        return


    if algorithm == "DFS":
        s, p, d, n, t = DFS.dfs(intial_state)

    elif(algorithm=="BFS"):
        s, p, d, n, t=bfs.bfs(intial_state)
    success_state.set(str(s))
    cost.set(str(len(p) - 1))
    depth.set(str(d))
    nodes_num.set(str(n))
    run_time.set(str(t) + " ms")
    if s:
        global scrollable_frame
        i = 0

        solutionsteps = ""
        #calculate the moves needed and put it in solution steps

        for path in p:
            path = str(path)
            if len(path) < 9: path = "0" + path

            solutionsteps = solutionsteps + "\n" + path
        #text area to show steps solution
        text_area = st.ScrolledText(scrollable_frame, width=30, height=8, font=("Times New Roman", 15))
        text_area.grid(column=0, pady=10, padx=10)
        # Inserting Text which is read only
        text_area.insert(tk.INSERT, solutionsteps)
        # Making the text read only
        text_area.configure(state='disabled')
        update(p, labels, 0)



def create_stepslabel():
    """
    create label to display steps solution
    :return:
    """
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
    """
    to clear every thing after clicking reset button
    :return:
    """
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





#GUI #

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


window.mainloop()

