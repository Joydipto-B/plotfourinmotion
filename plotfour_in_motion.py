import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)
btn=[]
N=8
arr=[0]*N
p=0
sfflag=0
mv=0
rows=6
cols=7
arr2=[['A' for _ in range(cols)] for _ in range(rows)]
m4='A'
chk=0

def update_state_char(m3,am,an,my_oval1):
    abc=0
    arr2[am][an]=m3
    for rowbr in arr2:
        print(rowbr)

        for x in range(6):
            for y in range(7):
                if (arr2[x][y]==arr2[x-1][y]) and (arr2[x][y]==arr2[x-2][y]) and (arr2[x][y]==arr2[x-3][y]) and (arr2[x][y]!='A'):

                    print(arr2[x][y], " won vertically")
                    abcx=x
                    abcy=y
                    abc=1
        if abc==1 and abcx==0:
                     
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((2+abcx)), 77.5+45*(abcy), 102.5+45*(2+abcx), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((3+abcx)), 77.5+45*(abcy), 102.5+45*((3+abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((4+abcx)), 77.5+45*(abcy), 102.5+45*((4+abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((5+abcx)), 77.5+45*(abcy), 102.5+45*((5+abcx)), fill="green",tags="circle")
            abc=0
        elif abc==1 and abcx!=0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-1)), 77.5+45*(abcy), 102.5+45*(abcx-1), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-2)), 77.5+45*(abcy), 102.5+45*((abcx-2)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-3)), 77.5+45*(abcy), 102.5+45*((abcx-3)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-4)), 77.5+45*(abcy), 102.5+45*((abcx-4)), fill="green",tags="circle")
            abc=0

        for y in range(7):
            for x in range(6):
                if ((arr2[x][y]==arr2[x][y-1]) and (arr2[x][y]==arr2[x][y-2]) and (arr2[x][y]==arr2[x][y-3]) and (arr2[x][y]!='A')):

                    print(arr2[x][y], " won horizontally")
                    abcx=x
                    abcy=y
                    abc=1

        if abc==1 and abcx==0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx+5)), 77.5+45*(abcy), 102.5+45*((abcx+5)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-1), 67.5+45*((abcx+5)), 77.5+45*(abcy-1), 102.5+45*((abcx+5)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-2), 67.5+45*((abcx+5)), 77.5+45*(abcy-2), 102.5+45*((abcx+5)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-3), 67.5+45*((abcx+5)), 77.5+45*(abcy-3), 102.5+45*((abcx+5)), fill="green",tags="circle")
            abc=0

        elif abc==1 and abcx!=0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx)), 77.5+45*(abcy), 102.5+45*((abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-1), 67.5+45*((abcx)), 77.5+45*(abcy-1), 102.5+45*((abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-2), 67.5+45*((abcx)), 77.5+45*(abcy-2), 102.5+45*((abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-3), 67.5+45*((abcx)), 77.5+45*(abcy-3), 102.5+45*((abcx)), fill="green",tags="circle")
            abc=0


        for y in range(4):
            for x in range(6):
                if ((arr2[x][y]==arr2[x-1][y+1]) and (arr2[x][y]==arr2[x-2][y+2]) and (arr2[x][y]==arr2[x-3][y+3]) and (arr2[x][y]!='A')):

                    print(arr2[x][y], " won diagonally a")
                    abcx=x
                    abcy=y
                    abc=1
        if abc==1 and abcx!=0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-1)), 77.5+45*(abcy), 102.5+45*((abcx-1)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+1), 67.5+45*((abcx-2)), 77.5+45*(abcy+1), 102.5+45*((abcx-2)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+2), 67.5+45*((abcx-3)), 77.5+45*(abcy+2), 102.5+45*((abcx-3)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+3), 67.5+45*((abcx-4)), 77.5+45*(abcy+3), 102.5+45*((abcx-4)), fill="green",tags="circle")
            abc=0

        if abc==1 and abcx==0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx+5)), 77.5+45*(abcy), 102.5+45*((abcx+5)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+1), 67.5+45*((abcx+4)), 77.5+45*(abcy+1), 102.5+45*((abcx+4)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+2), 67.5+45*((abcx+3)), 77.5+45*(abcy+2), 102.5+45*((abcx+3)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+3), 67.5+45*((abcx+2)), 77.5+45*(abcy+3), 102.5+45*((abcx+2)), fill="green",tags="circle")
            abc=0

        for y in range(7):
            for x in range(6):
                if ((arr2[x][y]==arr2[x-1][y-1]) and (arr2[x][y]==arr2[x-2][y-2]) and (arr2[x][y]==arr2[x-3][y-3]) and (arr2[x][y]!='A')):

                    print(arr2[x][y], " won diagonally b")
                    abcx=x
                    abcy=y
                    abc=1
        if abc==1 and abcx!=0:
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx-1)), 77.5+45*(abcy), 102.5+45*((abcx-1)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+1), 67.5+45*((abcx)), 77.5+45*(abcy+1), 102.5+45*((abcx)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+2), 67.5+45*((abcx+1)), 77.5+45*(abcy+2), 102.5+45*((abcx+1)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy+3), 67.5+45*((abcx+2)), 77.5+45*(abcy+3), 102.5+45*((abcx+2)), fill="green",tags="circle")
            abc=0

        if abc==1 and abcx==0:
            my_oval1=canvas.create_oval(42+45*(abcy-3), 67.5+45*((abcx+2)), 77.5+45*(abcy-3), 102.5+45*((abcx+2)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-2), 67.5+45*((abcx+3)), 77.5+45*(abcy-2), 102.5+45*((abcx+3)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy-1), 67.5+45*((abcx+4)), 77.5+45*(abcy-1), 102.5+45*((abcx+4)), fill="green",tags="circle")
            my_oval1=canvas.create_oval(42+45*(abcy), 67.5+45*((abcx+5)), 77.5+45*(abcy), 102.5+45*((abcx+5)), fill="green",tags="circle")
            abc=0

def deletion_circle():

    global arr
    global arr2
    canvas.delete("circle")
    arr=[0]*N
    arr2=[['A' for _ in range(cols)] for _ in range(rows)]

def move_oval(button_id):

        for m in range(len(btn)+1):

            if m==button_id:
                global p
                global m4
                global arr2
                global chk

                p=sum(arr)

                if arr2[0][m-1]!='A' and arr2[1][m-1]!='A' and arr2[2][m-1]!='A' and arr2[3][m-1]!='A' and arr2[4][m-1]!='A' and arr2[5][m-1]!='A':
                        
                    chk=1
                
                if chk==0:

                    if p%2==0:
                        my_oval=canvas.create_oval(42+45*(m-1), 53, 77.5+45*(m-1), 87, fill="red",tags="circle")
                        m4='R'
                    elif p%2==1:
                        my_oval=canvas.create_oval(42+45*(m-1), 53, 77.5+45*(m-1), 87, fill="blue",tags="circle")
                        m4='B'
            


                for i in range(16+3*arr[m]):
                    canvas.move(my_oval,0,15)
                    root.update()
                    root.after(100)
                
                if chk==0:

                    
                    m2=m-1
                    n2=arr[m]
                    arr[m]=arr[m]-1
                    
                    update_state_char(m4,n2,m2,my_oval)

                else:
                    chk=0

k=0



for j in range(7):

    k=k+1
    button=tk.Button(root,text="",width=4,height=1, command=lambda l=k: move_oval(l))    
    button.place(x=42.5+(45*j),y=35)
    btn.append(button)

    for i in range(6):
       
        if i<1:
            canvas.create_rectangle(42+45*j, 67.5+45*(i), 77.5+45*j, 102.5+45*(i), outline="black",fill="lightyellow")
        
        elif i>=1 and i<3:
            canvas.create_rectangle(42+45*j, 67.5+45*(i), 77.5+45*j, 102.5+45*(i), outline="black",fill="lightgreen")

        elif i>=3:
            canvas.create_rectangle(42+45*j, 67.5+45*(i), 77.5+45*j, 102.5+45*(i), outline="black",fill="lightblue")

button1=tk.Button(root,text="Refresh", width=8, height=1, command= deletion_circle)

button1.place(x=42.5+(45*2.7),y=5)


root.mainloop()
