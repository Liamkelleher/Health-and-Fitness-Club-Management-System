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
	membership INT,
	trainingSession INT,
	otherServices INT,
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
	scheduleID INT,
	memberID INT,
	FOREIGN KEY (scheduleID) REFERENCES Availabilities(availabilityID),
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
CREATE TABLE ParticipatesIn (
	memberID INT,
	classID INT,
	FOREIGN KEY (memberID) REFERENCES ClubMember(memberID),
	FOREIGN KEY (classID) REFERENCES Class(classID)
);

-- Admin monitors
CREATE TABLE TrainingEquipment (
    equipID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(255)
);

-----------------------------
CREATE FUNCTION createNewUser()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Dashboard(memberID, restHR, weight, height)
    VALUES (NEW.memberID, 0, 0, 0);

	INSERT INTO Billing(memberID, membership, trainingSession, otherServices)
	VALUES (NEW.memberID, 40, 0, 0);
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER createDashboardTrigger
AFTER INSERT ON ClubMember
FOR EACH ROW
EXECUTE FUNCTION createNewUser();

-----------------------------
CREATE FUNCTION noLongerFreeAvailibility()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE Availabilities
    SET isFree = FALSE
    WHERE availabilityID = NEW.scheduleID;

	UPDATE Billing
	SET trainingSession = trainingSession+40
	WHERE memberID = NEW.memberID;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER noLongerFreeTrigger
AFTER INSERT ON TrainingSession
FOR EACH ROW
EXECUTE FUNCTION noLongerFreeAvailibility();

-----------------------------
CREATE FUNCTION freeAvailability()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE Availabilities
    SET isFree = TRUE
    WHERE availabilityID = OLD.scheduleID;
RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER freeAvailabilityTrigger
AFTER DELETE ON TrainingSession
FOR EACH ROW
EXECUTE FUNCTION freeAvailability();

-----------------------------
CREATE FUNCTION participateInClass()
RETURNS TRIGGER AS $$
BEGIN
	UPDATE Class
	SET spots = spots-1
	WHERE classID = NEW.classID;

	UPDATE Billing
	SET otherServices = otherServices+20
	WHERE memberID = NEW.memberID;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER participateInClassTrigger
AFTER INSERT ON ParticipatesIn
FOR EACH ROW
EXECUTE FUNCTION participateInClass();

-----------------------------
CREATE FUNCTION cancelClass()
RETURNS TRIGGER AS $$
BEGIN
	UPDATE Class
	SET spots = spots+1
	WHERE classID = OLD.classID;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER cancelClassTrigger
AFTER DELETE ON ParticipatesIn
FOR EACH ROW
EXECUTE FUNCTION cancelClass();

-----------------------------
CREATE FUNCTION removeClass()
RETURNS TRIGGER AS $$
BEGIN 
	DELETE FROM ParticipatesIn
	WHERE classID = OLD.classID;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER removeClassTrigger
BEFORE DELETE ON Class
FOR EACH ROW
EXECUTE FUNCTION removeClass();

-----------------------------
CREATE FUNCTION removeSchedule()
RETURNS TRIGGER AS $$
BEGIN 
	DELETE FROM TrainingSession
	WHERE scheduleID=OLD.availabilityID;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER removeScheduleTrigger
BEFORE DELETE ON Availabilities
FOR EACH ROW
EXECUTE FUNCTION removeSchedule();
