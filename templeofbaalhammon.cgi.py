#!/usr/bin/python   
print('Content-type: text/html\r\n\r')

import time
import random

#dictionary storying all game variables
#game variables are changed and updated throughout the game
#as well as during game restart (if restarted via the "play again" menu)
game_status = {
    #basic character info
    'weapon': 'no weapon',
    'original_weapon': 'no weapon',
    'torch': True,
    'flask': 1,
    'items': ['gold coins'],
    'base_AP': 5,
    'base_SP': 5,
    'bonus_AP' : 0,
    'bonus_SP' : 0,

    #statuses
    'character_status': [],
    'poison_count': 5,
    'courage_buff' : False,
    
    #score info
    'kill_count':0,
    'legendary_kill_count':0,
    'flee_count':0,
    'chamber_count': 0,
    'sacrifice': 0,

    #companion mechanics
    'dog': False,
    'dog_name': 0,
    'lower_dog_name': 0,
    'companion': [],
    'companion_entry': [],
    'met_fisherman': False,
    'met_hoplite': False,
    'met_physician': False,
    'met_scholar': False,
    'met_merchant': False,
    'girl_reduction': [],
    'met_girl' : False,
    
    #god mechanics
    'met_dido': False,
    'dido_trigger': False,
    'met_dido_ingame': False,
    'met_tanit':0,
    'met_baal': False,
    'met_musician_carthage': False,
    'met_musician': 0,
    'musician_quest' : False,
    'entered_musician_chamber': 0,
    'musician_done' : False,
    'elephant': True,
    'moloch_explanation': False,
    'musician_hint' : False,
    'minotaur_boost' : False,
    
    #game mechanic counters
    'status': True,
    'life': 'alive',
    'warning': 0,
    'how_to': 0,
    'intro': 0,
    'abandoned': 0,
    'location': 'home',
    'path': 0,
    'chamber': 0,
    'left_count':0,
    'right_count':0,
    'level': 1,
    'tanit_shrine': 0,
    'lost_adventurer': 0,
    'moloch_shrine': 0,
    'met_cave_merchant': 0,

    #quest counters
    'god_killer': False,
    'fisherman_quest': False,
    'scholar_quest': True,
    'mother_quest': False,
    'ghost_quest': False,
    'hoplite_quest': False,
    'collector_quest': False,
    'collector_version': [],
    'versus_collector': 0,
    'physician_quest': False,
    'chimera_quest': False,
    'chimera_lives': False,
    'musician_quest': False,
    'cave_merchant_inventory': ['1 flask','poor sword','new torch','dog eyes'],
    'city_merchant_inventory': ['1 flask','poor sword','new torch','dog eyes'],
    'cerberus_lives': True,
    'basilisk_lives': True,
    'mother_lives': True,
    'minotaur_lives': True,
    'spider_count': 0,

    #enemy stats and counters
    'baal': [45,45],
    'spiders': [10,10],
    'spider_room_count': 0,
    'rats': [10,10],
    'rat_count': 0, 
    'dogs': [18,12],
    'dog_count': 0,
    'baboons': [15, 18],
    'baboon_count': 0,
    'blemyae': [10,15],
    'blemyae_count': 0,
    'blemyae_room_count': 0,
    'shadows': [25,25],
    'shadow_count': 0,
    'cerberus': [30,15],
    'cerberus_count': 0,
    'basilisk': [30,15],
    'basilisk_count': 0,
    'minotaur': [35,35],
    'minotaur_count': 0,
    'halfform': [20,5],
    'halfform_count': 0,
    'fisherman': [27,27],
    'mother': [30,20],
    'mother_count': 0,
    'ghost': [35,25],
    'collector': [0,0],
    'chimera':[30,5],

    #Flowers Hidden - release in V2
    'flowers': [20,5],
    'flowers_count':0,
}

#primary gameplay function, "spine" of the game
#game loops through this function to determine level function (listed below)
#level functions determine specific room/battle/encounter
def main():
    if game_status['warning'] == 0:
        trigger_warning()
    if game_status['how_to'] == 0:
        how_to()
    while game_status['status'] == True:
        if game_status['intro'] == 0:
            intro_sequence()
        elif game_status['location'] == 'home' and game_status['life'] == 'alive':
            game_start()
        elif game_status['location'] == 'carthage' and game_status['life'] == 'alive':
            carthage()
        elif game_status['location'] == 'at sea' and game_status['life'] == 'alive':
            out_at_sea()
        elif game_status['location'] == 'first room' and game_status['life'] == 'alive':
            first_room()
        elif game_status['location'] == 'caverns' and game_status['life'] == 'alive':
            if game_status['level'] < 9 and game_status['life'] == 'alive':
                the_caverns()
            else :
                end_game()
        elif game_status['life'] != 'alive':
            game()

#Beginning sequences
def trigger_warning():
    #This provides a content warning at the start of the game.
    print('WARNING: This game contains textual descriptions of violence, including violence against women, animals, and children.')
    print('It also includes themes of slavery, war, genocide, black magic, and human sacrifice.')
    game_status['warning'] = 1
    print(" ")
    answer = input('If you would like to continue to the game, hit any key.')
    print(" ")
    return
def intro_sequence():
    print("")
    print("")
    print("")
    print("                T~~         ")
    time.sleep(0.1)
    print("                  |           ")
    time.sleep(0.1)
    print("                 /*\          ")
    time.sleep(0.1)
    print("         T~~     |'| T~~      ")
    time.sleep(0.1)
    print("     T~~ |    T~ WWWW|        ")
    time.sleep(0.1)
    print("     |  /*\   |  |  |/\T~~    ")
    time.sleep(0.1)
    print("    /*\ WWW  /''\ |' |WW|      ")
    time.sleep(0.1)
    print("   WWWWW/*\|/   \|'/*\|/*\    ")
    time.sleep(0.1)
    print("   |   /___\/]WWW[\/__\WWWW   ")
    time.sleep(0.1)
    print("   |  WWWW'|I_I|'WWWW'| | |   ")
    time.sleep(0.1)
    print("  _|_ ___ _|_ _|_ ___ |_| |__ ") 
    time.sleep(0.1)
    print("  ]-[_]-[_]-[_]-[_]-[_]-[_]-[ ")
    time.sleep(0.1)
    print("   THE TEMPLE OF BA'AL HAMMON ")
    time.sleep(0.1)
    print("    Created by Maren J.A.")
    time.sleep(0.1)
    print("text art by Maren J.A., Bill March,")
    time.sleep(0.1)
    print("Ojo, Glory Moon, & Michael Naylor")
    time.sleep(0.1)
    print("  ]-[_]-[_]-[_]-[_]-[_]-[_]-[ ")
    time.sleep(0.1)
    print("1      []           []        1")
    time.sleep(0.1)
    print("2    [][][]     [][][][][]    2")
    time.sleep(0.1)
    print("3  [][]   [][]  []   []  []   3 ")
    time.sleep(0.1)
    print("4   []   []  [][][]    []     4  ")
    time.sleep(0.1)
    print("5  [][][][][]    []   [][][]  5    ")
    time.sleep(0.1)
    print("6  []      []    [][][]   []  6   ")
    time.sleep(0.1)
    print("7        [][] [][]   []   []  7   ")
    time.sleep(0.1)
    print("8     ___[]__[]____[]____     8")
    time.sleep(0.1)
    print("     {|W|W|W|W|W|W|W|W|W|}   ")
    time.sleep(0.1)
    print("9    ||o||  ||oo||  ||o||     9")
    time.sleep(0.1)
    print("     ||_||_/||  ||\_||_|| ")
    time.sleep(0.1)
    print("     {|M|M|M|M|M|M|M|M|M|}   ")
    time.sleep(0.1)
    print("  + + + + + + + + + + + + +  ")
    time.sleep(0.1)
    print("")
    print("")
    game_status['intro'] = 1
    return
def how_to():
    print("==========================================")
    print("Do you know the rules of the game?")
    while True:
        answer = input(" ")
        print("==========================================")
        print("")
        if answer.lower() in ['no','n','rules','help','learn rules']:
            print("||| || |||| ")
            print("HOW TO PLAY")
            print("||| || |||| ")
            print("This is a text based adventure game called THE TEMPLE OF BA'AL HAMMOND created by Maren J. Aadne in 2023.")
            print("This game takes place on the eve of Rome's invasion of the ancient city of Carthage.")
            print("As the player, your goal is to reach level 9 of an ancient and dangerous cave system, where you will find the Temple of Ba'al Hammon.")
            print("There, you will pray to him to humbly ask him to save the city of Carthage and crush the Roman legions.")
            print(" ")
            print("There are 4 main endings, 3 secret endings, and many ways to die.") 
            print(" ")
            print("Hit any button to continue.")
            x = input(" ")
            print("")
            print("")
            print("CONTROLS")
            print("")
            print("Move forward in the story by typing answers to questions when prompted. ")
            print("Answers are not case sensitive.")
            print("")
            print("Type STATUS or INVENTORY at any point to bring up your character information.")
            print("Type HELP at any point to bring up the gameplay rules.")
            print("")
            cont()
            print("FIGHTING AND FLEEING")
            print("")
            print("If you wish to kill the enemy, you must have superior attack power.")
            print("Total Attack Power = Base AP + Bonus AP + Dice Roll")
            print("")
            print("If you wish to evade the enemy, you must have superior speed.")
            print("Total Speed = Base SP + Bonus SP + Dice Roll")
            print("")
            print("The dice roll is between 0-10.")
            print('Bonus AP/SP is determined by companions, weapons, and/or items.')
            print('Certain companions, weapons, and/or items may have extra bonuses against some enemy types or in certain situations.')
            print("")
            cont()
            print("Let the game begin!")
            break
        if answer.lower() in ['yes','y','skip']:
            print("Let the game begin!")
            break
        else: 
            print("Please try again.")
    game_status['how_to'] = 1    
    return

#game levels
def game_start():
    print(" ")
    print("The year is 146 B.C.")
    print("You are a citizen of Carthage, and the Scipio's troops are just outside the walls!")
    print("The siege on the city has lasted months, but rumor has it the Roman troops are finally ready to attack at dawn.")
    print("The people of Carthage mourn openly in the streets. There is no hope!!!")
    print("")
    print("Except...")
    cont()
    print("")
    print("Years ago, your father told you of the secret temple dedicated to Carthage's patron god Ba'al Hammon.")
    print("Unlike the temple in the city center, this one is located deep underground inside a dangerous, terrifying cave system.")
    print("Death-- or worse!-- awaits all who enter those caverns. But you have no choice.")
    print("In order to save the city, you must make it to this temple.")
    print("There, you will ask for Ba'al Hammon's blessing. Perhaps with that, what remains of Carthage's megre armies will stand some chance of success...")
    print("")
    print("YOUR GOAL: Make it to Level 9 of the caverns, and pray for Ba'al Hammons blessing!")
    print(" ")
    cont()
    print("|| ||||")
    print("AT HOME")
    print("|| |||| ")
    print("")
    print("Inside your home-- situated on the east side of the lesser Byrsa-- it is possible to see just beyond the third wall.")
    print("Normally a lovely sight, the view is now marred by thousands of soldiers camps, rising smoke, and ever present dust.")
    print("Hopefully, it is the last time you will be forced to look at it!")
    print("")
    print("You have just completed the preparations for your journey to the caverns.")
    print('You have never been yourself, but if the stories your father told you are true, it is somewhere you do not want to be caught unprepared.')
    print("")
    print("You take your TORCH.")
    print("Freshly pitched, this torch will be invaluable to seeing through the darkness of the caverns.")
    print("")
    print("You take your FLASK.")
    print("This was passed down to you from your mothers side, and said to contain traces of a magic Bedouin spice that revitalizes fallen soldiers.")
    print("")
    print("You take your small sack of GOLD COINS.")
    print("There is not much use for gold inside the caverns, but it may be valuable if you meet a merchant on the way.")
    print("Or, if not, it may be a good sacrificial gift to Ba'al Hammon.")
    print("")
    cont()
    print("Finally, you grab your weapon.")
    print("In these final days of the siege, the government has ordered all weaponry provisions be sent to guard the walls of the city.")
    print("As such, it is difficult to find quality equipment for you to use, but you have managed to put together a few options.")
    print(" ")
    print("OLD AXE")
    print("An old axe used for cutting wood.")
    print("Its handle is cracked and its blade is chipped, but under a powerful strike it still deals a heavy blow.")
    print("Particularly effective against large enemies, but less effective against smaller ones.")
    print("+10 AP, +5 SP")
    print(" ")
    print("BROKEN SWORD")
    print('This sword only evaded the call for arms due to being snapped off at the top.')
    print("The blade is still sharp enough to deal a serious blow.")
    print("A balanced weapon which is particularly effective against human foes.")
    print("+7 AP, +7 SP")
    print(" ")
    print("SMALL DAGGER")
    print("A small dagger used for field dressing.")
    print("It is not a particularly effective as a weapon, but it is easier to run with.")
    print("Easier to weild against very small enemies.")
    print("+5 AP, +10 SP")
    print(" ")
    print("NO WEAPON")
    print("You need no weapon.")
    print("(Permanent +5 AP, +5 SP courage bonus)")
    print(" ")
    print("---STARTING STATS---")
    print("AP: ", game_status['base_AP'])
    print("SP: ", game_status['base_SP'])
    print(" ")
    print("==========================================")
    print("Which weapon will you take with you?")
    while True:
        answer = input(" ")
        print("==========================================")
        print("")
        if answer.lower() in ['axe','old axe','the axe','the old axe']:
            game_status['weapon']="Old Axe"
            game_status['original_weapon']='Old Axe'
            break
        elif answer.lower() in ['sword','broken sword','the sword',]:
            game_status['weapon']='Broken Sword'
            game_status['original_weapon']='Broken Sword'
            break
        elif answer.lower() in ['dagger','small dagger','the dagger','the small dagger']:
            game_status['weapon']='Small Dagger'
            game_status['original_weapon']='Small Dagger'
            break
        elif answer.lower() in ['d','none','nothing','no weapon']:
            game_status['character_status'].append("courage buff")
            game_status['base_AP'] += 5
            game_status['base_SP'] += 5
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else :
            print("Please try again.")
    x = game_status['weapon']
    if x == 'no weapon':
        print('You have chosen to go unarmed! How daring...! ')
    else:
        print("You have chosen the", x)
    print("")
    get_total_AP_SP()
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    print(" ")
    print("With your things gathered, there is nothing more for you to do here.")
    print("It is time to go.")
    cont()
    print("Then, just as you go to close your front door, you hear something... barking!")
    print("It's your dog!")
    print("")
    print("==========================================")
    print("What is your dog's name?")
    while True:
        y = input(" ")
        print("==========================================")
        print("")
        if len(y) > 1:
            game_status['dog_name'] = y
            game_status['lower_dog_name'] = y.lower()
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else:
            print("Please input a name longer than 1 character.")
    print("")
    print("YOU: No ",game_status['dog_name']," you cannot come with me. It is too dangerous.")
    print(game_status['dog_name'],": Woof!")
    print("")
    print("A compelling argument.")
    print("")
    print("==========================================")
    print("Do you bring him with you?")
    while True:
        answer = input("")
        print("==========================================")
        print("")
        if answer.lower() in ['yes','y']:
            game_status['dog'] = True
            game_status['companion'].append(game_status['dog_name'])
            print("He stares up at you with those big puppy dog eyes of his and... you just can't resist.")
            print("You bring him along.")
            print("")
            print("COMPANION ADDED: ",game_status['dog_name'])
            print("(+5 AP, +5 SP. Bonus damage against canine enemies.)")
            print("")
            break
        elif answer.lower() in ['no', 'n']:
            game_status['dog'] = False
            print("YOU: I'm sorry, ", game_status['dog_name'], "but it is just too dangerous.")
            print(" ")
            print('He does not understand, but you know it is for the best.')
            break
        elif answer.lower() in ['kill','kill dog','take eyes','dog eyes']:
            print("YOU: What a good boy you are...")
            print(" ")
            print("You grab the broken sword. It will get the job done quickest, and you would like to spare the little guy the pain...")
            print('You strike, cutting quick across the neck.', game_status['dog_name']," did't even flinch. He trusted you.")
            game_status['dog'] = False
            game_status['kill_count'] += 1
            game_status['items'].append("dog eyes")
            print("")
            print("ACQUIRED: dog eyes")
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else :
            print("Please try again.")
    game_status['location']='carthage'
    print("")
    print("With one last look around, you step out the door and into the city streets of Carthage.")
    cont()
    return
def carthage():
    game_status['location']='first room'
    print('  __                                 ') 
    time.sleep(0.1)
    print(' |""|  ___    _   __               ~~      ')   
    time.sleep(0.1)
    print(' |""|_|"""|__|"| |""|         _._ |_     ')
    time.sleep(0.1)
    print(' |""|"|"""|""|"|_|""| __     (__((_(    ')
    time.sleep(0.1)
    print(' |""|"|"""|""|"|"|""||""|  \"-:--:-./    ')
    time.sleep(0.1)
    print(' """""""""""""""""""""""""~~~~~~~~~~~~~~ ')
    time.sleep(0.3)
    print("")
    print("|| ||||||||")
    print("IN CARTHAGE")
    print("|| ||||||||")
    print("")
    time.sleep(0.1)
    while game_status['path'] < 3:
        x = random.randint(0,100)
        #no event, just take the normal path to the cave
        if 0 <= x < 30:
            if game_status['path'] == 0 :
                print("You walk through the narrow streets of the city. The sun hangs heavy overhead, bathing the towering white citadel of the city in golden light.")
                print("Who could ever wish to destroy this?")
            if game_status['path'] == 1 :
                print("Despite the siege, the Agora is full of people. Still, it seems to have changed...")
                print("Before, the markets would be filled with people-- merchants selling spices from the East, smoked meats and fish, fruit and fine linen.")
                print("Now the merchants remain, but they hawk other wares... smuggled weaponry, rotting food, meat of mysterious origin...")
            if game_status['path'] == 2 :
                print('Youve reached the outside of the Cothon, where the walls meet the seaside cliffs.')
                print("You see the cave on the horizon, looming ominously.")
                print("It is not far, now.")
            game_status['path'] += 1
            game_status['location']='first room'
            cont()
        #meet Hoplite
        elif 30 <= x < 45 and game_status['met_hoplite'] == False: 
            game_status['path'] += 1
            if game_status['met_hoplite'] == False:
                game_status['met_hoplite'] = True
                print("Walking through the city streets, you spy down the lane a Hoplite on his way to somewhere. You notice he is dressed in the shimmering bronze armor of the Sacred Band. You had thought they were disbanned ages ago?")
                print("Regardless, it would be best to not draw his attention. As you walk, you keep your head down, your things tucked beneath your clothes. However, as you pass, you feel his gaze land upon you.")
                print("")
                print("HOPLITE: My friend, where are you going to so quickly? ")
                cont()
                print("")
                print("You do not answer, instead trying rush past him.")
                print("Before you can get far, he grabs you by the wrist.")
                print("")
                cont()
                print("HOPLITE: My friend, my friend, please do not rush. I see you are going somewhere important.")
                print("YOU: I am.")
                print("HOPLITE: Where might that be? Ha, do you mean to fight the Romans yourself?")
                print("")
                print("You are unsure what to do. If caught lying to a member of the Sacred Band, it could mean your head.")
                cont()
                print("Reluctantly, you decide on the truth.")
                print("")
                print("YOU: I am  going to the caverns... to find the Temple of Ba'al Hammon.")
                print("HOPLITE: Ba'al Hammon? If you wish to pray, my friend, why not go to the Byrsa? It is safer than the caves.")
                print("YOU: I cannot. It must be the caverns. it is the only place--")
                print("HOPLITE: -- speak no further, my friend.")
                print("")
                print("You shrink back, afraid you have said too much, but The Hoplite only smiles, his bright white teeth shining beneath his bronze helm.")
                print(" ")
                cont()
                print("HOPLITE: It is my duty to protect the people of Carthage. If what you say is true, then perhaps I should go with you.")
                print("")
                if 'The Physician' in game_status['companion']:
                    print("The Physician nudges you, making a not-so-subtle gesture to ignore this fellow and leave him behind. The Hoplite catches it, and scowls at him.")
                if game_status['dog'] == True:
                    print("For what it is worth, ",game_status['dog_name'],"seems to like him. He runs up, and The Hoplite lays a gentle hand on his head.")
                print("")
                print("==========================================")
                print('Will you let The Hoplite join your party?')
                while True:
                    answer = input("")
                    print("==========================================")
                    print(" ")
                    if answer.lower() in ['yes','y']:
                        game_status['companion'].append('The Hoplite')
                        game_status['hoplite_quest'] = True
                        print("You nod in agreement. The Hoplite seems pleased.")
                        print("")
                        print("HOPLITE: Let us go then! I have heard troubling rumors of a looming attack... we may not have much time.")
                        print(" ")
                        cont()
                        print("COMPANION ADDED: The Hoplite")
                        print("(The Hoplite provides +10 AP bonus)")
                        break
                    elif answer.lower() in ['no','n']:
                        print("YOU: I am sorry, but I must go alone.")
                        print("HOPLITE: Ah... I understand. Be safe, my friend.")
                        print("")
                        print("He nods gravely at you, and then continues on his way.")
                        break
                    elif answer.lower() in ['inventory','status','info','info']:
                        get_info()
                    elif answer.lower() == 'help':
                        get_help()
                    else :
                        print('Please try again.')
                cont()
        #meet Physician
        elif 45 <= x < 60 and game_status['met_physician'] == False:
            game_status['path'] += 1
            if game_status['met_physician'] == False:
                game_status['met_physician'] = True
                print("You pass by a small crowd that has gathered in the street.")
                print("Edging your way around the side, the crowd suddenly erupts into cries of joy and applause.")
                print("'He is saved! He is saved!' they cry. You crane your neck but cannot see anything until suddenly, the  crowd parts.")
                print("Out of the center strolls a tall, thin man, dressed in long flowing robes. His hands are stained with blood.")
                print("Behind him lies a young man, bandaged and just begining to sit up.")
                print("As The Physician leaves, young woman grabs him by the sleeve.")
                cont()
                print(" ")
                print("WOMAN: Please, sir, my father is sick, he--")
                print("PHYSICIAN: -- Goodness, are you ALL ill? ")
                print("WOMAN: Please! If you will only look at him.")
                print("")
                print("The Physician pushes past her dismissively.")
                cont()
                print("")
                print("PHYSICIAN: Apologies, but if I took the time to heal all of you, I'd never sleep! I have important work to do. I must find an escort to get me to the caverns.")
                print(" ")
                print("The crowd gasps, then begins to whisper amongst themselves.")
                print("You step forward.")
                print(" ")
                cont()
                print("YOU: You are going to the caverns? The one's that house the Temple of Baal Hammon?")
                print("PHYSICIAN: There's a temple in there as well? I hadn't known... but yes, I am, so if you please--")
                print(" ")
                print("It could be beneficial to have someone capable of healing with you.")
                print(" ")
                print("==========================================")
                print('Do you ask him to join?')
                while True:
                    answer = input("")
                    print("==========================================")
                    print(" ")
                    if answer.lower() in ['yes','y']:
                        game_status['companion'].append('The Physician')
                        print("YOU: I am going to the caverns.")
                        print("")
                        print("The Physician stops and turns to you. His eyes light up in a manic sort of glee.")
                        print("")
                        print("PHYSICIAN: Are you now? Well then, let's go together.")
                        print("YOU: Why are you going to the caverns? ")
                        print("PHYSICIAN: My business is my own. Just keep me alive and I'll keep you alive, agreed?")
                        print("")
                        print("With that, he joins your party, and you set off to the caverns.")
                        print(" ")
                        cont()
                        print("COMPANION ADDED: The Physician")
                        print("(The Physician provides +3 AP, +3 SP and can heal Injuries)")
                        break
                    elif answer.lower() in ['no','n']:
                        print("No, it is best to keep your intentions secret.")
                        print("You let The Physician pass by you, then continue on your way alone. ")
                        break
                    elif answer.lower() in ['inventory','status','info','info']:
                        get_info()
                    elif answer.lower() == 'help':
                        get_help()
                    else :
                        print('Please try again.')
            cont()
        #meet Musician
        elif 60 <= x < 70 and game_status['met_musician_carthage'] == False:
            game_status['met_musician_carthage'] = True
            game_status['path'] += 1
            print('You walk along the walls of the city. They are lined with apricot trees that are just beginning to bloom.')
            print('As you near the beginning of the southern section, you hear a sound... it is the soft strumming of a kithara.')
            print("Approaching closer, you see The Musician sat upon the ground beneath a tree, it's leaves blackened and dried as if it were dead.")
            print("They wear the veil of a woman, but seem to have the face of a man. Confusing...")
            print("You pass by without a word, but then the Musician calls out to you.")
            cont()
            print("")
            if game_status['met_musician'] == 0:
                print("MUSICIAN: On your way to the caves, are you?")
                print("")
                print("You stop, startled by their astuteness.")
                if game_status['dog'] == True:
                    print("Next to you, ",game_status['dog_name'],"begins to whimper.")
                print("")
                print("YOU: How did you know? ")
                print("MUSICIAN: You remind me of someone I have seen before.")
                print("")
            if game_status['met_musician'] > 1:
                print("MUSICIAN: Back to the caverns, are we?")
                print("")
                print("You stop, startled by their statement.")
                if game_status['dog'] == True:
                    print("Next to you, ",game_status['dog_name'],"begins to whimper.")
                print("")
                print("YOU: Going... back? This is the first time I've gone there.")
                print("MUSICIAN: Are you sure?")
                print("")
            cont()
            print("A cryptic answer. Something about this person is very off-putting.")
            print("You are not sure why, but for some reason you sense this person may be important.")
            print(" ")
            print("==========================================")
            print('Do you ask them to join you?')
            while True:
                answer = input("")
                print("==========================================")
                print(" ")
                if answer.lower() in ['yes','y']:
                    print("YOU: Would you care to join me?")
                    print("")
                    print("The Musician laughs, still strumming absent mindedly upon their kithara. The song sounds sad.")
                    print("")
                    print("MUSICIAN: I think not. It is not my way to travel around with... people such as yourself.")
                    print("YOU: I see...")
                    cont()
                    print("MUSICIAN: But perhaps we will encounter each other again? I am always easy to find.")
                    print("YOU: Oh?")
                    print("MUSICIAN: Of course! Simply go left, then left, then left, and then left again, and there I will be.")
                    if game_status['met_musician'] == 0:
                        print("YOU: Wont that just take me in a circle?")
                        print("")
                        print("They laugh. It sounds condescending.")
                        print("")
                        print("MUSICIAN: The caverns are not like here... You will learn that, in time.")
                        print("YOU: Oh...")
                        print("MUSICIAN: Good luck...")
                    elif game_status['met_musician'] > 0 and game_status['entered_musician_chamber'] == 0:
                        print("YOU: What if I cannot go left?")
                        print("MUSICIAN: You can do anything you set your mind to.")
                        print("")
                        print("More riddles... Frustrated, you depart without another word.")
                        print("")
                        print("MUSICIAN: Good luck...")
                    else: 
                        print("YOU: Right... I remember.")
                    if 'The Physician' in game_status['companion']:
                        cont()
                        print("")
                        print("As you depart, The Physician leans in, whispering conspiratorily.")
                        print("")
                        print("PHYSICIAN: They aren't very good, are they?")
                    break
                elif answer.lower() in ['no','n']:
                    print("")
                    print("You say nothing, and continue on your way.") 
                    print("The Musician smiles.")
                    print("")
                    print("MUSICIAN: Good luck...")
                    break
                elif answer.lower() in ['inventory','status','info','info']:
                    get_info()
                elif answer.lower() == 'help':
                    get_help()
                else :
                    print('Please try again.')
            game_status['met_musician'] += 1
            cont()
        #meet Fisherman
        elif 70 <= x < 85 and game_status['met_fisherman'] == False and 'gold coins' in game_status['items']: 
            game_status['path'] += 1
            if game_status['met_fisherman'] == False: 
                game_status['met_fisherman'] = True
                print('Nearing the Cothon, you spy a fisherman sat upon a crate. He is beckoning you, and you go.')
                print("")
                print("FISHERMAN: Such times upon us... such dreadful times, yes?")
                print("YOU: Indeed...")
                print("FISHERMAN (whispering): Perhaps you seek to leave this strife behind? I can help you, if you like...")
                print("")
                print("You had heard of men like this... the Romans have blocked the port, but small fishing vessels often pass by unnoticed.")
                print("You do not intend to be so cowardly.")
                cont()
                print("YOU: No, thank you. I do not intend to flee.")
                print("FISHERMAN: I would think not! You look too brave to do so. But may I ask, where are you going?")
                print("YOU: The caverns, if you must know.")
                print("FISHERMAN: The caverns! A dangerous place, most certainly... but I can help you with that as well.")
                print("")
                print("You pause. Perhaps it is best to hear him out...")
                print("The fisherman smiles. He is missing many teeth.")
                print("")
                cont()
                print("FISHERMAN: Oh yes, 8 levels of a winding labyrinth, filled with terrifying beasts! But you know, there is another way...")
                print("YOU: Oh?")
                print("FISHERMAN: It is not well known except among my kind, but yes... there is a secret entrance, only accessible from the sea.")
                print("FISHERMAN: It opens up directly onto the third level of the caves. It would save you quite a bit of time...")
                print("YOU: Interesting... And you would take me?")
                print("FISHERMAN: Oh yes! For a small fee, of course... Those gold coins of your would do nicely, I think!")
                print(" ")
                print("You contemplate the offer.")
                if 'The Hoplite' in game_status['companion']:
                    print("The Hoplite nudges you, subtly shaking his head. It seems he does not trust this man.")
                print("")
                print("==========================================")
                print('Will you go with the fisherman')
                while True:
                    answer = input("")
                    print("==========================================")
                    print(" ")
                    if answer.lower() in ['yes','y']:
                        game_status['fisherman_quest'] = True
                        game_status['location']='at sea'
                        game_status['path'] = 4
                        game_status['items'].remove('gold coins')
                        print("")
                        print("You nod, and hand over your small pouch of gold coins.")
                        print("")
                        print("FISHERMAN: A good decision! Now, come this way, my boat is tied just up over here...")
                        cont()
                        print("")
                        return
                    elif answer.lower() in ['no','n']:
                        print("")
                        print("He does not seem trustworthy.")
                        print("You shake your head no and continue on your way.")
                        print('He continues to call after you, but you pay it no mind.')
                        break
                    elif answer.lower() in ['inventory','status','info','info']:
                        get_info()
                    elif answer.lower() == 'help':
                        get_help()
                    else :
                        print('Please try again.')
                cont()
        #meet City Merchant
        elif 85 <= x <= 100 and game_status['met_merchant'] == False:
            game_status['met_merchant'] = True
            game_status['path'] += 1
            print("Striding quickly through the Agora, you accidentally collide with a large, imposing merchant. You quickly apologize, but he puts up two thick hands to stop you. With a sly smile from beneath his bushy beard, he seizes the opportunity, showcasing his wares.")
            print("")
            print("CITY MERCHANT: Brave adventurer! You seem to be dressed for danger-- are you properly prepared?")
            print("")
            print("He has seen right through you. Though you wish to move on quickly, you DO feel quite under prepared... perhaps it is best to hear him out?")
            print("You step up to his stall to examine some items.The merchant has already laid out three items to show you.")
            cont()
            print("")
            print("MERCHANT: If you are on an adventure, take one of these! Very special, very hard to get in the city now...")
            print("")
            print("POOR SWORD")
            print("A cheap but useable blade. Better than your broken one.")
            print("+11 AP, +11 SP")
            print("Particularly effective against human enemies.")
            print("")
            print("EXTRA FLASK")
            print("Another flask! This could be useful...")
            print("")
            print("DOG EYES")
            print("A small jar filled with something horrible. The label reads 'dog eyes' but it looks more like jelly...")
            print("You dont know what this does.")
            print("")
            print("MERCHANT: Ill gladly take those GOLD COINS of yours in exchange for any one of them. What do you say?")
            print("")
            print("==========================================")
            print("Do you wish to trade for an item?")
            while True:
                answer = input("")
                print("==========================================")
                print("")
                if answer.lower() in ['yes','y','trade','trade for item','buy','purchase','buy item','purchase item']:
                    print("Which item will you purchase?")
                    game_status['items'].remove("gold coins")
                    while True:
                        answer2 = input("")
                        print("==========================================")
                        print("")
                        if answer2.lower() in ['sword','poor sword','weapon','the sword']:
                            print("You exchange your gold for the weapon.")
                            print("")
                            get_total_AP_SP()
                            print("--PREVIOUS STATS--")
                            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                            print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                            print("")
                            game_status['weapon'] = 'Poor Sword'
                            game_status['original_weapon'] = 'Poor Sword'
                            get_total_AP_SP()
                            print("--CURRENT STATS--")
                            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                            print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                            print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                            break
                        elif answer2.lower() in ['flask','extra flask','the flask','a flask']:
                            print("You exchange your gold for the extra flask.")
                            print("You now have 2 Flasks.")
                            game_status['flask'] += 1
                            break
                        elif answer2.lower() in ['eyes','jar of eyes','dog eyes','jar of dog eyes','the jar of dog eyes','the eyes','the jar','the jar of eyes']:
                            print("You exchange your gold for the jar of dog eyes.")
                            print("The Merchant seems glad to be rid of it...")
                            print("")
                            print("ACQUIRED: dog eyes")
                            game_status['items'].append('dog eyes')
                            break
                        elif answer2.lower() in ['inventory','status','info','info']:
                            get_info()
                        elif answer2.lower() == 'help':
                            get_help()
                        else:
                            print("Please try again.")
                    print("")
                    print("The Merchant looks at you, pleased, and claps you on the back.")
                    print("")
                    print("MERCHANT: You have made a smart decision, my friend! Best of luck on your journey!")
                    break
                elif answer.lower() in ['no','n','skip',"don't trade","dont trade",'keep coins']:
                    print("None of these things are to your liking.")
                    print("The Merchant tries to call you back to offer you more, but you wave him off and continue on your way.")
                    break
                elif answer.lower() in ['inventory','status','info','info']:
                    get_info()
                elif answer.lower() == 'help':
                    get_help()
                else:
                    print("Please try again.")
            cont()
        print("")
    print('                //7;<\   ---\=,__,>,_"-.    | ')
    time.sleep(0.1)
    print('#,,_ "-  ""####//7;<\  --z--;" /_/  ". ".   | ')
    time.sleep(0.1)
    print('"""."|"|| } }|.""|""//7;<\  "//"/"  " \  ". | ')
    time.sleep(0.1)
    print('     ||   |  |  :    :  ,_\---_\._   :  ".\ | ')
    time.sleep(0.1)
    print(' :   |  |   || :  : :    //--"> ___ ""-,_   \ ')
    time.sleep(0.1)
    print(':  " ||   || |   //7;<\  =-""," / "-, __"-. | ')
    time.sleep(0.1)
    print(':  : |  |    |    ---  //7;<\     / ,--._ " | ')
    time.sleep(0.1)
    print('  :  |   ||| | "  :    -/;\"/" -="/|(    \     ')
    time.sleep(0.1)
    print('    "| |||   |  :   : :  // "\   // | "   | | ')
    time.sleep(0.1)
    print('  :  || # | ||   :              "   .   : | |  ')
    time.sleep(0.1)
    print(' :   | ||#|#||  :   :    /\/\        :    | |  ')
    time.sleep(0.1)
    print('   : | ||,|, |   :    /\/::::\/\_     __: | | ')
    time.sleep(0.1)
    print(' :  \\|\ # #//"//    |:::::::::::|  :[__]/  | ')
    time.sleep(0.1)
    print('   / >\\> <\/\< ___\\|:/\:/\::/\::|//__||_/  | ')
    time.sleep(0.3)
    print(" ")
    print("Finally, you have reached the caverns. You can just spy the dark entrance tucked between a short waterfall and a towering tree.")
    print("There is no trail leading to it and its entrance is unadored, save for a single hand-painted sign that reads:")
    print("")
    print("  ____________________________")
    print(" |  ________________________  | ")
    print(" | |                        | | ")
    print(" | |       !!DANGER!!       | | ")
    print(" | |    Horrors beyond      | |  ")
    print(" | |  comprehension await!  | |  ")
    print(" | |      TURN BACK!        | | ")
    print(" | |________________________| | ")
    print(" |____________________________| ")
    print("")
    print("You briefly consider turing back, but all that awaits you at home is death by Roman troops. You continue onward.")
    cont()
    print(" ")
    print("Just as you are about to head into the cave entrance, you spy something beneath the tree.")
    if game_status['elephant'] == True:
        print("You gasp. It is a war elephant! You had thought they were all dead, but here is one right before your very eyes!")
        print("The ancient beast lies in repose, his head lolling from side to side. Despite it's ancient appearance, it's armor appears polished and new, shining as if only forged yesterday.")
        print("It's tusks are encased in glittering bronze, with long, sharp bayonettes attached at the ends. You examine them carefully. It seems you could easily remove them without hurting the old beast, and then use the covers as a weapon for yourself. It would certainly be better than what you have now.")
        print(" ")
        print("WAR ELEPHANTS TUSK")
        print("The standard war regalia for Carthage's famous War Elephants.")
        print("Provides bonus against human enemies.")
        print("+14 AP, +14 SP")
        print(" ")
        if game_status['dog'] == True: 
            print(game_status['dog_name'], "growls low in his throat, as if in warning. Perhaps it is better to leave the old beast alone...")
            print(" ")
        print("==========================================")
        print("Do you take its tusk as a weapon?")
        while True:
            answer = input(" ")
            print("==========================================")
            print(" ")
            if answer.lower() in ['yes','y','take','take tusk','take war elephants tusk',"take elephants tusk","take elephant's tusk","take war elephant's tusk"]:
                print("The elephant looks at you with sad eyes as you gently remove the covering. You pet it gently, in thanks for its help.")
                game_status['weapon'] = 'War Elephants Tusk'
                game_status['original_weapon'] = 'War Elephants Tusk'
                game_status['sacrifice'] -= 10
                game_status['elephant'] = False
                print("")
                print("---PREVIOUS STATS---")
                print("AP: ", game_status['base_AP'])
                print("SP: ", game_status['base_SP'])
                print(" ")
                get_total_AP_SP()
                print("--CURRENT STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                print(" ")
                cont()
                print("As you step towards the cavern, you suddenly feel a tremble rising up from beneath the ground.")
                print("You look down at the weapon in your hands. Perhaps you shouldn't have taken it?")
                break
            if answer.lower() in ['no','n']:
                print("It is perhaps best not to touch it. Elephants are the sacred beast of Carthage, after all. To find one here of all places means it may very well be a familiar of Ba'al Hammon itself!")
                break
            if answer.lower() in ['inventory','status','info']:
                get_info()
            if answer.lower() == 'help':
                get_help()
            else:
                print("Please try again.")
    else:
        print("You gasp. It is a war elephant! ")
        print("With a deep sadness, you realize that it is not moving. It is dead.")
        print("For some reason, you are filled with a deep sense of guilt.")
        print("")
    print("With one more look back at the elephant, you slip up and into the entrance to the cave.")
    cont()
    return
def out_at_sea():
    print("                   \ | /  ")
    time.sleep(0.1)
    print("              ,~ -= (_) =-")
    time.sleep(0.1)
    print("             |\    / | \ ")
    time.sleep(0.1)
    print("            /| \ ")
    time.sleep(0.1)
    print("~~~~~~~~~~~/_|__\~~~~~~~~~~")
    time.sleep(0.1)
    print(" ~~~~~~~ ~ ~======~~  ~~ ~")
    time.sleep(0.1)
    print("  ~~~~~~~~~ ~~~~~  ~~~ ~'")
    print(" ")
    time.sleep(0.3)
    print("|| |||")
    print("AT SEA")
    print("|| |||")
    print("")
    print("It takes nearly an hour of suffering the old man's small talk until you come to a stop, floating just off shore.")
    print("The fisherman points to the cliffside. You see a small opening just below the rock.")
    print("")
    print("FISHERMAN: There it is, as promised.")
    print("YOU: Thank you.")
    print("FISHERMAN: Hm...")
    print("")
    print("He has stopped rowing, and is eyeing you warily.")
    print("")
    print("FISHERMAN: Rather difficult to come out this way, you know. Rip tides... many rip tides.")
    print("YOU: I am sorry for any inconvenience...")
    print("FISHERMAN: Hm...")
    cont() 
    print("")
    if 'The Hoplite' in game_status['companion']:
        print("The Hoplite gets to his feet, rocking the boat. He appears furious.")
        print("")
        print("HOPLITE: You are a liar! How can you dare to rob your own countrymen, at a time like this!")
    else: 
        print("You say nothing. You are sure he is up to something.")
        print("After a moment, the fisherman leans back and shakes his head.")
        print("")
    print("FISHERMAN: I do not meant to put you in a difficult position! But I'm afraid I can take you no further... not for what you have paid me.")
    print("YOU: That is not what you said on the shore...")
    print("FISHERMAN: I said I would try, but these seas! They are so rough... what you have paid is not enough.")
    print("YOU: What must I do to have you take me the rest of the way? ")
    print("")
    print("The fisherman shows his mangled smile once more.")
    print("")
    if game_status['weapon'] == 'no weapon':
        print("FISHERMAN: Give me something else. That flask you have will do.")
    else: 
        print("FISHERMAN: Give me something else. That flask you have, or your weapon will do.")
    print("YOU: Or...? ")
    print("FISHERMAN: I would not ask questions you do not want the answer to...")
    print("")
    if 'The Physician' in game_status['companion']:
        print("The Physician leans in, whispering in your ear.")
        print("")
        print("PHYSICIAN: I say give him what he wants. I'm sure we will find plently of interesting things inside the caverns. Treasures and such, yes?")
    print(" ")
    print("You consider your options.")
    if game_status['weapon'] == 'no weapon':
        print("You can give him your torch or your flask.")
    else: 
        print("You can give him your weapon, your torch, or your flask.")
    print("Or, if you think you can take him... you can try to fight back.")
    print("")
    opponent = game_status['fisherman']
    dice_attack = random.randint(0,10)
    get_total_AP_SP()
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    attack = dice_attack + game_status['bonus_AP']
    if 'eye' in game_status['items']:
        print("FISHERMAN'S STATS:")
        print("AP: ", opponent[0])
    else:
        print("FISHERMAN'S STATS:")
        print("AP: ???")
    print("")
    print("==========================================")
    print("Will you fight or will you give him something?")
    while True:
        answer1 = input(" ")
        print("==========================================")
        print(" ")
        if answer1.lower() in ['fight','fight him', 'battle','kill','kill him']:
            if game_status['weapon'] == 'no weapon':
                print("You take a moment to pretend to consider and look through your things.")
            else: 
                print("Under the guise of looking through your things for something to pay him with, you carefully reach to grab your weapon.")
            roll_dice()
            print("You rolled a", dice_attack)
            if attack >= opponent[0]:
                print("")
                time.sleep(0.5)
                print("Success!")
                print("")
                game_status['kill_count'] += 1
                game_status['fisherman_quest'] = True
                if game_status['weapon'] in ['Old Axe','Broken Sword','Small Dagger']:
                    print("In an instant, you swing and strike the fisherman, who is caught completely off guard by your attack.")
                    print("The blade catches him across the face, breaking bone and cutting flesh in the blink of an eye.")
                    print("His body slumps forward, blood gushing out and filling the bottom of the boat.")
                elif game_status['weapon'] in ['no weapon']:
                    print("In an instant, you lunge at him, taking him entirely off guard.")
                    print("You throw him down to the bottom of the boat and pin him down, ignoring his thrashing limbs and wrapping both hands tightly around his neck.")
                    print("You push down with your full weight until his gasps turn to nothing more than a pathetic gurgling.")
                    print("He stops moving.")
                print("")
                print("You move to push his body overboard, when something falls out of the sleeve of his robe.")
                print("It looks like a child's doll. It is stained with blood.")
                print("")
                game_status['items'].append('bloody doll')
                print("ACQUIRED: Bloody doll")
                print(" ")
                print("You push his limb body off overboard and then row yourself to the cavern entrance.")
                print("")
            else :
                print("")
                time.sleep(0.5)
                print("")
                game_status['life'] ='dead_at_sea'
            break
        elif answer1.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer1.lower() == 'help':
            get_help()
        elif answer1.lower() in ['give','give something','give him something','bribe','pay','bribe him','pay him','give flask','give him my flask','give weapon','give him my weapon']:
            print("==========================================")
            print(" ")
            print("Will you give him your weapon or your flask")
            game_status['fisherman_quest'] = True
            while True:
                answer = input(" ")
                print("==========================================")
                print(" ")
                if answer.lower() in ['weapon', 'my weapon', 'the weapon', 'a weapon', 'sword', 'my sword', 'the sword', 'broken sword', 'axe', 'the axe', 'my axe', 'old axe', 'dagger', 'small dagger','the small dagger','the dagger','my dagger','my small dagger'] and game_status['weapon'] != 'no weapon':
                    game_status['location'] = 'first room'
                    game_status['weapon'] = 'no weapon'
                    print("You hand over your weapon.")
                    break
                elif answer.lower() in ['flask', 'my flask','the flask','a flask', '1 flask', 'one flask']:
                    game_status['flask'] = 0
                    game_status['location']='first room'
                    print("You hand over your flask.")
                    break
                elif answer.lower() in ['inventory','status','info','info']:
                    get_info()
                elif answer.lower() == 'help':
                    get_help()
                else :
                    print("Please try again.")
            print("")
            print("FISHERMAN: Good man. I knew you were smart.")
            print("")
            print("With that, you set off towards the secret entrance.")
            break
        else: 
            print("Please try again.")
    cont()
    game_status['level']=3
    game_status['location']='first room'
    #returns to main()
    return
def first_room():
    print("iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii")
    time.sleep(0.1)
    print(";;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;")
    time.sleep(0.1)
    print(" \    /\  / \   \/\  /  \  /\/  \    /")
    time.sleep(0.1)
    print("  \  /  \/   \    /\/    \/      \  /")
    time.sleep(0.1)
    print("   \/          \/                 \/")
    time.sleep(0.3)
    print("")
    print("||| |||||||")
    print("THE CAVERNS")
    print("||| |||||||")
    print("")
    if game_status['fisherman_quest'] == True:
        print("You enter the cavern... it is dark and damp.")
        print("You hear howls from within.. the beast of the cave are hungry. Perhaps they have noticed your arrival.")
        print("")
        print("Just as the fisherman said, you appear to have entered at the third level.")
        print("")
        print("A moment of panic seizes you!")
        print("You cannot do this! This is madness!")
        print("You turn to leave again, but suddenly find the door has vanished behind you.")
        print("On the wall where the door once stood, you instead find an engraving, rough around the edges as if it were not etched, but rather desperately clawed into the stone.")
        print("It reads: ")
        print(" ")
        print('>< >< >< >< >< >< >< >< >< >< >< ')
        print("    THE ONLY WAY OUT IS DOWN")
        print('>< >< >< >< >< >< >< >< >< >< >< ')
        print(" ")
        print("Steeling yourself you take a deep breath, and then venture further inside.")
        cont()
    else: 
        print("You enter the cavern... it is dark and damp.")
        print("You hear howls from within.. the beast of the cave are hungry. Perhaps they have noticed your arrival.")
        print("")
        print("A moment of panic seizes you!")
        print("You cannot do this! This is madness!")
        print("You turn to leave again, but suddenly find the door has vanished behind you.")
        print("On the wall where the door once stood, you instead find an engraving, rough around the edges as if it were not etched, but rather desperately clawed into the stone.")
        print("It reads: ")
        print(" ")
        print('>< >< >< >< >< >< >< >< >< >< >< ')
        print("    THE ONLY WAY OUT IS DOWN")
        print('>< >< >< >< >< >< >< >< >< >< >< ')
        print(" ")
        print("Steeling yourself you take a deep breath, and then venture further inside.")
        cont()
    game_status['location'] = 'caverns'
    print(" ")
    print("   /\    /\  /\      /\      /\/\/\ ")
    time.sleep(0.1)
    print("  /  \/\/  \/  \  /\/  \/\  /  \/  \ ")
    time.sleep(0.1)
    print(" /    \ \  /    \/ /   /  \/    \   \ ")
    time.sleep(0.1)
    print(";;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;")
    time.sleep(0.1)
    print("iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii")   
    return
def the_caverns():
    print("iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii")
    time.sleep(0.1)
    print(";;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;")
    time.sleep(0.1)
    print("\      /   \   \  /   /\   \  /\      /")
    time.sleep(0.1)
    print(" \    /\  / \   \/\  /  \  /\/  \    /")
    time.sleep(0.1)
    print("  \  /  \/   \    /\/    \/      \  /")
    time.sleep(0.1)
    print("   \/          \/                 \/")
    time.sleep(0.3)
    print(" ")
    if 'poisoned' in game_status['character_status']:
        if game_status['poison_count'] == 0:
            print("YOU HAVE DIED OF POISON")
            game_status['life'] = 'poisoned'
            cont()
            game()
        print("You have ", game_status['poison_count']," turns until DEATH")
        game_status['poison_count'] -= 1
        cont()
    print("LEVEL: ", game_status['level'])
    game_status['chamber_count'] += 1
    print("")
    select_chamber()
    if game_status['chamber'] =='empty':
        print("This chamber is empty.")
    elif game_status['chamber'] == 'musician':
        run_musician()
    elif game_status['chamber'] == 'musician_quest':
        run_musician_quest()
    elif game_status['chamber'] == 'musician_quest_fail':
        run_musician_quest_fail()
    elif game_status['chamber'] == 'girl':
        run_girl()
    elif game_status['chamber'] == 'ghost':
        run_ghost()
    elif game_status['chamber'] == 'hoplite':
        run_hoplite()
    elif game_status['chamber'] == 'collector':
        run_collector()
    elif game_status['chamber'] == 'physician':
        run_physician()
    elif game_status['chamber'] == 'chimera':
        run_chimera()
    elif game_status['chamber'] == 'mother':
        run_mother()
    elif game_status['chamber'] == 'tanit_shrine':
        run_tanit_shrine()
    elif game_status['chamber'] == 'dido_shrine':
        run_dido_shrine()
    elif game_status['chamber'] == 'scholar':
        run_scholar()
    elif game_status['chamber'] == 'moloch_shrine':
        run_moloch_shrine()
    elif game_status['chamber'] == 'lost adventurer':
        lost_adventurer()
    elif game_status['chamber'] == 'cave_merchant':
        run_cave_merchant()
    elif game_status['chamber'] == 'coin thief':
        run_thief_coins()
    elif game_status['chamber'] == 'weapon thief':
        run_thief_weapon()
    else :
        #selects if torch goes out or not
        if game_status['torch'] == True:
            weather_report = random.randint(0,100)
            if weather_report < 5:
                print("")
                print("As you enter the chamber, water drips from the ceiling and extinguishes your torch.")
                print("Your torch has gone out...")
                print(" ")
                print("This will make it difficult to see, but perhaps it will be easier to slip by unnoticed.")
                print("(-5 AP, +5 SP)")
                cont()
                game_status['torch'] = False
        new_torch_status = game_status['torch']
        chamber_description()
        battle()
    if game_status['life'] == 'alive':
        choose_path()
        if game_status['level'] != 9:
            print("   /\    /\  /\      /\      /\/\/\ ")
            time.sleep(0.1)
            print("  /  \/\/  \/  \  /\/  \/\  /  \/  \ ")
            time.sleep(0.1)
            print(" /    \ \  /    \/ /   /  \/    \   \ ")
            time.sleep(0.1)
            print(";;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;")
            time.sleep(0.1)
            print("iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii")   
    else :
        game()
    game_status['chamber'] = 0
    print(" ")
    #returns to main()
    return
def end_game():
    print("               ___        O_._._._A_._._._O          ___          ")
    time.sleep(0.1)
    print("                 \`--.___,'=================`.___,--'/          ")
    time.sleep(0.1)
    print("                  \`--._.__                 __._,--'/          ")
    time.sleep(0.1)
    print("                    \  ,. l`~~~~~~~~~~~~~~~'l ,.  /          ")
    time.sleep(0.1)
    print("                      \|| || || || | || || || ||/                      ")
    time.sleep(0.1)
    print("        _______        ||_||_||_||_|_||_||_||_||        _______          ")
    time.sleep(0.1)
    print("         \\    `==---='-----------'='-----------`=---=='    //          ")
    time.sleep(0.1)
    print("         | `--.                                         ,--' |          ")
    time.sleep(0.1)
    print("          \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /          ")
    time.sleep(0.1)
    print("            \||  ____,-------._,-------._,-------.____  ||/          ")
    time.sleep(0.1)
    print("             ||\|___!`======='!`======='!`======='!___|/||     ")
    time.sleep(0.1)
    print("             || |---||--------||-| | |-!!--------||---| ||          ")
    time.sleep(0.1)
    print("   __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__          ")
    time.sleep(0.1)
    print("   o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o          ")
    time.sleep(0.1)
    print("  ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___          ")
    time.sleep(0.1)
    print("                           /|=============|\                                ")
    time.sleep(0.1)
    print(" ")
    game_status['sacrifice'] += game_status['kill_count']
    game_status['sacrifice'] += game_status['legendary_kill_count']*5
    print("||| |||||| || |||| |||||")
    print("THE TEMPLE OF BAAL HAMMON")
    print("||| |||||| || |||| |||||")
    print("")
    print("You have found the Temple of Ba'al Hammon!")
    print("Praise be to you!!!")
    cont()
    print("You cautiously step forward, entering the massive underground temple.")
    if game_status['companion'] != []:
        if 'The Girl' in game_status['companion']:
            print("The Girl latches onto your robes. It seems the sudden gradiosity of the chamber has frightened her.")
        if 'The Hoplite' in game_status['companion']:
            print("")
            print("HOPLITE: Well done, my friend! We have arrived!")
            print("YOU: I'm not sure I would have made it, without your help.")
            print("")
            print("You are speaking honestly, but The Hoplite waves you off with a smile.")
            print("")
            print("HOPLITE: Nonsense! I barely lifted a finger. Now, let us go to save Carthage!")
            print("")
    print("The air thickens with an eerie silence as you begin your way down the stone steps. Shadows dance along the ancient walls, and a sense of foreboding engulfs you. Despite the fear, you press on, determined to uncover its mysteries.")
    if game_status['companion'] != []:
        if 'The Scholar' in game_status['companion']:
            print("The Scholar shares none of your trepidation. She quickly runs ahead of you, her eyes fixed on the walls of the temple, mapping out its intricate carvings.")
            print("")
            print("SCHOLAR: These ships look like those of Tyre, but the god illustrated upon them is not Melqart... That means this temple must have been erected after the establishment of Sidon, but-- no! These markings here, this style predates even Sardinian works! Could it be that--")
            print("")
            print("You leave her to her mutterings, continuing on your way. Without the light of your torch she is eventually forced to give up her musings and instead makes you follow you, muttering excitedly to herself.")
        elif 'The Physician' in game_status['companion']:
            print("Suddenly, you notice The Physician lagging behind. His gaze is fixed longingly on the tunnel you have just emerged from.")
            print("")
            print("YOU: We can go back, if you like.")
            print("")
            print("The Physician seems about to take you up on the offer before he realizes it was meant to be a joke. He scowls, then follows sullenly behind you.")
    cont()
    print("As you wander through the hallowed halls of the ancient temple, your eyes fixate on a grand chamber. There, standing tall, is the imposing statue of Ba'al Haamon, its presence evoking both awe and trepidation.")
    print("You approach the Tophet, you take in its splendor. The sacrificial altar stands adorned with flowers, their petals vibrant. How are these flowers still living, so deep in this dark cavern? Goblets of crimson wine reflect flickering candlelight. Fragments of exotic fruits, precious gems, and tokens of devotion rest at its edges...")
    print("")
    if game_status['dog'] == True:
        print(game_status['dog_name']," approaches the tophet, sniffing around its base, his tail wagging excitedly.")
    cont()
    print("You fall to your knees, prostrating yourself before the towering statue of Ba'al Hammon.")
    print("")
    print("Suddenly, a booming voice sounds, as if reverberated through the very walls of the temple.")
    print("")
    if game_status['met_baal'] == False and game_status['elephant'] == True:
        print("BAAL: Who is this? One of my flock, but I have not seen you before...")
    elif game_status['met_baal'] == False and game_status['elephant'] == False:
        print("BAAL: Ah, the defiler has entered my chamber!")
        print("YOU: Defiler...?")
        print("")
        print("An image flashes across your mind... a war elephant... a sacred beast of carthage standing at the gates to the caverns. A terrible choice was made...")
        print("")
        print("BAAL: And now you come to me for help! Humans are always so selfish...")
        print("")
        print("You feel a deep sense of guilt, but do not back away. You do not ask for mercy for yourself, only to save the city!")
        print("")
    elif game_status['met_baal'] == True and game_status['elephant'] == False:
        print("BAAL: The defiler has returned! Here to disappoint me with more shallow offerings?")
        print(" ")
        print("He seems to remember you.")
    else: 
        print("BAAL: You have returned... I hope you will not disappoint me this time.")
        print(" ")
        print("He seems to remember you.")
    print("")
    print("YOU: Oh, mighty Ba'al Hammon, hear my plea! The Roman horde threatens Carthage's existence. I implore you to lend your divine strength and protect our great city. May your power guide us to victory and preserve our land.")
    print("BAAL: Is that so? Hm... I maybe persuaded.")
    print("")

    print("A god does not bestow favor without recieving something in return... Pushing down your fear, you move towards the Tophet. ")
    print("The god remains silent, awaiting your offering.")
    print("")
    if game_status['musician_hint'] == True:
        print("You move to give up your weapon, but then recall the advice of The Musician. Is this truly right? Does Baal Hammon really deserve your tribute, or your sacrifice...?")
    print("")
    print("==========================================")
    print('Would you like to offer your inventory as a sacrifice?')
    if game_status['musician_hint'] == True:
        print("Or do you attempt the ultimate sin... ")
    while True:
        choice = input(" ")
        print("==========================================")
        print("")
        if choice.lower() in ['y','yes','give offering','offer gift']:
            print("You give him everything you have.")
            if game_status['weapon'] == 'Old Axe':
                game_status['sacrifice'] += 5
            if game_status['weapon'] == 'Broken Sword':
                game_status['sacrifice'] += 5
            if game_status['weapon'] == 'Small Dagger':
                game_status['sacrifice'] += 5
            if game_status['weapon'] == 'Poor Sword':
                game_status['sacrifice'] += 10
            if game_status['weapon'] == 'Hoplites Dagger':
                game_status['sacrifice'] += 15
            if game_status['weapon'] == 'Leg of Mother Spider':
                game_status['sacrifice'] += 15
            if game_status['weapon'] == "Hoplites Spear":
                game_status['sacrifice'] += 15
            if game_status['weapon'] == "War Elephant's Tusk":
                game_status['sacrifice'] -= 10
            if game_status['weapon'] == "Maidens Chain":
                game_status['sacrifice'] += 15
            if 'Eyes of Cerberus' in game_status['items']:
                game_status['sacrifice'] += 10
            if 'dog eyes' in game_status['items']:
                game_status['sacrifice'] += 5
            if 'Basilisk Fang' in game_status['items']:
                game_status['sacrifice'] += 10
            if "Hoplite's Finger" in game_status['items']:
                game_status['sacrifice'] += 10
            if "Horns of the Minotaur" in game_status['items']:
                game_status['sacrifice'] += 10
            if 'gold coins' in game_status['items']:
                game_status['sacrifice'] += 15
            if 'bloody doll' in game_status['items']:
                game_status['sacrifice'] -= 5
            if 'Shining Amulet' in game_status['items']:
                game_status['sacrifice'] += 15
            if game_status['torch'] == True:
                game_status['torch'] = False
                game_status['sacrifice'] += 2
            if game_status['flask'] > 0 :
                game_status['sacrifice'] += 5*game_status['flask']
                game_status['flask'] = 0
            if 'poppy flower' in game_status['items']:
                game_status['sacrifice'] += 10
            game_status['weapon'] = 'no weapon'
            game_status['items'] = []
            break
        elif choice.lower() in ['no','n','no offering',"dont give offering","don't give offering"]:
            print("You offer nothing at the Tophet.")
            break
        elif choice.lower() in ['sin','ultimate sin','kill','attack','attack baal hammon','kill baal hammon','attack god','kill god','fight','fight baal hammon',"fight ba'al hammon","battle","battle baal","battle god","battle the god","battle baal hammon"]:
            run_god_killer()
        elif choice.lower() in ['inventory','status','info','info']:
            get_info()
        elif choice.lower() == 'help':
            get_help()
        else: 
            print("Please try again.")
    if game_status['companion'] != []:
        sacrifice_response_tracker = 0
        while game_status['companion'] != []:
            if game_status['sacrifice'] < 35 and sacrifice_response_tracker == 0:
                print("Oh this simply will not do! He will not grant you his favor, this way. You should have thought to bring more!")
                print("But then... an idea comes to you...")
                print("It is not something you ever thought you would do. You shielded your eyes and ears when those wicked monks performed it at the Byrsa, unable to tolerate the screams and the blood. But now... desperate times call for desperate measures... Carthage must be saved!")
                cont()
                if len(game_status['companion']) > 1:
                    print("")
                    print("==========================================")
                    print('Do you sacrifice one of your companions to earn further favor?')
                else:
                    print("")
                    print("==========================================")
                    print('Do you sacrifice ',*game_status['companion'],'to earn further favor?')
            elif game_status['sacrifice'] >= 35 and sacrifice_response_tracker == 0:
                print("The candles seem to glow more brightly... you sense that Baal Hammon may have appreciated your gift.")
                print("")
                print("But... is it really enough? It is no small thing you ask... ")
                print("It is not something you ever thought you would do. You shielded your eyes and ears when those wicked monks performed it at the Byrsa, unable to tolerate the screams and the blood. But now... desperate times call for desperate measures... Carthage must be saved!")
                cont()
                if len(game_status['companion']) > 1:
                    print("")
                    print("==========================================")
                    print('Do you sacrifice one of your companions to earn further favor?')
                else:
                    print("")
                    print("==========================================")
                    print('Do you sacrifice ',*game_status['companion'],'to earn further favor?')
            elif game_status['sacrifice'] < 35 and sacrifice_response_tracker > 0:    
                print("The candles glow brightly. Perhaps he is pleased... ")
                print("")
                print("==========================================")
                print("Do you sacrifice another, just to be sure?")
            else:    
                print('The temple remains dark and forboding. It is not enough!')
                print("")
                print("==========================================")
                print("Who else?")
            print("")
            print("--CURRENT COMPANIONS--")
            print(*game_status['companion'], sep =', ')
            print(" ")
            sacrifice = input(" ")
            print("==========================================")
            print(" ")
            if sacrifice.lower() in ['everyone','all of them','sacrifice everyone','sacrifice all of them','offer all','offer everyone']:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("One by one, you subdue your companions.")
                if 'The Girl' in game_status['companion']: 
                    print("The Girl struggles valiantly, but is easily overcome.")
                    game_status['sacrifice'] += 10
                if 'The Hoplite' in game_status['companion']: 
                    print("The Hoplite goes willingly, eager to serve the greater good.")
                    game_status['sacrifice'] += 5
                if 'The Physician' in game_status['companion']:
                    print("The Physician fights back, but he is no match for your strength.")
                    game_status['sacrifice'] += 5
                if 'The Scholar' in game_status['companion']:
                    print("The Scholar is oddly eager to meet the mythic god. She puts up no fight.")
                    game_status['sacrifice'] += 5
                if game_status['dog_name'] in game_status['companion']: 
                    print(game_status['dog_name'],"does not fight you, trusting you implicitly. You do your best to make the blow swift.")
                    game_status['sacrifice'] += 20
                    game_status['dog'] = False
                game_status['companion'] = []
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                break
            elif sacrifice.lower() in ['girl','the girl']:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("You lead the small girl to the alter. She struggles against your grip, but she is so weak, she is easily overcome.")
                print("She dies screaming for mercy. Perhaps she will find some in the afterlife.")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                game_status['sacrifice'] += 10
                game_status['companion'].remove("The Girl")
            elif sacrifice.lower() in ['the hoplite','hoplite','the knight','knight']:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("You turn to the Hoplite, but before you are forced to take him in hand, he bows to you.")
                print("")
                print("HOPLITE: I understand, my friend. It is for the good of Carthage. I only ask you make it quick!")
                print("")
                print("Overcome with gratitude, you nod. The blow is swift and hard. You hope he felt no pain.")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                game_status['sacrifice'] += 5
                game_status['companion'].remove("The Hoplite")
            elif sacrifice.lower() in ['the scholar','scholar']:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("You turn to The Scholar, ready to subdue her as necessary, but find her staring up at the statue with wide eyes. ")
                print("")
                print("SCHOLAR: In all my years, I never imagined I would get this close...")
                print("")
                print("Gently you take her head in your hands, and bring her to the Tophet.")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                game_status['sacrifice'] += 5
                game_status['companion'].remove("The Scholar")
            elif sacrifice.lower() in ['the physician','physician','doctor','the doctor']:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("You turn to The Physician, but he is already running back towards the caverns.")
                print("However, he is slow... you catch him easily, wrenching him back towards the Tophet.")
                print("He screams and struggles, but you force him down and deliver a swift blow to the back of his head.")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                game_status['sacrifice'] += 5
                game_status['companion'].remove("The Physician")
            elif sacrifice.lower() in ['dog','the dog','my dog',game_status['lower_dog_name']]:
                sacrifice_response_tracker = sacrifice_response_tracker + 1
                print("You look down at ", game_status['dog_name']," with tears forming in your eyes.")
                print("")
                print("YOU: I am so sorry, my sweet boy... but we must do what we can.")
                print("")
                print("His gaze is warm. He does not understand.")
                print("You call him to you, petting his head lightly. When he finally closes his eyes, contented in your arms, you deliver a hard blow to his neck.")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                game_status['sacrifice'] += 10
                game_status['companion'].remove(game_status['dog_name'])
                game_status['dog'] = False
            elif sacrifice.lower() in ['none','no','n','no one','no one else','no more','cancel','no sacrifice',"don't sacrifice","dont sacrifice","give up"]:
                print('How valiant of you...')
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                break
            elif sacrifice.lower() in ['kill','attack','attack baal hammon','kill baal hammon','attack god','kill god']:
                run_god_killer()
            elif sacrifice.lower() in ['inventory','status','info','info']:
                get_info()
            elif sacrifice.lower() == 'help':
                get_help()
            else: 
                print("Please try again.")
            print(" ")
        print('Tears in your eyes, you once again beg for Baal Hammons favor...')
    else:
        print("With that, you once again beg for Baal Hammon's favor...")
    cont()
    print('□')
    time.sleep(0.3)
    print('...◇')
    time.sleep(0.3)
    print('.......□')
    time.sleep(0.3)
    print('..........◇')
    time.sleep(0.3)
    print('.............□')
    time.sleep(0.3)
    print('................◇')
    time.sleep(0.3)
    print('....................□')
    time.sleep(0.5)
    if game_status['kill_count'] == 0:
        game_status['life'] = 'saintly'
    else: 
        if game_status['sacrifice'] >= 40:
            game_status['life'] = 'favored'
        elif 30 < game_status['sacrifice'] < 40:
            game_status['life'] = 'neutral'
        elif 10 < game_status['sacrifice'] <= 30:
            game_status['life'] = 'unfavored'
        else:
            game_status['life'] = 'cursed'
    #returns to main()
    return
#game() is game results/game over options, NOT main gameplay function
def game():
    if game_status['life'] == 'dead':
        if game_status['chamber'] == 'spiders':
            print("It is hopeless! No matter how many times you try to keep them off, the spiders keep coming, swarming you entirely.")
            print("Though small, their venom is a powerful paralytic, and soon you feel your limbs begin to slow.")
            print("It is only a few moments before you are rendered completely immobile.")
            print("The last thing you see before the venom stops your breathing are thousands of tiny spiders wrapping your paralyzed body in their sticky web.")
        elif game_status['chamber'] == 'rats':
            print("How could it have come to this?")
            print('You thought you had the upper hand, but the rats are quicker and more numerous.')
            print("You try to fight your way out of the swarm, but it is hopeless.")
            print("You feel them biting at you. As soon as you brush one away, two more take its place.")
            print("You are devoured alive.")
        elif game_status['chamber'] == 'dogs':
            print("These dogs are like nothing you have seen before!")
            print("They move quickly, almost in concert, as if they think as one.")
            print("You feel the first bite connect with your ankle, the next on your backside.")
            print('Soon, the pain of their teeth is all you can feel. You are devoured alive.')
        elif game_status['chamber'] == 'baboons':
            print("First, the monkeys throw things at you-- sticks, stones, detritus.")
            print("Then, they grow more bold, throwing themselves down to meet you with their wailing limbs and teeth barred.")
            print("You manage to hold them off, but one gets you from behind.")
            print("Before you know it, you are overwhelmed. Their teeth rip into your flesh and their fists beat you bloody.")
        elif game_status['chamber'] == 'blemyae':
            print("You are no match for the headless men. It was foolish to think you could be!")
            print("They have been raised in these dark caverns, while you know them barely at all.")
            print("After a moments struggle, you are struck upon the head.")
            print("The beating is painful, but swift.")
        elif game_status['chamber'] == 'shadows':
            print("Perhaps it was foolish to even try... the darkness cannot be fought. It cannot be escaped.")
            print("The shadows overwhelm you and the voices grow louder and louder and louder, your own cries of anguish joining the dark chorus.")
        elif game_status['chamber'] == 'basilisk':
            print("Try as you might, you are unable to succeed against the Basilisk. As the Basilisk's gaze locks with yours, petrification grips your body, freezing you in eternal stone, forever trapped in its deadly stare.")
        elif game_status['chamber'] == 'cerberus':
            print("Try as you might, you are unable to best the great Cerberus. One moment you are on your feet, the next you find yourself trapped within the mighty jaws of one of it's terrifying heads. You are ripped to shreds and devoured.")
        elif game_status['chamber'] == 'mother':
            print("Try as you might, you are unable to avoid the venemous fangs of the Mother Spider. Her fangs pierce your flesh, paralyzing you instantly. The last thing your eyes see is the steady winding of her sticky web around your immobile form.")
        elif game_status['chamber'] == 'chimera':
            print("Try as you might, the horrifying power of The Physician's maleficient beast overwhelms you. You are devoured and, as you writhe in agony in the stomach of the great beast, you feel a strange sensation... you are being absorbed into it! Perhaps soon the dreaded Chimera will find itself with a human face...")
        elif game_status['chamber'] == 'collector':
            print("Try as you might, you are unable to best the dreaded Collector! Its pale, grasping hands grab your throat and squeeze. As the light fades from your eyes, you marvel at the shining, shimmering splendor of his stolen cache.")
        elif game_status['chamber'] == 'ghost': 
            print("It was hopeless from the start-- the ghost obeys no law of man. Try as you might, its terrifying power quickly overwhelms you, mind and body. You find yourself possessed, overtaken by horrific visions and an endless pain. Perhaps, though, it is all that you deserve...")
        print("")
        print("You have been killed. Your quest has failed.")
        print("Carthage will burn, and these caverns will become your tomb.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print("  \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("   \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'poisoned':
        game_status['character_status'].remove("poisoned")
        print("Your wounds fester and pulse. Your vision is beginning to go. Looking down at yourself, you swear it is as if your skin moves in the low light, as if something has crawled inside and taken over.")
        print("Unable to go on, you sit down to catch your breath.")
        print("You do not get up.")
        print("")
        print("Your quest has failed.")
        print("Carthage will burn, and these caverns will become your tomb.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'dido_fail':
        print(" ")
        print("In your final moments, as the world is going dark, you suddenly see a small light. It grows brighter, and brighter. A single flame in the darkness.")
        print("The demi-god Dido appears before your eyes.")
        print("You smile contentedly.")
        print(" ")
        print("YOU: Queen Dido, I did as you said... I would not let my companions fall. I took their place.")
        print(" ")
        print("As you stare up into the face of the illustrious demi-god, you watch in horror as her lip curls in disdain.")
        print(" ")
        print("DIDO: This is not what I intended at all. Were you even paying attention?")
        print(" ")
        print("Her image fades. The flame goes out. You are left alone in the darkness.")
        print("Your quest has failed.")
        print("Carthage will burn, and these caverns will become your tomb.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'dead_at_sea':
        print("The fisherman sees right through your scheme.")
        print("Before you even have a chance to try and take him out, you see him suddenly snatch up his ore and swing.")
        print("You have only a moment to shout in surprise before the world goes black.")
        print(" ")
        print("After robbing you of your valuables, he pushes your body overboard.")
        print("You have been killed. Your quest has failed.")
        print("Carthage will burn, and the sea will become your tomb.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'favored':
        print("Bathed in divine light, you are bestowed the favor of Ba'al Hammon.")
        print("Ravaged by a relentless plague, the Roman armies crumble while Carthage, touched by divine grace, is saved from impending ruin. Victory and salvation intertwine, altering the course of history.")
        print("")
        print("")
        cont()
        print("           _______                      _______  _         ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /| ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( | ")
        time.sleep(0.1)
        print("  \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | | ")
        time.sleep(0.1)
        print("   \   /  | |   | || |   | |  | |( )| || |   | || (\ \) | ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | || || || |   | || | \   | ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | () () || (___) || )  \  | ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______)(_______)|/    )_) ")
        print(" ")
    elif game_status['life'] == 'neutral':
        print("Bathed in divine light, you are bestowed the favor of Ba'al Hammon... but it is not enough.")
        print("The Roman armies invade the next day. Carthage is burned, its peoples massacred or sold off into slavery.")
        print("You, blessed by divine light, are somehow spared. The sole survivor of everyone you know. The guilt haunts you for the rest of your life.")
        print("Some may say you have won but can this really be considered a victory?")
        print(" ")
        print("")
        cont()
        print("  ______   _______  _______           ")
        time.sleep(0.1)
        print(" (  __  \ (  ____ )(  ___  )|\     /| ")
        time.sleep(0.1)
        print(" | (  \  )| (    )|| (   ) || )   ( | ")
        time.sleep(0.1)
        print(" | |   ) || (____)|| (___) || | _ | | ")
        time.sleep(0.1)
        print(" | |   | ||     __)|  ___  || |( )| | ")
        time.sleep(0.1)
        print(" | |   ) || (\ (   | (   ) || || || | ")
        time.sleep(0.1)
        print(" | (__/  )| ) \ \__| )   ( || () () | ")
        time.sleep(0.1)
        print(" (______/ |/   \__/|/     \|(_______) ")
    elif game_status['life'] == 'unfavored':
        print("A darkness descends upon you. You failed to earn Ba'al Hammon's favor.")
        print("The Roman armies invade the next day. Carthage is burned, its peoples massacred or sold off into slavery.")
        print("You have lost.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'cursed':
        print("A darkness descends upon you. You have insulted Ba'al Hammon with your miserliness and weak disposition! ")
        print('Not only does withhold his favor, he curses you!')
        print("The Roman armies invade the next day. Carthage is burned, its peoples massacred or sold off into slavery.")
        print("And you, the loathsome coward, are particularly unlucky. You are captured, restrained, and paraded in Scipio's Triumph, humiliated in front of the Roman nobility and then taken out to the field and slaughtered like an animal.")
        print("You have lost.")
        print("")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    elif game_status['life'] == 'saintly':
        print("A darkness descends upon you. You have insulted Ba'al Hammon with your miserliness and weak disposition! ")
        print('Not only does withhold his favor, he curses you!')
        print(" ")
        time.sleep(0.5)
        print("But...")
        cont()
        print("Suddenly, a bright, white light bursts forth, and from within it the veiled form of Tanit! She stays the hand of her husband.")
        print("")
        print("TANIT: My dear child... despite all the horror you have faced, never once have you raised your hand in violence. Such feats do not come easily, and speak to your strength of heart. In honor of your heroic mercy, I shall elevate you beyond this mortal toil to take a place among my retinue.")
        print("YOU: Exalted Goddess, I thank you for your kindness! But what will become of Carthage?")
        print("TANIT: Worry not about such things. You will learn in time that death comes for all.")
        print("")
        print("The Roman armies invade the next day. Carthage is burned, its peoples massacred or sold off into slavery.")
        print("It is a horror. However, from your place within the retinue of Tanit, you find your vision no longer confined to what you once called 'the present'. Instead, you see all time and understand the inevitability of the rise and fall of nations.")
        print("Carthage may have fallen, but you have won.")
        print("")
        cont()
        print("           _______                      _______  _         ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /| ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( | ")
        time.sleep(0.1)
        print("  \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | | ")
        time.sleep(0.1)
        print("   \   /  | |   | || |   | |  | |( )| || |   | || (\ \) | ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | || || || |   | || | \   | ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | () () || (___) || )  \  | ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______)(_______)|/    )_) ")
        print(" ")
    elif game_status['life'] == 'Friend of Dido':
        print("With all the might you can muster, you dash your own head against the hard, cold stone of the Tophet. You feel the blood rush down your face, dizzy and overcome with pain. It is not enough. You go again, and again, and again.")
        print("You do not know how long it takes. Your vision is black, your body stiff, but still you try to complete your mission-- your self sacrifice.")
        print("There, in the darkness, you wait. You cannot hear the voice of Ba'al Hammon. You cannot hear anything.")
        print("")
        print("Then...")
        print("")
        print("A sudden light in the darkness. A flame, growing ever brighter.")
        print("Your vision returns, entranced by the flame. You try to crawl towards it, but are stayed by a slender hand upon your shoulder.")
        print("The demi-goddess Dido speaks into your ear.")
        print("")
        print("DIDO: Come, my valiant soldier. Protector of Carthage. Bravest of all the Phoenicians.")
        print("")
        print("You are elevated. The world-- time and space together-- unwraps like a papyrus scroll as you take your place among Dido's retinue.")
        print("Carthage is saved. The people commemorate you as a hero!")
        print("You have won.")
        print("")
        cont()
        print("           _______                      _______  _         ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /| ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( | ")
        time.sleep(0.1)
        print("  \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | | ")
        time.sleep(0.1)
        print("   \   /  | |   | || |   | |  | |( )| || |   | || (\ \) | ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | || || || |   | || | \   | ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | () () || (___) || )  \  | ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______)(_______)|/    )_) ")
        print(" ")
    elif game_status['life'] == 'killer':
        print("")
        print("With unwavering resolve, you clash with Ba'al Hammon, defying all odds. Your undying courage and indomitable spirit lead to victory, toppling the seemingly invincible deity and leaving the world in awe of your triumph.")
        print("Torn between worlds, you see the fallen god-- a corpse stretching through time and space, defiled.")
        print("With the last of your strength, you reach within it, grasping at its heart. You bring the beating flesh to your mouth, and devour it. The greatest of sin!")
        print("The world goes black. Time ends. The sound of a Kithara fills your ears.")
        print("")
        cont()
        print("In the gaping black of immortality, your vision slowly returns.")
        print("You see the shrine. The ancient temple. You stand atop it now, your heart beating at the same pace as the world.")
        print("A small figure is before you, on both knees in suplication.")
        print("")
        print("MAN: Oh, mighty Ba'al Hammon, hear my plea! The Roman horde threatens Carthage's existence--")
        print("")
        print("You hear his plea, and await your sacrifice.")
        print("")
        cont()
        print("           _______                      _______  _         ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /| ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( | ")
        time.sleep(0.1)
        print("  \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | | ")
        time.sleep(0.1)
        print("   \   /  | |   | || |   | |  | |( )| || |   | || (\ \) | ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | || || || |   | || | \   | ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | () () || (___) || )  \  | ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______)(_______)|/    )_) ")
        print(" ")
    elif game_status['life'] == 'failure':
        print("With unwavering resolve, you clash with Ba'al Hammon. However, it is hopeless-- the timeless power of the god overwhelms you, ripping to pieces, smaller and smaller, until nothing is left.")
        print("Not even death awaits you now.")
        print("You are nothing.")
        print(" ")
        cont()
        print("           _______             _        _______  _______ _________ ")
        time.sleep(0.1)
        print(" |\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/ ")
        time.sleep(0.1)
        print(" ( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   ")
        time.sleep(0.1)
        print(" \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   ")
        time.sleep(0.1)
        print("  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   ")
        time.sleep(0.1)
        print("    ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   ")
        time.sleep(0.1)
        print("    | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   ")
        time.sleep(0.1)
        print("    \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   ")
    print(" ")
    cont() 
    print(" ")
    print("")
    print("")
    print("||||| |||||")
    print("FINAL SCORE")
    print("||||| |||||")
    print("")
    print("Total Kills: ", game_status['kill_count'])
    print("Legendary Kills: ", game_status['legendary_kill_count'])
    print("Successful Flees: ", game_status['flee_count'])
    print("Chambers Cleared: ", game_status['chamber_count'])
    print(" ")
    print("=====================")
    print("Would you like to play again?")
    answer = input("")
    print("==========================================")
    print(" ")
    if answer.lower() in ['yes', 'y']:
        game_reset()
        print('Good luck...')
    elif answer.lower() in ['no', 'n']:
        print('Thanks for playing!')
        game_status['status'] = False
    elif answer.lower() in ['fuck you', 'this game sucks', 'i hate this game']:
        print('Fuck you too!')
        game_status['status'] = False
    print("")
    print("")
    print("")
    print("")
    print("")
    return

#cavern-specific mechanics
def battle():
    #gives opponent
    opponent = game_status[game_status['chamber']]
    #gives stat info so player may make an informed choice
    get_total_AP_SP()
    print("")
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    print(" ")
    dice_attack = random.randint(0,10)
    dice_speed = random.randint(0,10)
    attack = dice_attack + game_status['bonus_AP'] + game_status['base_AP']
    speed = dice_speed + game_status['bonus_SP'] + game_status['base_SP']
    print(" ")
    #opponent stats are pulled from dictionary, index_0 = attack, index_1 = flee
    if 'Eyes of Cerberus' in game_status['items']:
        print("The Eyes of Cerberus reveals to you the enemy's secrets...")
        print("---ENEMY STATS---")
        print("AP: ", opponent[0])
        print("SP: ",opponent[1])
    elif 'dog eyes' in game_status['items']:
        print("The dog eyes reveal a faint image of the enemy's power...")
        upperAP = random.randint(5,10)
        lowerAP = random.randint(-10,-5)
        upperSP = random.randint(5,10)
        lowerSP = random.randint(-10,-5)
        upper_APbound = opponent[0] + upperAP
        lower_APbound = opponent[0] + lowerAP
        upper_SPbound = opponent[1] + upperSP
        lower_SPbound = opponent[1] + lowerSP
        if lower_APbound < 0:
            lower_APbound = 0
        if lower_SPbound < 0:
            lower_SPbound = 0
        print("---ENEMY STATS---")
        print("AP: ", lower_APbound,"-",upper_APbound)
        print("SP: ",lower_SPbound,"-",upper_SPbound)
    else:
        print("---ENEMY STATS---")
        print("AP: ???")
        print("SP: ???")
    print("")
    print("==========================================")
    print("Do you wish to Fight or Flee?")
    while True:
        answer = input("")
        print("==========================================")
        print(" ")
        if answer.lower() in ['fight','fight them','fight him', 'fight her', 'fight it', 'kill', 'kill him', 'kill them', 'kill her', 'kill it', 'attack', 'attack them', 'attack him', 'attack her', 'attack it']:
            roll_dice()
            print("You rolled a", dice_attack)
            if attack >= opponent[0]:
                print("")
                time.sleep(0.5)
                print("Success!")
                successful_kill()
                injury_margin = attack - opponent[0]
                if injury_margin <= 4 and game_status['chamber'] not in ['basilisk','chimera']:
                    injured()
                print("")
            else :
                print("")
                time.sleep(0.5)
                print ("You could not defeat the enemy.")
                print("")
                print("==========================================")
                if game_status['companion'] != [] and game_status['flask'] > 0:
                    print("If you wish to continue, you may either sacrifice a companion or take a flask.")
                    while True:
                        answer2 = input(" ")
                        print("==========================================")
                        print(" ")
                        if answer2.lower() in ['flask','take flask']:
                            use_flask()
                            break
                        elif answer2.lower() in ['sacrifice','companion','sacrifice companion','leave behind','leave','abandon']:
                            take_the_fall()
                            break
                        elif answer2.lower() in ['die','just die','give up','sacrifice myself','self sacrifice','end']:
                            if game_status['met_dido'] >0:
                                game_status['life'] = 'dido_fail'
                                return
                            else: 
                                game_status['life'] = 'dead'
                                return
                        elif answer2.lower() in ['inventory','status','info']:
                            get_info()
                        elif answer2.lower() == 'help':
                            get_help()
                        else: 
                            print("Please try again.")
                    break
                elif game_status['companion'] != [] and game_status['flask'] <= 0:
                    print("You have no more flasks... but you can sacrifice a companion!")
                    take_the_fall()
                    break
                elif game_status['companion'] == [] and game_status['flask'] > 0:
                    print("Use a flask to revive and escape?")
                    use_flask()
                    break
                else :
                    game_status['life'] ='dead'
                    return
            break
        elif answer.lower() in ['flee','run','run away']:
            roll_dice()
            print("You rolled a", dice_speed)
            if speed >= opponent[1]:
                print("")
                time.sleep(0.5)
                print("Success!")
                successful_flee()
                print("")
                game_status['flee_count'] += 1
            else :
                print("")
                time.sleep(0.5)
                print ("The enemy caught you trying to escape!")
                print("")
                if game_status['companion'] != [] and game_status['flask'] > 0:
                    print("==========================================")
                    print("If you wish to continue, you may either sacrifice a companion or take a flask.")
                    while True:
                        answer2 = input(" ")
                        print("==========================================")
                        print(" ")
                        if answer2.lower() in ['flask','take flask']:
                            use_flask()
                            break
                        elif answer2.lower() in ['sacrifice','companion','sacrifice companion','leave behind','leave','abandon']:
                            take_the_fall()
                            break
                        elif answer2.lower() in ['die','just die','give up','sacrifice myself','self sacrifice']:
                            if game_status['met_dido'] >0:
                                game_status['life'] = 'dido_fail'
                                return
                            else: 
                                game_status['life'] = 'dead'
                                return
                        elif answer2.lower() in ['inventory','status','info']:
                            get_info()
                        else: 
                            print("Please try again.")
                    break
                elif game_status['companion'] != [] and game_status['flask'] <= 0:
                    take_the_fall()
                    break
                elif game_status['companion'] == [] and game_status['flask'] > 0:
                    use_flask()
                    break
                else :
                    game_status['life'] ='dead'
                    return
            break
        elif answer.lower() in ['inventory','status','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else :
            print("Please try again.")
    #returns to the_abyss() OR out_at_sea() OR end_game()
    game_status['chamber'] = 0
    return
def chamber_description():
    if game_status['chamber'] == 'spiders':
        #note spider count does not follow normal convention
        #at time of dev, spider_count was used to trigger Mother Quest
        #therefore spider_room_count established to count number of spider encounters for player engagement
        if game_status['torch'] == True:
            if game_status['spider_room_count'] == 0:
                print("You see nothing. It appears empty.")
                print("Cautiously, you begin to move to the other end of the chamber, sticking close to the wall in case of an ambush. ")
                print("Nearly to the other side, you trip over a fallen stone and put your hand out to the wall to catch your balance, only to find it sticks!")
                print("You realize with horror that the walls are covered in spider webs!")
                print("Suddenly, thousands of SPIDERS spill out from cracks in the walls, swarming you.")
            else:
                print("You see nothing. It appears empty.")
                print("You bring your torch closer to the wall to inspect it and… it is as you thought. SPIDERS!")
            game_status['spider_room_count'] += 1
            if 'The Girl' in game_status['companion']:
                print("")
                print('The Girl lets out a horrified shriek, batting them away in a frenzy.')
        else : 
            print("You cannot hear nor see anything in the darkness.")
            print("It is impossible to determine what lays ahead.")
    elif game_status['chamber'] == 'rats':
        if game_status['torch'] == True:
            if game_status['rat_count'] == 0:
                print("A putrid smell fills the air. Along the ground you spy the remains of what must have been some beast of the caverns. It is long dead.")
                print("RATS move among its corpse, much larger in size and aggressive in disposition than the ones you have seen on the surface. ")
                print("They look diseased.")
                if 'The Physician' in game_status['companion']:
                    print('The Physician wears a look of horror on his face.')
                    print("")
                    print("PHYSICIAN: I would not get too close to those things, if I were you! I have seen rat bites do horrific things to the flesh...")
                    print("")
            else: 
                print("What a horrible smell!")
                print("You have stumbled upon another corpse, and more diseased RATS feasting upon it.")
            game_status['rat_count'] += 1
        else: 
            print("You cannot hear nor see anything in the darkness.")
            print("All you can recognize is a putrid smell, like something rotting.")
    elif game_status['chamber'] == 'dogs':
        if game_status['torch'] == True:
            if game_status['dog_count'] == 0:
                print("Along the back wall you spot a small pack of WILD DOGS, though they look… abnormal. Pale, with red eyes and long snouts.")
                print("Perhaps they ventured down to these caves centuries ago and adapted. Perhaps they aren’t dogs at all…")
                print("They have already spotted you and hold perfectly still and silent, their red eyes watchful in the dark.")
            else: 
                print('Immediately you spot them: WILD DOGS.')
                print("These dogs too seem abnormal. They share the same white coats and red eyes as the ones before.")
                print("Hopefully they do not share their viciousness...")
            game_status['dog_count'] += 1
        else:
            print("You cannot hear nor see anything in the darkness.")
            print("It is impossible to determine what lays ahead.")
        if game_status['dog'] == True:
            print(" ")
            print(game_status['dog_name']," growls low in his throat, his fur standing on end.")
            print("Whatever they are, he does not seem to like them...")
        opponent = game_status['dogs']
    elif game_status['chamber'] == 'baboons':
        if game_status['torch'] == True:
            if game_status['baboon_count'] == 0:
                print("This chamber has more greenery than the others. ")
                print("Vines weave across the ceiling and against a far wall you can see the root system of a tree burrowing further underground.")
                print("It is such a wonderful sight, until you spot them: MONKEYS hiding in the leaves! Big ones, with peering black eyes set into sneering red faces. ")
            else: 
                print("Another lush chamber.")
                print("This time, your eyes immediately move to scan the vines and-- yes, there!")
                print("MONKEYS! Just as big and mean looking as the last ones.")
            game_status['baboon_count'] += 1
        else: 
            print("You can hear a soft rustling. The air smells fresher in here.")
            print("Beyond that, you do not know.")
    elif game_status['chamber'] == 'blemyae':
        if game_status['torch'] == True:
            if game_status['blemyae_count'] == 0 and game_status['blemyae_room_count'] == 0:
                print("The first thing you notice is the smell of smoke. ")
                print("The chamber is massive, with stepped crevasses up its side and a long drop down to an underground river below. ")
                print("Dotted throughout you can make out the source of the smell—little fires, not much more than embers, burn in the darkness. ")
                print("Not only that but… are those huts? ")
                print("You see a figure moving among the fires. It looks like a person, but you realize with a gasp, the figure has no head! ")
                print("It turns towards the flames and you can see it now—one large eye staring out from the center of its chest.")
                print("Not humans— HEADLESS MEN!")
                game_status['blemyae_room_count'] += 1
            elif game_status['blemyae_count'] == 0 and game_status['blemyae_room_count'] > 0: 
                print('You smell the smoke before you see them... more of the HEADLESS MEN!')
                print("The exit of the chamber is not far. You think perhaps you can reach it unnoticed.")
                game_status['blemyae_room_count'] += 1
            elif game_status['blemyae_count'] == 1:
                print('You smell the smoke before you see them... more of the HEADLESS MEN!')
                print("The exit of the chamber is not far. You think perhaps you can reach it unnoticed, but before you can begin there is a sudden loud, bellowing sound. It sounds like a trumpet.")
                print("HEADLESS MEN who had been hiding jump out in ambush. ")
                print("This time, they are armed with clubs.")
                game_status['blemyae_room_count'] += 1
                if 'The Scholar' in game_status['companion']:
                    print("")
                    print("Suddenly, The Scholar lets out an exited gasp.")
                    print("")
                    print("SCHOLAR: Of course! These are the Blemyae! The mythic headless men of the Sebou River! How did they get here?")
                    print("YOU: Whatever they are, they are in our way.")
                    print("")
                    print("The Scholar moves to stand bodily in front of you.")
                    print("")
                    print("SCHOLAR: You must not attack them! They are an intelligent species-- unless you have the means to kill them all it will only make things worse for us.")
                    if 'The Hoplite' in game_status['companion']:
                        print("HOPLITE: They are humans like us? Then certainly, my friend, we should not kill them! We have enough wars to fight as it is!")
                    print("")
            elif game_status ['blemyae_count'] > 2:
                print("Another large chamber, with little huts and fire pits.")
                print("This time, the fires are out, but this make-shift village has not been abandoned...")
                print("Standing guard are more of the HEADLESS MEN, armed and even stronger than before.")
                print("They were expecting you.")
                if 'The Hoplite' in game_status['companion']:
                    print("")
                    print("The Hoplite sighs next to you.")
                    print("")
                    print("HOPLITE: This war will never end, now...")
                    print("")
                game_status['blemyae_room_count'] +=1 
        else: 
            print("You cannot see anything in the darkness.")
            print("However, you can smell something. It smells like smoke.")
    elif game_status['chamber'] == 'shadows':
        if game_status['torch'] == True and game_status['shadow_count'] == 0:
            print("This chamber is narrower than the others, and dark.")
            print('As you cautiously move toward the other end, it almost feels as if the shadows come with you, creeping along the walls.')
            print("Perhaps it is only your imagination, but the darkness feels different here.")
            print("You thrust out your torch toward a shadowy patch on the wall. It disappears under the light but somehow... slower than it should. As if it nearly forgot to it was supposed to.")
            print(" ")
            print("Then, you hear it-- a soft whisper.")
            print("It is a kind voice, but what it speaks to you... what it tells you to do...")
            print("")
            print("YOU: Hello? Is someone there?")
            print("") 
            print("The whispers do not acknowledge your shout. They are growing louder and more persistent.")
            print("You try not to listen, but the voices find a way inside.") 
            print("The SHADOWS moving along the wall! They are growing!")
            if 'The Girl' in game_status['companion']:
                cont()
                print("")
                print("You glance to your side and see The Girl, looking deep into the darkness.")
                print("")
                print("GIRL: I remember you... You saved me...")
                print("")
                print("She reaches out to them. The shadows wrap around her frail wrist. You have only a moment to yank her back before she is swallowed completely. Her unfocused gaze fixes on your face, and then she begins to cry.")
        elif game_status['torch'] == False and game_status['shadow_count'] == 0: 
            print("Without your torch, it is dark. However, this place seems... darker than the rest.")
            print("You cannot explain it, but it feels as if the SHADOWS are getting closer, invading into your skin, your eyes...")
            print("Then, you hear it-- a soft whisper.")
            print("It is a kind voice, but what it speaks to you... what it tells you to do...")
            print("")
            print("YOU: Hello? Is someone there?")
            print("") 
            print("The whispers do not acknowledge your shout. They are growing louder and more persistent.")
            print("You try not to listen, but the voices find a way inside.") 
            print("The shadows moving along the wall! They are growing!")
        elif game_status['shadow_count'] > 0: 
            print("Upon entering the chamber, you erupt in violent shivers.")
            print('The darkness in this chamber... it feels alive..')
            if 'The Girl' in game_status['companion']:
                print('The Girl clutches to your side. You can feel her trembling.')
            print("The voices begin to grow inside your head as SHADOWS envelops you.")
            if game_status['torch'] == False:
                print("Without your torch, the voices seem even stronger than before!")
        game_status['shadow_count'] += 1
    elif game_status['chamber'] == 'cerberus':
        if game_status['cerberus_count'] == 0:
            print("A dim light shines inside from a crack in the ceiling, illuminating a horrifying sight... Bones and congealed blood carpet the floor, whispering tales of unspeakable horrors. What beast could have caused this?")
            print("")
            print("Then, from the shadows, a massive creature emerges... the mythical three-headed dog CERBERUS!")
            print("A beast of legend in the flesh, all six of its red eyes fixed upon you, all three mouths curled into a snarl.")
            print(" ")
            if game_status['dog'] == True:
                print("At your side,",game_status['dog_name'],"barks viciously at the beast.")
            if 'The Hoplite' in game_status['companion']:
                print("The Hoplite claps you on the shoulder. Despite it all, he is smiling, a look of fierce determination showing from beneath his helm.")
                print("")
                print("HOPLITE: A legendary creature! Let us slay it together, my friend!")
        else: 
            print("Immediately you are overwhelmed with the scent of blood and decay.")
            print("Bodies of men and beast alike! Just as before...")
            print("You are sure you have never been to this chamber... could this place also be the lair of the CERBERUS?")
            print(" ")
            print("You do not have much time to wonder before the beast makes itself known.")
            print("It is indeed the legendary Cerberus! Has it followed you all this way?")
            print(" ")
            if game_status['dog'] == True:
                print("At your side,",game_status['dog_name'],"barks viciously at the beast.")
            if 'The Hoplite' in game_status['companion']:
                print("The Hoplite claps you on the shoulder. ")
                print("")
                print("HOPLITE: He shall not escape us this time, my friend!")
        game_status['cerberus_count'] += 1
    elif game_status['chamber'] == 'basilisk':
        if game_status['basilisk_count'] == 0:
            print("Your footsteps echo. This chamber is cavernous, and dimly lit by what appear to be sconces along the walls.")
            print("A collection of three stone statues stand directly in front of you. They appear to be of adventurers-- a swordsman, a young woman, a dog...")
            print("You step closer to examine them. They look terribly lifelike, as if they could get up and run if not made of stone.")
            print("But their expressions... they look afraid.")
            print("")
            print("There is a soft noise behind you. Nothing more than the sound of something softly slipping over stone, but enough to grab your attention. You turn and your heart stops at the sight before you-- a massive snake, larger than horse!")
            if 'The Physician' in game_status['companion']:
                print("Next to you, The Physician gasps, his eyes wide.")
                print("")
                print("PHYSICIAN: Is that could it be...? I did not know any still existed!")
                print("YOU: You know of this creature?")
                print("PHYSICIAN: Yes! Yes! It is said their fangs can fight off the effects of poison! It is the legendary BASILISK!")
            else: 
                print("You think you may have heard of this creature before-- it is the legendary BASILISK!")
        else: 
            print("At first glance, this chamber appears empty.")
            print("However... along the wall you see them-- sconces lit with an everlasting flame.")
            print("Could the BASILISK be here?")
            print("You turn just in time to see it slithering up the passage behind you!")
            if 'The Physician' in game_status['companion']:
                print("")
                print("The Physician grabs you by the robes, shaking you.")
                print("")
                print("PHYSICIAN: You must kill it! I must see that fang!")
        if 'poisoned' in game_status['character_status'] and 'The Physician' in game_status['companion']:
            print("")
            print("Perhaps it would be best to run, but you recall what The Physician said.")
            print("Slay the Basilisk, and perhaps you can find a cure for the poison...")
            print("")
        game_status['basilisk_count'] +=1
    elif game_status['chamber'] == 'minotaur':
        if game_status['minotaur_count'] == 0: 
            print("The room you have entered is by far the largest you have seen thus far.")
            print("It is empty... and cold. An unnatural light shines up from the floor, illuminating everything in a sickly blue glow.")
            print("You look to the far end of the chamber and see a figure, large and ominous, standing upright and staring in your direction.")
            print("It appears to be a man, but is too large to be a man... And... it has horns.")
            if 'The Scholar' in game_status['companion']:
                print("The Scholar rushes towards you, her arms waving excitedly towards the best.")
                print("")
                print("SCHOLAR: Do you see! Do you see! It is the legend of legends! The strongest beast that ever walked the earth!")
                print("")
                print("As if you could miss it!")
            print("It is the dreaded beast of legend, the MINOTAUR!")
            print("")
        else:
            print("You enter into a very large room. It has a familiar sickly blue glow.")
            print("And yes, there, just as before...")
            print("At the far end it stands, menacing and massive... the MINOTAUR!")
        if game_status['entered_musician_chamber'] > 0 :
            print(" ")
            print("It would be better to run, but then you recall the words of The Musician.")
            print("Perhaps if you bring them the horns of the Minotaur they can help you...")
            print(" ")
        game_status['minotaur_count'] += 1
    #HIDDEN - Quests Unfinished
    elif game_status['chamber'] == 'flowers':
        print("Flowers!!")
    elif game_status['chamber'] == 'halfform':
        print("Time!!!")
        game_status['halfform_count'] += 1
    print(" ")
    return
def successful_kill():
    print("")
    if game_status['chamber'] == 'rats':
        game_status['kill_count'] += 1
        if game_status['weapon'] != 'no weapon':
            print("Gripping your sword tightly, you become an avenging force against the vermin. With calculated strikes, you cleave through the diseased horde, the clang of metal against fur ringing in your ears. Adrenaline courses through your veins as you eradicate the pestilence, leaving only silence in your wake. ")
        else:
            print("Unfazed by the swarm of scurrying rats, you rely on your primal instincts. Your hands become lethal weapons, crushing the vermin with unmatched strength.")
    elif game_status['chamber'] == 'dogs':
        game_status['kill_count'] += 1
        if game_status['weapon'] != 'no weapon':
            print("Fear turns to resolve as you brandish your weapon, its blade glinting in the gloom. With each strike, you fend off the savage creatures, finding your mark with unwavering accuracy. Determination fuels your every move as you vanquish the evil that lurks within the darkness.")
        else: 
            print("Fear turns to resolve as you face off against the dogs. You fend off the savage creatures with savage blows. Determination fuels your every move as you vanquish the evil that lurks within the darkness.")
        print(" ")
        drop_chance = random.randint(0,100)
        if drop_chance < 25 and 'dog eyes' not in game_status['items']:
            print("")
            print("When the battle is won, you approach the corpses of the abnormal canines.")
            print("You have heard rumors about these creatures... that their red eyes can reveal secrets.")
            print('Carefully you pluck the few left in tact and take them with you.')
            print("")
            print("ACQUIRED: dog eyes")
            game_status['items'].append("dog eyes")
            print("")
            if game_status['dog'] == True:
                print(game_status['dog_name']," sniffs at the eyes, then wretches.")
    elif game_status['chamber'] == 'spiders':
        game_status['kill_count'] += 1
        print("Swift and relentless, you strike at the countless spiders that scuttle toward you, their fangs poised to strike. With each swing of your blade, you fend off their venomous threat, the echoes of steel against exoskeleton filling the cavernous chamber. Determined, you emerge victorious, leaving behind a trail of fallen arachnids in your wake.")
        game_status['spider_count'] += 1
        spider_status = game_status['spider_count']
        if spider_status == 3:
            print(" ")
            print("Suddenly, you hear a bellowing cry echo up from the depths... Something has been awakened... hopefully it will not find you...!")
            print("")
            cont()
            game_status['mother_quest'] = True
    elif game_status['chamber'] == 'shadows':
        game_status['kill_count'] += 1
        shadow_stats = game_status['shadows']
        shadow_stats = [x - 3 for x in shadow_stats]
        game_status['shadows'] = shadow_stats
        print("Unwavering, you draw upon inner resolve to confront the intangible threat. With gestures of command, you banish the shadows with an aura of light that pierces the darkness. Their murmurs fade into oblivion, replaced by a newfound serenity.")
        print("It feels as if you have cleansed this cavern, if only a little bit.")
    elif game_status['chamber'] == 'baboons':
        game_status['kill_count'] += 1
        print("With quick reflexes and strategic moves, you engage in battle with the mischievous troop of monkeys. Skillfully, you fend off their playful attacks, emerging victorious.")
    elif game_status['chamber'] == 'blemyae':
        game_status['kill_count'] += 1
        print("Undeterred by their grotesque forms, you tap into an inner strength. Each blow lands with a resounding force, dismantling the threat before you. Your indomitable spirit prevails, a testament to your unyielding courage in the face of the macabre.")
        blemyae_stats = game_status['blemyae']
        new_blemyae_stats = []
        for elem in blemyae_stats:
            new_blemyae_stats += [elem + 5]
        game_status['blemyae'] = new_blemyae_stats
        if 'The Scholar' in game_status['companion']:
            print("The Scholar lets out a disappointed sigh.")
            print("")
            print("SCHOLAR: If only you had let me speak to them... perhaps they could have given us directions!")
            if 'The Physician' in game_status['companion']:
                print("PHYSICIAN: You're more than welcome to go look for more, if you like.")
                print("")
                print("She sticks her tongue out at him and he returns the favor, before they both follow you out.")
    elif game_status['chamber'] == 'basilisk' :
        game_status['legendary_kill_count'] += 1
        game_status['items'].append("Basilisk Fang")
        game_status['basilisk_lives'] = False
        print("")
        if game_status['weapon'] != 'no weapon':
            print("Fear grips your heart, but you muster all your courage. Swinging your weapon with precision, you deliver a fatal blow, vanquishing the deadly beast. The cave echoes with your triumphant roar as you emerge, victorious and unscathed.")
        else: 
            print("With a daring move, you lunge forward, grappling its scaly neck with all your might. Wrapping your hands tightly around its throat, you squeeze, feeling its strength wane. Gasping for breath, the Basilisk falls lifeless to the ground. You stand, victorious, your hands still trembling from the deadly encounter.")
        print("")
        print("You slayed the legendary Basilisk!")
        print("")
        cont()
        print("You pry out one of its massive fangs, to keep as a memento of your victory.")
        print(" ")
        print("ACQUIRED: Basilisk Fang")
        if 'poisoned' in game_status['character_status']:
            cont()
            print("")
            print("As soon as you grasp the Basilisk Fang you begin to feel a tingle in your hands. It moves up your arms, then your whole body. You feel refreshed.")
            print("Your poison is cured!")
            game_status['character_status'].remove('poisoned')
        print("")
        if 'The Physician' in game_status['companion']:
            print("The Physician approaches you from behind. You turn sharply, and find his eyes wide in wonder, his hands reaching.")
            print("")
            print("PHYSICIAN: May I...? May I hold it... please?")
            print("")
            print("You consider, but something about The Physician unsettles you. You quickly tuck the fang away and head to the end of the chamber, muttering something about needing to be quick. You can feel The Physician's furious gaze on you, but do your best to pay it no mind.")
    elif game_status['chamber'] == 'cerberus' :
        game_status['legendary_kill_count'] += 1
        print("The menacing growls of Cerberus reverberate through the air. Undeterred by its three ferocious heads, you summon every ounce of courage. With a primal roar, you engage the monstrous guardian. You strikes true, finding vulnerable spots with relentless precision until at last the beast is felled. ")
        print("You slayed the legendary three headed dog Cerberus!")
        print(" ")
        print("Before leaving, you gouge out its eyes, to keep as a memento of your victory.")
        print("")
        print("ACQUIRED: Eyes of Cerberus")
        game_status['cerberus_lives'] = False
        game_status['items'].append("Eyes of Cerberus")
    elif game_status['chamber'] == 'minotaur' :
        print("")
        game_status['legendary_kill_count'] += 1
        if game_status['weapon'] != 'no weapon':
            print("Your grip tightens around your weapon as you face the hulking beast, its snarling visage filled with malice. With calculated strikes, you engage in a fierce battle, dodging its massive horns. Finally, a decisive blow pierces through, and the Minotaur falls, defeated.")
        else: 
            print("With a surge of adrenaline, you unleash a thunderous punch, connecting with the beast's snarling face. The impact sends shockwaves through your hand and jolts the Minotaur backward, stunned. Seizing the moment, you follow up with swift strikes, unleashing a flurry of blows that bring the creature to its knees. The deafening silence that follows is a testament to your strength and valor.")
        print("")
        print("You slayed the legendary Minotaur!")
        print("The feat was thought impossible...")
        print(" ")
        print("ACQUIRED: Horns of the Minotaur")
        game_status['items'].append('Horns of the Minotaur')
        game_status['minotaur_lives'] = False
    elif game_status['chamber'] == 'collector' :
        game_status['legendary_kill_count'] += 1
        if game_status['versus_collector'] == 'hoplite fingers':
            print("You safely tuck the Hoplite's Finger into your pocket, then face the beast.")
            print("It still doesn't seem to have noticed you. Or if it did, it does not care, it's large black eyes fixed upon its littany of treasures.")
            if game_status['weapon'] != 'no weapon':
                print("You sneak up behind it and with one swift stroke slit its thin throat!")
            else: 
                print('You sneak up behind it and with a sudden surge of strength wrap your hands about its thin throat, choking until it falls to the ground.')
        else:
            if game_status['versus_collector'] == 'hoplite':
                print("The moment you pull The Hoplite up from the littany of golden treasures, The Collectors large black eyes fall upon you.")
                print("It seems to be slightly strengthened by its desperation for the coins.")
            elif game_status['versus_collector'] == 'dagger':
                print("The moment you pull The Hoplite up from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'hoplite spear':
                print("The moment you pull the Hoplite's Spear out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
                print("It seems to be somewhat strengthened by desperation.")
            elif game_status['versus_collector'] == 'weapon':
                print("The moment you pull your weapon out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'coins':
                print("The moment you pull the gold coins out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
                print("It seems to be greatly strengthened by its desire for the coins.")
            print("")
            print("COLLECTOR: Mine... Mine... MINE!!")
            print("")
            print("The Collector scurries forth, its malevolent grin etched on its twisted face.")
            print("Determination surges through you as you confront the grotesque creature. The humanoid beast has surprising strength and swiftness, but with a final, decisive strike, you send the creature sprawling, its lifeless form vanquished. ")
        print("You slayed the dreaded Collector!")
        print("")
        if game_status['versus_collector'] == 'hoplite':
            print("With the beast dead, you and The Hoplite continue on together.")
        elif game_status['versus_collector'] == 'hoplite fingers':
            print("With the beast dead, you continue on, The Hoplite's finger tucked away in your pocket.")
        elif game_status['versus_collector'] == 'hoplite dagger':
            print("With the beast dead, you continue on, The Hoplite's Dagger heavy in your hand.")
        elif game_status['versus_collector'] == 'hoplite spear':
            print("With the beast dead, you continue on, The Hoplite's shining spear in your hand.")
        elif game_status['versus_collector'] == 'weapon':
            print("With the beast dead, you continue on, your", game_status['weapon']," back in your hands once more.")
        elif game_status['versus_collector'] == 'coins':
            print("With the beast dead, you continue on, your gold coins once again in your possession.")
        print("")
        print("Perhaps you can help yourself to a trophy for your efforts...")
        print(" ")
        game_status['items'].append('Shining Amulet')
        print("ACQUIRED: Shining Amulet")
    elif game_status['chamber'] == 'chimera' :
        game_status['legendary_kill_count'] += 1
        print("Each head bares fangs dripping with sorrow, a reflection of its tormented existence. With a heavy heart, you raise your weapon, knowing that ending its suffering is your solemn duty. As each strike lands, a melancholic howl pierces the air, resonating with the weight of lost souls. In this somber battle, you are both conqueror and mourner, bringing an end to a tragic creature's plight.")
        print("Some things are not of this world... some things should never be.")
        cont()
        print("Turning now to The Physician who betrayed you, you stalk forward. He cowers, hands in front of his face, begging for mercy.  You give him none.")
        print("You slayed The Physician and his horrific creature, the chimera!")
        print("")
        print("Your hands soaked with it's blood, you are suddenly overcome with great weakness.")
        print("You fear it may be poisoned but soon the feeling fades, and you feel even better than before.")
        game_status['character_status'].append('Chimera Blood')
        game_status['chimera_lives'] = False
        if 'injured' in game_status['character_status']:
            print("Your injuries heal themselves!")
            game_status['character_status'].remove('injured')
    elif game_status['chamber'] == 'mother' :
        if game_status['weapon'] != 'no weapon':
            print('ts monstrous form looms above, fangs dripping with venom. Fear fades as your resolve takes hold. With unyielding bravery, you face the arachnid terror. Swinging your weapon with unwavering precision, you strike at its vulnerable underbelly. The creature writhes in agony, its monstrous screech filling the air.')
        else: 
            print("As you confront the nightmarish sight of the mother of all spiders, instinct takes over. With fearless determination, you charge forward. Gripping its venomous jaws, you summon unimaginable strength. Muscles strain as you wrench them apart, the cracking sound reverberating through the chamber. The spider writhes in agony, its monstrous form succumbing to your merciless grip. ")
        print("")
        print("You slayed the legendary mother of all spiders!")
        print("")
        print("With great care, you cut off one of her massive legs.")
        print("This will make a fine weapon!")
        print(" ")
        print("LEG OF MOTHER SPIDER")
        print("+15 AP, +8 SP") 
        print("Bonus against large enemies")
        print("")
        print("==========================================")
        print("Would you like to exchange your current weapon for the Leg of Mother Spider?")
        while True:
            answer = input("")
            print("==========================================")
            print("")
            if answer.lower() in ['yes','y','exchange','take leg','take spider leg','exchange weapon']:
                print("You trade your weapon for the Leg of Mother Spider.")
                print(" ")
                get_total_AP_SP()
                print("--PREVIOUS STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                game_status['weapon'] = 'Leg of Mother Spider'
                game_status['original_weapon'] = 'Leg of Mother Spider'
                #must set this so mother quest is not triggered again
                get_total_AP_SP()
                print("")
                print("--CURRENT STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                cont()
                break
            elif answer.lower() in ['no','n','keep weapon',"don't trade","don't trade weapons",'dont trade',"don't trade weapons"]:
                print("You leave the spider leg behind.")
                print("")
                cont()
                break
            elif answer.lower() in ['inventory','status','info']:
                get_info()
            elif answer.lower() == 'help':
                get_help()
            else :
                print("Please try again.")
        game_status['legendary_kill_count'] += 1
        game_status['mother_lives'] = False
    elif game_status['chamber'] == 'ghost':
        print("")
        print("Perhaps it is pointless, but you don't intend to go down without a fight!")
        print("You meet the white gaze of the ghost, ready to defend yourself.")
        print(" ")
        print("Miraculously... she stops.")
        print('The anger in her eyes slowly shifts to fear. The power you display is enough to overwhelm her.')
        print('Suddenly, she looks very much like the little girl you rescued.')
        print(" ")
        print("With a wailing cry, her form shifts, twists, and vanishes from the room.")
        print("You are safe.")
        cont()
        print("Just as you are about to leave the chamber, you notice something glinting in the corner.")
        print("You approach and find a long chain coiled where the ghost of the girl once sat.")
        print(" ")
        print("MAIDEN'S CHAIN")
        print("A ghostly chain made of some sort of composite ectoplasmic steel")
        print("+10 AP, +25 SP")
        print("Bonus against unearthly beings")
        print("")
        print("==========================================")
        print("Would you like to replace your current weapon with Maidens Chain?")
        while True:
            answer = input(" ")
            print("==========================================")
            print(" ")
            if answer.lower() in ['yes','y','replace','replace weapon','take chain','trade','trade weapon','take the chain','take the maidens chain',"take the maiden's chain","take maiden's chain",'take maidens chain']:
                print("You trade your weapon for the Maidens Chain.")
                print(" ")
                get_total_AP_SP()
                print("--PREVIOUS STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                game_status['weapon'] = 'Maidens Chain'
                game_status['original_weapon'] = 'Maidens Chain'
                #must set this so mother quest is not triggered again
                get_total_AP_SP()
                print("")
                print("--CURRENT STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                cont()
                break
            elif answer.lower() in ['no','n','keep weapon',"don't trade","don't trade weapons",'dont trade',"don't trade weapons"]:
                print("You leave the chain behind.")
                print("")
                cont()
                break
            elif answer.lower() in ['inventory','status','info']:
                get_info()
            elif answer.lower() == 'help':
                get_help()
            else :
                print("Please try again.")
    return
def successful_flee():
    if game_status['chamber'] == 'rats':
        print("As the diseased rats swarm around you in the dark cave, panic sets in. You desperately scramble for an exit, heart pounding. With every ounce of strength, you evade their gnashing teeth, narrowly slipping through a crevice just in time, leaving the relentless pack behind.")
    elif game_status['chamber'] == 'spiders':
        print("Surrounded by a relentless swarm of spiders, your instincts take over. With agile moves, you dart through narrow gaps, brushing webs aside. Adrenaline propels you forward until you break free, gasping for breath, leaving the creepy crawlers behind.")
    elif game_status['chamber'] == 'dogs':
        print("With a burst of adrenaline, you sprint towards safety, their snarls echoing behind you. Breathless, you escape their clutches, heart pounding with relief.")
    elif game_status['chamber'] == 'shadows':
        print("Enveloped by a sinister, whispering shadow, you sprint through the darkness. Its chilling voice lingers in your mind, urging you to succumb. Determination fuels your escape, breaking free from its grasp, leaving the haunting presence behind in the abyss.")
    elif game_status['chamber'] == 'baboons':
        print("As the mischievous troop of monkeys closes in, you sprint through the cavern. Their chattering pursuit echoes behind you, but you navigate the terrain with agility, eventually losing them.")
    elif game_status['chamber'] == 'blemyae':
        if game_status['blemyae_count'] == 0: 
            print("Quietly, you slip along the edge of the cavern, escaping the horde without their notice.")
        else: 
            print("Surrounded by a horde of headless men, you flee, their aimless groans filling the air. With agility and quick thinking, you navigate the chaos, narrowly escaping their grasping hands. Relief washes over you as you leave the eerie horde behind.")
    elif game_status['chamber'] == 'basilisk':
        print("Facing the deadly gaze of the basilisk, you muster every ounce of courage. Swiftly, you turn and sprint, the monster's slithering pursuit fueling your frantic escape. Heart pounding, you break free, leaving the petrifying creature behind.")
    elif game_status['chamber'] == 'cerberus':
        print("Confronted by the ferocious Cerberus, you feel a surge of adrenaline. Dodging its snapping jaws, you sprint through the darkness, heart pounding. In a daring move, you find an opening and slip away, leaving the menacing guardian of the underworld behind.")
    elif game_status['chamber'] == 'minotaur':
        print("As the Minotaur charges towards you, you swiftly maneuver through the cavern's twisting passages. Heart pounding, you seize the opportunity to slip away, leaving the enraged beast behind. Relief washes over you, triumphant in your escape from the clutches of the fearsome Minotaur.")
    elif game_status['chamber'] == 'chimera':
        print("With courage blazing in your eyes, you run past the howling chimera. Determined, you sprint towards freedom, leaving behind The Physician and his wicked beast.")
    elif game_status['chamber'] == 'mother':
        print("As the giant spider looms over you, you summon all your agility and sprint away. Its venomous fangs snap just inches from your heels as you narrowly escape its clutches, leaving the monstrous arachnid behind in your wake.")
    elif game_status['chamber'] == 'collector' :
        if game_status['versus_collector'] == 'hoplite fingers':
            print("You safely tuck the Hoplite's Finger into your pocket, then flee.")
            print("It does not even turn to watch you go. It's large black eyes remain fixed upon its littany of treasures.")
        else:
            if game_status['versus_collector'] == 'hoplite':
                print("The moment you pull The Hoplite up from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'dagger':
                print("The moment you pull The Hoplite up from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'hoplite spear':
                print("The moment you pull the Hoplite's Spear out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'weapon':
                print("The moment you pull your weapon out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            elif game_status['versus_collector'] == 'coins':
                print("The moment you pull the gold coins out from the littany of golden treasures, The Collectors large black eyes fall upon you.")
            print("")
            print("COLLECTOR: Mine... Mine... MINE!!")
            print("")
            print("As the Collector's pale, grasping hands close in, adrenaline surges through your veins. With a desperate lunge, you narrowly evade its grasp. The air fills with the creature's menacing snarls as you sprint away, heart pounding.")
        print("You escaped the dreaded Collector!")
        print("")
    return
def choose_path():
    #returns likelihood of a staircase appearing
    if 'The Scholar' in game_status['companion']:
        chance_down = random.randint(0,80)
    else: 
        chance_down = random.randint(0,100)
    #if 'go down stairs' is an option:
    if chance_down <= 40:
        option_1 = 'down the stairs'
        if game_status['left_count'] == 3:
            option_2 = random.choice(['straight','right'])
        elif game_status['right_count'] == 3:
            option_2 = random.choice(['straight','left'])
        else:
            option_2 = random.choice(['left','straight','right'])
        print('You may either go',option_1,"or",option_2)
        print(" ")
        print("==========================================")
        print("Which way will you go?")
        #player answer conditionals
        while True:
            answer = input(" ")
            print("==========================================")
            print(" ")
            if answer.lower() in ['left','go left','to left']:
                if option_1 != 'left' and option_2 != 'left':
                    print("There is no door to go left.")
                    time.sleep(1)
                    print("However...")
                    time.sleep(1)
                    print("You turn left and place your palms on the wall.")
                    print("You clear your mind, press forward, and suddenly are transported to a new chamber.")
                game_status['left_count'] += 1
                game_status['right_count'] = 0
                print("You go left.")
                break
            elif answer.lower() in ['right', 'go right', 'to right']:
                if option_2 != 'right':
                    print("You cannot go right.")
                else:
                    game_status['left_count'] = 0
                    game_status['right_count'] += 1
                    print("You go right.")
                    break
            elif answer.lower() in ['straight','go straight','to straight']:
                if option_2 != 'straight':
                    print("You cannot go straight.")
                else:
                    game_status['left_count'] = 0
                    game_status['right_count'] = 0
                    print("You go straight.")
                    break
            elif answer.lower() in ['down','stairs','go down']:
                game_status['left_count'] = 0
                game_status['right_count'] = 0
                game_status['level'] += 1
                print("You go down the stairs.")
                break
            elif answer.lower() in ['inventory','status','info']:
                get_info()
            elif answer.lower() == 'help':
                get_help()
            else :
                print("Please try again.")
    #if 'go down stairs' is not an option:
    else: 
        if game_status['left_count'] == 3:
            option_1 = random.choice(['straight','right'])
        elif game_status['right_count'] == 3:
            option_1 = random.choice(['straight','left'])
        else:
            option_1 = random.choice(['left','straight','right'])
        if game_status['left_count'] == 3:
            option_2 = random.choice(['straight','right'])
        elif game_status['right_count'] == 3:
            option_2 = random.choice(['straight','left'])
        else:
            option_2 = random.choice(['left','straight','right'])
        while option_1 == option_2 :
            if game_status['left_count'] == 3:
                option_2 = random.choice(['straight','right'])
            elif game_status['right_count'] == 3:
                option_2 = random.choice(['straight','left'])
            else:
                option_2 = random.choice(['left','straight','right'])
        print('You may either go',option_1,"or",option_2)
        print(" ")
        print("==========================================")
        print("Which way will you go?")
        #player answer conditionals
        while True:
            answer = input(" ")
            print("==========================================")
            print(" ")
            if answer.lower() in ['left','go left','to left']:
                if option_1 != 'left' and option_2 != 'left':
                    print("There is no door to go left.")
                    time.sleep(1)
                    print("However...")
                    time.sleep(1)
                    print("You turn left and place your palms on the wall.")
                    print("You clear your mind, press forward, and suddenly are transported to a new chamber.")
                game_status['left_count'] += 1
                game_status['right_count'] = 0
                print("You go left.")
                break
            elif answer.lower() in ['right', 'go right', 'to right']:
                if option_1 != 'right' and option_2 != 'right':
                    print("You cannot go right.")
                else: 
                    game_status['left_count'] = 0
                    game_status['right_count'] += 1
                    print("You go right.")
                    break
            elif answer.lower() in ['straight','go straight','to straight']:
                if option_1 != 'straight' and option_2 != 'straight':
                    print("You cannot go straight.")
                else: 
                    game_status['left_count'] = 0
                    game_status['right_count'] = 0
                    print("You go straight.")
                    break
            elif answer.lower() in ['down','stairs','go down']: 
                print("There is no stairwell in this room.")
            elif answer.lower() in ['inventory','status','info']:
                get_info()
            elif answer.lower() == 'help':
                get_help()
            else :
                print("Please try again.")
    #returns to the_caverns()
    if game_status['chamber'] == 'musician' and game_status['companion'] != []:
        if len(game_status['companion']) >2 and game_status['dog'] == True:
            print("As you exit the odd chamber, you suddenly find your companions back with you again.")
            print(game_status['dog_name'],"bounds up to you, barking and licking you excitedly, as if you had been gone for a very long time.")
            print("The others, however, do not seem to have noticed your absence. You decide not to mention it.")
        if len(game_status['companion']) == 2 and game_status['dog'] == True:
            companion = game_status['companion']
            print("As you exit the odd chamber, you suddenly find your companions back with you again.")
            print(game_status['dog_name'],"bounds up to you, barking and licking you excitedly, as if you had been gone for a very long time.")
            print(companion[2]," however, does seem to notice your absence. You decide not to mention it.")
        if game_status['companion'] == 1 and game_status['dog'] == True:
            print("As you exit the odd chamber, ",game_status['dog_name'],"bounds up to you, barking and licking you excitedly, as if you had been gone for a very long time.")
        if game_status['companion'] == 1 and game_status['dog'] == False:
            print("As you exit the odd chamber, you suddenly find ",*game_status['companion'],"back with you again.")
            print('They do not seem to have recognized your absence. You decide not to mention it.')            
    cont()
    return  
def select_quest():
    dice = random.randint(0,100)
    if game_status['left_count'] >= 4:
        if game_status['musician_done'] == True:
            game_status['chamber'] = 'moloch_shrine'
        elif game_status['musician_quest'] == False:
            game_status['chamber'] = 'musician'
        else:
            if 'Horns of the Minotaur' in game_status['items']:
                game_status['chamber'] = 'musician_quest'
            else:
                game_status['chamber'] = 'musician_quest_fail'
    elif game_status['level'] > 3 and dice <= 5 and game_status['met_girl'] == False:
        game_status['chamber'] = 'girl'
    elif game_status['scholar_quest'] == True and dice <=5:
        game_status['chamber'] = 'scholar'
    elif game_status['ghost_quest'] == True and dice <= 10:
        game_status['chamber'] = 'ghost'
    elif 'The Hoplite' in game_status['companion'] and dice <=10:
        game_status['chamber'] = 'hoplite'
    elif game_status['collector_quest'] == True and dice <= 5:
        game_status['chamber'] = 'collector'
    elif game_status['physician_quest'] == True and game_status['flask'] > 0 and dice <= 100:
        #only triggers if physician has seen flask being used (1st condition) and the user has flasks (2nd condition)
        game_status['chamber'] = 'physician'
    elif game_status['chimera_quest'] == True and dice <= 10:
        game_status['chamber'] = 'chimera'
    elif game_status['mother_quest'] == True and dice <= 10 and game_status['mother_lives'] == True:
        game_status['chamber'] = 'mother'
    elif 'gold coins' in game_status['items'] and dice <=5:
        game_status['chamber'] = 'coin thief'
    elif game_status['weapon'] != 'no weapon' and dice <= 2:
        game_status['chamber'] = 'weapon thief'
    #returns to select_chamber()
    return
def select_chamber():
    select_quest()
    while game_status['chamber'] == 0:
        if game_status['minotaur_boost'] == True:
            dice = random.randint(1,105)
            if 1 <= dice < 10:
                game_status['chamber']='empty'
                break
            elif 10 <= dice < 20:
                game_status['chamber']='spiders'
                break
            elif 20 <= dice < 30:
                game_status['chamber']='rats'
                break
            elif 30 <= dice < 40:
                game_status['chamber']='dogs'
                break
            elif 40 <= dice < 50:
                game_status['chamber']='baboons'
                break
            elif 50 <= dice < 60:
                game_status['chamber']='blemyae'
                break
            elif 60 <= dice < 68:
                game_status['chamber']='shadows'
                break
            elif 68 <= dice < 72 and game_status['cerberus_lives'] == True:
                game_status['chamber']= 'cerberus'
                break
            elif 72 <= dice < 76 and game_status['basilisk_lives'] == True:
                game_status['chamber']= 'basilisk'
                break
            elif 76 <= dice < 81 and game_status['lost_adventurer'] == 0 and game_status['weapon'] == 'no weapon':
                game_status['chamber'] = 'lost_adventurer'
                break
            elif 81 <= dice < 87 and game_status['tanit_shrine'] < 3:
                game_status['chamber'] = 'tanit_shrine'
                break
            elif 87 <= dice < 91 and game_status['level'] > 1:
                game_status['chamber'] = 'moloch_shrine'
                game_status['moloch_shrine'] += 1
                break
            elif 91 <= dice < 97:
                game_status['chamber'] = 'dido_shrine'
                break
            elif 97 <= dice <= 105 and game_status['minotaur_lives'] == True:
                game_status['chamber']= 'minotaur'
                break
        else: 
            dice = random.randint(1,100)            
            if 1 <= dice < 10:
                game_status['chamber']='empty'
                break
            elif 10 <= dice < 20:
                game_status['chamber']='spiders'
                break
            elif 20 <= dice < 30:
                game_status['chamber']='rats'
                break
            elif 30 <= dice < 40:
                game_status['chamber']='dogs'
                break
            elif 40 <= dice < 50:
                game_status['chamber']='baboons'
                break
            elif 50 <= dice < 59:
                game_status['chamber']='blemyae'
                break
            elif 59 <= dice < 68:
                game_status['chamber']='shadows'
                break
            elif 68 <= dice < 72 and game_status['cerberus_lives'] == True:
                game_status['chamber']= 'cerberus'
                break
            elif 72 <= dice < 76 and game_status['basilisk_lives'] == True:
                game_status['chamber']= 'basilisk'
                break
            elif 76 <= dice < 81 and game_status['lost_adventurer'] == 0 and game_status['weapon'] == 'no weapon':
                game_status['chamber'] = 'lost_adventurer'
                break
            elif 81 <= dice < 87 and game_status['tanit_shrine'] < 3:
                game_status['chamber'] = 'tanit_shrine'
                break
            elif 87 <= dice < 91 and game_status['level'] > 1:
                game_status['chamber'] = 'moloch_shrine'
                game_status['moloch_shrine'] += 1
                break
            elif 91 <= dice < 97:
                game_status['chamber'] = 'dido_shrine'
                break
            elif 97 <= dice <= 100 and game_status['minotaur_lives'] == True:
                game_status['chamber']= 'minotaur'
                break
    #returns to battle()
    return

#core game mechanics
def cont():                
    print("")
    print("CONTINUE?")
    while True:
        x = input(" ")
        if x.lower() in ['inventory','status','info']:
            get_info()
        elif x.lower() == 'help':
            get_help()
        else: 
            break
    print("")
    return
def get_info():
    print(" ")
    print("CHARACTER INFO")
    print('Weapon:', game_status['weapon'])
    if game_status['torch'] == True:
        print("Torch: lit")
    else :
        print("Torch: unlit")
    print("Flasks: ", game_status['flask'])
    print("")
    print("Active status effects:")
    if game_status['character_status'] == []:
        print("No active status effects")
    else:
        print(*game_status['character_status'], sep =', ')
    print(" ")
    print('Inventory: ')
    if game_status['items'] == []:
        print("Nothing in your inventory")
    else:
        print(*game_status['items'], sep =', ')
    print("")
    print("Companions:")
    if game_status['companion'] == []:
        print("You are alone")
    else:
        print(*game_status['companion'], sep =', ')
    return
def get_help():
    print("")
    print("HELP")
    print("Move forward in the story by typing answers to questions when prompted. ")
    print("Answers are not case sensitive.")
    print("")
    print("Type STATUS or INVENTORY at any time to bring up your current character details.")
    print("Type HELP at any time to bring up the gameplay rules.")
    print("")
    print("Total AP and SP are determiend by the following formulas, but may change based on gameplay factors:")
    print("Total AP = Base AP + Bonus AP + Dice Roll")
    print("Total SP = Base SP + Bonus SP + Dice Roll")
    print("You can get bonus AP/SP from weapons, companions, and items.")
    print("Some weapons, companions, and items may have increased bonus AP/SP against certain enemy types or in certain situations.")
    print(" ")
    return
def roll_dice():
    print(" ")
    print("Hit any key to roll the dice")
    answer = input(" ")
    print('□')
    time.sleep(0.3)
    print('...◇')
    time.sleep(0.3)
    print('.......□')
    time.sleep(0.2)
    print('..........◇')
    time.sleep(0.2)
    print('.............□')
    time.sleep(0.1)
    print('................◇')
    time.sleep(0.1)
    print('....................□')
    time.sleep(0.4)
    return      
def get_total_AP_SP():
    APbuff = 0
    SPbuff = 0
    if game_status['torch'] == False:
        APbuff = APbuff - 5
        SPbuff = SPbuff + 5
    if game_status['weapon'] == 'Old Axe':
        if game_status['chamber'] in ['basilisk','cerberus','minotaur','flowers','chimera','mother']:
            APbuff = APbuff + 15
            SPbuff = SPbuff + 5
        else :
            APbuff = APbuff + 10
            SPbuff = SPbuff + 5
    if game_status['weapon'] == "Hoplites Spear":
        if game_status['chamber'] in ['basilisk','cerberus','minotaur','flowers','chimera','mother']:
            APbuff = APbuff + 25
            SPbuff = SPbuff + 10
        else :
            APbuff = APbuff + 20
            SPbuff = SPbuff + 10
    if game_status['weapon'] == 'Leg of Mother Spider':
        if game_status['chamber'] in ['basilisk','cerberus','minotaur','flowers','chimera']:
            APbuff = APbuff + 20
            SPbuff = SPbuff + 8
        else :
            APbuff = APbuff + 15
            SPbuff = SPbuff + 8
    if game_status['weapon'] == 'Broken Sword':
        if game_status['chamber'] in ['baboons','blemyae','fisherman','collector_hoplite_version','collector_weapon_version','collector_coin_version','collector_spear_version']:
            APbuff = APbuff + 12
            SPbuff = SPbuff + 7
        else :
            APbuff = APbuff + 7
            SPbuff = SPbuff + 7
    if game_status['weapon'] == 'Poor Sword':
        if game_status['chamber'] in ['baboons','blemyae','fisherman','collector_hoplite_version','collector_weapon_version','collector_coin_version','collector_spear_version']:
            APbuff = APbuff + 16
            SPbuff = SPbuff + 11
        else: 
            APbuff = APbuff + 11
            SPbuff = SPbuff + 11
    if game_status['weapon'] == 'War Elephants Tusk':
        if game_status['chamber'] in ['baboons','blemyae','fisherman','collector_hoplite_version','collector_weapon_version','collector_coin_version','collector_spear_version']:
            APbuff = APbuff + 19
            SPbuff = SPbuff + 14
        else: 
            APbuff = APbuff + 14
            SPbuff = SPbuff + 14
    if game_status['weapon'] == 'Small Dagger':
        if game_status['chamber'] in ['spiders','rats','dogs']:
            APbuff = APbuff + 10
            SPbuff = SPbuff + 10
        else :
            APbuff = APbuff + 5
            SPbuff = SPbuff + 10
    if game_status['weapon'] == "Hoplites Dagger":
        if game_status['chamber'] in ['spiders','rats','dogs']:
            APbuff = APbuff + 15
            SPbuff = SPbuff + 20
        else :
            APbuff = APbuff + 10
            SPbuff = SPbuff + 20
    if game_status['weapon'] == 'Maidens Chain':
        if game_status['chamber'] in ['shadows','baal']:
            APbuff = APbuff + 25
            SPbuff = SPbuff + 15
        else :
            APbuff = APbuff + 10
            SPbuff = SPbuff + 25
    if game_status['weapon'] == 'Falcata':
        APbuff = APbuff + 40
        SPbuff = SPbuff + 40
    if 'Hoplites Finger' in game_status['items']:
        APbuff = APbuff +5
    if game_status['dog'] == True:
        if game_status['chamber'] in ['dogs','cerberus']:
            APbuff = APbuff + 10
            SPbuff = SPbuff 
        else :
            APbuff = APbuff + 5
            SPbuff = SPbuff 
    if 'The Girl' in game_status['companion']:
        girl_reduction = game_status['girl_reduction']
        APbuff = APbuff - girl_reduction[0]
        SPbuff = SPbuff - girl_reduction[1]
    if 'The Hoplite' in game_status['companion']:
        APbuff = APbuff + 10
        SPbuff = SPbuff + 0 
    if 'The Physician' in game_status['companion']:
        APbuff = APbuff + 3 
        SPbuff = SPbuff + 3
    game_status['bonus_AP'] = APbuff
    game_status['bonus_SP'] = SPbuff
    return
def take_the_fall():
    game_status['dido_trigger'] = True
    while True:
        print("==========================================")
        print("Who will you sacrifice?")
        print(" ")
        print("--COMPANIONS--")
        print(*game_status['companion'], sep =', ')
        print(" ")
        sacrifice = input(" ")
        print("==========================================")
        print(" ")
        if sacrifice in ['dog','the dog','my dog',game_status['lower_dog_name']] and game_status['dog'] == True:
            game_status['dog'] = False
            game_status['kill_count'] += 1
            print("Even on the brink of death, ",game_status['dog_name'],"stands by your side, teeth bared and snarling at the enemy.")
            print("If he could speak, would he tell you to go on ahead? Would he tell you to save yourself?") 
            print("He has always protected you. Always been loyal by your side. It's what he would want.") 
            print(" ")
            print("You begin to back away towards the door, but as you do, you find him following just behind.")
            print("The enemy is approaching. if he follows you, you will both be killed... ")
            print(" ")
            print("YOU: Stay, ",game_status['dog_name'],". You have to stay.")
            print(" ")
            print(game_status['dog_name']," does as he is told. Only his eyes move to follow as you turn and walk towards the door.")
            print("Yes, this is what he would want.")
            game_status['companion'].remove(game_status['dog_name'])
            break
        elif sacrifice in ['girl', 'the girl'] and 'The Girl' in game_status['companion']: 
            #NOTE NEW QUEST START! 
            game_status['ghost_quest'] = True
            game_status['kill_count'] += 1
            print("Bile rises in your throat at the thought, but you know what must be done.")
            print("She is slower than you, still injured from her capture. Perhaps it is cruel, but you have a mission to complete.")
            print("She was a burden, anyway...")
            print(" ")
            print("You bolt for the door. The Girl, who had shielded herself behind you, notices immediately.")
            print(" ")
            print("GIRL: Wait! Wait for me!")
            print(" ")
            print("You do not stop or slow. It only takes her a few moments to realize that you are not merely moving ahead, but intend to abandon her entirely.")
            print("Her shouts turn to desperate cries, then to sobs, and finally, to screams...")
            game_status['companion'].remove('The Girl')
            break
        elif sacrifice in ['physician', 'the physician', 'doctor', 'the doctor'] and 'The Physician' in game_status['companion']: 
            game_status['physician_quest'] = False
            game_status['kill_count'] += 1
            print("You are quick, but The Physician is quicker. He bolts")
            print("Behind you, the enemy begins their pursuit. You are running out of time. You must act quickly!")
            print(" ")
            if game_status['weapon'] in ['no weapon']:
                print("Without hesitation, you reach out, just barely managing to grab the tail end of his robe. He is yanked back towards you, and you swiftly but surely bring a powerful uppercut under his jaw.")
                print("His frail figure falls immediately to the floor. Blood begins to pour from his nose.")
            else:
                print("Without hesitation, you strike with your ", game_status['weapon'],". The strike connects, blood blooming across his back, and he falls to the ground.")
            print("You step around him, and then bolt for the door as he calls out for you.")
            print(" ")
            print("PHYSICIAN: You cannot do this!! I won't let you! I will find you, I swear, and I will make you pay for this!")
            print(" ")
            game_status['companion'].remove('The Physician')
            break
        elif sacrifice in ['hoplite', 'the hoplite', 'the knight'] and 'The Hoplite' in game_status['companion']: 
            game_status['hoplite_quest'] = False
            game_status['kill_count'] += 1
            print("You look to The Hoplite, unsure of what to do. He is much stronger than you, how can you possibly get away? Trip him? Stab him yourself? Then you see it-- he is looking right at you.")
            print("There is a sinking sensation in your stomach. He has caught you. Perhaps it is HIM who will leave YOU behind?")
            print("But then... he smiles. Gives you a short nod.")
            print(" ")
            print("HOPLITE: You go ahead, my friend. I will hold them off.")
            print(" ")
            print("You are speechless.  He would do so willingly? You almost mean to protest, to change your mind and fight it out together, but he interrupts before you get a chance.")
            print(" ")
            print("HOPLITE: Do not mourn me. I shall play my role, and you shall play yours. Go!")
            print(" ")
            print("You hesitate for a moment more, before turning and running for the door, the sound of The Hoplite's battlecry ringing in your ears.")
            game_status['companion'].remove('The Hoplite')
            break
        elif sacrifice in ['scholar', 'the scholar', 'the woman'] and 'The Scholar' in game_status['companion']: 
            game_status['kill_count'] += 1
            print("You look to The Scholar. Despite her small stature, she is doing her best to fend off the enemy.")
            print("She would not even notice...")
            print("")
            print("With that, you take off at a run, leaving The Scholar behind.")
            print("As you near the end of the chamber you hear her cry out to you, but it is too late. You are safe and she... well...")
        elif sacrifice in ['no one', 'noone','no sacrifice', 'nevermind', 'cancel','no','yourself','myself','me','suicide']:
            print("How valiant of you...")
            print(" ")
            print(" ")
            if len(game_status['companion']) >1:
                print("You sacrifice no one. You and your companions die together.")
            else:
                companion = game_status['companion']
                print("You sacrifice no one. You and ", companion[0]," die together.")
            if game_status['met_dido'] > 1:
                game_status['life'] = 'dido_fail'
                return
        elif sacrifice in ['flask','use flask']:
            if game_status['flask'] == 0:
                print("You have no flasks to use.")
            else:
                use_flask()
                return
        elif sacrifice in ['inventory','status','info','info']:
            get_info()
        elif sacrifice == 'help':
            get_help()
        else :
            print("Please try again.")
    print("")
    if game_status['companion'] != []:
        if 'The Hoplite' in game_status['companion']:
            print("As you leave The Hoplite gives you a sideways glance. He looks disappointed in you.")
        elif 'The Physician' in game_status['companion']:
            print("As you leave The Physician gives you a knowing smile. It seems highly inappropriate, and you scowl back.")
            print("")
            print("PHYSICIAN: Don't look at me like that. You're the one who left them behind, not me.")
            print("")
            print("Perhaps he has a point.")
        elif 'The Scholar' in game_status['companion']:
            print("The Scholar mutters a prayer as you take your leave. You are not sure to whom she is praying. Perhaps it is better not to ask.")
        elif 'The Girl' in game_status['companion']:
            print('The Girl watches you with wide eyes as you leave the chamber.')
            print("")
            print("GIRL: What about--")
            print("YOU: -- They'll catch up later. They'll be fine.")
            print("")
            print("She doesn't seem to believe you. But, when faced with following you or going on her own again, she warily begins to follow.")
    return
def use_flask():
    print("You take a drink of your flask.")
    flask_status = len(game_status['companion'])
    if flask_status == 0:
        print("Suddenly, you find yourself revitalized!")
    elif flask_status == 1:
        print("Suddenly, you find yourself and ", *game_status['companion']," revitalized!")
    elif flask_status > 1:
        print("Suddenly, you find yourself and your companions revitalized!")
    game_status['flask'] -= 1
    new_flask_status = game_status['flask']
    if new_flask_status == 0:
        print("But that was your last flask...")
    else :
        print("You have ",game_status['flask']," left.")
        print("Better be careful from now on.")
    print("Careful to not alert the enemy again, you quietly move toward the end of the chamber.")
    cont()
    if 'The Physician' in game_status['companion']:
        print("As you reach the end, you notice The Physician is not with you.")
        print("You look back and find him back where he fell, sitting and staring, as if possessed.")
        print("You call out to him as quiet as you can. After a few tries, you finally grab his attention and he crawls over to join you. In the low light, you can see he is smiling.")
        print(" ")
        print("YOU: Are you alright?")
        print("PHYSICIAN: Hm? Oh, yes, yes. Fine. I've just a wonderful idea, that's all. Bit of inspiration! Haha.")
        print(" ")
        print("You eye him warily, but say no more.")
        game_status['physician_quest'] = True
        cont()
    return     
def injured():
    print("")
    print("It was a very close call.")
    print("Now, as your sweat cools and your breathing slows, you realize you are INJURED.")
    if 'The Physician' in game_status['companion']:
        print("Thankfully, The Physician is here to help you.")
        print("You are HEALED.")
        print(" ")
    elif 'Chimera Blood' in game_status['character_status']:
        print("But... what's this?")
        print("Your wounds are closing all on their own! How miraculous!")
        print("You are HEALED.")
        print("")
    else:
        game_status['base_AP'] -= 5
        game_status['base_SP'] -= 5
        if 'injured' in game_status['character_status']:
            game_status['character_status'].remove('injured')
            game_status['character_status'].append('heavily injured')
            print("(Baseline AP and SP further reduced by 5.)")
        if 'heavily injured' in game_status['character_status']:
            print("(Baseline AP and SP further reduced by 5.)")
        else: 
            game_status['character_status'].append('injured')
            print("(Baseline AP and SP reduced by 5.)")
    status = game_status['character_status']
    if game_status['chamber'] in ['dogs','rats','blemyae','baboons','cerberus'] and 'injured' in status:
        chance = random.randint(0,1)
        if chance == 1:
            cont()
            print("You closely inspect the wound. It looks particularly gruesome, and smells foul. You swear you see something black and wriggling just beneath the blood, but you blink and it is gone.")
            print("You have been POISONED!")
            print("")
            if 'Basilisk Fang' in game_status['items']:
                print("Wait...")
                print("The poison is disappearing!")
                print("It seems that being in proximity to the Basilisk Fang makes poison ineffective.")
                print("You are HEALED.")
                print("")
            else:
                game_status['character_status'].append('poisoned')
                print("If you do not cure the poison or reach the temple of Ba'al Hammon within 5 turns, the poison will kill you.")
    cont()
    return
def game_reset():
    #character info
    game_status['weapon'] = 'no weapon'
    game_status['original_weapon'] = 0
    game_status['torch'] = True
    game_status['flask'] = 1
    game_status['items'] = ['gold coins']
    game_status['base_AP'] = 5
    game_status['base_SP'] = 5
    game_status['bonus_AP'] = 0
    game_status['bonus_SP'] = 0
    if game_status['elephant'] == False:
        game_status['sacrifice'] = -10
    #statuses
    game_status['character_status'] = []
    game_status['poison_count'] = 5
    game_status['courage_buff'] = False
    #score info
    game_status['kill_count'] = 0
    game_status['legendary_kill_count'] = 0
    game_status['flee_count'] = 0
    game_status['chamber_count'] = 0
    #companion mechanics
    game_status['dog'] = False
    game_status['dog_name'] = 0
    game_status['lower_dog_name'] = 0
    game_status['companion'] = []
    game_status['companion_entry'] = []
    game_status['met_fisherman'] = False
    game_status['met_hoplite'] = False
    game_status['met_physician'] = False
    game_status['met_scholar'] = False
    game_status['met_merchant'] = False
    game_status['met_girl'] = False
    game_status['girl_reduction'] = []
    #god mechanics
    game_status['dido_trigger'] = False
    game_status['met_dido_ingame'] = False
    game_status['met_musician_carthage'] = False
    game_status['entered_musician_chamber'] = 0
    game_status['musician_done'] = True
    game_status['moloch_explanation'] = False
    game_status['musician_hint'] = False
    game_status['minotaur_boost'] = False
    #game mechanic counters
    game_status['status'] = True
    game_status['life'] = 'alive'
    game_status['warning'] = 1
    game_status['how_to'] = 1
    game_status['intro'] = 0
    game_status['location'] = 'home'
    game_status['path'] = 0
    game_status['chamber'] = 0
    game_status['left_count'] = 0
    game_status['right_count'] = 0
    game_status['level'] = 1
    game_status['lost_adventurer'] = 0
    game_status['met_cave_merchant'] = 0
    game_status['moloch_shrine'] = 0
    game_status['tanit_shrine'] = 0
    #quest counters
    game_status['god_killer'] = False
    game_status['fisherman_quest'] = False
    game_status['scholar_quest'] = False
    game_status['mother_quest'] = False
    game_status['ghost_quest'] = False
    game_status['hoplite_quest'] = False
    game_status['collector_quest'] = False
    game_status['collector_version'] = []
    game_status['versus_collector'] = 0
    game_status['physician_quest'] = False
    game_status['chimera_quest'] = False
    game_status['cave_merchant_wares'] = ['1 flask','poor sword','new torch','dog eyes']
    game_status['city_merchant_wares'] =  ['1 flask','poor sword','new torch','dog eyes']
    game_status['cerberus_lives'] = True
    game_status['basilisk_lives'] = True
    game_status['mother_lives'] = True
    game_status['chimera_lives'] = False
    game_status['minotaur_lives'] = True
    game_status['spider_count'] = 0
    #enemy counters
    game_status['spider_room_count'] = 0
    game_status['mother'] = [30,20]
    game_status['mother_count'] = 0
    game_status['blemyae'] = [10,15]
    game_status['shadows'] = [25,25]
    game_status['blemyae_room_count'] = 0
    game_status['blemyae_count'] = 0
    game_status['rat_count'] = 0
    game_status['dog_count'] = 0
    game_status['baboon_count'] = 0
    game_status['shadow_count'] = 0
    game_status['halfform_count'] = 0
    game_status['cerberus_count'] = 0
    game_status['basilisk_count'] = 0
    game_status['minotaur_count'] = 0
    game_status['flower_count'] = 0
    return

#quests, special events, and special rooms
def run_tanit_shrine():
    print("   / /\ ")
    time.sleep(0.1)
    print("  / /  \ ")
    time.sleep(0.1)
    print("  \_\__/   ____ ")
    time.sleep(0.1)
    print("      \\  /   / ")
    time.sleep(0.1)
    print("____   \\/___/ ")
    time.sleep(0.1)
    print("\   \ -// ")
    time.sleep(0.1)
    print(" \___\//- ")
    time.sleep(0.1)
    print("    -// ")
    time.sleep(0.1)
    print("     \\ ")
    time.sleep(0.1)
    print("     // ")
    time.sleep(0.3)
    print(" ")
    print("You found a SHRINE dedicated to the goddess TANIT!")
    print("")
    print("Bathed in an ethereal glow, it is adorned with vibrant red flowers and lush greenery, creating a breathtaking sanctuary in the heart of darkness.")
    print('The air is warm and smells sweet, like the seaside on a warm summers day.')
    print("You feel yourself revitalized.")
    print("")
    if game_status['character_status'] == 'injured':
        print("Your injury is healed! A miracle!")
        game_status['character_status'].remove('injured')
        print("")
    if game_status['character_status'] == 'poisoned':
        print("Unfortunately, the shrine cannot heal your poison.")
        print("")
    else :
        print("On the dais you spy a small, glimmering item... it is a flask!")
        print("Tanit must be smiling on you. She surely meant for you to take it.")
        print("")
        print("(You are granted 1 flask.)")
        print(" ")
        game_status['flask'] += 1
    cont()
    if game_status['met_tanit'] == False:
        if game_status['kill_count'] == 0:
            game_status['met_tanit'] = True
            print("As you turn to leave, a small orange cat suddenly jumps up onto the dais.")
            print("It is surprising-- The cat does not look demonic or abnormal in anyway. Just as you begin to wonder how it could have gotten here, the cat begins to speak.")
            print(" ")
            print("CAT: Do not be frightened, mortal. It is I, the Goddess Tanit.")
            print("")
            print("You jump back and get to your knees. To think, the Goddess would speak to you directly!")
            if 'The Hoplite' in game_status['companion']:
                print("The Hoplite follows your lead, though he does not seem to understand why.")
            if 'The Physician' in game_status['companion'] and 'The Scholar' in game_status['companion']:
                print("Neither the Physician nor the Scholar get to their knees. You hear them tittering conspiratorily behind you, no doubt laughing at your strange behavior, but you pay them no mind.")
            if 'The Physician' in game_status['companion'] and 'The Scholar' not in game_status['companion']:
                print("The Physician looks at you as if you've lost your mind.")
                print("Paying him no mind, you focus your attention on the goddess in front of you.")
            if 'The Physician' not in game_status['companion'] and 'The Scholar' in game_status['companion']:
                print("The Scholar looks at you as if you've lost your mind.")
                print("Paying her no mind, you focus your attention on the goddess in front of you.")
            print(" ")
            print("TANIT: You are not the first to make it this far. Many have done so before you. However, you are the first in a long time to do so without the taint of violence...")
            print(" ")
            cont()
            print("You are surprised. Indeed, you have not killed even a stray spider since your journey began, but how does she know this?")
            print(" ")
            print("TANIT: Though the journey may be hard, I pray you maintain your peaceful disposition. Do so, and perhaps I may be able to find a place for you among my retinue.")
            print(" ")
            print("Moved beyond words, you drop your head in a deep bow.")
            print("Member of a godly retinue... it is a tempting offer.")
            print("But is it possible to survive the caverns without enacting violence even once? ")
            print("Raising your gaze, you find the cat is now just a cat. The room just a room. The presence of the Goddess has left.")
            print(" ") 
        else :
            if game_status['tanit_shrine'] == 0:
                print("As you turn to go, you spy an odd sight-- a small orange cat, lounging in the corner.")
                if game_status['dog'] == True:
                    print(game_status['dog_name']," barks playfully at it, but the cat seems neither afraid nor interested.")
                print("It does not look demonic or abnormal in anyway. Just a cat.")
                if 'The Girl' in game_status['companion']:
                    print("The Girl runs up to it excitedly. You are pleased to see it tolerates her rough petting. It seems to have brightened her mood.")
                else:
                    print("You pet the cat lightly, before continuing onward.")
            else: 
                print("As you turn to go, you spy an odd sight-- a small orange cat, lounging in the corner.")
                if game_status['dog'] == True:
                    print(game_status['dog_name']," barks playfully at it, but the cat seems neither afraid nor interested.")
                print("Is it the same cat as before? How did it get here?")
                if 'The Girl' in game_status['companion']:
                    print("The Girl runs up to it excitedly. You are pleased to see it tolerates her rough petting. It seems to have brightened her mood.")
                else:
                    print("You pet the cat lightly, before continuing onward.")
    #runs if player has never met Goddess Tanit in ANY game
    else:
        if game_status['kill_count'] > 0:
            if game_status['tanit_shrine'] == 0:
                print("As you turn to leave, a small orange cat suddenly jumps up onto the dais.")
                print("")
                print("TANIT: Fear not, mortal! It is I, the goddess Tanit!")
                print(" ")
                print("You jump back and get to your knees. To think, the Goddess would speak to you directly!")
                if 'The Hoplite' in game_status['companion']:
                    print("The Hoplite follows your lead, though he does not seem to understand why.")
                if 'The Physician' in game_status['companion'] and 'The Scholar' in game_status['companion']:
                    print("Neither the Physician nor the Scholar get to their knees. You hear them tittering conspiratorily behind you, no doubt laughing at your strange behavior, but you pay them no mind.")
                if 'The Physician' in game_status['companion'] and 'The Scholar' not in game_status['companion']:
                    print("The Physician looks at you as if you've lost your mind.")
                    print("Paying him no mind, you focus your attention on the goddess in front of you.")
                if 'The Physician' not in game_status['companion'] and 'The Scholar' in game_status['companion']:
                    print("The Scholar looks at you as if you've lost your mind.")
                    print("Paying her no mind, you focus your attention on the goddess in front of you.")
                print("")
                print("TANIT: Ah, my dear child. Still struggling against the dark, I see.")
                print("YOU: You remember me?")
                print("TANIT: Of course. I remember all my children.")
                print(" ")
                print("The goddess seems to faulter then. Her ethereal expression darkens into something terrible.")
                print("")
                print("TANIT: The smell of blood... you have defiled yourself.")
                print("")
                print("You hang your head in shame.")
                print("")
                print("TANIT: I had hoped that perhaps you would maintain your compassion. But you mortals are so fragile... so afraid.")
                print("")
                print("With that, the cat jumps from the dais and slinks off out of the chamber.")
                print("It seems you have upset her.")
            else: 
                print("You look about the chamber hoping to spot the orange cat from before, but it is no where to be found.")
                print("Perhaps you upset her?")
        else:
            if game_status['tanit_shrine'] == 0:
                print("As you turn to leave, a small orange cat suddenly jumps up onto the dais.")
                print("")
                print("TANIT: Fear not, mortal! It is I, the goddess Tanit!")
                print(" ")
                print("You jump back and get to your knees. To think, the Goddess would speak to you directly!")
                print("You jump back and get to your knees. To think, the Goddess would speak to you directly!")
                if 'The Hoplite' in game_status['companion']:
                    print("The Hoplite follows your lead, though he does not seem to understand why.")
                if 'The Physician' in game_status['companion'] and 'The Scholar' in game_status['companion']:
                    print("Neither the Physician nor the Scholar get to their knees. You hear them tittering conspiratorily behind you, no doubt laughing at your strange behavior, but you pay them no mind.")
                if 'The Physician' in game_status['companion'] and 'The Scholar' not in game_status['companion']:
                    print("The Physician looks at you as if you've lost your mind.")
                    print("Paying him no mind, you focus your attention on the goddess in front of you.")
                if 'The Physician' not in game_status['companion'] and 'The Scholar' in game_status['companion']:
                    print("The Scholar looks at you as if you've lost your mind.")
                    print("Paying her no mind, you focus your attention on the goddess in front of you.")
                print(" ")
                print("TANIT: Ah, my dear child. Still struggling against the dark, I see.")
                print("")
                print("You are taken aback.")
                print("")
                print("YOU: You remember me?")
                print("TANIT: Of course. I remember all my children. Though the journey may be hard, I pray you maintain your peaceful disposition. Do so, and perhaps I may be able to find a place for you among my retinue.")
                print(" ")
                print("Moved beyond words, you drop your head in a deep bow.")
                print("Member of a godly retinue... it is a tempting offer.")
                print("But is it possible to survive the caverns without enacting violence even once? ")
                print("Raising your gaze, you find the cat is now just a cat. The room just a room. The presence of the Goddess has left.")
                print(" ") 
            else:
                print("Your eyes rove the chamber for a sign of the cat, but you do not see it.")
                if 'The Girl' in game_status['companion']:
                    print("The Girl suddenly exclaims excitedly. It seems she has found something!")
                elif 'The Scholar' in game_status['companion']:
                    print("The Scholar then calls your attention. It seems she has found something!")
                else:
                    print("Ah, but what is that there!")
                print(" ")
                print("It is yet another flask! It seems the goddess is truly smiling down on you.")
                print("(You are granted 1 flask.)")
                print(" ")
                game_status['flask'] += 1
                print(" ")
    print("")
    game_status['tanit_shrine'] += 1
    cont()
    return
def run_dido_shrine():
    print(" ")
    print("    (")
    time.sleep(0.1)
    print("     )")
    time.sleep(0.1)
    print("    ()")
    time.sleep(0.1)
    print("   |--|")
    time.sleep(0.1)
    print("   |  |")
    time.sleep(0.1)
    print(" .-|  |-.")
    time.sleep(0.1)
    print(":  |  |  :")
    time.sleep(0.1)
    print(":  '--'  :")
    time.sleep(0.1)
    print(" '-....-' ")
    time.sleep(0.3)
    print(" ")
    print("You found a SHRINE dedicated to the demi-goddess DIDO!")
    print("")
    print("An eternal flame dances at its center, casting flickering light on the ancient battle carvings adorning the walls, a testament to forgotten wars and tales.")
    if 'The Hoplite' in game_status['companion']:
        print("The Hoplite goes down to a knees before the shrine, his hands raised in supplication.")
        if 'The Physician' in game_status['companion']:
            print("Sneering at his efforts, The Physician looks to you, but you say nothing. You may not be as devout as The Hoplite, but Dido is still your Queen, even in death.")
    print("")
    if game_status['torch'] == False:
        print("Your TORCH is RELIT by the eternal flame of Dido!!")
        game_status['torch'] = True
    if 'poisoned' in game_status['character_status']:
        print("")
        print("Relief floods over you as the shrine heals you, curing your body of the poison's grip!!!!")
        print("You are HEALED of your poison!")
        game_status['character_status'].remove("poisoned")
    print(" ")
    cont()
    if game_status['dido_trigger'] == True:
        print("Suddenly, your torch begins to flicker, the flames rising high up to the ceiling of the small chamber.")
        print("The image of the demi-goddess Dido materializes within the fiery embrace of the torch, her ethereal form radiating divine grace and mystique. She appears upset with you, her delicate face twisted in anger.")
        print("")
        if game_status['met_dido'] == False: 
            game_status['met_dido'] = True
            game_status['met_dido_ingame'] = True
            print("DIDO: Filthy coward! You dare to come to my shrine after what you have done?")
            print("YOU: What I have done...? ")
            print("DIDO: Sacrificing your companions to save yourself? Pathetic!")
            print("")
            print("You are overcome with shame. Still, you refuse to let guilt take hold.")
            print("")
            print("YOU: If I did not, I would be dead.")
            print("DIDO: Oh! And are you truly so important?")
            print("YOU: I am no more important than those who have fallen, but my mission stands alone. I must reach Ba'al Hammon. I must save Carthage.")
            print(" ")
            print("She seems to contemplate this. Her image flickers in the fire, before she finally barks out a harsh laugh.")
            print(" ")
            print("DIDO: If you truly wish to save Carthage, maybe you should sacrifice YOURSELF to Ba'al Hammon! It's what a true hero would do.")
            print("")
            print("With that the flames seem to flicker, and her image is gone.")
            dido_dialog()
        else: 
            if game_status['met_dido_ingame'] == False:
                game_status['met_dido_ingame'] = True
                print("DIDO: You never learn, do you! At this rate half of Carthage will be dead before you're even granted an audience!")
                print("YOU: Half of Carthage IS dead...")
                print(" ")
                print("She seems to contemplate this. Her image flickers in the fire, before she finally barks out a harsh laugh.")
                print("")
                print("DIDO: If you truly wish to save Carthage, maybe you should sacrifice YOURSELF to Ba'al Hammon! It's what a true hero would do.")
                print("")
                print("With that the flames seem to flicker, and her image is gone.")
                dido_dialog()
            else:    
                print("You peer into the flames, wondering if perhaps the spirit of Dido will make herself known to you.")
                print("She does not. It seems you have upset her.")
                print(" ")
    else:
        if game_status['met_dido'] == False:
            print("You warm your hands by the fire for a few moments, before taking your leave.")
        else:
            if game_status['met_dido_ingame'] == False:
                game_status['met_dido_ingame'] = True
                print("Suddenly, your torch begins to flicker, the flames rising high up to the ceiling of the small chamber.")
                print("The image of the demi-goddess Dido materializes within the fiery embrace of the torch, her ethereal form radiating divine grace and mystique. She appears upset with you, her delicate face twisted in anger.")
                print("")
                print("DIDO: Ah, the coward returns! But what is this...? Your hands... this time, they are free from innocent blood.")
                print("YOU: This time? You remember me?")
                print("DIDO: I remember all my subjects, regardless of whatever unfortunate time they may find themselves mired in.")
                print("")
                print("You are surprised, but say nothing. Perhaps it would offend the demi-goddess, were you to ask too many questions.")
                print("Her expression towards you softens.") 
                print("")
                print("DIDO: I hope you will continue on this path-- a true hero would sacrifice THEMSELVES to save Carthage, not others. When it is time for you to meet Baal Hammon, I hope you remember that.") 
                print("")
                print("With that, her image is extinguished from the flames.")
                print("For some reason, you feel stronger than before!")
                print("Dido's Blessing gives you +7 AP and +7 SP.")
                game_status['character_status'].append('Didos Blessing')
                game_status['base_AP'] += 7
                game_status['base_SP'] += 7
                dido_dialog()
            else: 
                print("You peer into the flame and think you can just barely make out the image of the demi-goddess.")
                if 'The Hoplite' in game_status['companion']:
                    print("The Hoplite claps you on the shoulder.")
                    print(" ")
                    print("HOPLITE: Do not worry, my friend. Our Queen is always watching her people.")
                else:
                    print("You think she may be watching you, but you are not sure.")
    cont()
    return
def dido_dialog():
    cont()
    if 'The Physician' in game_status['companion']:
            print("The Physician looks at you, curiously.")
            print(" ")
            print("PHYISICIAN: Feeling alright?")
            print(" ")
    elif 'The Girl' in game_status['companion'] and 'The Physician' not in game_status['companion']:
        print("The Girl is watching you. You realize must look mad, speaking to your own torch like that!")
    else:
        print("You realize must look mad, speaking to your own torch like that!")
    if 'The Hoplite' in game_status['companion']:
        print("You glance towards the Hoplite to see if he has noticed. He has, but he does not seem bothered by it.")
        if 'The Scholar' or 'The Physician' in game_status['companion']:
            print("He leans in to whisper, so your other companions cannot hear.")
            print(" ")
        else:
            print(" ")
        print("HOPLITE: Is this the first time you have seen her?")
        print("YOU: Yes... Have you...?")
        print("HOPLITE: Ah, once. Only once.")
        print(" ")
    if 'The Scholar' in game_status['companion']:
        print("As you near the door, The Scholar approaches you, speaking under her breath.")
        print(" ")
        print("SCHOLAR: What did you see?")
        print("YOU: Nothing. I am only tired.")
        print(" ")
        print("She does not seem to believe you, but thankfully falls silent.")
    return
def run_moloch_shrine():
    print("._____. ._____.")
    time.sleep(0.1)
    print("| ._. | | ._. |")
    time.sleep(0.1)
    print("| !_| |_|_|_! |")
    time.sleep(0.1)
    print("!___| |_______!")
    time.sleep(0.1)
    print(".___|_|_| |___.")
    time.sleep(0.1)
    print("| ._____| |_. |")
    time.sleep(0.1)
    print("| !_! | | !_! |")
    time.sleep(0.1)
    print("!_____! !_____!")
    time.sleep(0.3)
    print(" ")
    if game_status['moloch_explanation'] == False:
        print("You have found a SHRINE, of some sort....")
    else:
        print("You have found a SHRINE to MOLOCH!")
    print("")
    print("The room is centered around a small, pedestal platform. You cautiously approach the eerie structure, its surroundings adorned with withered plants. Around you, the walls ripple like water, undulating with an otherworldly energy, leaving you captivated by the mysterious presence that permeates the space.")
    print("You hear the strumming of a kithara, soft and echoic, as if played from a great distance.")
    if 'The Scholar' in game_status['companion'] and game_status['moloch_explanation'] == False:
        print("The Scholar approaches the shrine, closely inspecting markings along the base of the pedestal before crying uot in excitement.")
        print(" ")
        print("SCHOLAR: This is a shrine to Moloch!")
        print("YOU: Moloch?")
        print("SCHOLAR: The god of child sacrifice! Or, well, so it is said-- to my knowledge, no one in Alexandria has reported finding a full shrine intact!")
        print(" ")
        print("She sounds thrilled by the discovery. Your mind, however, is stuck on 'child sacrifice' and the stomach-churning stain on the top of the pedestal...")
        if 'The Girl' in game_status['companion']:
            print("The Girl curls a hand into your robes. You pat her head reassuringly.")
    if game_status['moloch_explanation'] == True:
        print("You pass through the shrine as quickly as possible, looking anywhere but at the sacrificial pedestal. This place gives you the creeps.")
    movement = random.randint(1,8)
    print("As you move toward the exit of the chamber, a strange sensation overcomes you.")
    if 'The Scholar' in game_status['companion'] and game_status['moloch_explanation'] == False:
        game_status['moloch_explanation'] = True
        print("")
        print("YOU: Do those markings say anything about why this chamber is so--")
        print("SCHOLAR: --Strange? No. Though I have heard of some texts that characterize Moloch more as a god of time than sacrifice... perhaps... hm...")
    if 'The Hoplite' in game_status['companion']:
        print(" ")
        print("HOPLITE: Carthaginians meet the unknown with courage! Isnt that right, my friend?")
        print("")
        print("With that, The Hoplite sprints forward. His form seems to shift and twist, as if seen through running water.")
    print(" ")
    print("Time and space shifts, and you are transported to Level ",movement,".")
    game_status['level'] = movement
    cont()
    return
def run_girl():
    game_status['met_girl'] = True
    print("")
    print("This chamber thankfully appears to be empty.")
    print("Cautious, you cross the chamber towards the otherside. However, as you are halfway there, you notice something skulking in the shadows.")
    print('You can just see it in the corner, curled up and facing the wall. It is impossible to tell what it is.')
    if game_status['weapon'] == 'no weapon':
        print('Steeling yourself, you begin to approach.')
    else: 
        ("Your weapon in hand, you begin to approach.")
    print("As you get closer, the shadows give way and you are able to make out the figure. It appears to be human!")
    print(" ")
    print("YOU: Hello?")
    print(" ")
    print("The figure whips around, scurrying back further into the darkness.")
    cont()
    print("It looks like a girl. She looks young and terribly frightened. Her wrists and ankles are scabbed and bleeding-- an odd wound.")
    print(" ")
    print("YOU: Are you okay?")
    print(" ")
    print("The girl practically jumps out of her skin.")
    if game_status['dog'] == True:
        print("You seek to calm the young girl, but before you can, ", game_status['dog_name'],"runs up to greet her. As he licks at her face excitedly, the Girl seems to relax. After a few moments of deliberation, she speaks.")
    else:
        if game_status['weapon'] != 'no weapon':
            print("You lower your weapon, doing your best to look non-threatening.")
        else:
            print('You do your best to look non-threatening.')
        print('The girls looks uncertain, but after a few moments of deliberation, decides to trust you. She speaks.')
    print(" ")
    print("GIRL: After we ran away, I got lost...")
    print("YOU: You ran away? From what?")
    print("GIRL: The fisherman... My father had sent my sisters and I on his boat to go to Sicily, but when we got onto the ocean he said we needed to pay more.")
    print("GIRL: We didn't have any money, so he brought us here instead. He told us not to try to escape or the cave beasts would kill us.")
    print("GIRL: We didn't believe him and tried to run away and then... my sisters...")
    print(" ")
    print("She then begins to cry.")
    if 'The Physician' in game_status['companion'] and 'The Hoplite' not in game_status['companion']:
        print("The Physician turns to you, whispering beneath his breath.")
        print(" ")
        print("PHYSICIAN: I do not hope to sound cold, but please be rational about this. We are barely making it through as it is-- to try and drag along a young child would be madness!")
    if 'The Physician' not in game_status['companion'] and 'The Hoplite' in game_status['companion']:
        print("The Hoplite turns to you, whispering beneath his breath.")
        print(" ")
        print("HOPLITE: We must take her with us, my friend! If we leave her here, she is sure to die!")
    if 'The Physician' in game_status['companion'] and 'The Hoplite' in game_status['companion']:
        print("The Hoplite turns to you, whispering beneath his breath.")
        print(" ")
        print("HOPLITE: We must take her with us, my friend! If we leave her here, she is sure to die!")
        print(" ")
        print("The Physician scoffs derisively. The Hoplite turns to him with a deep set scowl.")
        print(" ")
        print("HOPLITE: It is the right thing to do!")
        print("PHYSICIAN: But is it the smart thing to do? After all, what happens if she falls behind?")
        print("HOPLITE: Then we will help her to keep up!")
        print("PHYSICIAN: YOU might, but I certainly don't intend to!")
        print(" ")
    if 'The Physician' not in game_status['companion'] and 'The Hoplite' not in game_status['companion'] and 'The Scholar' in game_status['companion']:
        print("You turn to The Scholar for guidance. You hoped as a woman she might know better what to do with a child, but she seems just as lost as you are. She shrugs.")
    print("You are not sure what to do. You could take her with you, but with her injuries she would undoubtedly be a hinderance.")
    print("But if you leave her to her fate, she will surely perish.")
    print(" ")
    print("==========================================")
    print("Will you let her join you?")
    while True:
        answer = input("")
        print("==========================================")
        print(" ")
        if answer.lower() in ['yes','y']:
            game_status['companion'].append('The Girl')
            print(" ")
            print("YOU: Would you like to come with me? I can help protect you.")
            print(" ")
            print("She hesitates for a moment, big brown eyes searching your face desperately for any sign of trickery.")
            print("Finding none, she wipes her tears, stands up, and joins you.")
            print(" ")
            if 'The Physician' in game_status['companion']:
                print("The Physician gives a frustrated sigh, before setting to work doing his best to cure her injuries.")
                print(" ")
                print("COMPANION ADDED: The Girl")
                print("(The Girl provides no AP or SP bonus)")
                game_status['girl_reduction'] = [0,0]
            else:
                print("COMPANION ADDED: The Girl")
                print("(The Girl causes -5 AP, -5 SP reduction)")
                game_status['girl_reduction'] = [-5,-5]
            cont()
            break
        elif answer.lower() in ['no','n']:
            print(" ")
            print("You wish to help, but she would be too much of a hinderance. Carthage is counting on you. You cannot risk thousands of lives just to save one.")
            print("Without a word, you get up and move toward the door.")
            print("The girl makes no attempt to follow, save a single cry in the darkness.")
            print(" ")
            print("GIRL: Please don't leave me... it's so dark in here...")
            print(" ")
            if game_status['dog'] == True:
                print(game_status['dog_name'],"seems hesitant to leave her behind. You grab him by the scruff of his neck, and force him away.")
            else:
                print("You pretend you cannot hear her and continue on your way.")
            cont()
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else :
            print("Please try again.")
    return
def run_scholar():
    game_status['scholar_quest'] = False
    print("")
    print("As you step into the dark cave, a harrowing sight unfolds. A young woman fights off a swarm of relentless rats. Without hesitation, you rush to her aid, joining the intense struggle against the frenzied creatures.")
    print("You make quick work of the rats. Once they are disposed of, the young girl turns to you, bowing deeply. You notice she is dressed in the garb of a scholar.")
    print("")
    print("SCHOLAR: Thank you for your aid! I thought I would not make it.")
    print("YOU: It is no trouble...")
    print("")
    if 'The Girl' in game_status['companion']:
        print("Before you can stop her, The Girl has wandered up to the woman. She stares up open mouthed.")
        print("")
        print("GIRL: You're pretty...")
        if 'The Physician' in game_status['companion']:
            print(" ")
            print("The Physician scoffs.")
            print(" ")
            print("PHYSICIAN: In a provincial sort of way, perhaps...")
        print(" ")
        print("The woman seems a little offended.")
    else:
        print("You hesitate to ask. It would be rude. But...")
        print("Thankfully, The Scholar guesses your question before it must be voiced.")
    print("")
    print("SCHOLAR: I know I do not look the part of a warrior. You probably think me foolish to have ventured this far, but...")
    print("YOU: But...?")
    print("SCHOLAR: I have come from Alexandria. When word of the Roman invasion reached our ears, we feared the secrets of the Temple of Baal Hammon may be lost to time... I am here to try and recover what I can before... well... before...")
    print("")
    print("She does not finish her thought. You both know what threat awaits the city of Carthage.")
    print("She hesitates, biting her thumb and avoiding your gaze, before quietly putting forth the question.")
    print("")
    print("SCHOLAR: Perhaps we  could... travel together? I could be of use. I have a map of the caverns which may aid in your journey, though it seems to be somewhat inaccurate... ")
    print(" ")
    print("==========================================")
    print("Will you let her join you?")
    while True:
        answer = input("")
        print("==========================================")
        print(" ")
        if answer.lower() in ['yes','y']:
            game_status['companion'].append('The Scholar')
            print(" ")
            print("YOU: I would welcome your company.")
            print("SCHOLAR: Brilliant! Then please, lead the way.")
            print(" ")
            print("With that, you set off together into the caverns.")
            print(" ")
            print("COMPANION ADDED: The Scholar")
            print("(Scholar provides +5 AP, +5 SP and increases the chance of downward passages appearing.)")
            cont()
            break
        elif answer.lower() in ['no','n']:
            print(" ")
            print("YOU: I am sorry, but I cannot take you with me.")
            print("SCHOLAR: I understand...")
            print("")
            print("She seems disheartened, but makes no attempt to follow you.")
            cont()
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else :
            print("Please try again.")
    return
def run_ghost():
    game_status['ghost_quest'] = False
    print(" ")
    print("Entering into the next chamber, you are struck by a sudden sense of deja vu.")
    print('This cave system must have many rooms that look similar, you think. You are merely confused.')
    if game_status['dog'] == True:
        print(game_status['dog_name'],"begins barking wildly, almost in a frenzy. You try to calm him, but he will not be calmed, his barking growing higher pitched and desperate.")
    else:
        print("You feel your skin start to prickle on the back of your neck.")
    print(" ")
    if 'The Hoplite' in game_status['companion']:
        print("The Hoplite points to the far end of the chamber.")
        print(" ")
        print("HOPLITE: Look there! Is that...?")
    elif 'The Physician' in game_status['companion']:
        print("The Hoplite points to the far end of the chamber.")
        print(" ")
        print("HOPLITE: Look there! Is that...?")
    elif 'The Scholar' in game_status['companion']:
        print("The Scholar steps closer to you, her eyes wide.")
    else:
        print("Without knowing why, your eyes drift to a dark corner of the chamber.")
        print("Is that...?")
    cont()
    print("It looks like The Girl!")
    print(" ")
    if 'The Physician' in game_status['companion']:
        print("PHYSICIAN: How can that be? She is dead!")
    elif 'The Hoplite' in game_status['companion']:
        print("HOPLITE: How can that be? She is dead!")
    else:
        print("How can that be? She is dead! You are certain of it!")
    print('You realize she is staring at you. Her face looks drawn, her gaze intense.')
    print(" ")
    print("GIRL: You lied to me...")
    print("")
    print("You stumble backwards as her figure rises up as if floating.")
    print('You realize in horror that her feet do not touch the ground. A ghost?')
    print(" ")
    print("GIRL: You said you would protect me...")
    print(" ")
    print("She is coming for you. What do you do? You cannot hope to fight a ghost!")
    print("")
    cont()
    if 'bloody doll' in game_status['items']:
        print("In the blink of an eye, she suddenly appears in front of you as if teleported across the room.")
        print("You can see the hatred in her eyes. And, even now, you can see the fear...")
        print("Her ghostly hand reaches out towards you.")
        if game_status['weapon'] != 'no weapon':
            print("You strike out at her with your weapon, but it is no good... it just goes straight through her.")
        print("Then, suddenly, she stops.")
        print(" ")
        print("GIRL: Why do you have that...?")
        print(" ")
        print("You dont know what she's talking about, but you follow her gaze towards your satchel.")
        print('Reaching in, you dig around the contents until you see... Oh, yes.')
        print('The bloody doll.')
        cont()
        print('You remove the doll from your bag. Her gaze follows, white eyes wide.')
        print(" ")
        print("GIRL: Anna... That was Anna's.")
        print("YOU: I did not steal it, I--")
        print(" ")
        print('You try to explain, but she does not appear to be listening.')
        print('Instead, she just puts her little hands out.')
        print("You hand over the doll. Her hands close around it as if corporeal once more.")
        print("She strokes its hair. She either cannot see or does not mind the blood.")
        print("She takes one last look at you, then floats off into the darkness.")
        print(" ")
        print("You are safe.")
        cont()
        print("")
        print("Just as you are about to leave the chamber, you notice something glinting in the corner.")
        print("You approach and find a long chain coiled where the ghost of the girl once sat.")
        print(" ")
        print("MAIDEN'S CHAIN")
        print("A ghostly chain made of some sort of composite ectoplasmic steel")
        print("+10 AP, +25 SP")
        print("Bonus against unearthly beings")
        print("")
        print("==========================================")
        print("Would you like to replace your current weapon with Maidens Chain?")
        while True:
            answer = input(" ")
            print("==========================================")
            print(" ")
            if answer.lower() in ['yes','y','replace','replace weapon','take chain','trade','trade weapon','take the chain','take the maidens chain',"take the maiden's chain","take maiden's chain",'take maidens chain']:
                print("You trade your weapon for the Maidens Chain.")
                print(" ")
                get_total_AP_SP()
                print("--PREVIOUS STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                game_status['weapon'] = 'Maidens Chain'
                get_total_AP_SP()
                print("")
                print("--CURRENT STATS--")
                print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                cont()
                break
            elif answer.lower() in ['no','n','keep weapon',"don't trade","don't trade weapons",'dont trade',"don't trade weapons"]:
                print("You leave the chain behind.")
                print("")
                cont()
                break
            elif answer.lower() in ['inventory','status','info','info']:
                get_info()
            elif answer.lower() == 'help':
                get_help()
            else :
                print("Please try again.")
    else:
        battle()
    return
def run_hoplite():
    print("As you're walking with The Hoplite, you are suddenly struck on the back of the head!")
    print("You black out.")
    print(" ")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print("ZzZz")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print(" ")
    print("You wake up and are shocked to find The Hoplite is gone.")
    print("Not only that, but he's taken your weapon!")
    print(" ")
    print("Betrayed by that wolf in sheep's clothing! He did seem oddly chipper... perhaps he had been planning this betrayal since the moment you met him! Regardless, if you ever see him again, you are sure to make him pay!")
    print("")
    if 'The Physician' in game_status['companion']:
        print("PHYSICIAN: I knew he was suspicious! It is always the ones that present themselves as the most kind that betray you in the end!")
        print(" ")
    get_total_AP_SP()
    print("--PREVIOUS STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
    game_status['companion'].remove('The Hoplite')
    game_status['weapon'] = 'no weapon'
    get_total_AP_SP()
    game_status['hoplite_quest'] = False
    game_status['collector_quest'] = True
    game_status['collector_version'].append('hoplite')
    print("")
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    print("")
    return
def run_thief_coins():
    game_status['collector_quest'] = True
    game_status['collector_version'].append('coins')
    print("Suddenly you are struck on the back of the head!")
    print("You black out.")
    print(" ")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print("ZzZz")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print(" ")
    print("You wake up and are shocked to find that someone has stolen your gold coins!!")
    game_status['items'].remove('gold coins')
    get_info()
    return
def run_thief_weapon():
    game_status['collector_quest'] = True
    game_status['collector_version'].append('weapon')
    print("Suddenly you are struck on the back of the head!")
    print("You black out.")
    print(" ")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print("ZzZz")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print(" ")
    print("You wake up and are shocked to find that someone has stolen your weapon!!")
    print("")
    print("---PREVIOUS STATS---")
    get_total_AP_SP()
    game_status['weapon'] = 'no weapon'
    print("")
    print("---NEW STATS---")
    get_total_AP_SP()
    return
def run_collector():
    game_status['collector_quest'] = False
    print("As you cautiously navigate the treacherous cavern, a sight stops you in your tracks. A pale, humanoid creature stands before a mountain of stolen, shiny treasure, its large, black eyes filled with longing. ")
    print("It mutters quietly to itself. You strain to listen, catching fragments of longing and whispered dreams.")
    print("You dont know what to call this creature. Some sort of Collector...")
    print("")
    if 'coins' in game_status['collector_version']:
        print("Oh! There in the corner... are those your gold coins?")
        cont()
    if 'hoplite' in game_status['collector_version']:
        print("So many...")
        print("And... wait... is that... The Hoplite?")
        print("")
        print("It is!")
    if 'weapon' in game_status['collector_version']:
        print("And over there! Its your ", game_status['original_weapon'],"!")
        cont()
    print("He seems distracted. You could probably sneak past him, if you tried...")
    if game_status['companion'] != []:
        if len(game_status['companion']) >1:
            print("Your companions move ahead to the exit, leaving you to fend for yourself.")
        else:
            print(*game_status['companion']," moves to the other end of the chamber, leaving you to fend for yourself.")
    print("What do you want to do?")
    print(" ")
    print("==========================================")
    if 'hoplite' in game_status['collector_version']:
        print("Save The Hoplite")
    if 'weapon' in game_status['collector_version']:
        print("Grab the ", game_status['original_weapon'],"?") 
    if 'coins' in game_status['collector_version']:
        print("Grab the coins")
    print("or flee?")
    while True:
        answer = input("")
        print("==========================================")
        print(" ")
        if answer.lower() in ['hoplite', 'save hoplite','get hoplite','save the hoplite','get the hoplite','go to the hoplite','go to hoplite','the hoplite']:
            print("You rush to The Hoplite's side!")
            print("He is still. You note blood crusted on the side of his head and face. It appears he was hit over the head with something heavy.")
            print("You try and rouse him and, to your joy, he wakes!")
            print(" ")
            print("HOPLITE: My friend! I am so sorry to have left you!")
            print("")
            print("He is sorry? Ah, of course, he must have been attacked! You can't believe you thought this man a thief! To realize now it had been him who had the unlucky fate...")
            print("He is barely alive, too injured to walk, and you cannot carry him. He cannot escape in this state.")
            print(" ")
            print("HOPLITE: It is too late for me, my friend. You must leave me behind. Though, I have one request...")
            print(" ")
            print("You listen carefully to his dying words.")
            print("")
            print("HOPLITE: Use this small dagger to cut off my hand and take it to my family on the surface, so they may have something to bury! This beast will only attack if you take something that shines or glitters, so you should be safe...")
            print(" ")
            print("You nod along, considering.")
            print("You could do as he asks, and the beast would pay you no mind.")
            if game_status['flask'] > 0:
                print("Or, you could give the Hoplite a flask! It would revive him, but surely the beast would attack with viciousness if you were to steal away The Hoplite, in all his shining armor.")
            print("Or...")
            print(" ")
            print("You glance down and see he still has his weapon-- a shining, powerful spear of the Sicilian army. It is a strong weapon, and it would be better in your hands than in his...")
            print("' '")
            print("What do you do? Do you abide by his final request, take his hand, and slip away unnoticed, or will you take the spear and fight your way out?")
            if game_status['flask'] > 0:
                print("Or... do you give him one of your flasks and revive him?")
            print(" ")
            while True:
                answer1 = input(" ")
                if answer1.lower() in ['cut finger','cut off finger','take finger','finger','final request','request']:
                    print("You take the small dagger. Together, you and the Hoplite count to three, and then you bring the blade down. It cuts through most of the wrist, but not all-- you need two more cuts. The Hoplite remains stoic through it all. You mean to commend him for his bravery, but when you are finished to realize he has already died.")
                    game_status['items'].append("Hoplite's Finger")
                    print(" ")
                    print("ACQUIRED: HOPLITE'S FINGER")
                    print("Bonus +5 AP")
                    print(" ")
                    print("HOPLITE'S DAGGER")
                    print("+10 AP, +20 SP")
                    print("Bonus against small enemies")
                    print("")
                    print("==========================================")
                    print("Would you like to take the small dagger as your new weapon?")
                    while True:
                        answer2 = input(" ")
                        print("==========================================")
                        print(" ")
                        if answer2.lower() in ['yes','y','take dagger']:
                            print("You take the dagger.")
                            get_total_AP_SP()
                            print("--PREVIOUS STATS--")
                            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                            print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                            game_status['weapon'] = 'hoplites dagger'
                            get_total_AP_SP()
                            print(" ")
                            print("--CURRENT STATS--")
                            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                            print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                            print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                            game_status['collector'] = [8,8]
                            break
                        elif answer2.lower() in ['no','n',"don't take","dont take dagger"]:
                            print("You leave the dagger.")
                            game_status['collector'] = [0,0]
                            break
                        elif answer2.lower() in ['inventory','status','info','info']:
                            get_info()
                        elif answer2.lower() == 'help':
                            get_help()
                        else:
                            print("Please try again.")   
                    print("")
                    game_status['collector'] = [8,8]
                    print("His wide, black eyes still fixed on his treasure, The Collector does not pay you any mind.")
                    print("It would be easy to slip out now. Or, if you like, to take him on while his guard is down.")
                    battle()
                    break
                elif answer1.lower() in ['give flask','flask','save','save hoplite'] and game_status['flask'] > 0:
                    print("You reach into your satchel and take out a flask, then give it to him.")
                    print("The Hoplite is confused, but he drinks when you tell him to. A few sips, and suddenly he is revived!")
                    game_status['flask'] -= 1
                    flask_number = game_status['flask']
                    print("Remaining flasks: ", flask_number)
                    print("")
                    print("HOPLITE: Oh my friend! My wonderful friend! What is this magic thing?")
                    print("")
                    print("You both embrace quickly, before a shrill cry is heard across the chamber. The Collector has noticed you, and he is coming to attack!")
                    game_status['collector'] = [15,15]
                    game_status['companion'].append("The Hoplite")
                    cont()
                    battle()
                    break
                elif answer1.lower() in ['get spear','grab spear','take spear','spear']:
                    print("You hesitate, then whisper a soft apology. The Hoplite looks confused, then horrified as it dawns on him what you mean to do.")
                    print("You take his Spear.")
                    print(" ")
                    print("HOPLITE'S SPEAR")
                    print("+20 AP, +10 SP")
                    print("Bonus against large enemies")
                    print("")
                    get_total_AP_SP()
                    print("--PREVIOUS STATS--")
                    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                    print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
                    game_status['weapon'] = 'hoplites spear'
                    print(" ")
                    get_total_AP_SP()
                    print("--CURRENT STATS--")
                    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
                    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
                    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
                    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
                    cont()
                    print("As you stand, the glittering spear in your hands, a horrific cry is heard across the chamber. The Collector has noticed you, and is coming to attack!")
                    game_status['collector'] = [18,18]
                    battle()
                    break
                elif answer1.lower() in ['inventory','status','info','info']:
                    get_info()
                elif answer1.lower() == 'help':
                    get_help()
                else:
                    print("Please try again.")
            break
        elif answer.lower() in ['sword', 'broken sword', 'grab broken sword','grab weapon','grab sword','grab axe','grab spider leg','grab leg','take sword','take axe','take spider leg','take spiderleg','grab spiderleg','dagger','small dagger','take small dagger',"poor sword",'take poor sword',"grab poor sword","war elephants tusk","elephants tusk","elephant's tusk","war elephant's tusk","take war elephant's tusk","grab war elephant's tusk","take war elephant's tusk","take elephant's tusk","take elephants tusk","take tusk","grab tusk"]:
            print("From a distance, you watch. The Hoplite is not moving. He is likely already dead, and you will be too, if you don't get your weapon!")
            print("Rather than rush to his side, you instead rush to grab your weapon.")
            print("")
            get_total_AP_SP()
            print("--PREVIOUS STATS--")
            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
            print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
            game_status['weapon'] = game_status['original_weapon']
            print(" ")
            get_total_AP_SP()
            print("--CURRENT STATS--")
            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
            print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
            print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
            cont()
            print("Once you lay your hand on your weapon, you hear a cry from across the chamber. The Collector has noticed you, and is rushing this way!")
            game_status['collector'] = [12,12]
            battle()
            break
        elif answer.lower() in ['grab coins','get coins','coins','take coins']:
            print("From a distance, you watch. The Hoplite is not moving. He is likely already dead, and you will be too, if you don't get your weapon!")
            print("Rather than rush to his side, you instead rush to take back your gold coins.")
            print(" ")
            print("ACQUIRED: Gold Coins")
            game_status['items'].append("gold coins")
            cont()
            print("Once you lay your hand on the coins, you hear a cry from across the chamber. The Collector has noticed you, and is rushing this way!")
            game_status['collector'] = [30,30]
            battle()
            break
        elif answer.lower() in ['flee','leave','run away','runaway']:
            print("Despite the allure of the treasure and your companion's predicament, you really do not like the look of this odd Collector... It is perhaps best to just move on!")
            break
        elif answer.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer.lower() == 'help':
            get_help()
        else:
            print("Please try again.")
    game_status['chamber'] = 0  
    return
def run_physician():
    print("As you're walking into the next chamber, you are suddenly struck on the back of the head.")
    print("Everything goes black.")
    print(" ")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print("ZzZz")
    time.sleep(.5)
    print("zZzZzZzZz")
    time.sleep(.5)
    print(" ")
    print("You wake up and are shocked to find The Physician is gone!")
    if game_status['flask'] > 1:
        print("Not only that, but he's taken your all your flasks!")
    else:
        print("Not only that, but he's taken your flask!")
    print(" ")
    print("That trecherous little rat! That glint in his eye when you used your flask in that last chamber-- he must have begun his plotting then! Wherever he has gone, you hope for his sake it is far away, for once you catch him, the retribution will be swift and painful!!")
    print("")
    if 'The Hoplite' in game_status['companion']:
        print("HOPLITE: I have disliked that man since the moment I met him! Oh, I am sorry, my friend, that we have been tricked like this...")
    game_status['flask'] = 0
    game_status['physician_quest'] = False
    game_status['chimera_quest'] = True
    game_status['chimera_lives'] = True
    game_status['companion'].remove('The Physician')
    cont()
    return
def run_chimera():
    game_status['chimera_quest'] = False
    print("")
    print("The chamber you enter into smells rancid.")
    print("Peering along the ground, you see what appears to be a trail of viscera... gore and organ meat strewn about haphazardly.")
    print("As you wonder what could have caused this, there is a sudden loud, anguished moan from deeper inside the room-- it sounds inhuman.")
    print("")
    print("Keeping to the shadows, you slowly move towards the source of the sound, only to find... The Physician!")
    if 'The Hoplite' in game_status['companion']:
        print("The Hoplite jumps out into the center of the chamber, leveling his spear at him.")
        print("")
        print("HOPLITE: You devious man! Prepare to face justice!")
        print("")
        print("He lunges for an attack, but stops short when another anguished moan diverts his attention to a shadowy corner.")
        print(" ")
    else:
        print("And something else... Some sort of horrific creature. Slow, it emerges from the darkness.")
    print("")
    print("The creature is massive. Some parts dog, some parts monkey, even perhaps some parts human... It makes another gutteral groan, exposing its long fangs. It seems to be in pain.")
    print("Scattered across the floor are the remains of your flasks. Is that why he stole them? To conduct this horrific experiment?")
    if 'The Scholar' in game_status['companion']:
        print("The Scholar lets out a horrified gasp.")
        print(" ")
        print("SCHOLAR: The poor thing... I had heard of chimera before, but I did not know it was so grotesque!")
        print(" ")
    if 'The Girl' in game_status['companion']:
        print("The Girl clings to you, tears forming in her eyes at the sight of it.")
    cont() 
    print("The creature seems powerful, but slow. You could likely escape safely, but perhaps it is better to put this poor creature out of its misery?")
    game_status['chamber'] = 'chimera'
    battle()
    if game_status['life'] == 'alive' and game_status['chimera_lives'] == False:
        print("As you are leaving the room, you also see something on the ground...")
        print("It is your flask!")
        print("")
        print("ACQUIRED: +1 Flask")
        game_status['flask'] += 1
        cont()
        choose_path()
    game_status['chamber'] = 0  
    return
def run_mother():
    game_status['mother_quest'] = False
    print("This room appears empty.")
    print("As you venture deeper into the eerily silent cavern, unease creeps up your spine. The absence of any sound amplifies your every footstep, heightening your senses. Something feels off, like the calm before an impending storm.")
    print(" ")
    print("Suddenly, eight gleaming eyes pierce the shadows, and a monstrous spider lunges at you, fangs dripping with venom. Panic surges as you realize you've stumbled into the deadly lair of a monsterous spider!")
    print("Its massive body emerges from the darkness, crawling along the ceiling of the cave. Then, to your horror, it speaks!")
    print(" ")
    print("MOTHER: My babies... you killed... my babies...!")
    print(" ")
    if 'The Girl' in game_status['companion']:
        print("The Girl shrieks.")
        print("In a moment of profound panic, she picks up a stone and throws it at the giant creature. It strikes it in one of its many eyes, and the beast howls in pain!")
        print(" ")
        print("(Mother Spider's AP and SP reduced by 5!)")
        mother_stats = game_status['mother']
        new_mother_stats = []
        for elem in mother_stats:
            new_mother_stats += [elem + 5]
        game_status['mother'] = new_mother_stats
        print(" ")
    if 'The Hoplite' in game_status['companion']:
        print("The Hoplite valiantly leaps forward, branishing his trusty spear.")
        print(" ")
        print("HOPLITE: Come, my friend, let us slay the horrid beast together!")
    battle()
    return
def run_musician():
    print("._____. ._____.")
    time.sleep(0.1)
    print("| ._. | | ._. |")
    time.sleep(0.1)
    print("| !_| |_|_|_! |")
    time.sleep(0.1)
    print("!___| |_______!")
    time.sleep(0.1)
    print(".___|_|_| |___.")
    time.sleep(0.1)
    print("| ._____| |_. |")
    time.sleep(0.1)
    print("| !_! | | !_! |")
    time.sleep(0.1)
    print("!_____! !_____!")
    time.sleep(0.3)
    print(" ")
    game_status['left_count'] = 0
    if 'Horns of the Minotaur' in game_status['items']:
        run_musician_quest()
        return
    print("You enter into a new chamber of the cavern.")
    print("")
    print("Looking around, this place seems... strange. The walls undulate like water, creating a mesmerizing dance of light and shadow. Dead flowers and vines litter the ground, a haunting reminder of life extinguished within this ethereal realm.")
    if game_status['companion'] != []:
        print("Not only that, but you are alone... ")
        if len(game_status['companion']) > 1:
            print("Where has everyone gone to?")
        else: 
            print("Where has ", *game_status['companion'],"gone to?")
    if game_status['met_musician'] >0:
        print("There is no one else in the room, except for-- ah! At the center of the room, sat in a blackened ring of fallen leaves, is the Musician.")
    else:
        game_status['met_musician'] += 1
        print("There is no one else in the room, except for-- ah! Another person! They seem... odd. Dressed in a veil, and strumming a kithara, they appear to be some sort of Musician.")
    print("")
    if game_status['entered_musician_chamber'] == 0:
        print("MUSICIAN: You made it.")
        print("YOU: What is this place?")
        print("MUSICIAN: Just a little corner I've made for myself. A little reprieve from the drudgery of time and space.")
        if game_status['companion'] != []:
            if len(game_status['companion']) > 1:
                print("YOU: And what of my companions?")
                print("MUSICIAN: Do not worry. They will meet you on the otherside. I merely felt it best we speak alone.")
            else: 
                print("YOU: And what of ",*game_status['companion'],"?")
                print("MUSICIAN: Do not worry. They will meet you on the otherside. I merely felt it best we speak alone.")
        print("")
        print("You feel lightheaded.")
    else:
        print("MUSICIAN: Back again, I see.")
        print("YOU: You... remember me?")
        print("MUSICIAN: You remember ME! Why should I not remember you?")
        print("")
        print("You have no answer for that.")
    cont()
    print("MUSICIAN: How goes your journey? Everything to your liking?")
    print("")
    print("You hesitate to tell them the truth of it-- the gore, the violence, the terror. If they have made it this far then surely they are familiar with it. Then again, looking at their attire, there is no blood. Not even a speck of dirt!")
    print("Perhaps they are more versed in this cavern than you thought.")
    print("")
    print("YOU: How much further must I go to reach the Temple?")
    print("MUSICIAN: Are you truly so eager to meet with your god?")
    print("YOU: I must reach the temple. I must ask for his blessing to save Carthage.")
    print("MUSICIAN: Are you sure hell give it?")
    print("")
    print("You faulter at that. All this time, you hadnt considered the possibly that even if you did arrive, you may be refused.")
    print("Maybe Baal Hammon will not look favorably on you. Maybe he will reject you. Maybe he isnt even there at all...")
    cont()
    print("MUSICIAN: The life of a mortal man is such pain, isnt it? To be forced to capitulate to the whims of an angry god, even in your greatest hour of need...")
    print("YOU: That is just the way of things.")
    print("MUSICIAN: Must it be?")
    print("")
    print("You do not know what they mean.") 
    print("Whatever it is, it does not seem like something that should be spoken of. The Musician smiles wickedly.")
    print("")
    print("MUSICIAN: I will make you a deal... bring me the HORNS OF THE MINOTAUR, and I will share with you something that may be of interest.")
    print("YOU: What sort of thing?")
    print("MUSICIAN: No hints, I'm afraid. You'll have to wait to find out.")
    print("")
    print("Frustrated, you turn from The Musician and their crpytic conversation.")
    game_status['musician_quest'] = True
    game_status['entered_musician_chamber'] += 1
    game_status['minotaur_boost'] = True
    return
def run_musician_quest_fail():
    print("._____. ._____.")
    time.sleep(0.1)
    print("| ._. | | ._. |")
    time.sleep(0.1)
    print("| !_| |_|_|_! |")
    time.sleep(0.1)
    print("!___| |_______!")
    time.sleep(0.1)
    print(".___|_|_| |___.")
    time.sleep(0.1)
    print("| ._____| |_. |")
    time.sleep(0.1)
    print("| !_! | | !_! |")
    time.sleep(0.1)
    print("!_____! !_____!")
    time.sleep(0.3)
    game_status['left_count'] = 0
    print(" ")
    print("Stepping into the cavern, a familiar sight unfolds. The walls undulate like liquid, casting a mesmerizing glow. Amidst the eerie beauty, dead flowers and vines sprawl.")
    print("In the center, once again, is the Musician. They look up at you with a bored gaze.")
    print("")
    print("MUSICIAN: Not going so well?")
    print("YOU: It is... more difficult than I thought. Tell me, do you have any advice for me?")
    print("")
    print("The Musician smiles wickedly, their mouth full of black teeth.")
    print("")
    print("MUSICIAN: The Minotaur is a woefully simply creature, both in life and in death. There are no tricks. You simply must defeat him.")
    print("YOU: Is there nothing you can give me?")
    print("MUSICIAN: I quite think I've given you enough already.")
    print("")
    print("Dishearted, you leave the chamber, embarking once more on your fruitless quest.")
    return
def run_musician_quest():
    print("._____. ._____.")
    time.sleep(0.1)
    print("| ._. | | ._. |")
    time.sleep(0.1)
    print("| !_| |_|_|_! |")
    time.sleep(0.1)
    print("!___| |_______!")
    time.sleep(0.1)
    print(".___|_|_| |___.")
    time.sleep(0.1)
    print("| ._____| |_. |")
    time.sleep(0.1)
    print("| !_! | | !_! |")
    time.sleep(0.1)
    print("!_____! !_____!")
    time.sleep(0.3)
    print(" ")
    game_status['left_count'] = 0
    game_status['musician_quest'] = False
    game_status['musician_done'] = True
    print("Stepping into the cavern, a familiar sight unfolds. The walls undulate like liquid, casting a mesmerizing glow. Amidst the eerie beauty, dead flowers and vines sprawl.")
    print("In the center, once again, is the Musician. They smile at you with black teeth, their eyes wide.")
    print("")
    print("MUSICIAN: Oh... you've done it.")
    print("")
    print("You approach, the Horns of the Minotaur in hand. The Musician's thin fingers grasp towards you, and you hand them over. They look pleased.")
    print("They stroke the horns almost lovingly, the kithara entirely forgotten. After a few moments of being utterly ignored, you cough pointedly to make your presence known. The Musician looks up, a bemused smile on their face.")
    print("")
    print("MUSICIAN: No matter how many times I see it, you never fail to surprise me.")
    cont()
    print("MUSICIAN: I have seen many like you-- honest, desperate, kind, delusional mortals clawing their way through these caverns in an attempt to find Ba'al Hammon and gain his favor. Do you know what happens to them?")
    print("YOU: ...")
    print("MUSICIAN: Ah, of course you don't. Well, I will tell you, it is not what they expect! Not at all! Haha. It is just the way of things. But, as things can be one way, such they may be another... do you follow?")
    print("")
    print("You do not. They take pity on you.")
    print("")
    print("MUSICIAN: You see, Ba'al Hammon is a fiercesome god. It is so very hard to earn his favor, and yet you keep trying... it's sad, really. I see this suffering, and I wish to help.")
    print("")
    cont()
    print("The Musician strums definitively upon their kithara. You suddenly feel a weight in your hand. Your weapon has been replaced with something new! A strange blade, long and curved and shining like oil.")
    print("")
    print("FALCATA")
    print("A long, curved blade. It has a strange energy.")
    print("+40 AP, +40 SP")
    print(" ")
    get_total_AP_SP()
    print("--PREVIOUS STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
    game_status['weapon'] = 'Falcata'
    get_total_AP_SP()
    print("")
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    print("")
    cont()
    print("YOU: What is this?")
    print("MUSICIAN: A gift. Your earthly weapons are little match for Ba'al Hammon. If you hope to kill him, this is how you do it.")
    print("YOU: ... Kill him? Kill Baal Hammon?")
    print("MUSICIAN: When he asks for a sacrifice, you must KILL. Do so, and great rewards may be yours... ")
    print("")
    print("You gaze down at the weapon. Kill Baal Hammon? Can such a thing be done?")
    print("You return your gaze to The Musician only to find them gone. The only thing that remains of them is the gentle sound of the kithara, sounding through the chamber as if from a great distance.")
    print("")
    game_status['musician_hint'] = True
    return
def run_cave_merchant():
    #HIDDEN - not active chamber
    room = random.randint(0,1)
    if room == 0:
        print("The next room you enter is hardly a chamber at all.")
        print("The path narrows, a steep wall on one side, and a sharp drop to the other.")
        print("You carefully slide along the edge, and as you round a corner suddenly spot a glowing light.")
        print("Its a lantern, hung from the back of an ox cart, and sitting in the cart is a man.")
    elif room == 1:
        print("The next room you enter is smaller than the others, damp and filled with ferns and moss.")
        print("You push through a few stray fern stocks before spotting the soft glow of a lantern.")
        print("It is hung on the back of an ox cart, and in the ox cart is sitting a man.")
    print("")
    if game_status['met_cave_merchant'] > 1: 
        print("As you approach, he looks up, his clouded eyes searching the darkness.")
        print("")
        print("MERCHANT: Ah, it's you again. Glad to see you're still alive.")
        if game_status['met_cave_merchant'] == 1:
            print("YOU: It really is you! I had wondered.")
            print("MERCHANT: Oh?")
            print("YOU: It is only... the cart...")
            print("")
            print("You signal towards the large ox cart. It seems the question 'how the hell are you dragging this around' is fairly implied by the context.")
            print("The merchant just laughs, his voice reedy and thin.")
            print("")
            print("MERCHANT: Oh, I manage. Anyway, are you looking to trade?")
        else: 
            print("YOU: And you. Still dragging this thing around? ")
            print("MERCHANT: If I weren't, what would I have to trade you?")
    else: 
        game_status['met_cave_merchant'] = True
        print("You approach slowly. What manner of beast is this that sits so peacefully out in the open?")
        print("Of course it could just be a man but how on earth did he manage to get such a large cart all the way down here?")
        print("Suddenly, the man calls out to you.")
        print(" ")
        print("MERCHANT: You there! Human?")
        print(" ")
        print("You hesitate a moment before nodding.")
        print("The man smiles. He is missing teeth. And, as you get closer, you see he is actually rather old and... frail. ")
        print(" ")
        print("YOU: Do you... need help, sir? ")
        print("MERCHANT: Hm, me? Oh no, no. I'm just on my way to the agora, got a bit lost is all.")
        print("YOU: I see...")
        print("MERCHANT: But while we're both here... interested in a trade?")
    print(" ") 
    print("")
    print("MERCHANTS INVENTORY")
    print(*game_status['cave_merchant_inventory'], sep =', ')
    print(" ")
def lost_adventurer():
    print(" ")
    print("This room of the cavern is narrow, slightly elevated toward the center. There, against the wall, you see a figure, collapsed to the ground and in a pool of blood.")
    print("They appear to be human...")
    print("")
    print("You approach cautiously, glancing about the room, ensuring whatever it is that did this to the man is no longer in your presence.")
    print("Deeming it safe, you finally approach. Up close you can now see in the dim light a woven insignia of a large lemon tree.")
    print("He has a deep gash in his side cut right through his linothorax armor. His face is cold, his eyes open. He has died.")
    print("You offer a quick prayer on his behalf, before noticing at his side... a sword. It is chipped and broken, but still sharp in places. It would serve better than your empty fists, at least.")
    print("")
    print("==========================================")
    print("Do you take his weapon?")
    while True:
        answer1 = input(" ")
        print("==========================================")
        print(" ")
        if answer1.lower() in ['yes','y','take','take it','take weapon','take his weapon']:
            print("The dead have no need for such things.")
            print("You approach the corpse. It's cold hands grip the handle of the sword tightly.")
            if 'the scholar' in game_status['companion']:
                print("The Scholar looks to you, repulsed.")
                print(" ")
                print("YOU: What?")
                print("SCHOLAR: This man is an Amalfi warrior!")
                print("YOU: So...?")
                print("SCHOLAR: They believe that after death one must fight their way past demons to enter the Kingdom. For this reason, they are always buried with their swords. By taking this from him, you doom him to eternal suffering...")
                print("YOU: It is not my religion.")
                print(" ")
                print("The Scholar frowns at you, and goes quiet.")
            print("You pull and pull until there is a sickening crack. The fingers now bent backwards, you extract the sword, and take it for your own.")
            get_total_AP_SP()
            print(" ")
            print("POOR SWORD")
            print("+11 AP, +11 SP")
            print("Bonus against humanoid enemies")
            print(" ")
            print("--PREVIOUS STATS--")
            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
            print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
            game_status['weapon'] = 'Poor Sword'
            #must set this due to potential weapon switching during Collector plotline
            game_status['original_weapon'] = 'new sword'
            get_total_AP_SP()
            print(" ")
            print("--NEW STATS--")
            print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
            print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
            print("TOTAL: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll AP, ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll SP")
            
            break
        elif answer1.lower() in ['flask','use flask','save him']:
            if game_status['flask'] > 0:
                print("You reach into your satchel and pull out your flask.")
                print("Gently, you pry open the man's lips. The body is stiff and does not come easily.")
                print("Still you manage to pour the contents of the flask down his throat.")
                cont()
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print("..")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("He does not awaken. Perhaps his soul had already left this world...")
                if 'The Physician' in game_status['companion']:
                    print(" ")
                    print("The Physician steps up behind you, eyes wide and fixed on the flask in your hand.")
                    print(" ")
                    print("PHYSICIAN: What is that you just used?")
                    print(" ")
                    print("He sounds almost eager, too distracted by the curiousity to pay respect to the fallen adventurer.")
                    print("You do not answer and move on.")
                game_status['flask'] -= 0
                get_info()
                break
            else:
                print("You do not have a flask to give him...")
        elif answer1.lower() in ['no','n','leave it']:
            print("You leave the adventurer undisturbed.")
            print("This cavern will become his tomb. Surely the beasts within will take no mercy on his corpse, once it is found.")
            print("But for now, his dignity remains.")
            if 'the scholar' in game_status['companion']:
                print("As you turn to go, you catch The Scholar with a soft smile on her face.")
                print(" ")
                print("YOU: What?")
                print("SCHOLAR: This man is an Amalfi warrior!")
                print("YOU: So...?")
                print("SCHOLAR: They believe that after death one must fight their way past demons to enter the Kingdom. For this reason, they are always buried with their swords. He may have died here, but perhaps now he has a chance to live on in the after life.")
                print("")
                print("You did not know that. Perhaps you have done the right thing.")
            print(" ")
            break
        elif answer1.lower() in ['inventory','status','info','info']:
            get_info()
        elif answer1.lower() == 'help':
            get_help()
        else:
            print('Please try again.')
    game_status['lost_adventurer'] = 1
    cont()
    return 
def run_god_killer():
    print("Steeling yourself, you prepare to do the unthinkable.")
    print("You deliver a heavy blow to the towering stone statue of Ba'al Hammon. The sound reverberates through the ancient chamber, echoing through the caverns above.")
    print('You strike again. Then again. Then again.')
    print("On the fourth strike, a small crack forms in the base. Suddenly, the chamber goes eerily quiet.")
    print("")
    print("Then, as if from a great distance, you hear the sound of war drums.")
    cont()
    print("Boom.")
    time.sleep(0.3)
    print("Boom.")
    time.sleep(0.3)
    print("Boom!")
    time.sleep(0.3)
    print("The floor falls away. The earth itself crumbles. You are thrust into the eather, into the godly realm, with the magnificent form of Ba'al Hammon standing before you.")
    print("")
    print("BAAL: Foolish mortal... you dare to stand against me? You dare to take up arms against your own god?!")
    print("")
    print("You raise your weapon in reply!!")
    print("")
    game_status["chamber"] = 'baal'
    run_god_killer_combat()
    if game_status['god_killer'] == True:
        print("You have succeeded!")
        game_status['life'] = 'killer'
        game()
    else :
        print("You have failed!")
        if game_status['flask'] > 0:
            print(" ")
            print("==========================================")
            print('Use a flask to revive and try again?')
            answer = input(" ")
            print("==========================================")
            print(" ")
            while True:
                if answer.lower() in ['revive','use flask','take flask','try again','again','yes','y']:
                    print("You take a flask.")
                    flask_status = len(game_status['companion'])
                    if flask_status == 0:
                        print("Suddenly, you find yourself revitalized!")
                    elif flask_status == 1:
                        print("Suddenly, you find yourself and ", game_status['companion']," revitalized!")
                    elif flask_status > 1:
                        print("Suddenly, you find yourself and your companions revitalized!")
                        print("")
                    break
                elif answer.lower() in ['no','n']:
                    game_status['life'] == 'failure'
                    game()
                elif answer.lower() in ['inventory','status','info','info']:
                    get_info()
                elif answer.lower() == 'help':
                    get_help()
                else: 
                    print("Please try typing again.")
            run_god_killer_combat()
        else: 
            if game_status['god_killer'] == True:
                print("You have succeeded!")
                game_status['life'] = 'killer'
                game()
            else :
                print("You have failed...")
                game_status['life'] = 'failure'
                game()
def run_god_killer_combat():
    #gives stat info so player may make an informed choice
    get_total_AP_SP()
    opponent = game_status["baal"]
    print("--CURRENT STATS--")
    print("Base: ", game_status['base_AP']," AP, ",game_status['base_SP']," SP")
    print("Bonus: ", game_status['bonus_AP']," AP, ",game_status['bonus_SP']," SP")
    print("TOTAL AP: ", game_status['bonus_AP'] + game_status['base_AP'],"+ dice roll")
    print("TOTAL SP: ",game_status['bonus_SP'] + game_status['base_SP'],"+ dice roll")
    dice_attack = random.randint(0,10)
    dice_speed = random.randint(0,10)
    attack = dice_attack + game_status['bonus_AP'] + game_status['base_AP']
    speed = dice_speed + game_status['bonus_SP'] + game_status['base_SP']
    #opponent stats are pulled from dictionary, index_0 = attack, index_1 = flee
    if 'Eyes of Cerberus' in game_status['items']:
        print("The Eyes of Cerberus reveals to you the enemy's secrets...")
        print("ENEMY STATS:")
        print("AP: ", opponent[0], ", SP: ",opponent[1])
    elif 'dog eyes' in game_status['items']:
        print("The dog eyes reveal a faint image of the enemy's power...")
        upperAP = random.randint(5,10)
        lowerAP = random.randint(-10,-5)
        upperSP = random.randint(5,10)
        lowerSP = random.randint(-10,-5)
        upper_APbound = opponent[0] + upperAP
        lower_APbound = opponent[0] + lowerAP
        upper_SPbound = opponent[1] + upperSP
        lower_SPbound = opponent[1] + lowerSP
        if lower_APbound < 0:
            lower_APbound = 0
        if lower_SPbound < 0:
            lower_SPbound = 0
        print("ENEMY STATS:")
        print("AP: ", lower_APbound,"-",upper_APbound)
        print("SP: ",lower_SPbound,"-",upper_SPbound)
    else:
        print("ENEMY STATS:")
        print("AP: ???, SP: ???")
    print("")
    print("You cannot flee! You must fight, there is no other way!!")
    cont()
    print("")
    print("")
    print("         .                      .")
    time.sleep(0.1)
    print("          .                      ;")
    time.sleep(0.1)
    print("          :                  - --+- -")
    time.sleep(0.1)
    print("          !           .          !")
    time.sleep(0.1)
    print("          |        .             .")
    time.sleep(0.1)
    print("          |_         +")
    time.sleep(0.1)
    print("       ,  | `.")
    time.sleep(0.1)
    print(" --- --+-<#>-+- ---  --  -")
    time.sleep(0.1)
    print("       `._|_,'")
    time.sleep(0.1)
    print("          T")
    time.sleep(0.1)
    print("          |")
    time.sleep(0.1)
    print("          !")
    time.sleep(0.1)
    print("          :         . : ")
    time.sleep(0.1)
    print("          .       *")
    time.sleep(0.5)
    print("                             ____")
    time.sleep(0.05)
    print("                     __,-~~/~    `---.")
    time.sleep(0.05)
    print("                   _/_,---(      ,    )")
    time.sleep(0.05)
    print("               __ /        <    /   )  \___")
    time.sleep(0.05)
    print("- ------===;;;'====------------------===;;;===----- -  -")
    time.sleep(0.05)
    print("                  \/  ~'~'~'~'~'~\~'~)~'/")
    time.sleep(0.05)
    print("                  (_ (   \  (     >    \)")
    time.sleep(0.05)
    print("                   \_( _ <         >_>'")
    time.sleep(0.05)
    print("                      ~ `-i' ::>|--')")
    time.sleep(0.05)
    print("                          I;|.|.|")
    time.sleep(0.05)
    print("                         <|i::|i|`.")
    time.sleep(0.05)
    print("                        (` ^'`-' )")
    if attack >= opponent[0]:
        game_status['god_killer'] = True
        print("You have succeeded!")
        game_status['life'] = 'killer'
        game()
    else: 
        game_status['god_killer'] = False
        return



if __name__ == "__main__":
    main()