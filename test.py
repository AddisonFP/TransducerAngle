import calc_angle as ca
import os

for root, dir, files in os.walk("Transducer Initialization Files/"):
    for file in files:
        if file == ".DS_Store": #dumb apple file you can't remove
            continue
        results = ca.load_element_file("Transducer Initialization Files/" + file)
        print("\n{}".format(file))
        print("angle: {} radians\nlength correction factor: {} normalized".format(results[0], results[1]))
