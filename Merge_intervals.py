def merge(intervals):
        list_2 = []
        result = []

        if len(intervals) == 1:
            return intervals

        intervals.sort()

        for i in range(intervals[0][0], intervals[0][1] + 1):
            list_2.append(i)

        length = len(intervals)

        for j in range(1, length):
            if (intervals[j][0] in list_2) or (intervals[j][1] in list_2):
                for k in range(intervals[j][0], intervals[j][1] + 1):
                    list_2.append(k)
            else:
                result.append([min(list_2),max(list_2)])
                list_2 = []
                for k in range(intervals[j][0], intervals[j][1] + 1):
                    list_2.append(k)
        
        listt = [min(list_2), max(list_2)]
        result.insert(0, listt)
        return result

intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
output = merge(intervals))
print(output)

#output = [[4,7],[1,3]]
