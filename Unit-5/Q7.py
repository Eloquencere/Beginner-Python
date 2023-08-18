import sqlite3 as sql


def printRows(Data):
    for row in Data:
        print(row)
    print()


data = [
    ("Newfoundland and Labrador", "St. Johns", 172918),
    ("Prince Edward Island", "Charlottetown", 58358),
    ("Nova Scotia", "Halifax", 359183),
    ("New Brunswick", "Fredericton", 81346),
    ("Quebec", "Quebec City", 682757),
    ("Ontario", "Toronto", 4682897),
    ("Manitoba", "Winnipeg", 671274),
    ("Saskatchewan", "Regina", 192800),
    ("Alberta", "Edmonton", 937845),
    ("British Columbia", "Victoria", 311902),
    ("Yukon Territory", "Whitehorse", 21405),
    ("Northwest Territories", "Yellowknife", 16541),
    ("Nanavut", "Iqaluit", 5236),
]

con = sql.connect("Python/Unit5Sol/population.db")
cur = con.cursor()

# Creating table
cur.execute("CREATE TABLE Capitals(Province TEXT, Capital TEXT, Population INTEGER)")

# Inserting Data
for row in data:
    cur.execute("INSERT INTO Capitals VALUES(?,?,?)", row)
con.commit()

cur.execute(
    "SELECT PopByRegion.LandArea FROM PopByRegion INNER JOIN Capitals WHERE Capitals.Province = PopByRegion.Region AND Capitals.Population>100000"
)
printRows(cur.fetchall())
# Random
cur.execute(
    "SELECT PopByRegion.Region FROM PopByRegion INNER JOIN Capitals WHERE Capitals.Province = PopByRegion.Region AND PopByRegion.Population/PopByRegion.LandArea<2 AND Capitals.Population>500000"
)
printRows(cur.fetchall())
# Total Land Area of Canada
cur.execute("SELECT SUM(LandArea) FROM PopByRegion")
printRows(cur.fetchall())

# Average Capital city population
cur.execute("SELECT AVG(Population) FROM Capitals")
printRows(cur.fetchall())

# Lowest Capital City population
cur.execute("SELECT Capital, MIN(Population) FROM Capitals")
printRows(cur.fetchall())

# Maxmimum population capital
cur.execute("SELECT Capital, MAX(Population) FROM Capitals")
printRows(cur.fetchall())

# Print a pair of provinces whoose Densities are within 0.5 of each other
cur.execute(
    "SELECT A.Region, B.Region FROM PopByRegion A INNER JOIN PopByRegion B WHERE ABS((A.Population/A.LandArea)-(B.Population/B.LandArea)) <= 0.5 AND A.Region<B.Region"
)
printRows(cur.fetchall())

cur.execute("DROP TABLE Capitals")
