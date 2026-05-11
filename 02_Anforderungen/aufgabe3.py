def calculateTotalTime(times: list):
    totalTime = 0
    for time in times:
        totalTime += time
    return totalTime

def calculateAverageTime(times: list):
    if not times or len(times) == 1:
        return 0
    return (calculateTotalTime(times) - times[0]) / (len(times) -1)

print(calculateTotalTime([10, 20, 30]) == 60)
print(calculateAverageTime([10, 20, 30]) == 25)