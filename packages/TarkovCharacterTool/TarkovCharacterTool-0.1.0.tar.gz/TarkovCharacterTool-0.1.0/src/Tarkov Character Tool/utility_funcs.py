import character_operations
import mysql.connector
import leaderboard_functions

from config_file import PASSWORD


class Navigation:
    @staticmethod
    def user_navigation():
        while True:
            try:
                x = int(input("Would you like to create a character, "
                              "access an existing character, view the current "
                              "leaderboard rankings, or exit?\n"
                              "\n1: Create A Character "
                              "\n2: Access Existing Character "
                              "\n3: Leaderboard Rankings"
                              "\n4: Exit \n"))

            except ValueError:
                print("Invalid input. Please choose a valid option.")
                continue

            if x == 1:
                create_new_char = character_operations.CharacterCreator()
                create_new_char.get_character_name()

            elif x == 2:
                access_char = character_operations.CharacterManager()
                access_char.check_existing_character()

            elif x == 3:
                lbmt = leaderboard_functions.LeaderboardManagementTool(
                    column='',
                    limit=0,
                    sort_by='',
                    faction='')
                lbmt.navigation()

            elif x == 4:
                exit()

            if x not in (1, 2, 3, 4):
                print("Sorry. That was an incorrect response. "
                      "Please try again.")
                continue


def create_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="tarkovcharacterdatabase"
    )


class KappaFunctions:
    KAPPA_CONTAINER = {
        "Kappa": {
            "Level Requirement": 55,
            "Kappa Container Slots": 12,
            "Weight": "2 kg"
        }
    }

    @staticmethod
    def kappa_level_subtraction(char_level):
        if char_level is None:
            return None

        kap_lvls = KappaFunctions.KAPPA_CONTAINER["Kappa"]["Level Requirement"]
        remaining_level_calc = kap_lvls - char_level
        return remaining_level_calc

    @staticmethod
    def kappa_level_requirements(char_level):
        if char_level is None:
            print("Cannot determine your Kappa Container eligibility "
                  "as character level is None.")
            return

        if char_level <= \
                KappaFunctions.KAPPA_CONTAINER["Kappa"]["Level Requirement"]:
            print("You do not have the Kappa Container." + "\n")
            remaining_lvl = KappaFunctions.kappa_level_subtraction(char_level)

            if remaining_lvl is not None:
                print("You have", remaining_lvl, "levels remaining.")

        else:
            print("Congratulations. You are the required level to unlock the "
                  "Kappa Container!")
