import requests
import json
import os
from typing import Final
from dotenv import load_dotenv
from ast import literal_eval

load_dotenv()
player_id_dict : Final[dict] = literal_eval(os.getenv('PLAYER_ID_DICT'))   
player_record_dict : Final[dict] = literal_eval(os.getenv('PLAYER_RECORD_DICT'))
url = "https://gmserver-api.aki-game2.net/gacha/record/query"
cardPoolId = "5c13a63f85465e9fcc0f24d6efb15083"
serverId = "10cd7254d57e58ae560b15d51e34b4c8"
languageCode = "en"

def create_request_body(player_id,recordId,  cardPoolType):
    return {"playerId":player_id, "cardPoolId":cardPoolId,"cardPoolType":cardPoolType ,"serverId":serverId, "languageCode":languageCode, "recordId":recordId}

def count_pity(player_name):
    standard_resonators = ["Verina", "Calcharo", "Ling Yang", "Jianxin", "Encore"]
    hard_pity_status = "(50/50)"
    resonator_pull_data = json.loads(requests.post(url, json = create_request_body(player_id_dict[player_name],player_record_dict[player_name],1)).text)['data']
    weapon_pull_data = json.loads(requests.post(url, json = create_request_body(player_id_dict[player_name], player_record_dict[player_name], 2)).text)['data']
    
    resonator_pulls = [pull['qualityLevel'] for pull in resonator_pull_data]
    weapon_pulls = [pull['qualityLevel'] for pull in weapon_pull_data]

    if 4 in resonator_pulls:
        resonator_4star_pity = resonator_pulls.index(4)
    else:
        resonator_4_star_pity = len(resonator_pulls)
    if 5 in resonator_pulls:
        resonator_5star_pity = resonator_pulls.index(5)
        if resonator_pull_data[resonator_5star_pity]['name'] in standard_resonators:
            hard_pity_status = "(Guaranteed)"
           
    else:
        resonator_5star_pity = len(resonator_pulls)


    if 4 in weapon_pulls:
        weapon_4star_pity = weapon_pulls.index(4)
    else:
        weapon_4star_pity = len(weapon_pulls)
    if 5 in weapon_pulls:
        weapon_5star_pity = weapon_pulls.index(5)
    else:
        weapon_5star_pity = len(weapon_pulls)

    if resonator_4star_pity > resonator_5star_pity : resonator_4star_pity = resonator_5star_pity
    if weapon_4star_pity > weapon_5star_pity : weapon_4star_pity = weapon_5star_pity
    
    return {"resonator_5star_pity":resonator_5star_pity, "resonator_4star_pity":resonator_4star_pity,
            "weapon_5star_pity":weapon_5star_pity, "weapon_4star_pity":weapon_4star_pity, "hard_pity_status":hard_pity_status}