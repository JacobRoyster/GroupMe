import requests
import json
import time
import sys
"""
userToken should be a valid GroupMe  user token. (string)
groupID should be a valid group that you have access to. (string)
nickname should be the desired name for the user in the group. (string)
identifier should be a valid identifier for the user you want to add. (string)
identifierType should be an int in the range [1,3] 1 corresponds to we are expecting user_id,
  2 corresponds to we are expecting a phone_number, 3 corresponds to we are expecting email
purpose of this function is to add someone to a group.
"""
def AddToGroup(userToken, groupID, nickname, identifier, identifierType):
    # Standard start for the request string for the GroupMe API
    standardBeginning = "https://api.groupme.com/v3/groups"
    # Decoding which identifierType we are using.
    idType = ""
    if (identifierType == 1):
        idType = "user_id"
    elif(identifierType == 2):
        idType = "phone_number"
    elif(identifierType == 3):
        idType = "email"
    else:
        raise ValueError("The identifier type provided is not in the range [1,3]")
    # Generating a GUID based off of system time. This Will only be distinct till milliseconds
    # I decided to drop a marker that if you are trying to someone to a group more than
    # once per millisecond that is too quickly
    milliseconds = int (round(time.time()*1000))
    generatedGUID = "GUID-" + str(milliseconds)

    # Putting together in a dict
    messageToPost = {"members": [ {"nickname": nickname,
                                    idType: identifier
                                    } ] }    
    print(messageToPost)
    # Assembling the request
    response = requests.post( (standardBeginning + "/" + groupID  + "/members/add?token=" +userToken ), json = messageToPost)

    # Printing response code. Response code key available at https://dev.groupme.com/docs/responses
    # Additional info will be availabe if you print out the entire translated json package
    print(response)

    # It is possible to result in non bmp characters (such as emojiis)
    # Non bmp characters will be mapped to � (oxfffd)
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode +1), 0xfffd)
    jsonInterpretedResponse = json.loads(response.text.translate(non_bmp_map))

    # Printing out entire json resonse package
    if (jsonInterpretedResponse['meta']['code'] < 400):
        # We have a least sent a validly formatted packet and recieved a response
        return()
    else:
        print(jsonInterpretedResponse) 
        raise ValueError("We have a packet with a meta code != 200")
    
def TestAddToGroup():
    # Load in my token, then use that token to add 
    with open("C://Users//Public//Documents//groupmetoken.txt") as f:
        userToken = f.read()
    # Which group to add the member to
    with open("C://Users//Public//Documents//groupmegroupid.txt") as f:
        groupID = f.read()
    # Which user to add to the group
    with open("C://Users//Public//Documents//groupmeuserid.txt") as f:
        userID = f.read()
    AddToGroup(str(userToken),str(groupID),"Test Dummy",str(userID),1)
