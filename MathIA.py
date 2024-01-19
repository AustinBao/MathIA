import math

VertexCoordinates = [
    "4.14 10.27",
    "4.09 9.73",
    "6.12 10.66",
    "6.16 10.16",
    "4.95 9",
    "6.49 9.69",
    "6.49 8.88",
    "7.91 9.63",
    "7.95 8.91",
    "6.13 8.23",
    "5.24 8.23", 
    "2.53 8.66",
    "1.37 8.33",
    "4.88 7.73",
    "3.34 6.48",
    "4.75 7.13",
    "6.19 5.84",
    "5.97 5.69",
    "7.86 5.76",
    "7.82 7.65",
    "6.88 7.5",
    "8.39 8.02",
    "9.2 4.94",
    "8.26 4.06",
    "5.31 4.07",
    "3.41 2.24"
] 


normalizedValues = [
    0.22, # ALES
    0.84, # Arts 
    0.41, # Business
    0.44, # Education
    0.71, # Engineering
    0.14, # KSR
    0.04, # Law
    0.4,  # Medicine & Dentistry + Nursing + Public Health
    0.0,  # Native Studies
    0.12, # Open Studies
    0.05, # Pharmacy
    0.09, # Rehabilitation Medicine
    1.0   # Science 
]

BuildingCoordinates = [
    "3.73 9.38",  # ALES
    "7.42 10.01", # Arts
    "6.63 10.53", # buisness
    "5.93 7.64",  # education
    "3 11",       # engineering
    "3.91 7.85",  # KSR
    "8.18 8.02",  # law
    "4.29 5.62",  # medicine
    "4.23 9.12",  # native studies
    "4.86 8.7",   # open studies
    "5.12 6.53",  # pharmacy
    "5.53 3.01",  # rehab
    "4.56 11.06", # Science  
]

def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


totaldistance = []

for vertex in VertexCoordinates:
    distances = []
    sum = 0

    vertexcoordinate = vertex.split(" ")
    Vx = float(vertexcoordinate[0])
    Vy = float(vertexcoordinate[1])
    
    for i in range(len(BuildingCoordinates)):

        buildingcoordinate = BuildingCoordinates[i].split(" ")
        Bx = float(buildingcoordinate[0])
        By = float(buildingcoordinate[1])

        dist = distance_formula(Vx,  Vy,  Bx,  By)
        w = normalizedValues[i]
        distanceScore = dist * w

        distances.append(round(distanceScore, 2))
        sum += distanceScore

    totaldistance.append(distances)
    totaldistance.append(round(sum, 2))


populationscore = [element for index, element in enumerate(totaldistance) if index % 2 != 0 and isinstance(element, (int, float))]

radiusSquared = {
    "CDE": 1.26, # CDE 
    "DEK": 1.31, # DEK 
    "CEG": 1.36, # CEG 
    "EFG": 0.94, # EFG 
    "EFK": 0.91, # EFK
    "GFH": 0.59, # GFH
    "FHI": 0.5,  # FHI 
    "GHJ": 0.83, # GHJ
    "HIJ": 0.85, # HIJ 
    "FIM": 1.08, # FIM 
    "FKM": 1.4,  # FKM
    "DKL": 2.51, # DKL
    "DLR": 6.13, # DLR 
    "KLM": 1.3,  # KLM 
    "LRQ": 1.56, # LQR
    "LMQ": 1.32, # LMQ
    "MNP": 2,    # MNP
    "MPQ": 2.37, # MPQ 
    "NOP": 0.97, # NOP
    "INO": 1.27, # INO 
    "IMN": 1.04, # IMN
    "JIO": 1.87, # JIO
    "OPT": 3.81, # OPT 
    "PST": 1.76, # PST 
    "PSQ": 4.63, # PSQ 
    "SQR": 15.77 # SQR 
}

ratings = {
    "C": 4.2,
    "D": 3.6,
    "E": 4.5,
    "F": 4.3,
    "G": 3.1,
    "H": 4.6,
    "I": 4.1,
    "J": 4.1,
    "K": 4.8,
    "L": 3.6,
    "M": 4.7,
    "N": 4.4,
    "O": 4.8,
    "P": 4.1,
    "Q": 3.9,
    "R": 3.0,
    "S": 4.2,
    "T": 4.5
}

def averageRating(r):
    site1, site2, site3 = r[0], r[1], r[2]
    return round((ratings[site1] + ratings[site2] + ratings[site3])/3, 2)
    

ratingScore = []
distanceScore = []
for r in radiusSquared:
    distanceScore.append(round(math.sqrt(radiusSquared[r]), 2))
    ratingScore.append(averageRating(r))


print("\n", distanceScore, "\n", "\n", ratingScore, "\n", "\n", populationscore, "\n")


totalscore = []
for i in range(len(ratingScore)):
    totalscore.append(round(( ratingScore[i] - distanceScore[i] + populationscore[i])/3, 4))

# And there we have it... we now know the vertex with the minimum total score of 4.5633  
print(totalscore, "\n", "\n", min(totalscore), totalscore.index(min(totalscore)))


