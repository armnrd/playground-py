# Code you have previously used to load data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import os
import folium
import numpy as np
import matplotlib.pyplot as plt

def main_1():
    # Path of the file to read
    iowa_file_path = 'data/melb_data.csv'

    home_data = pd.read_csv(iowa_file_path)
    # Create target object and call it y
    y = home_data.Price
    # Create X
    features = ['Rooms', 'Landsize', 'BuildingArea', 'YearBuilt']
    X = home_data[features]

    # Split into validation and training data
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    # Specify Model
    iowa_model = DecisionTreeRegressor(random_state=1)
    # Fit Model
    iowa_model.fit(train_X, train_y)


    # Make validation predictions and calculate mean absolute error
    val_predictions = iowa_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

    # Using best value for max_leaf_nodes
    iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
    iowa_model.fit(train_X, train_y)
    val_predictions = iowa_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

def main_2():
    # Create a map centered around Berlin
    berlin_map = folium.Map(location=[52.52, 13.405], zoom_start=12)

    # Add library locations
    libraries = [
        {"name": "Staatsbibliothek zu Berlin (Potsdamer Straße)", "location": [52.509644, 13.368413]},
        {"name": "Staatsbibliothek zu Berlin (Unter den Linden)", "location": [52.517602, 13.391717]},
        {"name": "Amerika-Gedenkbibliothek", "location": [52.496365, 13.393049]},
        {"name": "Philologische Bibliothek", "location": [52.454768, 13.287458]},
        {"name": "Jacob-und-Wilhelm-Grimm-Zentrum", "location": [52.520301, 13.393508]},
        {"name": "Zentral- und Landesbibliothek Berlin", "location": [52.497121, 13.393412]},
        {"name": "Humboldt University Library", "location": [52.518623, 13.394324]},
        {"name": "Bezirksbibliothek Frankfurter Allee", "location": [52.514979, 13.469297]},
        {"name": "Berliner Stadtbibliothek", "location": [52.519153, 13.413429]},
        {"name": "Mediathek der Deutschen Kinemathek", "location": [52.509786, 13.375365]},
    ]

    # Add markers for each library
    for library in libraries:
        folium.Marker(
            location=library["location"],
            popup=library["name"],
            icon=folium.Icon(icon="book", prefix="fa")
        ).add_to(berlin_map)

    # Save the map to an HTML file and display it
    map_path = 'data/berlin_libraries_map.html'
    berlin_map.save(map_path)

def main_3():
    # Define the transition matrix for a simple Markov chain
    # Each row represents the probabilities of transitioning from that state to the others
    transition_matrix = np.array([[0.7, 0.3],  # State 0 transitions: 70% to stay in 0, 30% to go to 1
                                  [0.4, 0.6]])  # State 1 transitions: 40% to go to 0, 60% to stay in 1

    # Define the initial state (starting in state 0)
    initial_state = 0

    # Number of steps in the simulation
    num_steps = 1000

    # Storage for the state at each step
    state_history = [initial_state]

    # Perform the simulation
    current_state = initial_state
    for _ in range(num_steps):
        current_state = np.random.choice([0, 1], p=transition_matrix[current_state])
        state_history.append(current_state)

    # Plot the state history over time
    plt.figure(figsize=(10, 6))
    plt.plot(state_history, marker='o', linestyle='-', color='b')
    plt.title('Markov Chain State Transitions Over Time')
    plt.xlabel('Step')
    plt.ylabel('State')
    plt.yticks([0, 1], ['State 0', 'State 1'])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main_3()
