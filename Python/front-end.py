import mysql.connector

# Replace the values below with your actual database credentials
db_config = {
    'host': 'localhost', 
    'user': 'root',
    'password': 'chargers25',
    'database': 'nfl' 
}

def get_qb_players():
    query = "SELECT first_name, last_name FROM Players WHERE position = 'QB' LIMIT 10"
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        
        result = cursor.fetchall()
        print(f"10 Players with position QB:")
        for row in result:
            print(row)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def get_playoff_players():
    query = """
    SELECT first_name, last_name
    FROM Players
    WHERE team_name IN (
        SELECT team_name
        FROM Playoffs
        WHERE year = '2023'
    )
    LIMIT 10
    """
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        
        result = cursor.fetchall()
        print(f"10 Players who played in the 2023 playoffs:")
        for row in result:
            print(row)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def show_players_for_team(team_name):
    query = f"""
    SELECT first_name, last_name, position, number, height
    FROM Players
    WHERE team_name = '{team_name}'
    """
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        
        result = cursor.fetchall()
        print(f"Players for team '{team_name}':")
        for row in result:
            print(row)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def insert_new_team_and_players():
    team_name = input("Enter the new team name: ")
    city = input("Enter the team city: ")
    primary_color = input("Enter the primary color: ")
    secondary_color = input("Enter the secondary color: ")
    stadium = input("Enter the team stadium: ")

    query_team = f"""
    INSERT INTO Teams (team_name, city, primary_color, secondary_color, stadium)
    VALUES ('{team_name}', '{city}', '{primary_color}', '{secondary_color}', '{stadium}')
    """
    
    # Predefined list of players to insert
    predefined_players = [
        {"first_name": "John", "last_name": "Doe", "position": "QB", "number": 12, "height": 6.4},
        {"first_name": "Mike", "last_name": "Smith", "position": "WR", "number": 88, "height": 6.1},
        {"first_name": "James", "last_name": "Brown", "position": "RB", "number": 22, "height": 5.9},
        {"first_name": "Chris", "last_name": "Johnson", "position": "ILB", "number": 56, "height": 6.2}
    ]
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Insert the team into the database
        cursor.execute(query_team)
        
        # Insert predefined players for the new team
        for player in predefined_players:
            query_player = f"""
            INSERT INTO Players (first_name, last_name, team_name, position, number, height)
            VALUES ('{player["first_name"]}', '{player["last_name"]}', '{team_name}', '{player["position"]}', {player["number"]}, {player["height"]})
            """
            cursor.execute(query_player)
        
        connection.commit()
        print(f"Successfully inserted team {team_name} and players.")
        
        show_players_for_team(team_name)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def delete_team():
    team_name = input("Enter the name of the team to delete: ")
    
    query = f"""
    DELETE FROM Teams
    WHERE team_name = '{team_name}'
    """
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        
        connection.commit()
        print(f"Team '{team_name}' deleted.")
        

        query_check_players = f"""
        SELECT first_name, last_name
        FROM Players
        WHERE team_name = '{team_name}'
        """
        cursor.execute(query_check_players)
        result = cursor.fetchall()
        if result:
            print(f"Players still exist for team '{team_name}':")
            for row in result:
                print(row)
        else:
            print(f"No players found for team '{team_name}'.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def main():
    get_playoff_players()
    get_qb_players()
    insert_new_team_and_players()
    delete_team()


if __name__ == "__main__":
    main()
