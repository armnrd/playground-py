import sys
import requests
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout

# Replace with your Todoist API token
with open("secrets.json", "r") as file:
    secrets = json.load(file)
    API_TOKEN = secrets["todoist-token"]

class TodoistApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todoist Tasks for Today")
        self.setGeometry(100, 100, 500, 400)

        # Layout
        self.layout = QVBoxLayout()

        # Fetch today's tasks and display them
        self.tasks_label = QLabel("Fetching tasks...", self)
        self.layout.addWidget(self.tasks_label)

        # Set up the scroll area to contain the tasks
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_content.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_content)

        self.layout.addWidget(self.scroll_area)

        # Add a refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.fetch_tasks)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)

        # Fetch tasks initially
        self.fetch_tasks()

    def fetch_tasks(self):
        headers = {
            'Authorization': f'Bearer {API_TOKEN}',
        }

        # Fetch tasks for today (due today)
        params = {'filter': 'today'}
        response = requests.get("https://api.todoist.com/rest/v2/tasks", headers=headers, params=params)

        if response.status_code == 200:
            tasks = response.json()

            # Clear the layout before adding new tasks
            for i in reversed(range(self.scroll_area_layout.count())):
                widget = self.scroll_area_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            if tasks:
                for task in tasks:
                    task_label = QLabel(f"• {task['content']}", self)
                    task_label.setWordWrap(True)
                    self.scroll_area_layout.addWidget(task_label)
            else:
                self.scroll_area_layout.addWidget(QLabel("No tasks for today.", self))

        else:
            self.tasks_label.setText("Failed to fetch tasks.")
            print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoistApp()
    window.show()
    sys.exit(app.exec_())
