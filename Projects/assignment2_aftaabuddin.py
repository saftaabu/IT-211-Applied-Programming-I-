points       = [539, 1220, 996, 1485, 1938, 2019, 2461, 1557, 1819, 2832, 2430, 2323, 2201, 1970, 2078, 1616, 2133, 83, 782, 1161]
games_played = [71, 79, 50, 66, 68, 80, 82, 65, 66, 80, 77, 82, 82, 73, 82, 58, 78, 6, 35, 66]
fgm          = [176, 391, 362, 554, 701, 749, 868, 516, 573, 978, 813, 775, 800, 716, 740, 574, 738, 31, 266, 398]
pm2          = [125, 316, 335, 508, 640, 716, 744, 445, 442, 798, 676, 625, 682, 617, 625, 487, 606, 28, 212, 265]
pm3          = [51, 75, 27, 46, 61, 33, 124, 71, 131, 180, 137, 150, 118, 99, 115, 87, 132, 3, 54, 133]
fga          = [442, 913, 779, 1183, 1510, 1597, 1924, 1178, 1324, 2173, 1757, 1690, 1712, 1569, 1639, 1336, 1595, 73, 713, 1113]
blocks       = [23, 40, 50, 62, 43, 35, 67, 28, 53, 30, 36, 40, 37, 20, 12, 18, 25, 1, 7, 13]
steals       = [49, 74, 72, 106, 114, 118, 181, 112, 86, 147, 111, 151, 120, 113, 99, 69, 106, 7, 47, 62]
avg = []
#percentage of field goals 2 pointers
fgp = sum(pm2) / sum(fga)
fgpPercentage = fgp * 100
print("Percentage of career field goals made that were 2 pointers: ", fgpPercentage,"%")

#average steals per game for each season
for i in range(20):
    avg.append(steals[i] / games_played[i])
    rounded_avg = [round(num,2) for num in avg]
print("Average steals per game for EACH season: ", rounded_avg)

#top 3 in points
points.sort(reverse=True)
print("Top 3 in points:", points[:3])

#number of times Kobe had less than 25 blocks in a season
blocks.sort()
print("Number of times Kobe had less than 25 blocks in a season:", len(blocks[:7]))

 
#eFG%
#formula: (FG + 0.5 * 3P) / FGA
eFG = (sum(fgm) + 0.5 * sum(pm3)) / sum(fga)
eFGpercentage = eFG * 100
print("Career eFG%:", eFGpercentage,"%")

