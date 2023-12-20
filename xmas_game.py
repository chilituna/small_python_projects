#Little Xmas Game
#Santa Claus is coming to town.

print('''
                                                      *
   *                                                          *
                                *                  *        .--.
    \/ \/  \/  \/                                        ./   /=*
      \/     \/      *            *                ...  (_____)
       \ ^ ^/                                       \ \_((^o^))-.    *
       (o)(O)--)--------\.                           \   (   ) \ \._.
       |    |  ||================((~~~~~~~~~~~~~~~~~))|   ( )   |    \
        \__/             ,|        \. * * * * * * ./  (~~~~~~~~~~)    \
 *        ||^||\.____./|| |          \___________/     ~||~~~~|~'\____/ *
          || ||     || || A            ||    ||         ||    |   jurcy
   *      <> <>     <> <>          (___||____||_____)  ((~~~~~|   *

''')
print("Welcome to Little Xmas Game.")
print("Let's find out what the Santa has in his sack for you.") 

answer = input('How would you describe your behavior this year? Type "naughty" or "nice."\n')
while((answer.lower() != "naughty") and (answer.lower() != "nice")):
  answer = input('Wrong input. Type "naughty" or "nice."\n')
if answer.lower() == "naughty":
  print("Oijoijoi. That's not the way to go. Santa brings you a bag of coals. Maybe try being a bit nicer next year. Game Over.")
  break
else:
  print("Great! That seems to be aligned with the information Santa has received from the elves, that have been watching you.")
answer = input('Santa could use a little refresher. What will you offer? Type "Whiskey" or "Water".\n')
while(answer.lower() != "water" and answer.lower() != "whiskey"):
  answer = input('Wrong input.Type "water" or "whiskey."\n')
if answer.lower() == "whiskey":
  print("That is some fine whiskey. In fact, Santa likes it a bit too much and will pass out on your sofa. As a Christmas present you get to keep Santa for one night. Game Over.")
  break
else:
  print("Classic choice! Nothing beats good old Leitungswasser. Santa eases his thirst and then asks you to sing a song.")
answer = input('Which song will you sing? Type "silent" for Silent Night, "jingle" for Jingle Bells, or "joulu" for "Joulupukki"')
while(answer.lower() != "silent" and answer.lower() != "jingle" & answer.lower() != "joulu"):
  answer = input('Wrong input. Type "silent", "jingle" or "joulu."\n')
if answer.lower() == "silent":
  print("Santa falls asleep on 3rd verse and starts snoring. Luckily you find a pair of almost new earplugs in his bag. May that be your present - have a merry, silent night!")
elif answer.lower() == "jingle":
  print("Santa likes that: You get a lapdance while the bells are ringing, have a jingely xmas!")
elif answer.lower() == "joulu":
  print("Jackpot! As you know, the real Santa comes from Finland and loves this classic tune. He will sing with you and hand you the whole bag of presents.")
else:
  print("That's not an option. Game Over!")
