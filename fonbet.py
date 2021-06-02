import requests
import datetime
import os
import time
import webbrowser


STATS_FOLDER = "stats"

DATA_FOLDER = "footballData"
DATA_SPLITER = ";"
DATA_COLUMN_GOAL_1 = 0
DATA_COLUMN_GOAL_2 = 1
DATA_COLUMN_TEAM_1 = 2
DATA_COLUMN_TEAM_2 = 3
DATA_COLUMN_FIRST_GOAL = 4
DATA_COLUMN_FIRST_GOAL_MINUTE = 5
BLACK_LIST = ['Гости', 'желтая карточка']


def analyzeJSONbyRequest(request, fileName="JSON"):
    file = open(fileName+".html", "wb")
    file.write(request.content)
    file.close()
    webbrowser.open(fileName+".html")


class FonbetDataDownloader:
    __selfLink__ = "https://clientsapi41.bkfon-resources.com/results/results.json.php?locale=ru&lineDate={}"   # 2021-05-31
    __selfDatetime__ = None
    __selfDayShiftInPast__ = True

    __selfSession__ = None
    __selfRequest__ = None
    __selfJSON__ = None
    __selfTimeWaitNextRequest__ = 5
    __selfAutoRecconect__ = True
    __selfTimeAutoRecconect__ = 20
    __selfDaysDownload__ = -1  # -1 = download while not stop script

    selfFonbetSportId = 1
    __selfSports__ = {}
    __selfSections__ = []
    __selfEvents__ = []

    __selfFolderData__ = DATA_FOLDER
    __selfFileFormat__ = "{folder}\\{date}.csv"
    __selfFileName__ = None
    __selfRewriteMode__ = False
    __selfSpliter__ = DATA_SPLITER

    def __init__(self, daysDownload=-1, varDatetime=None, rewriteMode=False,
                 timeWaitNextRequest=5, autoRecconect=True, timeAutoRecconect=20):
        self.__selfDaysDownload__ = daysDownload
        if varDatetime is not None or not self.setDatetime(varDatetime):
            self.__selfDatetime__ = datetime.datetime.now() - datetime.timedelta(days=1)
        self.__selfSession__ = requests.session()
        if not os.path.exists(self.__selfFolderData__):
            os.mkdir(self.__selfFolderData__)
        self.__selfRewriteMode__ = rewriteMode
        self.__selfTimeWaitNextRequest__ = timeWaitNextRequest
        self.__selfAutoRecconect__ = autoRecconect
        self.__selfTimeAutoRecconect__ = timeAutoRecconect
        print(str(self.__selfDatetime__).split(' ')[0])

    def setDatetime(self, varDatetime):
        if type(datetime.datetime(1, 1, 1)) != type(varDatetime):
            return False
        self.__selfDatetime__ = varDatetime
        return True

    def getDate(self):
        return str(self.__selfDatetime__).split(" ")[0]

    def addDays(self, days=1):
        timeDelta = datetime.timedelta(days=days)
        self.__selfDatetime__ = self.__selfDatetime__ + timeDelta

    def minusDays(self, days=1):
        timeDelta = datetime.timedelta(days=days)
        self.__selfDatetime__ = self.__selfDatetime__ - timeDelta

    def __request__(self):
        if not self.__selfAutoRecconect__:
            self.__selfRequest__ = self.__selfSession__.get(self.__selfLink__.format(self.getDate()))
        else:
            requestResult = False
            while not requestResult:
                try:
                    self.__selfRequest__ = self.__selfSession__.get(self.__selfLink__.format(self.getDate()))
                    requestResult = True
                except:
                    time.sleep(self.__selfTimeAutoRecconect__)

    def getRequest(self):
        return self.__selfRequest__

    def __parse__(self):
        self.__selfJSON__ = self.__selfRequest__.json()
        labelSports = "sports"
        labelSections = "sections"
        labelEvents = "events"
        labels = [labelSports, labelSections, labelEvents]
        for label in labels:
            if label not in list(self.__selfJSON__):
                print("data parse error. Label - '{}' not found".format(label))
                # analyzeJSONbyRequest(self.__selfRequest__)
                return False
        self.__selfSports__ = {}
        for sport in self.__selfJSON__[labelSports]:
            self.__selfSports__[sport["name"]] = sport["fonbetId"]
        self.__selfSections__ = []
        for section in self.__selfJSON__[labelSections]:
            if section["fonbetSportId"] == self.selfFonbetSportId:
                self.__selfSections__.append({"events": section["events"], "name": section["name"]})
        self.__selfEvents__ = [0]
        for event in self.__selfJSON__[labelEvents]:
            self.__selfEvents__.append(event)
        return True

    def __createFileName__(self):
        self.__selfFileName__ = self.__selfFileFormat__.format(folder=self.__selfFolderData__, date=self.getDate())

    def __convertToDataAndSave__(self, enterFIFA=False):
        data = ""
        for section in self.__selfSections__:
            if "ставки" in section["name"]:
                continue
            if enterFIFA or "FIFA" not in section["name"]:
                for idEvent in section["events"]:
                    if " - " in self.__selfEvents__[idEvent]["name"] \
                            and self.__selfEvents__[idEvent]['status'] == 3 \
                            and len(self.__selfEvents__[idEvent]['score']) > 0:
                        teams = self.__selfEvents__[idEvent]["name"].split(" - ")
                        score = self.__selfEvents__[idEvent]["score"].split(" ")[0].split(":")
                        firstGoal = self.__selfEvents__[idEvent]["comment3"].split(" ")
                        if len(firstGoal) <= 1:
                            firstGoal = ["0", "0", "0"]
                        try:
                            dataRow = [score[0], score[1], teams[0], teams[1], firstGoal[2][0], firstGoal[-1].split("-")[0]]
                        except:
                            print(score, teams, firstGoal)
                            print(self.__selfEvents__[idEvent])
                            print("\n----------------------")
                            print("ERROR DATA DOWNLOADING")
                            print("\n----------------------")
                            exit()
                        data += self.__selfSpliter__.join(dataRow) + "\n"
        if len(data) > 0:
            file = open(self.__selfFileName__, "wb")
            file.write(data.encode('ansi', 'ignore'))
            file.close()

    def __doRequestAndSave__(self):
        self.__createFileName__()
        if self.__selfRewriteMode__ or not (os.path.exists(self.__selfFileName__)):
            self.__request__()
            self.__parse__()
            self.__convertToDataAndSave__()
            if self.__selfDaysDownload__ != 0:
                self.__selfDaysDownload__ -= 1
                self.minusDays(1)
                time.sleep(self.__selfTimeWaitNextRequest__)
        else:
            self.minusDays(1)
        print(str(self.__selfDatetime__).split(' ')[0])

    def download(self, daysDownload=0):
        if daysDownload != 0:
            self.__selfDaysDownload__ = daysDownload
        while (self.__selfDaysDownload__ != 0):
            self.__doRequestAndSave__()


class FootballDataAnalyzer:
    __selfFolderData__ = DATA_FOLDER
    __selfSpliter__ = DATA_SPLITER
    __files__ = []

    __selfFolderStats__ = STATS_FOLDER
    __selfFileStatsFormat__ = "{folder}\\{stats}.csv"

    def __init__(self):
        files = os.listdir(self.__selfFolderData__)
        self.__files__ = []
        fileFormat = self.__selfFolderData__ + '\\{file}'
        for file in files:
            self.__files__.append(fileFormat.format(file=file))
        if not os.path.exists(self.__selfFolderStats__):
            os.mkdir(self.__selfFolderStats__)

        print(self.__files__[0], self.__files__[-1])
        print("count games: {}".format(self.countGames()))
        print("count teams (need algorythm for group): {}".format(self.countTeams()))
        #print("wins with first goal "+
        #      "{} ({}) from {} = W{}% (WD{}%)  L{}%".format(statsFirstGoal[0], statsFirstGoal[1], statsFirstGoal[2], statsFirstGoal[3], statsFirstGoal[4], statsFirstGoal[5]))
        self.winsWichFirstGoalByMinutes()

    def __conservativeClean__(self, data):
        data = data.split("\n")
        dataOut = ""
        for rowOut in data[:-1]:
            row = rowOut.split(self.__selfSpliter__)
            if row[3] not in BLACK_LIST:
                dataOut += rowOut + "\n"
        return dataOut

    def __readFile__(self, file):
        csv = open(file)
        data = csv.read()
        data = self.__conservativeClean__(data)
        csv.close()
        return data

    def countGames(self):
        count = 0
        for file in self.__files__:
            count += self.__readFile__(file).count("\n")
        return count

    def countTeams(self):
        teams = {}
        for file in self.__files__:
            data = self.__readFile__(file).split('\n')
            for row in data[:-1]:
                row = row.split(self.__selfSpliter__)
                try:
                    teams[row[DATA_COLUMN_TEAM_1]] += 1
                except:
                    teams[row[DATA_COLUMN_TEAM_1]] = 1
                try:
                    teams[row[DATA_COLUMN_TEAM_2]] += 1
                except:
                    teams[row[DATA_COLUMN_TEAM_2]] = 1
        #print(sorted(list(teams)))
        #print(teams)
        return len(teams)

    def __saveStats__(self, data, fileName, headers=[]):
        csv = open(self.__selfFileStatsFormat__.format(folder=self.__selfFolderStats__, stats=fileName), 'w')
        for i in range(len(data)):
            data[i] = self.__selfSpliter__.join(data[i])
        headers = self.__selfSpliter__.join(headers)+'\n'
        csv.write(headers)
        csv.write("\n".join(data))
        csv.close()

    def winsWichFirstGoalByMinutes(self, startMinute=0, endMinute=90):
        data = []
        for minute in range(startMinute, endMinute):
            statsFirstGoal = self.__winsWichFirstGoal__(minute)
            print("({} min) wins with first goal ".format(minute) +
                  "{} ({}) from {} = W{}% (WD{}%)  L{}%".format(statsFirstGoal[0], statsFirstGoal[1], statsFirstGoal[2],
                                                            statsFirstGoal[3], statsFirstGoal[4], statsFirstGoal[5]))
            for i in range(3):
                statsFirstGoal[i] = statsFirstGoal[i].split('.')[0]
                statsFirstGoal[-i-1] += "%"
            data.append(statsFirstGoal)
        headers = ["Побед", "Победа или ничья", "Игр", "Побед %", "Победа или ничья %", "Поражение %"]
        self.__saveStats__(data, "firstGoal", headers)

    def __winsWichFirstGoal__(self, fromMinute=0):
        games = 0
        wins = 0
        winsAndDraw = 0
        lose = 0
        for file in self.__files__:
            data = self.__readFile__(file)
            for row in data.split("\n")[:-1]:
                row = row.split(self.__selfSpliter__)
                firstGoalAt = int(row[DATA_COLUMN_FIRST_GOAL_MINUTE])
                if firstGoalAt >= fromMinute:
                    firstGoal = int(row[DATA_COLUMN_FIRST_GOAL])
                    goalsTeam1 = int(row[DATA_COLUMN_GOAL_1])
                    goalsTeam2 = int(row[DATA_COLUMN_GOAL_2])
                    if firstGoal != 0:
                        games += 1
                    if (firstGoal == 1 and goalsTeam1 > goalsTeam2):
                        wins += 1
                    elif firstGoal == 2 and goalsTeam2 > goalsTeam1:
                        wins += 1
                    if (firstGoal == 1 and goalsTeam1 >= goalsTeam2):
                        winsAndDraw += 1
                    elif firstGoal == 2 and goalsTeam2 >= goalsTeam1:
                        winsAndDraw += 1
                    if (firstGoal == 1 and goalsTeam1 < goalsTeam2):
                        lose += 1
                    elif firstGoal == 2 and goalsTeam2 < goalsTeam1:
                        lose += 1
        outResult = [wins, winsAndDraw, games, (wins/games)*100, (winsAndDraw/games)*100, (lose/games)*100]
        for i in range(len(outResult)):
            outResult[i] = "{:.2f}".format(outResult[i])
        return outResult


#fonbet = FonbetDataDownloader(365)
#fonbet.download()

football = FootballDataAnalyzer()
