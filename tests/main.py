from betterneural.networks import ANN


brain = ANN(4)
brain.add(5)
brain.add(6)
print(brain.layers[1].weights)