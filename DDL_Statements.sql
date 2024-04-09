CREATE TABLE ClubMember (
	memberID SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	fName VARCHAR(255) NOT NULL,
	lName VARCHAR(255) NOT NULL
);

-- one-to-one relationship with ClubMember
CREATE TABLE Dashboard (
	memberID SERIAL PRIMARY KEY,
	restHR INT,
	weight INT NOT NULL,
	height INT NOT NULL,
	weightGoal INT,
	timeGoal DATE,
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID)
);

CREATE TABLE Achievements (	
	memberID INT,
	achievement TEXT,
	FOREIGN KEY (memberID) REFERENCES Dashboard(memberID)
);

CREATE TABLE Routines (
	memberID INT,
	routine TEXT,
	FOREIGN KEY (memberID) REFERENCES Dashboard(memberID)
);

CREATE TABLE Admin (
	adminID SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	fName VARCHAR(255) NOT NULL,
	lName VARCHAR(255) NOT NULL
);

-- one-to-many relationship with ClubMember
CREATE TABLE Billing (
	memberID INT PRIMARY KEY,
	membership VARCHAR(255),
	trainingSession INT,
	otherServices VARCHAR(255),
	date DATE,
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID)
);

CREATE TABLE Trainer (
	trainerID SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	fName VARCHAR(255) NOT NULL,
	lName VARCHAR(255) NOT NULL
);

-- one-to-many relationship with trainer
CREATE TABLE Availabilities (
	availabilityID SERIAL PRIMARY KEY,
	trainerID INT,
	day DATE,
	startTime TIME,
	endTime TIME,
	isFree BOOLEAN,
	FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID)
);

CREATE TABLE TrainingSession (
	scheduleID SERIAL PRIMARY KEY,
	memberID INT,
	trainerID INT,
	day DATE,
	startTime TIME,
	endTime TIME,
	FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID),
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID)
);


-- Admin updates class
CREATE TABLE Class (
	classID SERIAL PRIMARY KEY,
	roomNum INT,
	spots INT,
	type VARCHAR(255),
	day DATE,
	startTime TIME,
	endTime TIME
);

-- Many-to-One relation between ClubMember and Class
CREATE TABLE ParticipantsIn (
	memberID INT PRIMARY KEY,
	classID INT,
	day DATE,
	startTime TIME,
	endTime TIME,
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID),
	FOREIGN KEY (classID) REFERENCES Class(classID)
);

-- Admin monitors
CREATE TABLE TrainingEquipment (
    equipID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(255)
);

CREATE OR REPLACE FUNCTION createNewUserDashboard()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Dashboard (memberID, restHR, weight, height)
    VALUES (NEW.memberID, 0, 0, 0);
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER createDashboardTrigger
AFTER INSERT ON ClubMember
FOR EACH ROW
EXECUTE FUNCTION createNewUserDashboard();