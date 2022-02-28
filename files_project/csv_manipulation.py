fileName = "friendsInComp_csv.txt"
fhandler = open(fileName)
fheading = fhandler.readline().strip().split(",")
fdata = [d.strip() for d in fhandler.readlines()]
fhandler.close()

# friends_data = {d for d in data for data in fdata}
friends_data = []
for data in fdata:
    temp_data = data.split(",")
    temp_dict = dict()
    for i in range(0, len(temp_data)):
        # print(i, fheading[i], temp_data[i])
        temp_dict[f"{fheading[i]}"] = temp_data[i]
    friends_data.append(temp_dict)

print(fheading)
print(fdata)
print(friends_data)