def findSafe(data):
    count = 0
    for row in data:
        increasing = True
        decreasing = True
        for i in range(len(row) - 1):
            diff = row[i + 1] - row[i]
            if diff < 0:
                increasing = False
            if diff > 0:
                decreasing = False
            if abs(diff) > 3:
                increasing = False
                decreasing = False
                break
        if increasing or decreasing:
            count += 1
    return count
    

if __name__ == "__main__":
    data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]
    
    ans = findSafe(data)
    print(ans)
