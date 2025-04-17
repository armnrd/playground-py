import json
from todoist_api_python.api import TodoistAPI

# Replace with your Todoist API token
with open("secrets.json", "r") as file:
    secrets = json.load(file)
    API_TOKEN = secrets["todoist-token"]

# Initialize the API client
api = TodoistAPI(API_TOKEN)

# Define the task content string to match against
content = "Resume Stuff"

try:
    # Fetch all tasks
    tasks = api.get_tasks()

    for task in [task for task in tasks if task.parent_id == '8965729277']:
        print(f"- {task.content}")
        # Update the task content
        # api.update_task(task_id=task.id, content=task.content)
        # print(f"Updated task: {task.id} -> {updated_content}")

except Exception as e:
    print(f"An error occurred: {e}")

print("Done")
