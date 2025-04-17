import json
from todoist_api_python.api import TodoistAPI

# Replace with your Todoist API token
with open("secrets.json", "r") as file:
    secrets = json.load(file)
    API_TOKEN = secrets["todoist-token"]

# Initialize the API client
api = TodoistAPI(API_TOKEN)

# Define the label and the text to search and replace
label = "temp"
search_text = "Jobsuche: "
replace_text = ""

try:
    # Fetch all tasks
    tasks = api.get_tasks()

    for task in tasks:
        print(f"Processing task {task.id}")
        # Check if the task has the label "Jobsuche"
        if label in task.labels:
            # Check if the task content contains the search text
            if search_text in task.content:
                # Replace the text
                updated_content = task.content.replace(search_text, replace_text)

                # Update the task content
                api.update_task(task_id=task.id, content=updated_content)
                print(f"Updated task: {task.id} -> {updated_content}")

except Exception as e:
    print(f"An error occurred: {e}")

print("Done")
