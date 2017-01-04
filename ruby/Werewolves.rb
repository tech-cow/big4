#-------------------------------Variable-----------------------------------
rules = ("The game is composed of two teams: werewolves and townsfolk. The objective of the werewolves
is to kill off all the villagers without themselves being killed.
The objective of the townsfolk is to figure out who the werewolves are and kill them.
One of the townsfolk is a seer, who has the ability to tell whether other players are werewolves or not")

##
role = [
  #Special Villager
  "Seer",
  "Witch",
  "Hunter",
  "Idiot",
  #Villager
  "Villager","Villager" ,"Villager" ,"Villager",
  #Werewolf
  "Werewolf","Werewolf","Werewolf","Werewolf"]

roles_display = ("Seer|Witch|Hunter|Idiot|Villager|Werewolf")


#-------------------------------Methods-----------------------------------



def text_display_template(input_text)
  puts("--------------------------------------------------------------------------------------" +
  "\n"+ input_text + "\n"+
   "--------------------------------------------------------------------------------------" )
end

def assign_card(role,player)
  while(role.length != 0)
    # Select a card and remove it from the array
    random_number = rand(role.length)
    temp_card = role[random_number]
    role.delete_at(random_number)

    #Display
    puts("************")
    puts("|" + player.to_s + "|" + temp_card + "|" )
    puts("************")
    player = player + 1
    puts("\n")
  end
end

# This has nothing to do with this program LOL
def bestplayer()
  puts ("Do you think Yu is the best werewolves player in the world?")
  while true
    input = gets().chomp
    if input == "yes"
      break
    end
    puts ("The only acceptable answer is yes")
  end
end


#-------------------------------Main-----------------------------------

#Just random call lol
bestplayer()

puts ("\n"+ "Rules" + "\n")
text_display_template(rules)
puts ("\n"+ "Roles" + "\n")
text_display_template(roles_display)

# @test
player = 1
assign_card(role,player)


# user input
# puts("\n" + "So, Which card are you going to pick")
# name = gets.chomp()

#Loop
# while(name != "Seer" && name != "Villager" && name != "Werewolf")
#   puts(3>5)
#   puts("Please only type one of the following rules" + "\n" + roles + "\n")
#   name = gets.chomp()
# end
#   puts("Of course, your role is " + name)



#wakatime works now my goodness, life is good

#if-else
