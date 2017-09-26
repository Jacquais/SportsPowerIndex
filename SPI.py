import requests
import time
import sys
import csv
import os.path
from random import randint
import platform

x = randint(0, 4)
Formula = None


def Quit():
    print("\nBye Bye!")
    time.sleep(.5)
    sys.exit()


try:
    if platform.system() == "Windows":
        os.system('mode con: cols=115 lines=60')
        input("Press any key to continue...")
    elif platform.system() == "Darwin":
        os.system('printf "\e[8;60;115;t"')
        os.system('clear')
        input("Press any key to continue...")
    if x == 0:
        print('''
    #######################################
    #######################################
    ############   #(    /#   #   #########
    ############   #  (#  #   #  ##########
    ############   #  ##  #      ##########
    ############   #  #####     ###########
    ############   #  #####     ,##########
    ########   #   #  ##,,#   ,  ##########
    ########   #   #  ##  #   #  ##########
    ########      /#      #   #   #########
    ##########  .#####  ###///#///#########
    #######################################\n\n''')
    elif x == 1:
        print('''
       _____ _____ _____
      / ____|  __ \_   _|
     | (___ | |__) || |
      \___ \|  ___/ | |
      ____) | |    _| |_
     |_____/|_|   |_____|
    \n\n
                         ''')
    elif x == 2:
        print('''
                                 .*(%&&%%#*.
                    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@*
                &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
            /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
       ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@/      /@@@@@@@@@@@@@@@@@@@@(       %@@@@@@@
        ,@@@(    .,       .@@@@@@@@@@@@@@/       ((     @@@.  *
    *.  .@.  (@@@@@@@@        @@@@@@@@*       @@@@@@@@@  ,@
         @@@@@@@@@@@@@@@.       @@@@.      .@@@@@@@@@@@@@@@ ...
    @(   @@@@@@@@@@@@@@@@@% .  .@@@@&    (@@@@@@@@@@@@@@@@@.
      %@@@@% @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (@@@@@
    @@@@@@/ @@@@@#        @@@@@@@@@@@@@@@@         @@@@@ &@@@@@
    @@@@@@*/@@@@.          ,@@@@.@@@%@@@%           @@@@.@@@@@@
    @@@@@@@&@@@%           @@@@@.@@@%&@@@.          &@@@@@@@@@@
    @@@@@@@@@.,@@@@@@@@@& &@@@@/(@@@@,@@@& #@@@@@@@@@@.@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@ %@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@*,@@@@@@@@@@@@@@@ @@@@@@@@@@@ &@@@@@@@@@@@@@% @@@@@@
    @@@@@  .@@@@@@@@@@@@@@@ @@@@@@@@@@@@@ @@@@@@@@@@@@@@(  @@@@
    @@@/   @@@@@@@@@@@@@@@@.@@@@@@@@@@@@@*@@@@@@@@@@@@@@@   *@@
    @@/    .@@@@@@@@@@@@*     *@@@@@@&      ,@@@@@@@@@@@ .. .%@
    @@        @@@@@&.           %@@/            .@@@@&     . .@
    @@                                                   .   /@
    @@,                                        .    .       .@@
    .#@.                                       .  . .   . . @@
     . @@                     .       .. ..   .   ......  &@@..
       .@@@@@@@@@@@@@@@@@#/@@@//((#%@@@(,%&@@@@@@@@@@@@@@&...
    ...  @@@@@@@@@@@@@( .. .  .       . .. ...@@@@@@@@@@@@@....
    . . ..@@@@@@@@@@@@@@@            . ..  /@@@@@@@@@@@@@@. ...
          @@@@@@@@@@@@@@@@@@,       ..  #@@@@@@@@@@@@@@@@@ ....
    .... .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....
    .   . .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......
    . .  . %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%......
     ..  .. /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.......
    .... ...  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ........
    ...... ..  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,..........
    ....... . ... @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.............
    .... ....... ...&@@@@@@@@@@@@@@@@@@@@@@@@@@%...............
    ...... ........ ..@@@@@@@@@@@@@@@@@@@@@@@@.................
    /(////(//////((((##@@@@@@@#%%#%%&@@@@@@@@@@@&&&&&&&&&&&&&@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @*   &@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@@@@@@..#@@@@@@@@@
    #.*@@@@@*.%..@@@..&.@@@@  * @@@... @@@@%., %@@/.....@@ .@@.
    ... .&@,.*@@@@@..#@..@@ .@@&&@@@@. @@@@. @..#@@..%@@@@..@@.
    /./@@@@@@@@..@@..#@..@@ .@@@@@@@@. @@@@. @@@@@@..%@@@@..@@.
    *.(@@@@...#.%@@&. ..&@@& * .@@@......@@%...%@@@@....@@@.@. \n\n''')
    elif x == 3:
        print('''
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&(@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@
    @@&&@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@&&@@
    @@&&&&&&@@@@@@@&&&&&&&&&&&&&&/   ((/&&&&&&&&&@@@@&&&&&&&&@@
    @@&&&&&&&&&&&&&&&%&&&&&&&%   . .&   &&&&&&&&&&&&&&&&&&&&&@@
    @@&&&&& *&&&&&&&& &&&&&&   #   &    #&& &&&&&&&& (&&&&&@@
    @@&&&%    &&&&&/   (&&&    *      /&&,   %&&&&%   .&&&&@@
    @@&&&& %# &&&&&(,&.#&&* .&%         &&&./& %&&&&& %( &&&&@@
    @@&&&&&&&&&&&&&&&&&&&&   %         *&&&&&&&&&&&&&&&&&&&&&@@
    @@&&&&&,#&&&&&&&& &&&&  %         %&&&&&% &&&&&&&&.%&&&&&@@
    @@&&&,    (&&&%     &&...       #&&&&    .&&&&.    #&&&@@
    @@&&&& ,  &&&& ( %&&    ,&&&&&&&&&&/ / &&&&&& , ,&&&&@@
    @@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@
    @@&&,                                                 &&&@@
    @@&&,  ,***//   ,,,,,,,  ............  ,,,,,,,        &&&@@
    @@&&,  (######  (######. ############..#######        &&&@@
    @@&&,   ,#####.  ,####*  .####(//(###. ,#####         &&&@@
    @@&&,    ######   ####    (###(   (##.  ####(         &&&@@
    @@&&,    (#####(  ####    /###(         ####(         &&&@@
    @@&&.    (######. ####    /###(  ,##    ####(         &&&@@
    @@&&.    (####### ####    /#########    ####(         %&&@@
    @@&&.    (###.###(####    /#########    ####(         %&&@@
    @@&&.    (### (#######    /###/  .##    ####(         %&&@@
    @@&&.    (###  #######    /###/         ####(   ###   %&&@@
    @@&&.    /###   ######    /###/         ####(   ###   %&&@@
    @@&&.  /#####*  /#####    *###/         ####((#####   %&&@@
    @@&  (######(  #####    *###/        ,###########   &&&@@
    @@%&      ./#   ####   *####/        ######,       *&&&@@
    @@@,&&&&.           .(   ######/                   /&&&&@@@
    @@@@@@%&&&&&&%/            ,####             ,#&&&&&@@@@@
    @@@@@@@@@@@@&&&&&&&&&&,              (&&&&&&&&&&(@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@&&&&&&.     .&&&&&&&@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@%&&&, #&&&%@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&%@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n
        ''')
    elif x == 4:
        print('''
      _   _      _ _        __        __         _     _
     | | | | ___| | | ___   \ \      / /__  _ __| | __| |
     | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |
     |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |
     |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_|
                                                         ''')


    def NCAA():
        print("Not Implemented.")


    def NFL():
        FormulaFolder = os.path.join(os.path.expanduser('~'), 'Documents', "SPI")
        FormulaFile = FormulaFolder + "/Formulas.csv"

        def fetch(week):
            print("Fetching data from week {}".format(week))
            schedule = requests.get(
                'http://api.sportradar.us/nfl-ot2/games/2017/REG/schedule.json?api_key=z45b8e45rg282tyqq686g5n5')
            schedule = schedule.json()
            GamesCount = len(schedule["weeks"][week]["games"])
            games = -1
            teams = {}
            week -= 1
            global Formula
            EPI = input("[-1]Use EPI.\n"
                        "[Anything else]Dont.")
            if EPI != "-1":
                # GET FORMULA IF ONE CREATED
                if platform.system() == "Darwin":
                    if os.path.isfile(FormulaFile):
                        with open(FormulaFile) as csvfile:
                            readCSV = csv.reader(csvfile, delimiter=',')
                            formulas = []
                            num = [0]
                            for row in readCSV:
                                num[0] += 1
                                num[0] = str(num[0])
                                row[:0] = num
                                formulas.append(row)
                                print(formulas)
                                num[0] = int(num[0])
                        breakloop = False
                        while True:
                            for x in range(len(formulas)):
                                print("[" + str(formulas[x][0]) + "]" + str(formulas[x][1]))
                            print("[99]Back")
                            form = input("Select formula: ")
                            if form == "99":
                                print()
                                return
                            print(len(formulas))
                            for x in range(len(formulas)):
                                if form == formulas[x][0]:
                                    Formula = formulas[x]
                                    breakloop = True
                                    break
                            if breakloop:
                                break
                            elif breakloop:
                                print("Invalid Choice\n")
                elif platform.system() == "Windows":
                    if os.path.isfile("C:\\ProgramData\\Sports Power Index\\Formulas.csv"):
                        with open('C:\\ProgramData\\Sports Power Index\\Formulas.csv') as csvfile:
                            readCSV = csv.reader(csvfile, delimiter=',')
                            formulas = []
                            num = [0]
                            for row in readCSV:
                                num[0] += 1
                                num[0] = str(num[0])
                                row[:0] = num
                                formulas.append(row)
                                num[0] = int(num[0])
                        breakloop = False
                        while True:
                            for x in range(len(formulas)):
                                print("[" + str(formulas[x][0]) + "]" + str(formulas[x][1]))
                            print("[99]Back")
                            form = input("Select formula: ")
                            if form == "99":
                                print()
                                return
                            for x in range(len(formulas)):
                                if form == formulas[x][0]:
                                    Formula = formulas[x]
                                    breakloop = True
                                    break
                                else:
                                    print("Invalid Choice\n")
                                    break
                            if breakloop:
                                break

            print("Getting Data and Calculating\n")
            # GET TEAMS
            for _ in range(GamesCount):
                games += 1
                homenamekey = 'HomeName' + str(games)
                homeidkey = 'HomeID' + str(games)
                awaynamekey = 'AwayName' + str(games)
                awayidkey = 'AwayID' + str(games)
                teams[homeidkey] = schedule["weeks"][week]["games"][games]["home"]["id"]  # Home Team ID
                teams[homenamekey] = schedule["weeks"][week]["games"][games]["home"]["name"]  # Home Team Name
                teams[awayidkey] = schedule["weeks"][week]["games"][games]["away"]["id"]  # Away Team ID
                teams[awaynamekey] = schedule["weeks"][week]["games"][games]["away"]["name"]  # Away Team Name

                # CALCULATE
                time.sleep(1)
                HomeCall = requests.get("http://api.sportradar.us/nfl-ot2/seasontd/2017/REG/teams/" + teams[
                    homeidkey] + "/statistics.json?api_key=z45b8e45rg282tyqq686g5n5")
                HomeCall = HomeCall.json()

                time.sleep(1)
                AwayCall = requests.get("http://api.sportradar.us/nfl-ot2/seasontd/2017/REG/teams/" + teams[
                    awayidkey] + "/statistics.json?api_key=z45b8e45rg282tyqq686g5n5")
                AwayCall = AwayCall.json()


                hometouchdowns = HomeCall["record"]["touchdowns"]["total"]
                hometouchdownspergame = hometouchdowns / HomeCall["record"]["games_played"]

                homepasstouchdowns = HomeCall["record"]["touchdowns"]["pass"]
                homepasstouchdownspergame = homepasstouchdowns / HomeCall["record"]["games_played"]
                homeopponentpasstouchdownspergame = HomeCall["opponents"]["passing"]["touchdowns"] / HomeCall["opponents"]["games_played"]

                homerushtouchdowns = HomeCall["record"]["touchdowns"]["rush"]
                homerushtouchdownspergame = homerushtouchdowns / HomeCall["record"]["games_played"]
                homeopponentrushtouchdownspergame = HomeCall["opponents"]["rushing"]["touchdowns"] / HomeCall["opponents"]["games_played"]

                homerushyards = HomeCall["record"]["rushing"]["yards"]
                homerushyardspergame = homerushyards / HomeCall["record"]["games_played"]
                homeopponentrushyardspergame = HomeCall["opponents"]["rushing"]["yards"] / HomeCall["opponents"]["games_played"]

                homepassyards = HomeCall["record"]["passing"]["yards"]
                homepassyardspergame = homepassyards / HomeCall["record"]["games_played"]
                homeopponentpassyardspergame = HomeCall["opponents"]["passing"]["yards"] / HomeCall["opponents"]["games_played"]

                homerushespergame = HomeCall["record"]["rushing"]["attempts"] / HomeCall["record"]["games_played"]
                homepassespergame = HomeCall["record"]["passing"]["attempts"] / HomeCall["record"]["games_played"]
                homeopponentpassespergame = HomeCall["opponents"]["passing"]["attempts"] / HomeCall["opponents"]["games_played"]
                homeopponentrushespergame = HomeCall["opponents"]["rushing"]["attempts"] / HomeCall["opponents"]["games_played"]

                homefieldgoalspergame = HomeCall["record"]["field_goals"]["made"] / HomeCall["record"]["games_played"]
                homeconversions = HomeCall["record"]["extra_points"]["conversions"]["pass_successes"] + HomeCall["record"]["extra_points"]["conversions"]["rush_successes"]
                homeconversionspergame = homeconversions / HomeCall["record"]["games_played"]

                homepointspergameallowed = (
                                            (6*HomeCall["opponents"]["touchdowns"]["total"])+
                                            (3*HomeCall["opponents"]["field_goals"]["made"])+
                                            (HomeCall["opponents"]["extra_points"]["kicks"]["made"])+
                                            (2*(HomeCall["opponents"]["extra_points"]["conversions"]["pass_successes"] + HomeCall["opponents"]["extra_points"]["conversions"]["rush_successes"]))
                                            )



                awaytouchdowns = AwayCall["record"]["touchdowns"]["total"]
                awaytouchdownspergame = awaytouchdowns / AwayCall["record"]["games_played"]

                awaypasstouchdowns = AwayCall["record"]["touchdowns"]["pass"]
                awaypasstouchdownspergame = awaypasstouchdowns / AwayCall["record"]["games_played"]
                awayopponentpasstouchdownspergame = AwayCall["opponents"]["passing"]["touchdowns"] / AwayCall["opponents"]["games_played"]

                awayrushtouchdowns = AwayCall["record"]["touchdowns"]["rush"]
                awayrushtouchdownspergame = awayrushtouchdowns / AwayCall["record"]["games_played"]
                awayopponentrushtouchdownspergame = AwayCall["opponents"]["rushing"]["touchdowns"] / AwayCall["opponents"]["games_played"]

                awayrushyards = AwayCall["record"]["rushing"]["yards"]
                awayrushyardspergame = awayrushyards / AwayCall["record"]["games_played"]
                awayopponentrushyardspergame = AwayCall["opponents"]["rushing"]["yards"] / AwayCall["opponents"]["games_played"]

                awaypassyards = AwayCall["record"]["passing"]["yards"]
                awaypassyardspergame = awaypassyards / AwayCall["record"]["games_played"]
                awayopponentpassyardspergame = AwayCall["opponents"]["passing"]["yards"] / AwayCall["opponents"]["games_played"]

                awayrushespergame = AwayCall["record"]["rushing"]["attempts"] / AwayCall["record"]["games_played"]
                awaypassespergame = AwayCall["record"]["passing"]["attempts"] / AwayCall["record"]["games_played"]
                awayopponentpassespergame = AwayCall["opponents"]["passing"]["attempts"] / AwayCall["opponents"]["games_played"]
                awayopponentrushesspergame = AwayCall["opponents"]["rushing"]["attempts"] / AwayCall["opponents"]["games_played"]

                awayfieldgoalspergame = AwayCall["record"]["field_goals"]["made"] / AwayCall["record"]["games_played"]
                awayconversions = AwayCall["record"]["extra_points"]["conversions"]["pass_successes"] + AwayCall["record"]["extra_points"]["conversions"]["rush_successes"]
                awayconversionspergame = awayconversions / AwayCall["record"]["games_played"]

                awaypointspergameallowed = (
                                            (6*AwayCall["opponents"]["touchdowns"]["total"])+
                                            (3*AwayCall["opponents"]["field_goals"]["made"])+
                                            (AwayCall["opponents"]["extra_points"]["kicks"]["made"])+
                                            (2*(AwayCall["opponents"]["extra_points"]["conversions"]["pass_successes"] + AwayCall["opponents"]["extra_points"]["conversions"]["rush_successes"]))
                                            )


                if EPI != "-1":
                    if os.path.isfile("C:\\ProgramData\\Sports Power Index\\Formulas.csv"):
                        try:
                            '''
                            HomeScore = ((float(Formula[2]) * homepassyards) + (
                                             float(Formula[3]) * homerushyards) + (
                                             float(Formula[4]) * homerushtouchdowns) + (
                                             float(Formula[5]) * homepasstouchdowns) + (
                                             float(Formula[6]) * hometouchdowns) + (
                                             float(Formula[7]) * hometouchdownspergame) + (
                                             float(Formula[8]) * homepasstouchdownspergame) + (
                                             float(Formula[9]) * hometouchdownspergame) + (
                                             float(Formula[10]) * homerushyardspergame) + (
                                             float(Formula[11]) * homepassyardspergame) + (
                                             float(Formula[12]) * homerushtouchdownspergame) + (
                                             float(Formula[13]) * homerushespergame) + (
                                             float(Formula[14]) * homepassespergame)

                            AwayScore = ((float(Formula[2]) * awaypassyards) + (
                                             float(Formula[3]) * awayrushyards) + (
                                             float(Formula[4]) * awayrushtouchdowns) + (
                                             float(Formula[5]) * awaypasstouchdowns) + (
                                             float(Formula[6]) * awaytouchdowns) + (
                                             float(Formula[7]) * awaytouchdownspergame) + (
                                             float(Formula[8]) * awaypasstouchdownspergame) + (
                                             float(Formula[9]) * awaytouchdownspergame) + (
                                             float(Formula[10]) * awayrushyardspergame) + (
                                             float(Formula[11]) * awaypassyardspergame) + (
                                             float(Formula[12]) * awayrushtouchdownspergame) + (
                                             float(Formula[13]) * awayrushespergame) + (
                                             float(Formula[14]) * awaypassespergame) + (
                                             float(Formula[15]) * homerushtouchdownspergame) + (
                                             float(Formula[16]) * awaypassespergame)
                                            )
                                            '''
                        except Exception:
                            print("A error occurred. I dunno, Fix it?")
                            Quit()
                    elif os.path.isfile(FormulaFile):
                        try:
                            HomeScore = ((float(Formula[2]) * homepassyards) + (
                                float(Formula[3]) * homerushyards) + (
                                             float(Formula[4]) * homerushtouchdowns) + (
                                             float(Formula[5]) * homepasstouchdowns) + (
                                             float(Formula[6]) * hometouchdowns) + (
                                             float(Formula[7]) * hometouchdownspergame) + (
                                             float(Formula[8]) * homepasstouchdownspergame) + (
                                             float(Formula[9]) * hometouchdownspergame) + (
                                             float(Formula[10]) * homerushyardspergame) + (
                                             float(Formula[11]) * homepassyardspergame) + (
                                             float(Formula[12]) * homerushtouchdownspergame))

                            AwayScore = ((float(Formula[2]) * awaypassyards) + (
                                float(Formula[3]) * awayrushyards) + (
                                             float(Formula[4]) * awayrushtouchdowns) + (
                                             float(Formula[5]) * awaypasstouchdowns) + (
                                             float(Formula[6]) * awaytouchdowns) + (
                                             float(Formula[7]) * awaytouchdownspergame) + (
                                             float(Formula[8]) * awaypasstouchdownspergame) + (
                                             float(Formula[9]) * awaytouchdownspergame) + (
                                             float(Formula[10]) * awayrushyardspergame) + (
                                             float(Formula[11]) * awaypassyardspergame) + (
                                             float(Formula[12]) * awayrushtouchdownspergame))

                        except Exception:
                            print("A error occurred. I dunno, Fix it?")
                            Quit()
                    else:
                        print("Using Default Formula (All variables set to 1. Use a Formula Idiot)")
                        HomeScore = ((1 * homepassyards) + (1 * homerushyards) + (1 * homerushtouchdowns)
                                     + (1 * homepasstouchdowns) + (1 * hometouchdowns))

                        AwayScore = ((1 * awaypassyards) + (1 * awayrushyards) + (1 * awayrushtouchdowns)
                                     + (1 * awaypasstouchdowns) + (1 * awaytouchdowns))
                elif EPI == "-1":
                    HomeScore = (((((hometouchdownspergame*(6.98)+homefieldgoalspergame*(3)+homeconversionspergame*(2))+(((homerushtouchdownspergame+homeopponentrushtouchdownspergame)*(1+(homerushespergame+homeopponentrushespergame)/(homerushespergame+homeopponentpassespergame+homepassespergame+homeopponentpassespergame)))*(6.98))+(((homepasstouchdownspergame+homeopponentpasstouchdownspergame)*(1+(homepassespergame+homeopponentpassespergame)/(homerushespergame+homepassespergame+homeopponentrushespergame+homeopponentpassespergame))*(6.98))+homepointspergameallowed)/4)+((homerushyardspergame+homeopponentrushyardspergame)/115)+((homepassyardspergame+homeopponentpassyardspergame)/285))))
                    AwayScore = (

                        (
                            (awaytouchdownspergame*(6.98)+awayfieldgoalspergame*(3)+awayconversionspergame*(2))+
                            (((awayrushtouchdownspergame+awayopponentrushtouchdownspergame)*(1+(awayrushespergame+awayopponentrushesspergame)/(homerushespergame +awayopponentrushesspergame+awaypassespergame+awayopponentpassespergame)))*(6.98))+
                            (((awaypasstouchdownspergame+awayopponentpasstouchdownspergame)*(1+(awaypassespergame+awayopponentpassespergame)/(awayrushespergame+awayopponentrushesspergame+awaypassespergame+awayopponentpassespergame))*(6.98))+awaypointspergameallowed)/4
                        )+

                            ((awayrushyardspergame+awayopponentrushyardspergame)/115)+
                            ((awaypassyardspergame+awayopponentpassyardspergame)/285)
                        )
                print(HomeScore, " ", AwayScore)
                if HomeScore >= AwayScore:
                    print("The " + teams[homenamekey] + " will beat the " + teams[awaynamekey])
                elif HomeScore < AwayScore:
                    print("The " + teams[homenamekey] + " will lose to the " + teams[awaynamekey])

        def checkform(var):
            while True:
                try:
                    print(var)
                    if float(0) <= float(var) <= float(1):
                        break
                    elif float(var) < 0 or float(var) > 1:
                        var = input("Please enter a number between 0 and 1:")
                        continue
                except ValueError:
                    var = input("Please enter a number between 0 and 1:")
                    continue

        while True:
            Choice = input(
                "[1]Predict this weeks NFL games\n[2]Predict other weeks NFL games\n[3]Create New Formula\n[99]Back\n")
            if Choice == "1":
                date = time.strftime("%y-%m-%d")
                if date < "17-09-07":
                    # week 1
                    fetch(1)
                elif "17-09-11" <= date <= "17-09-18":
                    # week 2
                    fetch(2)
                elif "17-09-19" <= date <= "17-09-25":
                    # week 3
                    fetch(3)
                elif "17-09-26" <= date <= "17-10-2":
                    # week 4
                    fetch(4)
                elif "17-10-3" <= date <= "17-10-9":
                    # week 5
                    fetch(5)
                elif "17-10-10" <= date <= "17-9-16":
                    # week 6
                    fetch(6)
                elif "17-10-17" <= date <= "17-10-23":
                    # week 7
                    fetch(7)
                elif "17-10-24" <= date <= "17-10-30":
                    # week 8
                    fetch(8)
                elif "17-10-31" <= date <= "17-11-06":
                    # week 9
                    fetch(9)
                elif "17-11-07" <= date <= "17-11-13":
                    # week 10
                    fetch(10)
                elif "17-11-14" <= date <= "17-11-20":
                    # week 11
                    fetch(11)
                elif "17-11-21" <= date <= "17-11-27":
                    # week 12
                    fetch(12)
                elif "17-11-28" <= date <= "17-12-04":
                    # week 13
                    fetch(13)
                elif "17-12-05" <= date <= "17-12-11":
                    # week 14
                    fetch(14)
                elif "17-12-12" <= date <= "17-12-18":
                    # week 15
                    fetch(15)
                elif "17-12-19" <= date <= "17-12-25":
                    # week 16
                    fetch(16)
                elif "17-12-25" <= date <= "17-12-31":
                    # week 17
                    fetch(17)
                else:
                    print("I need to update this, or your clock is broken.")
            elif Choice == "2":
                while True:
                    weekInput = input("Enter the week you would like to predict.\n")
                    try:
                        if 1 <= int(weekInput) <= 17:
                            fetch(int(weekInput))
                            break
                        else:
                            print("That is not a valid week- There are 17 weeks in the NFL Regular season.\n")
                            continue
                    except ValueError:
                        print("That is not a valid week- There are 17 weeks in the NFL Regular season.\n")
                        continue
            elif Choice == "3":
                print("Im lazy, stfu ethan.")
                '''
                while True:
                    adv = input("[1]Basic\n[2]Advanced\n[3]Help with Removal/Editing of Formulas\n[99]Back\n\n")
                    if adv == "99":
                        break
                    elif adv == "1":
                        print(
                            "WARNING: FORMULAS CAN ONLY BE EDITED MANUALLY AFTER SAVING (SEE OPTION THREE ON LAST PAGE)\n")
                        Name = input("Enter Formula Name\n")
                        print(
                            "enter decimals bettwen 0 and 1 to weight different stats based on how important you feel each stat is.\n")
                        rushyards = input("Total Rushing Yards: ")
                        checkform(rushyards)

                        rushtouchdowns = input("Total Rushing Touchdowns:")
                        checkform(rushtouchdowns)

                        passyards = input("Total Passing Yards: ")
                        checkform(passyards)

                        passtouchdowns = input("Total Passing Touchdowns: ")
                        checkform(passtouchdowns)

                        touchdowns = input("Total Touchdowns")
                        checkform(touchdowns)

                        print("Saving Formula")
                        if platform.system() == "Windows":
                            if not os.path.exists("C:\\ProgramData\\Sports Power Index\\"):
                                os.makedirs("C:\\ProgramData\\Sports Power Index\\")
                            with open('C:\ProgramData\Sports Power Index\Formulas.csv', 'a', newline='') as Formulas:
                                newFileWriter = csv.writer(Formulas)
                                newFileWriter.writerow(
                                    [Name, passyards, rushyards, rushtouchdowns, passtouchdowns, touchdowns])
                        elif platform.system() == "Darwin":
                            if not os.path.exists(FormulaFolder):
                                os.makedirs(FormulaFolder)
                            with open(FormulaFile, 'a', newline='') as Formulas:
                                newFileWriter = csv.writer(Formulas)
                                newFileWriter.writerow(
                                    [Name, passyards, rushyards, rushtouchdowns, passtouchdowns, touchdowns])


                    elif adv == "3":
                        if platform.system() == "Darwin":
                            print(
                                "In order to manually modify or remove any formula, you must edit the csv file '/Documents/Formulas.csv'.\n"
                                "If you wish to delete any entire formula, you must delete the entire row.\n"
                                "If you wish to edit a formula, you may change any digits in a desired row to any number between 0 and 1.\n"
                                "CLOSE THE CSV FILE WHEN YOU HAVE COMPLETED EDITING")
                        elif platform.system() == "Windows":
                            print(
                                "In order to manually modify or remove any formula, you must edit the csv file 'C:\ProgramData\Sports Power Index\Formulas.csv'.\n"
                                "If you wish to delete any entire formula, you must delete the entire row.\n"
                                "If you wish to edit a formula, you may change any digits in a desired row to any number between 0 and 1.\n"
                                "CLOSE THE CSV FILE WHEN YOU HAVE COMPLETED EDITING")
                        x = input("Press 1 to see the corresponding statistics, or press any other key to go back:\n")
                        if x == "1":
                            print("Column A: Formula Name.")
                            print("Column B: Rushing Yards.")
                            print("Column C: Passing Yards.")
                            print("Column D: Rushing Touchdowns.")
                            print("Column E: Passing Touchdowns.")
                            print("Column F: Total Touchdowns.")
                            input("Press any key to continue...\n")
                            break
                    else:
                        print("That is not a valid response.")
            elif Choice == "99":
                break
            else:
                print("That is not a valid option.\n")
                continue
                '''


    while True:
        choice = input("[1] Predict NFL games\n"
                       "[2] Predict CFB games\n"
                       "[99] Quit\n")
        if choice == "1":
            NFL()
        elif choice == "2":
            NCAA()
        elif choice == "99":
            Quit()
        else:
            print("That is not a valid response.")
except (KeyboardInterrupt, EOFError):
    # Really weird, but it works.
    try:
        Quit()
    except KeyboardInterrupt:
        sys.exit()
