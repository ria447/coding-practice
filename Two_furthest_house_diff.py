#we need to find the maximum distance between two differently painted houses

def maxDistance(colors):
        arr = []
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    arr.append(abs(i - j))
            
        return max(arr)

colors = [1,1,1,6,1,1,1]
output = maxDistance(colors)
print(output)

#output = 3
