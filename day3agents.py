import json
from groq import Groq

# Load tasks
try:
    with open("mytasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

in_progress = []
isdone = []
priority = {}

# Set up Groq
client = Groq(api_key="groq_api")

print("=================================")
print("   Welcome to AI Task Tracker!   ")
print("=================================")
print("Just type what you want to do!")

while True:
    user_input = input("\nWhat is it that you want to do now: ")

    # Asking Groq what the user wants to do
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": """You are a task tracker assistant. 
            Based on the user's message, reply with ONLY one word:
            ADD - if they want to add a task
            VIEW - if they want to see tasks
            COMPLETE - if they want to complete a task
            DELETE - if they want to delete a task
            QUIT - if they want to quit
            Reply with ONLY the one word, nothing else."""},
            {"role": "user", "content": user_input}
        ]
    )

    command = response.choices[0].message.content.strip()
    print(f"AI understood: {command}")

    if command == "ADD":
        # existing add code here
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
        pass
    elif command == "VIEW":
        #existing view code here
        if (len(tasks)<=0):
            print("No tasks added")
        else:
            for i,t in enumerate(tasks):
                print(f"{i+1}.{t['task']}")
        tasklen= len(tasks)
        in_progresslen= len(in_progress)
        isdonelen=len(isdone)
        print(f"{tasklen} total tasks, {in_progresslen} tasks remaining, {isdonelen} currently done")
        pass
    elif command == "COMPLETE":
        #existing complete code here
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
        pass
    elif command == "DELETE":
        #existing delete code here
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
        pass
    elif command == "QUIT":
        #existing quit code here
        with open("mytasks.json","w") as f:
            json.dump(tasks,f)
            print("Thank you for using task tracker! See you again!")
            break
        pass