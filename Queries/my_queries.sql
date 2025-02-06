use test1;

-- select all the first and last name of the player with position 'QB'
-- works
SELECT first_name, last_name
FROM Players
WHERE position = 'QB';

-- names of head coaches and their team, team city, and team stadium
-- works
SELECT hc.first_name, hc.last_name, t.team_name, t.city, t.stadium
FROM Head_Coaches hc
JOIN Teams t ON hc.team_name = t.team_name;

-- select the first and last name of players who played in the 2023 playoffs
-- works
SELECT first_name, last_name
FROM Players
WHERE team_name IN (
    SELECT team_name
    FROM Playoffs
    WHERE year = 2023
);

-- total number of wins for each team across all seasons in the database
-- works
SELECT team_name, SUM(wins) AS total_wins
FROM Season
GROUP BY team_name;

-- a new team into the Teams table, and 2 players to modify later
-- works
INSERT INTO Teams (team_name, city, primary_color, secondary_color, stadium)
VALUES ('Frogs', 'Fort Worth', 'Purple', 'Black', 'Amon G Carter Stadium');

INSERT INTO Players (first_name, last_name, team_name, position, number, height)
VALUES ('Andrew', 'Potts', 'Frogs', 'QB', 10, 6.2);

INSERT INTO Players (first_name, last_name, team_name, position, number, height)
VALUES ('John', 'Smith', 'Frogs', 'RB', 22, 5.11);

SELECT * FROM Players WHERE team_name = 'Frogs';
-- delete andrew potts from the Player Table
-- works
DELETE FROM Players
WHERE first_name = 'Andrew' AND last_name = 'Potts';
SELECT * FROM Players WHERE team_name = 'Frogs';

-- update the team in Teams table
-- works
UPDATE Teams
SET team_name = 'Horned Frogs'
WHERE team_name = 'Frogs';

-- see that the players teams are changed to Horned Frogs
-- works
SELECT first_name, last_name, team_name
FROM Players
WHERE team_name = 'Horned Frogs';

-- delete the team from Teams table
-- works
DELETE FROM Teams
WHERE team_name = 'Horned Frogs';

-- show that there are no players for the Horned Frogs because i deleted them
-- works
SELECT * FROM Players
WHERE team_name = 'Horned Frogs';

