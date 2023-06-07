# Database-with-MySQL
In this project,I created a database based on life in villages in anime movies/shows in 4 phases.
## Phase 1
#### I listed down the requirements of the miniworld that we had planned.

## Phase 2
#### I designed an ER diagram for our mini-world which contains information about all the entities, their attributes and relationships. I used draw.io to draw the ER diagram.

## Phase 3
#### I converted the ER diagram into relational models for better understanding. Then, iteratively, I converted this to first, second and third normal forms.

## Phase 4
#### I have implemented the following SQL commands in our Project:

### (1) To insert the the data about Ninja in the database (Insert):
	query1 = "INSERT INTO Ninja(ID_no, Name, DOB, Team_no, Start_Date, Nin_Rank) VALUES (%d, %s, %s, %d, %s, %s)" % (row["ID_no"], row["Name"], row["DOB"], row["Team_no"], row["Start_Date"], row["nin_Rank"])
        
    query2 = "INSERT INTO Codenames(ID_no, codename) VALUES (%d, %s)" % (row["ID_no"], row["codename"])
    
    
### (2) To insert the data about Mission in the database (Insert):
	query = "INSERT INTO Missions(Mission_no, Mission_info, Mission_name, Team_assigned, Status, Client, Cost, Mission_rank) VALUES (%d, %s, %s, %d, %s, %s, %d, %s)" % (row["Mission_no"], row["Mission_info"], row["Mission_Name"], row["Team_assigned"], row["Status"], row["Client"], row["Cost"], row["Mission Rank"])
	
	
### (3) To insert the data about Team in the database (Insert):

	query = "INSERT INTO Teams(Team_no, Team_name, Leader_id) VALUES (%d, %s, %d)" % (row["Team_no"], row["Team_name"], row["Leader_id"])
	
### (4) To insert the data about Summon in the database (Insert):
	query1 = "INSERT INTO Residences(Species, Residence) VALUES (%s, %s)" % (row["Species"], row["Residence"])

	query2 = "INSERT INTO Summons(Name, Owner_id, Species) VALUES (%s, %d, %s)" % (row["Name"], row["Owner_id"], row["Species"])
	
	
### (5) To update the mission status of some mission identified by Mission_no (Update):
	query = "UPDATE Missions SET Status = %s WHERE Mission_no = %d" % (New_Stat, Mis_no)
	
	
### (6) To update the rank of a Ninja identified by ID_no (Update):
	query = "UPDATE Ninja SET Nin_Rank = %s WHERE ID_no = %d" % (NewNinRank, NinID)
	
	
### (7) 	To delete a weapon identified by its Name and Owner_id (Delete):
	query = "DELETE FROM Weapons WHERE Name = %s AND Owner_id = %d" % (w_name, w_own)
	

### (8) Select all ninja with rank as Genin (Selection ~ Query):
	query = "SELECT * FROM Ninja WHERE Nin_Rank = 'Genin'"
	
	
### (9) Select all missions with status as Ongoing (Selection ~ Query):
	query = "SELECT * FROM Missions WHERE Status = 'Ongoing'"


### (10) Select Team names of teams with greater than 2 members (Projection ~ Query):
	query = "SELECT Team_name, COUNT(*) FROM Team INNER JOIN Ninja on Team.Team_no = Ninja.Team_no GROUP BY Teams.Team_name HAVING COUNT(*) > 2"
	
### (11) Select Team Name and Learder_id of teams with no Jounin on them (Projection ~ query):
	query = "SELECT DISTINCT Team_name, Leader_id FROM Teams INNER JOIN Ninja on Teams.Team_no = Ninja.Team_no WHERE Nin_rank <> 'Jounin'"
	
	
### (12) Get Cost of Mission with minimum cost (aggregate ~ query):
	query = "SELECT Min(Cost) FROM Missions"
	
	
### (13) Get Cost of Mission with maximum cost (aggregate ~ query):
	query = "SELECT Max(Cost) FROM Missions"

	
### (14) Get the Average cost of all Missions(aggregate ~ query):
	query = "SELECT Avg(Cost) FROM Missions"
	
	
### (15) Search for team names containing a particular string in their name (Search ~ query):
	query = "SELECT Team_name FROM Teams WHERE Team_name LIKE '%" + string + "%'"
	
	
### (16) Search for codenames starting with a particular letter (Search ~ query):
	query = "SELECT codename FROM Codenames WHERE codename LIKE '" + n + "%'"
	
	
### (17) Get top 3 Ninja with highest number of successful missions completed (Analysis):
	query = "SELECT Ninja.ID_no, Count(*) FROM Ninja JOIN Missions ON Missions.Team_assigned = Ninja.Team_no WHERE Missions.Status = 'Successful' GROUP BY Ninja.ID_no ORDER BY Count(*) DESC LIMIT 3"
	
	
### (18) Get those CLients that have the sum of all the mission costs of missions requested by them to be greater than the avg cost of a mission (Analysis):
	query = "SELECT Clients.Ssn_no, Clients.Name, Sum(Cost) FROM Missions JOIN Clients ON Missions.Client = Clients.Ssn_no GROUP BY Clients.Ssn_No HAVING Sum(Cost) > (SELECT Avg(Cost) FROM Missions)"
