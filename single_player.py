from core import *
from shell import *
from random import randint, choice
from time import sleep


def player_name():
    name = input('What is your name?')

    return name


def player_stats():
    your_stats = new_gladiator(100, 10, 10, 20, 50, 0)
    return your_stats


def gladiator():
    name = 'Gladiator'
    return name


def enemy_glad():
    glad_stats = new_gladiator(100, 10, 10, 20, 50, 0)
    return glad_stats


def goblin():
    name = 'Goblin'
    return name


def enemy_gob():
    gob_stats = new_gladiator(100, 15, 15, 25, 45, 0)
    return gob_stats


def boss_1():
    name = 'Gnashmaw the Gobliator'
    return name


def gnash():
    maw_stats = new_gladiator(150, 25, 20, 25, 55, 0)
    return maw_stats


def intro(name):
    print('Welcome', name, 'to the world of Collisera!')
    print(
        'In Collisera you will fight for what you desire!\nThere is only one reason people choose to come to Collisera and, that is to become the Champion! '
    )
    print(
        'The Champion is the mightiest of the mighty! To defeat him would make you the strongest warrior in all of the realms! \nThe current Champion is Rastobad the God Slayer!\nTo get to him you will fight many others along the way! We shall start you off in The Pit and you shall work your way up from there'
    )


def enemy_ai_turn(name, stats, enemy_name, enemy_stats):
    while True:

        print('It is', enemy_name, "'s turn!".upper())
        print(enemy_name.upper(), "'S STATS", enemy_stats['Health'], '|||',
              enemy_stats['Rage'], '|||', enemy_stats['Precision'])
        sleep(1)
        print('WHAT WILL THE ENEMY DO?')
        sleep(1)
        enemy_options = ['A', 'H', 'E', 'P']
        last_resort = ['A', 'H']
        if enemy_stats['Health'] > 75:
            turn = choice(enemy_options)
            if turn == 'A':
                print('THE ENEMY ATTACKS!')
                attack(enemy_stats, stats)
                print(enemy_name.upper(), "'S STATS", enemy_stats['Health'],
                      '|||', enemy_stats['Rage'], '|||',
                      enemy_stats['Precision'])
                break
            elif turn == 'H':
                print("THE ENEMY HEALS")
                heal(enemy_stats)
                print(enemy_name.upper(), "'S STATS", enemy_stats['Health'],
                      '|||', enemy_stats['Rage'], '|||',
                      enemy_stats['Precision'])
                break
            elif turn == 'E':
                print('THE ENEMY ENRAGES!')
                enrage(enemy_stats)
                print(enemy_name.upper(), "'S STATS", enemy_stats['Health'],
                      '|||', enemy_stats['Rage'], '|||',
                      enemy_stats['Precision'])
                break
            else:
                print('THE ENEMY HAS PASSED!')
                break
        elif enemy_stats['Health'] > 50 and enemy_stats['Health'] < 75:
            print('THE ENEMY ATTACKS!')
            attack(enemy_stats, stats)
            print(enemy_name.upper(), "'S STATS", enemy_stats['Health'], '|||',
                  enemy_stats['Rage'], '|||', enemy_stats['Precision'])
            break
        elif enemy_stats['Health'] > 30 and enemy_stats['Health'] < 50:
            print('THE ENEMY ENRAGES!')
            enrage(enemy_stats)
            print(enemy_name.upper(), "'S STATS", enemy_stats['Health'], '|||',
                  enemy_stats['Rage'], '|||', enemy_stats['Precision'])
            break
        elif enemy_stats['Health'] == 30:
            print('THE ENEMY ATTACKS!')
            attack(enemy_stats, stats)
            print(enemy_name.upper(), "'S STATS", enemy_stats['Health'], '|||',
                  enemy_stats['Rage'], '|||', enemy_stats['Precision'])
            break
        else:
            turn = choice(last_resort)
            if turn == 'A':
                print('THE ENEMY ATTACKS!')
                attack(enemy_stats, stats)
                print(enemy_name.upper(), "'S STATS", enemy_stats['Health'],
                      '|||', enemy_stats['Rage'], '|||',
                      enemy_stats['Precision'])
                break
            else:
                print('THE ENEMY HEALS!')
                heal(enemy_stats)
                print(enemy_name.upper(), "'S STATS", enemy_stats['Health'],
                      '|||', enemy_stats['Rage'], '|||',
                      enemy_stats['Precision'])
                break


def battle(player_1_name, player_1, player_2_name, player_2):

    while True:
        if is_dead(player_1) == True:
            print(player_1_name.upper(), 'HAS FALLEN!')
            print(player_2_name.upper(), 'IS VICTORIOUS!')
            break
            exit()
        combatant_1_turn(player_1_name, player_1, player_2_name, player_2)
        if is_dead(player_2) == True:
            print(player_2_name.upper(), 'HAS FALLEN!')
            print(player_1_name.upper(), 'IS VICTORIOUS!')
            player_1['Health'] = 100
            player_1['Rage'] = 0
            player_1['Precision'] = 50
            player_1['Mana'] = 0
            return True
        enemy_ai_turn(player_1_name, player_1, player_2_name, player_2)


def level_1_1(name, stats, enemy_name, enemy_stats):

    print(
        '\n\nA trap door triggers beneath you as you fall into a dark and spiraling tunnel.\nOn the way down you tumble and hit your head, knocking you unconscious.\nYou awaken in what must be The Pit.\nWithout a moment\'s notice you are charged by your first opponent. THE GLADIATOR!'
    )
    sleep(3)
    print('''      ,-'""`-,               
    ,'        `.             
   /    _,,,_   \            
  /   ,'  |  `\/\\           
 /   /,--' `--.  `           
 |   /      ___\_            
 |  | /  ______|             
 |  | |  |_' \'|             
 \ ,' (   _) -`|             
  '--- \ '-.-- /             
 ______/`--'--<              
 |    |`-.  ,;/``--._        
 |    |-. _///     ,'`\      
 |    |`-Y;'/     /  ,-'\    
 |    | // <_    / ,'  ,-'\  
 '----'// -- `-./,' ,-'  \/  
  |   //[==]     \,' \_.,-\  
  |  //      `  -- | \__.,-' 
    // -[==]_      |   ____\ 
   //          `-- |--' |   \
        [==__,,,,--'    |-'" 
    ---""''             |    
hjm          ___...____/     
        --------------------.
               ,.        --.|
              /||\        /||
               ||        /  |
               ||       /   |
                |      /    |
''')
    results = battle(name, stats, enemy_name, enemy_stats)
    if results == True:
        return True


def level_1_2(name, stats, enemy_name, enemy_stats):
    print(
        '\n\nThe gladiator lays upon the ground pooling in his own blood as you carry on, hoping to find a way out.\nYou see a ray of light and begin to follow it until you stumble upon a goblin blocking the path.\nYou cannot go around him. You must go through him.'
    )
    sleep(3)
    print('''      -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//\'
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ \'
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) \'
   / / / / |  |   |  |\  \  \ \'
   / / // /|  |   |  |  \  \ \  
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
''')
    result = battle(name, stats, enemy_name, enemy_stats)
    if result == True:
        return True


def level1_boss(name, stats, enemy_name, enemy_stats):
    print(
        'After defeating the goblin you move along the dim path until you enter a medium sized room that is well lit.\nAt the back of the room you see a staircase and hope to the gods it is the way out.\nAs you rush to the door a thunderous crash occurs behind you as a gate slams barricading the staircase.\nYou turn and witness the horror know as Gnashmaw the Goblin Gladiator.\nThe battle commences. '
    )
    sleep(3)
    battle(name, stats, enemy_name, enemy_stats)


def game_play():
    name = player_name()
    stats = player_stats()
    intro(name)
    enemy_1 = gladiator()
    glad = enemy_glad()
    enemy_2 = goblin()
    gob = enemy_gob()
    enemy_3 = boss_1()
    gm = gnash()
    results = level_1_1(name, stats, enemy_1, glad)
    if results == True:
        result = level_1_2(name, stats, enemy_2, gob)
        if result == True:
            level1_boss(name, stats, enemy_3, gm)


def main():
    game_play()


if __name__ == '__main__':
    main()
