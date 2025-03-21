


# Animal Prediction Game

#### Video Demo: https://youtu.be/RjbXzql0swk


## DESCRIPTION

The Animal Prediction Game is an engaging and interactive program designed to guess the animal you are thinking of based on three simple features: size, habitat, and speed. This project is a great introduction to basic machine learning concepts and demonstrates how to implement them using Python. By playing this game, users can gain insights into how neural networks operate and learn to make predictions based on input data.

## Files in the Project

### 1. `project.py`

This file is the heart of the game, containing all the essential functions that make it work. Here’s a breakdown of what you will find in this file:

- **Weight Generation**: The program starts by generating random weights for the neural network. These weights are crucial as they determine how much influence each feature (size, habitat, and speed) has on the final prediction. The randomness in initial weights ensures a diverse learning process as the model is trained on various examples.

- **Input Sum**: This function calculates the weighted sum of the inputs. It multiplies each input by its corresponding weight and adds them together. This sum is then adjusted by a bias term (the last weight), allowing the neural network to make more nuanced predictions.

- **Activation Function**: The activation function takes the weighted sum as input and processes it to produce an output that corresponds to one of the four animals (Fish, Rabbit, Tiger, Turtle). The activation function helps introduce non-linearity into the model, allowing it to learn complex patterns.

- **Training Phase**: During the training phase, the program learns from a predefined dataset containing information about different animals. It compares its predictions with the actual labels to determine whether the guess was correct. If there is a mismatch, the program calls the error calculation function to adjust the weights, aiming to improve accuracy over time.

- **Game Function**: This is where the fun happens! The game function prompts the user to input the size, habitat, and speed of the animal they have in mind. Using the trained neural network, the program then predicts which animal it thinks the user is thinking of. This interactive element adds excitement and engagement to the learning process.

### 2. `test_project.py`

This file includes tests for the game, utilizing the `pytest` framework. The purpose of these tests is to verify that the `play_game` function operates as intended. By providing controlled inputs, the tests check whether the program can accurately predict the animal based on the features given. This ensures that the game is reliable and functions correctly, even after modifications to the code.

### 3. `README.md`

This document serves as a comprehensive guide to the project. It explains what the project is about, how to run the game, and details the functionalities of the code. The README aims to help users understand the project’s structure and encourage them to explore the code further.

## Design Choices

Throughout the development of this project, I faced several design decisions. One key choice was to focus on three specific features: size, habitat, and speed. I believe these features are both straightforward and effective in distinguishing between different animals.

I also opted to implement a simple neural network for this project because it allows the program to learn from data and improve its predictions over time. The training phase is a crucial part of this learning process, enabling the model to adjust its weights and become more accurate after encountering various examples of animals.

Another significant design choice was to use a modular approach in organizing the code. By separating different functionalities into functions, the code remains clean, easy to read, and maintainable. This approach also allows for easier debugging and future enhancements, as each component can be modified independently.

## TODO

To run the Animal Prediction Game, follow these simple steps:

1. Make sure you have Python installed on your computer. If you do not have it, you can download it from the official Python website.

2. Clone the project repository to your local machine. You can do this by using the command:

       git clone <url>

3. Navigate to the project directory using the command line:

       cd project

4. Run the game by executing the following command:

       python3 project.py

5. Follow the prompts to enter the size, habitat, and speed of the animal you are thinking of. The program will then predict the animal based on your input.

## Conclusion

The Animal Prediction Game is a fun and educational project that illustrates the basics of machine learning in an interactive way. It provides a hands-on opportunity to learn how neural networks can be applied to solve problems and make predictions.

I hope you enjoy playing this game and find it useful for understanding how machine learning works! As you explore the code, consider how you might extend its functionality. You could add more animals, features, or even enhance the neural network to improve its accuracy.

Thank you for taking the time to check out my project! I encourage you to explore, play, and learn from this simple yet powerful demonstration of machine learning principles.
