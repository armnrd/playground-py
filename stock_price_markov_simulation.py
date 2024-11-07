import numpy as np
import matplotlib.pyplot as plt

# Define the price levels (states) for the stock
price_levels = np.array([100, 105, 110, 115, 120])

# Define the transition matrix for the Markov chain
# Rows represent the current state, and columns represent the next state
transition_matrix = np.array([
    [0.4, 0.3, 0.2, 0.1, 0.0],  # From price level 100
    [0.2, 0.4, 0.3, 0.1, 0.0],  # From price level 105
    [0.1, 0.3, 0.4, 0.1, 0.1],  # From price level 110
    [0.0, 0.2, 0.3, 0.4, 0.1],  # From price level 115
    [0.0, 0.1, 0.2, 0.3, 0.4]   # From price level 120
])

# Function to simulate stock price movement using Markov chain
def simulate_stock_price(initial_price, num_steps):
    # Start at the initial price
    current_price_index = np.where(price_levels == initial_price)[0][0]
    price_history = [initial_price]

    # Simulate the price movement
    for _ in range(num_steps):
        current_price_index = np.random.choice(
            np.arange(len(price_levels)),
            p=transition_matrix[current_price_index]
        )
        price_history.append(price_levels[current_price_index])

    return price_history

# Parameters for the simulation
initial_price = 110
num_steps = 100  # Number of time steps to simulate

# Simulate the stock price
price_history = simulate_stock_price(initial_price, num_steps)

# Plot the results
plt.plot(price_history)
plt.title('Stock Price Simulation Using Markov Chain')
plt.xlabel('Time Steps')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()
