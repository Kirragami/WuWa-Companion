from union_calculator import calculate_time_to_target_level
from pity_counter import count_pity

def get_response(user_input, username, display_name):
  if user_input.startswith("!!union"):
    split_user_input = user_input.split()
    try:
      current_level = int(split_user_input[1])
      current_xp = int(split_user_input[2])
      target_level = int(split_user_input[3])

      if target_level <= current_level:
        return '''Blud's try'na go back in time :skull:'''

      return f'{calculate_time_to_target_level(current_level, current_xp, target_level)} days'
    except:
      pass
    
  elif user_input.startswith("!!pity"):
    pity = count_pity(username)
    message = f"""{display_name}'s Pity Count\n\nResonator 5 Star Pity : {pity['resonator_5star_pity']} {pity["hard_pity_status"]}\nResonator 4 Star Pity : {pity['resonator_4star_pity']}\n\nWeapon 5 Star Pity : {pity['weapon_5star_pity']}\nWeapon 4 Star Pity : {pity['weapon_4star_pity']}"""
    return message