"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
MARS_GRAVITY_PERCENTAGE = 0.378
def main():
    # name: earth_weight, type: string, value: 100
    earth_weight = input("What is your weight on earth? ")

    # name: earth_weight_number, type: int, value: 100.5
    earth_weight_number = int(earth_weight)

    # name: mars_weight, type: int, value: 100 * 0.378
    # earth_weight_number, type: int | MARS_GRAVITY_PERCENTAGE: int
    mars_weight = earth_weight_number * MARS_GRAVITY_PERCENTAGE

    #mars_weight 
    print("The equivalent on Mars: " + str(mars_weight))
    pass

if __name__ == "__main__":
    main()
