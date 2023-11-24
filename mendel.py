def crossGens(parent_1, parent_2):
    def seperateFeatures(parent):
        features = len(parent)//2
        for i in range(0, features+1, 2):
            germcell_1 = parent[i:i+2][0]
            germcell_2 = parent[i:i+2][1]
            print(germcell_1, germcell_2)

    seperateFeatures(parent_1)
    seperateFeatures(parent_2)
parent_1 = input('What\'s the first parent? ')
parent_2 = input('What\'s the second parent? ')
crossGens(parent_1, parent_2)