from reescrapper import GenerationTenerife, DemandTenerife

demand = DemandTenerife().get()
print(demand)

generation = GenerationTenerife().get()
print(generation)