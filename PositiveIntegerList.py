InitialList = [[22, -17, -22], [-68, 34, -12, -47, 8, 52,  99]]
FinalList = [[a for a in b if a > 0] for b in InitialList]
print("Initial List is :", InitialList)
print("Modified list is :", FinalList)