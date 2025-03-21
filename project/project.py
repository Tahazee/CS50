#Libraries
import random


#constants
input_size=3
weight_size=input_size + 1
learning_rate=0.01

#datasets
training_data_set = {"Fish": (0, 0, 0),"Rabbit": (0, 1, 1),"Tiger": (1, 1, 1),"Turtle": (0, 0, 1)
}
output_labels={"Fish": 0, "Rabbit": 1, "Tiger": 2, "Turtle": 3}



#random initial weight generator
def weight_generation():
    weights=[random.random() for i in range(weight_size)]
    return weights

#weight sum
def input_sum(weights,inp):
         sum=0
         for i in range(input_size):
              sum+=weights[i]*inp[i]
         sum+=weights[-1]
         return sum




#Activation function
def activation_func(output):
     return round(output)%4

#training phase
epochs=100
def comparing(weights):
    global inp
    for _ in range(epochs):
        for animal,features in training_data_set.items():
                des_out=output_labels[animal]
                sum=input_sum(weights,features)
                output=activation_func(sum)

                if des_out!=output:
                    weights=error_calc(weights,des_out,output,features)
    return weights

#Adjusting weights for reducing error
def error_calc(weights,des_out,output,inp):
    error=des_out-output
    for i in range(input_size):
        weights[i]+=learning_rate*error*inp[i]
    weights[-1]+=learning_rate*error
    return weights


#game function
def play_game(weights, size=None, speed=None, habitat=None):
    if size is None:
        size = int(input("Enter size (0 for small, 1 for large): "))
    if speed is None:
        speed = int(input("Enter speed (0 for slow, 1 for fast): "))
    if habitat is None:
        habitat = int(input("Enter speed (0 for water, 1 for land): "))

    print('---------------------PREDICT THE ANIMAL-------------------')
    print("Enter features to see if the neural network can guess the animal!")
    animals = {v: k for k, v in output_labels.items()}
    print(animals)
    inp = (size, speed,habitat)


    sum_val = input_sum(weights, inp)
    output = activation_func(sum_val)
    predicted_animal = animals.get(output, "Unknown")

    print(f"Predicted Animal: {predicted_animal}\n")
    return predicted_animal

#main function
def main():
     weights=weight_generation()
     new_weights=comparing(weights)
     play_game(new_weights)


if __name__=='__main__':
     main()

