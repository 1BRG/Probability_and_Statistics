# Probability and Statistics Laboratory

This repository contains solutions and simulations for various probability and statistics problems, implemented in Python. The exercises are part of the "Probability and Statistics" course at the Faculty of Mathematics and Informatics, University of Bucharest.

## Implemented Labs

This repository is a work in progress. Here's a summary of the implemented exercises so far:

### Laboratory #1: Geometric Probability (Bertrand's Paradox)

*   **Objective:** To explore different ways of randomly selecting a chord in a circle and to calculate the probability that the chord is longer than the side of an inscribed equilateral triangle. This is a classic problem that demonstrates how the definition of "randomness" can affect the outcome.
*   **Implementations:**
    *   **Variant 1:** Choosing two random points on the circumference of the circle and connecting them to form a chord.
    *   **Variant 2:** Choosing a random point within the circle using polar coordinates to serve as the midpoint of the chord.
*   **File:** `main.py`

### Laboratory #2: Simulations and Efficiency

*   **Objective:** To simulate various probabilistic scenarios, including coin tosses, the birthday problem, and a non-transitive dice game, while also comparing the performance of vectorized (efficient) vs. non-vectorized (inefficient) implementations.
*   **Implementations:**
    *   **Coin Toss Simulation:** Simulates a large number of coin flips and visualizes the convergence of the empirical probability to the theoretical probability. It also compares the execution time of a loop-based approach versus a more efficient, vectorized NumPy implementation.
    *   **Birthday Problem:** Estimates the probability that in a group of N people, at least two share the same birthday. The simulation is run for groups of 23, 60, and 100 people.
    *   **Non-Transitive Dice (Efron's Dice):** Simulates a game with three special dice (Red, Green, Black) to demonstrate the non-transitive property where Red is likely to beat Green, Green is likely to beat Black, but Black is likely to beat Red.
*   **File:** `main1.py`

### Laboratory #3/4: Conditional Probability and Bayesian Inference

*   **Objective:** To apply concepts of conditional probability and Bayesian thinking to solve problems related to code testing and spam filtering.
*   **Implementations:**
    *   **Code Bug Probability:** Calculates the probability that a piece of code has a bug given that it passed a test, considering the probabilities of false positives and false negatives. This problem is solved both with a standard simulation and a vectorized approach to compare performance.
    *   **Coin Sequence Probability:** A theoretical calculation for the probability of a specific sequence of coin flips occurring.
    *   **Monty Hall Problem:** A simulation of the classic Monty Hall problem to determine the best strategy (switching or staying with the initial choice).
    *   **Spam Filtering:** Calculates the probability that an email is spam given that it contains the word "lottery," based on the prior probabilities of receiving spam and the likelihood of the word appearing in spam vs. non-spam emails.
*   **File:** `main2.py`

## How to Run

To run the simulations, you will need Python with the following libraries installed:

*   NumPy
*   Matplotlib

You can install these dependencies using pip:

```bash
pip install numpy matplotlib
```

After installation, you can run any of the lab files from your terminal:

```bash
python main.py
python main1.py
python main2.py
```

Each script will execute the implemented simulations and print the results to the console. Some scripts may also generate plots to visualize the data.

## Future Work

This repository will be continuously updated with solutions for the remaining laboratory exercises. Future updates will include:

*   Implementations for all the exercises from the provided lab notes.
*   More detailed explanations and comments within the code.
*   Refactoring of the code for better organization and readability.
