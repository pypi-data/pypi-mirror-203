import utility_funcs


class home_page:
    @staticmethod
    def home():
        utility_funcs.Navigation.user_navigation()

    print("Welcome to the Tarkov Character Creation and Leaderboard Tool.\n")


if __name__ == '__main__':
    home_page.home()
