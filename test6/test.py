import DataGen

seed = DataGen.long_p()
DataGen.long_p.assign(seed,123456)
print(seed)
SourceBbit = DataGen.intArray(10)
DataGen.randombit_gene(SourceBbit,10,seed)
for i in range(10):
    print(i, SourceBbit[i])
