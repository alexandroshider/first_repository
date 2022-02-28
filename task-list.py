task_list=[]
def add(lista):
    task_add=input('Write your task:\n')
    lista.append(task_add)
    app(lista)

def show(lista):
    print('These are your tasks\n')
    for i in range(0,len(lista)):
        print(f'{i+1}. {lista[i]}')
    if len(lista)==0:
        print('Your list is empty\n')
    app(lista)

def rem(lista):
    x=int(input('What task you want to remove?'))
    lista.pop(x)
    app(lista)

def app(tasker):
    print('This program is a task list')
    print('1. Check the tasks\n2. Add a task\n3.Remove a task\n')
    op=int(input('Select an option\n'))
    if op == 1:
        show(tasker)
    elif op == 2:
        add(tasker)
    elif op == 3:
        rem(tasker)
    else:
        print('Invalid option. Closing program')

app(task_list)

