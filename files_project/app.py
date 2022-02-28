find_friend = input("(use Coma Seperation and No Space)\n\tEnter Names : ").split(",")

print(find_friend)

# Read Data from the File
fileName = "friends.txt"
fhandler = open(fileName, 'r')

fdata = [data.strip() for data in fhandler.readlines()]
fhandler.close()

print(fdata)

friends_set = set(fdata)
find_friend_set = set(find_friend)

mutual_friends = friends_set & find_friend_set

print(mutual_friends)

# Write Data into the File
fileName = "mutualFriends.txt"
fhandler = open(fileName, 'w')

for i in mutual_friends:
    fhandler.write(f"{i}\n")

fhandler.close()