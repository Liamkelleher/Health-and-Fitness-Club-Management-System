CREATE TABLE ClubMember (
	memberID SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	fName VARCHAR(255) NOT NULL,
	lName VARCHAR(255) NOT NULL,
	weightGoal DECIMAL(5,2),
	timeGoal DATE	
);

-- one-to-one relationship with ClubMember
CREATE TABLE Dashboard (
	memberID SERIAL PRIMARY KEY,
	restHR INT,
	weight DECIMAL(5,2) NOT NULL,
	height DECIMAL(3,2) NOT NULL,
	acheivements TEXT,
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID)
);

CREATE TABLE Achievements (
	achievementID SERIAL PRIMARY KEY,	
	clubMemberID INT,
	achievement TEXT,
	FOREIGN KEY (clubMemberID) REFERENCES ClubMember(memberID)
);

CREATE TABLE Routines (
	routineID SERIAL PRIMARY KEY,
	clubMemberID INT,
	routine TEXT,
	FOREIGN KEY (clubMemberID) REFERENCES ClubMember(memberID)
);

CREATE TABLE Admin (
	adminID SERIAL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	fName VARCHAR(255) NOT NULL,
	lName VARCHAR(255) NOT NULL,
);

-- one-to-many relationship with ClubMember
CREATE TABLE Billing (
	billingID SERIAL PRIMARY KEY,
	clubMemberID INT,
	adminID INT,
	membership VARCHAR(255),
	trainingSession INT,
	otherServices VARCHAR(255),
	date DATE,
	PRIMARY KEY (clubMemberID, Date),
	FOREIGN KEY (clubMemberID) REFERENCES ClubMember(memberID)
	FOREIGN KEY (adminID) REFERENCES Admin(adminID)
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
	trainerID INT,
	day DATE,
	startTime TIME,
	endTime TIME,
	isFree BOOLEAN,
	PRIMARY KEY (trainerID, day, startTime),
	FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID)
);

CREATE TABLE SchedulesWith (
	scheduleID SERIAL PRIMARY KEY,
	trainerID INT,
	memberID INT,
	day DATE,
	startTime TIME,
	endTime TIME,
	FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID),
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID)
);


-- Admin updates class
CREATE TABLE Class (
	classID SERIAL PRIMARY KEY,
	adminID INT,
	numSpots INT,
	type VARCHAR(255),
	startTime TIME,
	endTime TIME,
	roomNum INT,
	FOREIGN KEY (adminID) REFERENCES Admin(adminID)
);

-- Many-to-One relation between ClubMember and Class
CREATE TABLE ParticipantsIn (
	clubMemberID INT,
	classID INT,
	trainerID INT,
	date DATE,
	time TIME,
	PRIMARY KEY (classID),
	FOREIGN KEY (clubMemberID) REFERENCES ClubMember(memberID),
	FOREIGN KEY (classID) REFERENCES Class(classID)
	FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID)
);

-- Admin monitors
CREATE TABLE TrainingEquipment (
    equipID SERIAL PRIMARY KEY,
	adminID INT,
    name VARCHAR(255),
    status VARCHAR(255),
    room INT,
    description TEXT,
	FOREIGN KEY (adminID) REFERENCES Admin(adminID)
);

CREATE TABLE Booking (
	bookingID SERIAL PRIMARY KEY,
	adminID INT,
	room INT,
	classID INT,
	FOREIGN KEY (adminID) REFERENCES Admin(adminID),
	FOREIGN KEY (classID) REFERENCES Class(classID)
);




