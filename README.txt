
This is a basic NFL database system. The main goal is to be able to find records, and random facts from nfl history. The database consists of 8 tables:

Teams:
Stores: Information about NFL teams, including team name, city, primary and secondary colors, and stadium.
Key columns: team_name, city, primary_color, secondary_color, stadium.
Primary Key: team_name.
Relationship: This table is a parent table for multiple others. Other tables reference the team_name column to associate data with a specific team.

Head_Coaches:
Stores: Information about head coaches, including their names, associated team, and their win-loss record.
Key columns: first_name, last_name, team_name, wins, losses.
Primary Key: (first_name, last_name).
Foreign Key: team_name references Teams(team_name).
Relationship: Each head coach is associated with a team via team_name. This ensures that a head coach can only belong to an existing team.

Players:
Stores: Player data, including their name, position, number, height, and the team they play for.
Key columns: first_name, last_name, team_name, position, number, height.
Primary Key: (first_name, last_name).
Foreign Keys:
team_name references Teams(team_name).
Relationships:
Players are associated with teams through team_name.
Players can only exist for a team that exists in the Teams table.
The position column has a restricted set of valid values, which reflects the various football player positions (e.g., QB, RB, WR, etc.).

Awards:
Stores: Awards received by players, such as MVP, DPOY, etc.
Key columns: first_name, last_name, award_type, year, team_name.
Primary Key: award_id.
Foreign Keys:
first_name, last_name references Players(first_name, last_name).
team_name references Teams(team_name).
(year, team_name) references Season(season_year, team_name).
Relationships:
The award is tied to a player via first_name and last_name, ensuring that an award can only be assigned to an existing player.
The team_name references the team associated with the player.
The year and team_name references the corresponding season data.

Playoffs:
Stores: Information about playoff games, including the year, round (e.g., Wild Card, Divisional, Super Bowl), and the teams involved (winner and loser).
Key columns: year, round, game_number, team_winner, team_loser.
Primary Key: (year, game_number).
Foreign Keys:
team_winner references Teams(team_name).
team_loser references Teams(team_name).
Relationships:
The playoff game is tied to specific teams, with each team identified by team_winner and team_loser, which are foreign keys referencing the Teams table.
This relationship helps track which teams played and won or lost in specific playoff rounds.

Season:
Stores: Season data for each team, including the number of wins, losses, and playoff qualification.
Key columns: season_year, team_name, wins, losses, playoffs.
Primary Key: (season_year, team_name)
Foreign Key: team_name references Teams(team_name)
Relationships:
Each entry in the Season table is associated with a team via team_name, and each entry corresponds to a specific season (season_year).
This table helps track performance across different seasons for each team.
The playoffs field is a boolean indicating whether the team made it to the playoffs (0 for no, 1 for yes).

Regular_Season_Games:
Stores: Information about regular season games, including the winning and losing team and their respective scores.
Key columns: game_id, year, winner, loser, winner_points, loser_points.
Primary Key: game_id
Foreign Keys:
(year, winner) references Season(season_year, team_name).
winner and loser both reference Teams(team_name).
Relationships:
Each game result is tied to a specific season and teams.
The winner and loser columns ensure that only existing teams can be assigned as the winner or loser.
This table tracks individual game results for the regular season.

Super_Bowls:
Stores: Data about the Super Bowl, including the winning and losing teams.
Key columns: year, team_winner, team_loser.
Primary Key: year
Foreign Keys:
team_winner and team_loser both reference Teams(team_name).
(year, team_winner) and (year, team_loser) reference Season(season_year, team_name).
Relationships:
This table links the Super Bowl results to the winning and losing teams.
The year column ties each Super Bowl to a specific season, and the team_winner and team_loser columns reference teams that played in the Super Bowl.

I got the data from chatgpt, Chatgpt is not fully updated with infromation today, so it is not fully accurate, so some of it is fictional


Pre-requisites:
MySQL Installation:

Ensure MySQL Server is installed on your machine or use a MySQL database you have access to.
The MySQL server must be running, and you should have the credentials to access the database.
Python Environment:

Ensure Python is installed on your system.
Install the required library mysql-connector-python to establish the connection between Python and MySQL:
bash
pip install mysql-connector-python

Database Credentials:

Update the database connection credentials in the script with your MySQL username, password, and host (if applicable):
python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'nfl'
}
Save the Script:

Save the Python code in front-end.py.
Run the Script:

Open a terminal or command prompt.
Navigate to the directory where the front-end.py file is saved.
Execute the script by running the following command:
python front-end.py

Functions in the Script:
get_qb_players():

Fetches and prints a list of quarterbacks (position = 'QB') from the Players table.
get_playoff_players():

Fetches and prints players who played in the 2023 playoffs from the Players table.
insert_new_team_and_players():

Prompts for input to add a new team to the Teams table, including the team’s name, city, primary and secondary colors, and stadium.
Inserts a predefined list of players for the new team.
Displays the players of the newly added team.
delete_team():

Prompts for a team name to delete from the Teams table.
After deletion, checks that players associated with the deleted team no longer exist in the Players table.
show_players_for_team():

Displays all players for a specific team by querying the Players table using the team’s name.
