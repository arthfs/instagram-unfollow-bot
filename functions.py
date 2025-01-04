import json

def not_following():

    file_1 = open("path of following's file ",'r')
    json_1 = json.load(file_1)
    data_1 = json_1 [  "relationships_following" ]
    followings = [ d['string_list_data'][0]['value'] for d in data_1 ]

    file_2 = open("path of follower's file ",'r')
    json_2 = json.load(file_2)
    followers = [ d['string_list_data'][0]['value'] for d in json_2 ]

    not_following_me = set(followings).difference(set(followers))
    
    file_1.close()
    file_2.close()

    return not_following_me

