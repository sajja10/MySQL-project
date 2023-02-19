CREATE TABLE Ninja(
	ID_no int NOT NULL,
	Name varchar(255),
	DOB date,
	Team_no int,
	Start_Date date,
	Nin_rank varchar(20),
	PRIMARY KEY(ID_no)
);

CREATE TABLE Codenames(
	ID_no int NOT NULL,
	codename varchar(255),
	PRIMARY KEY(ID_no)
);

CREATE TABLE Missions(
	Mission_no int NOT NULL,
	Mission_info varchar(255),
	Mission_name varchar(255),
	Team_assigned int,
	Status varchar(50),
	Client int,
	Cost int,
	Mission_rank varchar(255),
	PRIMARY KEY(Mission_no)
);

CREATE TABLE Teams(
	Team_no int NOT NULL,
	Team_name varchar(255),
	Leader_id int,
	PRIMARY KEY(Team_no)
);

CREATE TABLE Clients(
	Name varchar(255),
	Ssn_no int NOT NULL,
	Address varchar(255),
	PRIMARY KEY(Ssn_no)
);

CREATE TABLE Weapons(
	Name varchar(255) NOT NULL,
	Owner_id int NOT NULL,
	Mfg_date date,
	PRIMARY KEY(Name, Owner_id)
);

CREATE TABLE Weapon_type(
	Name varchar(255) NOT NULL,
	Type varchar(255),
	PRIMARY KEY(Name)
);

CREATE TABLE Summons(
	Name varchar(255) NOT NULL,
	Owner_id int NOT NULL,
	Species varchar(255),
	PRIMARY KEY(Name, Owner_id)
);

CREATE TABLE Residences(
	Species varchar(255) NOT NULL,
	Residence varchar(255),
	PRIMARY KEY(Species)
);

INSERT INTO Ninja VALUES ('31', 'sajja', '2003-09-10', '11', '2010-09-20', 'Genin'),('32', 'bhumika', '2002-04-09', '12', '2012-02-20', 'Jounin'),('33', 'aishani', '2002-10-19', '13', '2015-08-17', 'Chunin'), ('34', 'anushka', '2004-04-11', '11', '2011-07-09', 'Genin'),('35', 'dhingru', '2002-05-09', '12', '2013-02-13', 'Jounin');

INSERT INTO Codenames VALUES ( 31, 'chonky'), (32, 'monke'), (33, 'honky');

INSERT INTO Teams VALUES (11, 'gazers', 31), (12, 'powerpuff', 32), (13, 'tudum', 33);

INSERT INTO Missions VALUES (1,'Murder','ABC',12,'Successful',201,3500,'VVIP'), (2,'Theft','XYZ',11,'Fail',203,3200,'General'), (3,'Rescue','PQY',13,'Ongoing',202,5000,'VIP');

INSERT INTO Clients VALUES ('Shinzo',202,'Tokyo'), ('Masaw',203,'Kasukabe'), ('Kazama',201,'Hiroshima');

INSERT INTO Weapons VALUES ('sword',31,'2001-01-01'), ('knife',33,'2003-05-05'), ('star',32,'2005-03-03');

INSERT INTO Weapon_type VALUES ('sword','gold'), ('star','copper'), ('knife','silver');
 
INSERT INTO Summons VALUES ('Kiyo',31,'cat'),('Shishimanu',32,'dog'), ('Jaggu',33,'monkey');

INSERT INTO Residences VALUES ('cat','Nagasaki'),('dog','Kyoto'),('monkey','Aoshima');


ALTER TABLE Ninja ADD FOREIGN KEY (Team_no) REFERENCES Teams(Team_no);

ALTER TABLE Codenames ADD FOREIGN KEY (ID_no) REFERENCES Ninja(ID_no);

ALTER TABLE Missions ADD FOREIGN KEY (Team_assigned) REFERENCES Teams(Team_no);

ALTER TABLE Missions ADD FOREIGN KEY (Client) REFERENCES Clients(Ssn_no);

ALTER TABLE Teams ADD FOREIGN KEY (Leader_id) REFERENCES Ninja(ID_no);

ALTER TABLE Weapons ADD FOREIGN KEY (Name) REFERENCES Weapon_type(Name);

ALTER TABLE Weapons ADD FOREIGN KEY (Owner_id) REFERENCES Ninja(ID_no);

ALTER TABLE Summons ADD FOREIGN KEY (Owner_id) REFERENCES Ninja(ID_no);

ALTER TABLE Summons ADD FOREIGN KEY (Species) REFERENCES Residences(Species);
