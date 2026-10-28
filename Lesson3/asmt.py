def prob_a_and_b(a, b, total):
    # probability of event a (getting an orange ball)
    prob_a = a / total

    # probability of event b given a (getting a blue ball given 1st was orange)
    prob_bga = b / (total - 1)

    # probability of intersection of events a and b
    prob_AandB = prob_a * prob_bga

    # return rounded result to 3 decimal places
    return round(prob_AandB, 3)


# taking input for total number of orange and blue balls
orange = int(input("Enter number of orange balls: "))
blue = int(input("Enter number of blue balls: "))
total = orange + blue

# call function for final result
print("Probability of Getting 1st orange and 2nd blue ball:")
print(prob_a_and_b(orange, blue, total))