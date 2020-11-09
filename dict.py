canbinet = {3:"치코리타", 100:"리아코", "A123":"피카츄"}
print(canbinet[3])
print(canbinet[100])
print(canbinet.get(3))
print(canbinet.get(5)) #none
print(canbinet.get(5, "브케인"))
print("gotcha")


print(3 in canbinet)
print(5 in canbinet)

print(canbinet["A123"])
print("A123" in canbinet)

#new dict
print(canbinet)
canbinet["C-20"] = "조세호" #값이 있으면 업데이트
canbinet["A123"] = "미뇽"
print(canbinet["A123"])

#del 

del canbinet[3]
print(canbinet.get(3))

print(canbinet)

# must key values
print(canbinet.keys())

# must values
print(canbinet.values())

#key, value 쌍
print(canbinet.items())

#clear
canbinet.clear
print(canbinet)

