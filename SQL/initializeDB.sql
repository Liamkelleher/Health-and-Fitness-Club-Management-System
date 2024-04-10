--  ClubMember
INSERT INTO ClubMember (email, password, fname, lname)
VALUES
    ('bob@cm.com', 'bob', 'Bob', 'Z'),
    ('bobby@cm.com', 'bobby', 'Bobby', 'Z');

-- Trainer
INSERT INTO Trainer (email, password, fname, lname)
VALUES
    ('liamkelleher@trainer.com', 'liam', 'Liam', 'Kelleher'),
    ('lilyczarnecki@trainer.com', 'lily', 'Lily', 'Czarnecki'),
    ('hughhang@trainer.com', 'hugh', 'Hugh', 'Hang');

-- Availabilities
INSERT INTO Availabilities (trainerID, day, startTime, endTime, isFree)
VALUES
    (1, '2023-10-01', '08:00:00', '10:00:00', TRUE),
    (1, '2023-10-01', '10:00:00', '12:00:00', FALSE),
    (2, '2023-10-02', '09:00:00', '11:00:00', TRUE),
    (2, '2023-10-02', '13:00:00', '15:00:00', TRUE),
    (3, '2023-10-03', '10:00:00', '12:00:00', TRUE),
    (3, '2023-10-03', '14:00:00', '16:00:00', FALSE);

-- Admin
INSERT INTO Admin (email, password, fname, lname)
VALUES
    ('admin1@admin.com', 'admin1', 'Admin', '1'),
    ('admin2@admin.com', 'admin2', 'Admin', '2'),
    ('admin3@admin.com', 'admin3', 'Admin', '3');

-- Insert sample data into TrainingEquipment
INSERT INTO TrainingEquipment (name, status)
VALUES
    ('Bench', 'Good'),
    ('Squat rack', 'Decent'),
    ('Treadmill', 'Not functional');
