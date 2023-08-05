import mysql.connector
import utility_funcs

from leaderboard_functions import LeaderboardManagementTool


class PlayableCharacters:
    def __init__(self, char_name, char_type, char_fact,
                 char_voice, char_level, char_kills):
        try:
            self.mydb = utility_funcs.create_database_connection()

        except mysql.connector.Error as err:
            print("Connection error:", err)
            exit()

        self.char_name = char_name
        self.char_type = char_type
        self.char_fact = char_fact
        self.char_voice = char_voice
        self.char_level = char_level
        self.char_kills = char_kills

    def __str__(self):
        return f"\nName: {self.char_name} \nType: {self.char_type}\n" \
               f"\nFaction: {self.char_fact} \nVoice: {self.char_voice}\n" \
               f"\nLevel: {self.char_level} \nKills: {self.char_kills}\n"

    character = None


class PMC_USEC(PlayableCharacters):
    def __init__(self, char_name, char_voice, char_level, char_kills):
        self.char_voice = char_voice
        super().__init__(char_name, "PMC", "USEC",
                         char_voice=self.char_voice,
                         char_level=char_level,
                         char_kills=char_kills)


class PMC_BEAR(PlayableCharacters):
    def __init__(self, char_name, char_voice, char_level, char_kills):
        self.char_voice = char_voice
        super().__init__(char_name, "PMC", "BEAR",
                         char_voice=self.char_voice,
                         char_level=char_level,
                         char_kills=char_kills)


class PlayerScav(PlayableCharacters):
    def __init__(self, char_name):
        super().__init__(char_name, "Scav", "Scavenger", "Russian", None, None)


def insert_char_to_database(character):
    try:
        mydb, cursor = establish_database_connection()

        values = (character.char_name,
                  character.char_type,
                  character.char_fact,
                  character.char_voice,
                  character.char_level,
                  character.char_kills)

        sql = "INSERT INTO character_params (char_name, " \
              "char_type, char_fact, char_voice, char_level, char_kills) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(sql, values)

        mydb.commit()

        print(cursor.rowcount, "character inserted.")

    except mysql.connector.Error as error:
        print("Failed to insert character into MySQL table {}".format(error))


def establish_database_connection():
    try:
        mydb = utility_funcs.create_database_connection()

    except mysql.connector.Error as err:
        print("Connection error:", err)
        exit()

    cursor = mydb.cursor()
    return mydb, cursor


def close_database_connection(mydb, cursor):
    cursor.close()
    mydb.close()


class CharacterCreator(PlayableCharacters):
    def __init__(self):
        super().__init__(char_name=None,
                         char_type=None,
                         char_fact=None,
                         char_voice=None,
                         char_level=None,
                         char_kills=None)

    def get_character_name(self):
        mydb, cursor = establish_database_connection()

        while True:
            self.char_name = input(
                "What would you like to name your character?\n")

            if not self.char_name:
                print("Sorry, you must enter a name for your character.")

            if self.char_name.isdigit():
                print("Sorry, the name cannot be all digits. "
                      "Please enter a valid name.")

            else:
                cursor.execute(
                    "SELECT * FROM character_params WHERE char_name = %s",
                    (self.char_name,))
                if cursor.fetchone():
                    print("Sorry, that character name already exists. "
                          "Please choose another.")

                else:
                    self.character_name_confirmation()
                    return self.char_name

    def character_name_confirmation(self):

        while True:
            char_name_confirm_choice = input(
                f"Your character's name is {self.char_name} "
                f"would you like to keep it?\n"
                f"1: Keep\n"
                f"2: Change\n")

            if char_name_confirm_choice == "1":
                print("Your character's name has been saved.")

                self.get_character_type()

            elif char_name_confirm_choice == "2":
                self.get_character_name()

            else:
                print("Sorry that was an incorrect input. Please try again.")

    def get_character_type(self):
        character_type_choice = None

        while True:
            try:
                character_type_choice = int(
                    input("What character type would you like?\n"
                          "1: PMC\n"
                          "2: Scav\n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")

            if character_type_choice == 1:
                self.char_type = 'PMC'
                print(f"Your character is successfully "
                      f"a {self.char_type} .")

            elif character_type_choice == 2:
                self.char_type = 'Scav'
                self.scav_character_type()
                break

            else:
                print("That was not a valid option. Please try again.")

            self.get_character_faction()
            return self.char_type

    def scav_character_type(self):
        character = PlayerScav(self.char_name)

        print(
            f"Your character is successfully a {self.char_type} a part "
            f"of the {self.char_fact} faction.")

        insert_char_to_database(character)
        print(character)

        while True:
            try:
                final_navi = int(input(
                    "\nWould you like to create another character or exit?\n"
                    "1: Create Another Character\n"
                    "2: Access Leaderboard\n"
                    "3: Exit\n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if final_navi == 1:
                self.get_character_name()

            elif final_navi == 2:
                lbmt = LeaderboardManagementTool(column='', faction='',
                                                 limit=10, sort_by='')
                lbmt.navigation()

            elif final_navi == 3:
                exit()

            else:
                print("Sorry that was an incorrect input. Please try again.")

    def get_character_faction(self):
        character_faction_choice = None

        while True:
            try:
                character_faction_choice = int(input(
                    "What faction do you want your character "
                    "to be a part of?\n"
                    "1: USEC\n"
                    "2: BEAR\n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")

            if character_faction_choice == 1:
                self.char_fact = 'USEC'
                print(
                    f"Your character is successfully a part of"
                    f" the {self.char_fact} faction.")

            elif character_faction_choice == 2:
                self.char_fact = 'BEAR'
                print(
                    f"Your character is successfully a part of"
                    f" the {self.char_fact} faction.")

            self.select_character_voice(self.char_fact)

            return self.char_fact

    def select_character_voice(self, char_fact):
        mycursor = self.mydb.cursor()

        if char_fact == 'USEC':
            mycursor.execute("SELECT usec_voices FROM usec_voices")

        elif char_fact == 'BEAR':
            mycursor.execute("SELECT bear_voices FROM bear_voices")

        voices = [row[0] for row in mycursor.fetchall()]

        while True:
            try:
                print("Please choose a voice for your character:\n")

                for i, voice in enumerate(voices):
                    print(f"{i + 1}: {voice}")

                char_voice_creation = int(input())

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if 1 <= char_voice_creation <= len(voices):
                self.char_voice = voices[char_voice_creation - 1]
                print(f"Your character's voice is set to {self.char_voice}.")
                self.get_character_level()
                return self.char_voice

            else:
                print("Sorry that was an incorrect input. Please try again.")

        mycursor.close()

    def get_character_level(self):
        while True:
            try:
                self.char_level = int(input("What level is your character?\n"))

            except ValueError:
                print(
                    "User failed to provide a level, level has been set to 0.")
                self.char_level = 0

            print(f"Your character's level is set to {self.char_level}.")

            self.get_character_kills()
            return self.char_level

    def get_character_kills(self):
        while True:
            try:
                self.char_kills = int(
                    input("How many character kills do you have?\n"))

            except ValueError:
                print("User failed to provide a kill amount, "
                      "kills have been set to 0.")
                self.char_kills = 0

            print(f"Your character has {self.char_kills} kills.")

            character = PlayableCharacters(
                self.char_name,
                self.char_type,
                self.char_fact,
                self.char_voice,
                self.char_level,
                self.char_kills)

            insert_char_to_database(character)

            print(character)

            self.end_of_character_navigation()
            return self.char_kills

    def end_of_character_navigation(self):
        while True:
            try:
                final_navi = int(
                    input("Would you like to create another character, "
                          "see your Kappa Progression, access the "
                          "Leaderboard, or exit? \n"
                          "1: Create Another Character \n"
                          "2: See Kappa Progression \n"
                          "3: Access Leaderboard \n"
                          "4: Return Home \n"
                          "5: Exit \n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if final_navi == 1:
                self.get_character_name()
                continue

            elif final_navi == 2:
                kappa_levels = self.char_level
                utility_funcs.KappaFunctions.kappa_level_requirements(
                    char_level=kappa_levels)

            elif final_navi == 3:
                lbmt = LeaderboardManagementTool(column='', faction='',
                                                 limit=10, sort_by='')
                lbmt.navigation()

            elif final_navi == 4:
                utility_funcs.Navigation.user_navigation()

            elif final_navi == 5:
                exit()

            else:
                print("Sorry that was an incorrect input. Please try again.")


class CharacterManager:
    def check_existing_character(self):
        try:
            mydb = utility_funcs.create_database_connection()

        except mysql.connector.Error as err:
            print("Connection error:", err)
            exit()

        cursor = mydb.cursor()

        while True:
            try:
                char_name = input("Please enter your character name:\n")

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            cursor.execute(
                'SELECT * FROM character_params WHERE char_name = %s',
                (char_name,))

            character_data = cursor.fetchone()

            if character_data:
                print(f"Name: {character_data[1]}")
                print(f"Type: {character_data[2]}")
                print(f"Faction: {character_data[3]}")
                print(f"Voice: {character_data[4]}")
                print(f"Level: {character_data[5]}")
                print(f"Kills: {character_data[6]}")

            else:
                print("\nSorry, no character found with that name.\n")
                while True:
                    try:
                        create_new_char = input(
                            "Would you like to create a new character "
                            "instead?\n"
                            "1: Yes\n"
                            "2: No\n")

                    except ValueError:
                        print("Invalid input. Please choose a valid option.")
                        continue

                    if create_new_char == "1":
                        new_char_creation = CharacterCreator()
                        new_char_creation.get_character_name()
                        return

                    elif create_new_char == "2":
                        break

                    else:
                        print(
                            "Sorry that was an incorrect input. Please try "
                            "again.")

                    close_database_connection(mydb, cursor)

            while True:
                try:
                    mydb = utility_funcs.create_database_connection()

                except mysql.connector.Error as err:
                    print("Connection error:", err)
                    exit()

                cursor = mydb.cursor()

                try:
                    cursor.execute(
                        "SELECT * FROM character_params "
                        "WHERE char_type = 'Scav' "
                        "AND char_name = %s",
                        (char_name,))

                    scav_kappa_check = cursor.fetchone()

                    if scav_kappa_check:
                        x = int(input(
                            "\nWould you like to access another existing "
                            "character, create a character, or "
                            "would you like to exit?\n"
                            "\n1: Access Another Character"
                            "\n2: Create A Character "
                            "\n3: Exit\n"))

                    else:
                        x = int(input(
                            "\nWould you like to access another existing "
                            "character, create a character, or would you "
                            "like to exit?\n"
                            "\n1: Access Another Character"
                            "\n2: Create A Character "
                            "\n3: See Kappa Progression "
                            "\n4: Return to Home "
                            "\n5: Exit \n"))
                except ValueError:
                    print("Invalid input. Please choose a valid option.")
                    continue

                if x == 1:
                    CharacterManager.check_existing_character(self)
                    continue

                elif x == 2:
                    create_new_char = CharacterCreator()
                    create_new_char.get_character_name()
                    continue

                elif x == 3:
                    cursor.execute(
                        "SELECT * FROM character_params "
                        "WHERE char_type = 'Scav' "
                        "AND char_name = %s",
                        (char_name,))

                    scav_check = cursor.fetchone()

                    if scav_check:
                        exit()

                    else:
                        kappa_levels = character_data[5]
                        utility_funcs.KappaFunctions.kappa_level_requirements(
                            char_level=kappa_levels)

                    close_database_connection(mydb, cursor)

                elif x == 4:
                    utility_funcs.Navigation.user_navigation()

                elif x == 5:
                    exit()

                else:
                    print(
                        "Sorry that was an incorrect input. Please try again.")
