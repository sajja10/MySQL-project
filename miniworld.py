import subprocess as sp
import pymysql
import pymysql.cursors

def insertNinja():
    try:
        row = {}
        print("Enter Ninja details: ")
        row["ID_no"] = int(input("ID Number: "))
        row["Name"] = input("Name: ")
        row["DOB"] = input("Date of Birth: ")
        row["Team_no"] = int(input("Team Number: "))
        row["Start_Date"] = input("Start Date: ")
        row["nin_Rank"] = input("Ninja Rank: ")
        row["codename"] = input("Codename: ")

        query1 = "INSERT INTO Ninja(ID_no, Name, DOB, Team_no, Start_Date, Nin_Rank) VALUES (%d, '%s', '%s', %d, '%s', '%s')" % (row["ID_no"], row["Name"], row["DOB"], row["Team_no"], row["Start_Date"], row["nin_Rank"])
        query2 = "INSERT INTO Codenames(ID_no, codename) VALUES (%d, '%s')" % (row["ID_no"], row["codename"])

        cur.execute(query1)
        cur.execute(query2)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def insertMission():
    try:
        row = {}
        print("Enter Mission Details: ")
        row["Mission_no"] = int(input("Mission Number: "))
        row["Mission_info"] = input("Mission Info: ")
        row["Mission_Name"] = input("Mission Name: ")
        row["Team_assigned"] = int(input("Team Assigned: "))
        row["Status"] = input("Status: ")
        row["Client"] = input("Client SSN: ")
        row["Cost"] = int(input("Mission Cost: "))
        row["Mission Rank"] = input("Mission Rank: ")

        query = "INSERT INTO Missions(Mission_no, Mission_info, Mission_name, Team_assigned, Status, Client, Cost, Mission_rank) VALUES (%d, '%s', '%s', %d, '%s', '%s', %d, '%s')" % (row["Mission_no"], row["Mission_info"], row["Mission_Name"], row["Team_assigned"], row["Status"], row["Client"], row["Cost"], row["Mission Rank"])

        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def insertTeam():
    try:
        row = {}
        print("Enter Team Details: ")
        row["Team_no"] = int(input("Team Number:"))
        row["Team_name"] = input("Team Name: ")
        row["Leader_id"] = int(input("Leader ID Number: "))

        query = "INSERT INTO Teams(Team_no, Team_name, Leader_id) VALUES (%d, '%s', %d)" % (row["Team_no"], row["Team_name"], row["Leader_id"])

        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def insertSummon():
    try:
        row = {}
        print("Enter Summon Details: ")
        row["Name"] = input("Name: ")
        row["Owner_id"] = int(input("Owner ID: "))
        row["Species"] = input("Species Name: ")
        row["Residence"] = input("Residence Address: ")

        query1 = "INSERT INTO Residences(Species, Residence) VALUES ('%s', '%s')" % (row["Species"], row["Residence"])
        query2 = "INSERT INTO Summons(Name, Owner_id, Species) VALUES ('%s', %d, '%s')" % (row["Name"], row["Owner_id"], row["Species"])

        cur.execute(query1)
        cur.execute(query2)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def updateMissionStatus():
    try:
        Mis_no = int(input("Enter Mission No.: "))
        New_Stat = input("Enter new status of mission")

        query = "UPDATE Missions SET Status = '%s' WHERE Mission_no = %d" % (New_Stat, Mis_no)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

def updateNinRank():
    try:
        NinID = int(input("Enter Ninja ID: "))
        NewNinRank = input("Enter new ninja rank: ")

        query = "UPDATE Ninja SET Nin_Rank = '%s' WHERE ID_no = %d" % (NewNinRank, NinID)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

def deleteWeapon():
    try:
        w_name = input("Enter Weapon name: ")
        w_own = int(input("Enter Owner_id: "))

        query = "DELETE FROM Weapons WHERE Name = '%s' AND Owner_id = %d" % (w_name, w_own)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def selectGenin():
    query = "SELECT * FROM Ninja WHERE Nin_Rank = 'Genin'"
    cur.execute(query)
    print(cur.fetchall())

def selectOngoingMission():
    query = "SELECT * FROM Missions WHERE Status = 'Ongoing'"
    cur.execute(query)
    print(cur.fetchall())

def greater2Team():
    query = "SELECT Team_name, COUNT(*) FROM Team INNER JOIN Ninja on Team.Team_no = Ninja.Team_no GROUP BY Teams.Team_name HAVING COUNT(*) > 2"
    cur.execute(query)
    print(cur.fetchall())

def NoJouninTeam():
    query = "SELECT DISTINCT Team_name, Leader_id FROM Teams INNER JOIN Ninja on Teams.Team_no = Ninja.Team_no WHERE Nin_rank <> 'Jounin'"
    cur.execute(query)
    print(cur.fetchall())

def MinCost():
    query = "SELECT Min(Cost) FROM Missions"
    cur.execute(query)
    print(cur.fetchall())

def MaxCost():
    query = "SELECT Max(Cost) FROM Missions"
    cur.execute(query)
    print(cur.fetchall())

def AvgCost():
    query = "SELECT Avg(Cost) FROM Missions"
    cur.execute(query)
    print(cur.fetchall())

def search_team_name():
    string = input("Enter the string to search in team name")
    query = "SELECT Team_name FROM Teams WHERE Team_name LIKE '%" + string + "%'"
    cur.execute(query)
    print(cur.fetchall())

def search_code_name():
    n = input("Enter the first letter of the codenames you want")
    query = "SELECT codename FROM Codenames WHERE codename LIKE '" + n + "%'"
    cur.execute(query)
    print(cur.fetchall())

def top3Ninja():
    query = "SELECT Ninja.ID_no, Count(*) FROM Ninja JOIN Missions ON Missions.Team_assigned = Ninja.Team_no WHERE Missions.Status = 'Successful' GROUP BY Ninja.ID_no ORDER BY Count(*) DESC LIMIT 3"
    cur.execute(query)
    print(cur.fetchall())

def AboveAvgClients():
    query = "SELECT Clients.Ssn_no, Clients.Name, Sum(Cost) FROM Missions JOIN Clients ON Missions.Client = Clients.Ssn_no GROUP BY Clients.Ssn_No HAVING Sum(Cost) > (SELECT Avg(Cost) FROM Missions)"
    cur.execute(query)
    print(cur.fetchall())


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insertNinja()
    elif(ch == 2):
        insertMission()
    elif(ch == 3):
        insertTeam()
    elif(ch == 4):
        insertSummon()
    elif(ch == 5):
        updateMissionStatus()
    elif(ch == 6):
        updateNinRank()
    elif(ch == 7):
        deleteWeapon()
    elif(ch == 8):
        selectGenin()
    elif(ch == 9):
        selectOngoingMission()
    elif(ch == 10):
        greater2Team()
    elif(ch == 11):
        NoJouninTeam()
    elif(ch == 12):
        MinCost()
    elif(ch == 13):
        MaxCost()
    elif(ch == 14):
        AvgCost()
    elif(ch == 15):
        search_team_name()
    elif(ch == 16):
        search_code_name()
    elif(ch == 17):
        top3Ninja()
    elif(ch == 18):
        AboveAvgClients()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              #port=30306,
                              user="root",
                              password="c2h5cooh",
                              db='pp',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Insert Ninja")  
                print("2. Insert Mission")  
                print("3. Insert Team") 
                print("4. Insert Summon") 
                print("5. Update Mission Status")
                print("6. Update Ninja Rank")
                print("7. Delete Weapon")
                print("8. Select Genin")
                print("9. Select Ongoing Missions")
                print("10.Teams with greater than 2 members")
                print("11.Teams with no jounins")
                print("12.Mininmum mission cost")
                print("13.Maximum mission cost")
                print("14.Average mission cost")
                print("15.Team name containing a particular string")
                print("16.Codename starting with particular letter")
                print("17.Top 3 Ninjas with most no. of sucessful missions")
                print("18.Clients with total mission cost greater than avg mission cost")
                print("19.Exit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 19:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
