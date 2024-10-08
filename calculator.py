import tkinter 
from tikender import*

root=tk()
root.title("Simple calculator")
root.geomatry("570*600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

label_result=label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()
Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5".place(x=10,y=100))
