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
client = Groq(api_key="key")

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
        extract = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": """Extract task name and priority from the message.
                Reply ONLY in this exact format with no other text: TASKNAME|PRIORITY
                Priority must be exactly one of: High, Medium, or Low.
                If no priority mentioned use Low.
                If no specific task name found, reply exactly: UNKNOWN|Low
                Do not add any explanation. Only reply with the format above."""},
                {"role": "user", "content": user_input} 
            ]
        )

        result = extract.choices[0].message.content.strip()
        parts = result.split("|")
        if len(parts) < 2:
           addtask = "UNKNOWN"
           priority_level = "Low"
        else:
           addtask = parts[0]
           priority_level = parts[1]

        if addtask == "UNKNOWN":
            addtask = input("What task? ")
    
        if priority_level == "Low" and "low" not in user_input.lower():
            priority_input = input(f"Priority for '{addtask}'? (High/Medium/Low): ")
            priority_level = priority_input.capitalize()

        tasks.append({"task": addtask, "done": False, "priority": priority_level})
        in_progress.append({"tasks": addtask})
        print(f"✅ Added: {addtask} [{priority_level}]")
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
        if len(tasks) <= 0:
            print("No tasks available to complete")
        else:
            task_list = [t["task"] for t in tasks]
        
            # Word to index mapping
            word_to_num = {
                "first": 0, "second": 1, "third": 2, "fourth": 3,
                "fifth": 4, "sixth": 5, "seventh": 6, "eighth": 7,
                "ninth": 8, "tenth": 9, "last": -1
            }

            def find_task(user_text):
                # Check for position words
                for word, index in word_to_num.items():
                    if word in user_text.lower():
                        return tasks[index]["task"]
            
                # Check if number
                if user_text.strip().isdigit():
                    return tasks[int(user_text.strip()) - 1]["task"]
            
                # Send to AI to match
                extract = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": f"""Match the user input to a task from this list: {task_list}
                        Reply with ONLY the exact task name from the list.
                        If no match found reply UNKNOWN.
                        Do not guess. Only match if clearly mentioned."""},
                        {"role": "user", "content": user_text}
                    ]
                )
                return extract.choices[0].message.content.strip()

            # First try with original input
            matched_task = find_task(user_input)

            # If still unknown ask once and try again
            if matched_task == "UNKNOWN":
                for i, t in enumerate(tasks):
                    print(f"{i+1}. {t['task']}")
                followup = input("Which task is completed? ")
                matched_task = find_task(followup)

            # If still unknown fall back to number
            if matched_task == "UNKNOWN":
                num = int(input("Could not find that task. Enter number: ")) - 1
                matched_task = tasks[num]["task"]

            # Complete it
            for i, t in enumerate(tasks):
                if t["task"].lower() == matched_task.lower():
                    tasks[i]["done"] = True
                    isdone.append({"tasks": t["task"]})
                    if {"tasks": t["task"]} in in_progress:
                        in_progress.remove({"tasks": t["task"]})
                    print(f"✅ Completed: {t['task']}")
                    break
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