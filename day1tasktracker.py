import json
import sys

print(sys.version)
print("Hello! I am starting my AI journey. Documenting each progress.")
name="Maisha"
goal="AI Engineer"
print("My name is "+name+ " and my goal is to become an "+ goal +".")
print(f"My name is {name} and my goal is to become an {goal}.")
# building a small task tracker
# Load saved tasks
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []
in_progress=[]
isdone=[]
priority={}
print("=================================")
print("     Welcome to Task Tracker     ")
print("=================================")
while True:
    print("What would you like to do?")
    print("Menu Options:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Quit")
    choice = input("\nYour Choice? Enter a valid number(1-5): ")
    if(choice=="1"):
        addtask = input("Task to add:")
        while True:
            priority_task=input("What is the priority?(L/M/H)")
            if(priority_task=="L"):
                priority[addtask]= "Low"
                tasks.append({"task":addtask, "done":False, "priority":"Low"})
                break
            elif(priority_task=="M"):
                priority[addtask]= "Medium"
                tasks.append({"task":addtask, "done":False, "priority":"Medium"})
                break
            elif(priority_task=="H"):
                priority[addtask]= "High"
                tasks.append({"task":addtask, "done":False, "priority":"High"})
                break
            else:
                print(f"Invalid input, please enter a valid letter.")
        
        in_progress.append({"tasks":addtask})
        print(f"Added in tasks {addtask} priority: {priority[addtask]}")
    elif(choice=="2"):
        if (len(tasks)<=0):
            print("No tasks added")
        else:
            for i,t in enumerate(tasks):
                print(f"{i+1}.{t['task']}")
        tasklen= len(tasks)
        in_progresslen= len(in_progress)
        isdonelen=len(isdone)
        print(f"{tasklen} total tasks, {in_progresslen} tasks remaining, {isdonelen} currently done")
    elif(choice=="3"):
        if (len(tasks)<=0):
            print("No tasks available to complete")
        else:
            for i,t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            num=int(input("Which task is completed?"))-1
            tasks[num]["done"]=True
            isdone.append({"tasks": tasks[num]["task"]})
            in_progress.remove({"tasks": tasks[num]["task"]})
            print(f"Completed!!!: {tasks[num]['task']}")
    elif(choice=="4"):
        if (len(tasks)<=0):
            print("No tasks available to delete")
        else:
            for i,t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            deletetask=int(input("Which task do you want to delete?"))-1
            taskname =tasks[deletetask]["task"]
            if {"tasks": taskname} in in_progress:
                in_progress.remove({"tasks": taskname})
            if {"tasks": taskname} in isdone:
                isdone.remove({"tasks": taskname})
            del tasks[deletetask]
            for i,t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
    elif(choice=="5"):
        with open("tasks.json","w") as f:
            json.dump(tasks,f)
            print("Thank you for using task tracker! See you again!")
            break





