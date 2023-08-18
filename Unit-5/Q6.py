import sqlite3 as sql


def printRows(Data):
    for row in Data:
        print(row)
    print()


data = [
    ("Newfoundland and Labrador", 512930, 370501.69),
    ("Prince Edward Island", 125294, 5684.39),
    ("Nova Scotia", 908007, 52917.43),
    ("New Brunswick", 729498, 71355.67),
    ("Quebec", 7237479, 1257743.08),
    ("Ontario", 11410046, 907655.59),
    ("Manitoba", 1119583, 551937.87),
    ("Saskatchewan", 978933, 586561.35),
    ("Alberta", 2974807, 639987.12),
    ("British Columbia", 3907738, 926492.48),
    ("Yukon Territory", 28674, 474706.97),
    ("Northwest Territories", 37360, 1141108.37),
    ("Nanavut", 26745, 1925460.18),
]

con = sql.connect("Python/Unit5Sol/population.db")  # Create database
cur = con.cursor()
cur.execute("CREATE TABLE PopByRegion(Region TEXT, Population INTEGER, LandArea REAL)")

# Inserting Values
for i in data:
    cur.execute("INSERT INTO PopByRegion VALUES(?,?,?)", i)

con.commit()
# Retrieve all cotents
cur.execute("SELECT * FROM PopByRegion")
printRows(cur.fetchall())

# Retrieve popuation
cur.execute("SELECT Population FROM PopByRegion")
printRows(cur.fetchall())

# Population less than 1 mil
cur.execute("SELECT Region FROM PopByRegion WHERE Population<10000000")
printRows(cur.fetchall())

# Population less than 1 & greater than 1 mil
cur.execute(
    "SELECT Region FROM PopByRegion WHERE Population<1000000 OR Population>50000"
)
printRows(cur.fetchall())

# Print province and pop density
cur.execute("SELECT Region, Population/LandArea FROM PopByRegion")
printRows(cur.fetchall())

cur.execute("DROP TABLE PopByRegion")
