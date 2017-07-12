from reescrapper import GenerationGranCanaria, DemandGranCanaria

demand = DemandGranCanaria().get()
print(demand)

generation = GenerationGranCanaria().get()
print(generation)