#  REQUIREMENTS
#The head of your favorite sports franchise has heard of your good work with her favorite bakery, and she wants you to design a program that allows you to enter a jersey number for a particular player, and receive stats for that player. 
#Stats include the following:
#Name
#Height
#Weight
#Hometown
#At least 3 players should be accessible in this program
#UI design is entirely up to you
#Once core requirements are met, additional features are welcome


#TEAM STATS IN DICTIONARY
sports_team = [
    {
        'name': "Joe",
        'height': "6'7",
        'weight': "300 lbs",
        'hometown': "Kansas City, KS"
    },
    {
        'name': "Drew",
        'height': "3'2",
        'weight': "500 lbs",
        'hometown': "Iowa City, Iowa"
    },
       {
        'name': "Mike",
        'height': "9'6",
        'weight': "1,203 lbs",
        'hometown': "Oklahoma City, OK"
    }, 
]

#WELCOME MESSAGE
print('Welcome to Sports World! You can enter the jersey number of your favorite rewardStyle Ping Pong player to view their stats.')

#JERSEY INFO
print('The current team has three players. Joe = 8, Drew = 2 and Mike = 9')

#GET INPUT FROM USER
desired_player = input('Please enter the jersey number of the player you would like to view: ')

#IF STATEMENTS TO PULL STATS
if desired_player == "8":
    print(sports_team[0])

if desired_player == "2":
    print(sports_team[1])

if desired_player == "9":
    print(sports_team[2])


