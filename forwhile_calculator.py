import random

playerhp=555
enemyatkl=50
enemyatkh=100

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    print(dmg)
    playerhp = playerhp - dmg
    print(playerhp)


    if playerhp<=0:
       playerhp = 0

    print("your damage is ", dmg, "your life left is ", playerhp)

    if playerhp==0:
        print("your damage is ", dmg, "your life left is ", playerhp,"and you have died")
    #break
