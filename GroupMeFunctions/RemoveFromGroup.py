import requests
import json
import sys
"""
userToken should be a valid GroupMe  user token. (string)
groupID should be a valid group that you have access to. (string)
userID should be a valid ID for the user you want to remove. If this userID is yours, you leave the group. (string)
purpose of this function is to remove someone (including yourself) from a group.
"""
def RemoveFromGroup(userToken, groupID, userID):
    # Standard start for the request string for the GroupMe API
    standardBeginning = "https://api.groupme.com/v3/groups"

    # Assembling the request
    response = requests.post( (standardBeginning + "/" + groupID  + "/members/" + userID +"/remove?token=" +userToken ) )

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

def TestRemoveFromGroup():
    # Load in my token, then use that token to view the groups
    with open("C://Users//Public//Documents//groupmetoken.txt") as f:
        userToken = f.read()
    with open("C://Users//Public//Documents//groupmegroupid.txt") as f:
        groupID = f.read()
    with open("C://Users//Public//Documents//groupmetestdummyid.txt") as f:
        testdummyid = f.read()
    RemoveFromGroup(str(userToken),str(groupID),str(testdummyid))
