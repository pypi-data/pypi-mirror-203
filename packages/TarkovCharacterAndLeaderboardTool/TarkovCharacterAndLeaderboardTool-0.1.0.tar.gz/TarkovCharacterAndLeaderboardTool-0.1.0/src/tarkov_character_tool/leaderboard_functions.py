import utility_funcs
from tabulate import tabulate


class LeaderboardManagementTool:

    def __init__(self, sort_by, limit, column, faction):
        self.sort_by = sort_by
        self.limit = limit
        self.column = column
        self.faction = faction
        self.offset = 10
        self.end_of_leaderboard = False

    def show_next_ten_rows(self):
        # This method fetches the next ten rows of data from the
        # leaderboard database based on the specified column and faction.

        mydb = utility_funcs.create_database_connection()
        mycursor = mydb.cursor()

        # Connection to the database is established.

        if self.limit is None:
            self.limit = 10

        # Set the limit to 10, if it is not already set.

        try:
            if self.column == 'Level':
                # If column is "Level", execute a query based on the faction.
                if self.faction == 'USEC' or self.faction == 'BEAR':
                    query = f"SELECT ROW_NUMBER() OVER " \
                            f"(ORDER BY char_level DESC) " \
                            f"as id, char_name, char_fact, char_level " \
                            f"FROM character_params " \
                            f"WHERE char_level < 80 " \
                            f"AND char_fact='{self.faction}' " \
                            f"ORDER BY char_level " \
                            f"DESC LIMIT 10 OFFSET {self.offset}"
                else:
                    query = f"SELECT ROW_NUMBER() OVER " \
                            f"(ORDER BY char_level DESC) " \
                            f"as id, char_name, char_fact, char_level " \
                            f"FROM character_params WHERE char_level < 80 " \
                            f"ORDER BY char_level " \
                            f"DESC LIMIT 10 OFFSET {self.offset}"

            elif self.column == 'Kills':
                # If column is "Kills", execute a query based on the faction
                # if specified.
                if self.faction is None:
                    query = f"SELECT ROW_NUMBER() OVER " \
                            f"(ORDER BY char_kills ASC) " \
                            f"as id, char_name, char_fact, char_kills " \
                            f"FROM character_params " \
                            f"WHERE char_fact IN ('USEC', 'BEAR') " \
                            f"ORDER BY char_kills " \
                            f"DESC LIMIT 10 OFFSET {self.offset}"
                else:
                    # If column is not "Level" or "Kills", execute a default
                    # query.
                    query = f"SELECT ROW_NUMBER() " \
                            f"OVER (ORDER BY char_kills DESC) " \
                            f"as id, char_name, char_fact, char_kills " \
                            f"FROM character_params " \
                            f"WHERE char_fact='{self.faction}' " \
                            f"ORDER BY char_kills " \
                            f"DESC LIMIT 10 OFFSET {self.offset}"
            else:
                query = f"SELECT * FROM character_params " \
                        f"WHERE char_fact IN ('USEC', 'BEAR') " \
                        f"LIMIT 10 OFFSET {self.offset}"

            mycursor.execute(query)
            myresult = mycursor.fetchall()
            # Execute the query and fetch the results.

            if len(myresult) == 0:
                # If there are no results, print a message and return N one.
                if not self.end_of_leaderboard:
                    print("\nEnd of leaderboard.\n")
                    self.end_of_leaderboard = True
                return None

            else:
                # If there are results, print the results using the tabulate
                # module and set end_of_leaderboard to False.
                self.end_of_leaderboard = False
                print(tabulate(
                    myresult,
                    headers=["Rank", "Name", "Faction", self.column],
                    tablefmt='psql'))

        except ValueError:
            # Displays an error to the user, if query failed to execute.
            print("Error occurred while executing query.")

        mycursor.close()
        mydb.close()
        # Connection is closed.

        self.offset += 10
        # With each iteration of the loop, an additional ten rows are to be
        # added.

        return self.offset
        # Value of self.offset has been returned back to the method.

    @staticmethod
    def sort_by_input():
        # The sort_by_input function prompts the user on how they wish to
        # sort the leaderboard. Currently, the user can choose if they would
        # like to sort the leaderboard by 'Level' or 'Kills'.
        try:
            user_choice = int(input("How would you like to sort the "
                                    "leaderboard?\n"
                                    "\n1: Sort by Character Level"
                                    "\n2: Sort by Character Kills \n"))

            if user_choice == 1:
                return 'Level'
            # Returns 'Level' to sort_by_input, dependent on the user input.

            elif user_choice == 2:
                return 'Kills'
            # Returns 'Kills' to sort_by_input, dependent on the user input.

            else:
                print("That was not a valid input, please try again.")
            # Anything else would display the following error to the user.

        except ValueError:
            print("Invalid input. Please choose a valid input.")
            # The ValueError exception would be raised if the user fails to
            # enter a correct key.

    def leaderboard_choice(self, sort_by, faction=None):
        # This function takes in two arguments, 'sort_by' which is required,
        # and 'faction' which is optional. The 'faction' argument is set to
        # None by default since the Global_Leaderboard function doesn't need
        # it. If the user selects a faction, the code then requires this
        # argument.

        if faction is None:
            # If 'faction' argument is None, set the offset to 10 and return
            # the result of the Global_Leaderboard function with the
            # 'sort_by' parameter passed in.
            self.offset = 10
            return self.global_leaderboard(sort_by=sort_by)

        else:
            # If 'faction' argument is not None, set the offset to 10 and
            # return the result of the Faction_Leaderboard function with both
            # 'sort_by' and 'faction' parameters passed in.
            self.offset = 10
            return self.faction_leaderboard(sort_by=sort_by, faction=faction)

    def navigation(self):
        # Ask the user how they want to sort the leaderboard.
        while True:
            # Ask the user which leaderboard they want to access.
            try:
                user_navi_choice = int(input(
                    "Would you like to access the global leaderboard, "
                    "the USEC leaderboard, the BEAR leaderboard,"
                    "return to home, or exit?\n"
                    "\n1: Global Leaderboard"
                    "\n2: USEC Leaderboard"
                    "\n3: BEAR Leaderboard"
                    "\n4: Return to Home"
                    "\n5: Exit \n"))
            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if user_navi_choice == 1:
                # Depending on the user's input, call the appropriate method
                # to generate the leaderboard.
                sort_by = LeaderboardManagementTool.sort_by_input()
                self.leaderboard_choice(sort_by=sort_by, faction=None)

                while True:
                    # If the user wants to see more than the first 10
                    # entries, loop until they're done.
                    offset = self.show_next_ten_rows()
                    if offset is None:
                        break

            elif user_navi_choice == 2:
                sort_by = LeaderboardManagementTool.sort_by_input()
                self.leaderboard_choice(sort_by=sort_by, faction='USEC')
                while True:
                    offset = self.show_next_ten_rows()
                    if offset is None:
                        break

            elif user_navi_choice == 3:
                sort_by = LeaderboardManagementTool.sort_by_input()
                self.leaderboard_choice(sort_by=sort_by, faction='BEAR')
                while True:
                    offset = self.show_next_ten_rows()
                    if offset is None:
                        break

            elif user_navi_choice == 4:
                # If the user wants to return to the main menu, call the
                # appropriate method.
                utility_funcs.Navigation.user_navigation()

            elif user_navi_choice == 5:
                # If the user wants to exit the program, call the exit()
                # function.
                exit()

            else:
                # If the user entered an invalid input, prompt them to try
                # again.
                print("Sorry. That was an incorrect response. "
                      "Please try again.")

    def global_leaderboard(self, sort_by):
        # This function is used to display a leaderboard of characters from
        # all character types and factions.

        self.offset = 10

        # Set the initial offset to 10 to display the first 10 results on the
        # leaderboard.

        mydb = utility_funcs.create_database_connection()
        mycursor = mydb.cursor()
        # Create a connection to the database and initalise the cursor.

        # Determine which query to execute based on the sorting criteria.
        if sort_by is None:
            query = "SELECT * FROM character_params"
            self.column = ''
        # If no sort criteria is provided, display all the characters in the
        # database

        elif sort_by == 'Level':
            # When sorting by level, show the top 10 characters but limit the
            # results to characters below level 80.
            query = "SELECT ROW_NUMBER() OVER (ORDER BY char_level DESC) " \
                    "as id, char_name, char_fact, char_level " \
                    "FROM character_params WHERE char_level < 80 " \
                    "ORDER BY char_level DESC LIMIT 10"
            self.column = 'Level'

        elif sort_by == 'Kills':
            # If sorting by kills, display the top 10 characters with the
            # highest number of kills
            query = "SELECT ROW_NUMBER() OVER (ORDER BY char_kills DESC) " \
                    "as id, char_name, char_fact, char_kills " \
                    "FROM character_params ORDER BY char_kills DESC LIMIT 10"
            self.column = 'Kills'

        else:
            # If sorting by faction, show the top 10 characters from the
            # specified faction(s).
            query = "SELECT * FROM character_params " \
                    "WHERE char_fact IN ('USEC', 'BEAR') DESC LIMIT 10"

        mycursor.execute(query)
        myresult = mycursor.fetchall()
        # Execute the query and fetch all the results

        print(tabulate(
            myresult,
            headers=["Rank", "Name", "Faction", self.column],
            tablefmt='psql'))
        # Display the results in a table format using the tabulate module.

        self.limit = 10
        # Set the limit to 10 to display the first 10 results on the
        # leaderboard.

        while True:
            # Keep asking the user if they want to see more results until
            # they choose to exit.
            try:
                show_more = int(input("\nWould you like to see the next 10 "
                                      "characters in the leaderboard?\n"
                                      "\n1: Yes"
                                      "\n2: No \n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if show_more == 1:
                # If the user chooses to see more results, call the
                # show_next_ten function to display the next results.
                self.limit = self.show_next_ten_rows()

                if self.limit is None:
                    break
                # If the limit is None, it means that all the results have
                # been displayed and the user wants to exit.

            elif show_more == 2:
                utility_funcs.Navigation.user_navigation()
                # If the user chooses to exit, call the user_navi function to
                # return to the main menu

            else:
                print("Invalid input. Please try again.")
                # If the user enters anything other than '1' or '2' the user
                # will continue to be asked to provide a valid input until
                # they enter one.

        mycursor.close()
        mydb.close()
        # Close the database and cursor connection.

    def faction_leaderboard(self, sort_by, faction):
        # This function takes two arguments, 'sort_by' which is the way the
        # leaderboard is sorted and 'faction' which is the faction to display
        # the leaderboard for.

        self.faction = faction
        # Set the 'faction' instance variable to
        # the passed in faction argument.

        mydb = utility_funcs.create_database_connection()
        mycursor = mydb.cursor()
        # Establish a connection to the database.

        # Check the value of the 'sort_by' argument and construct the
        # appropriate SQL query for that sort method.
        if sort_by == 'Level':
            query = f"SELECT ROW_NUMBER() OVER (ORDER BY char_level DESC) " \
                    f"as id, char_name, char_fact, char_level " \
                    f"FROM character_params WHERE char_level < 80 " \
                    f"AND char_fact = '{self.faction}' " \
                    f"ORDER BY char_level DESC LIMIT 10"
            self.column = 'Level'

        elif sort_by == 'Kills':
            query = f"SELECT ROW_NUMBER() OVER (ORDER BY char_kills DESC) " \
                    f"as id, char_name, char_fact, char_kills " \
                    f"FROM character_params " \
                    f"WHERE char_fact = '{self.faction}' " \
                    f"ORDER BY char_kills DESC LIMIT 10"
            self.column = 'Kills'

        else:
            query = f"SELECT * FROM character_params " \
                    f"WHERE char_fact = '{self.faction}'"
            self.column = ''

        mycursor.execute(query)
        myresult = mycursor.fetchall()
        # Execute the selected query and fetch the results.

        print(tabulate(
            myresult,
            headers=["Rank", "Name", "Faction", self.column],
            tablefmt='psql'))
        # Display the leaderboard result using the 'tabulate' function with
        # appropriate headers.
        self.limit = 10
        # Set the 'limit' instance variable to 10.

        while True:
            # Keep asking the user if they want to see more results until
            # they choose to exit.
            try:
                show_more = int(input("\nWould you like to see the next 10 "
                                      "characters in the leaderboard?\n"
                                      "\n1: Yes"
                                      "\n2: No \n"))
            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue
            if show_more == 1:
                self.limit = self.show_next_ten_rows()

                if self.limit is None:
                    break
            elif show_more == 2:
                utility_funcs.Navigation.user_navigation()
            else:
                print("Invalid input. Please try again.")

        mycursor.close()
        mydb.close()
        # Close the cursor and the database connection.
