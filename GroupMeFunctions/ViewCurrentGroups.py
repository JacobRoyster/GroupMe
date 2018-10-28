import requests
import json
import sys
"""
userToken should be a valid GroupMe  user token. (string)
purpose of this function is to get information for all of the groups the user that corresponds with the user token is in
"""
def ViewCurrentGroups(userToken):
    # Standard start for the request string for the GroupMe API
    standardBeginning = "https://api.groupme.com/v3/groups"

    # GroupMe API Defines maximum per_page value as 500. We use this value.
    inputParameters = { "per_page" : 500   }

    # Assembling the request
    response = requests.get((standardBeginning + "?token=" + userToken), params = inputParameters )

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
        return(jsonInterpretedResponse['response'])
    else:
        print(jsonInterpretedResponse) 
        raise ValueError("We have a packet with a meta code != 200")

def TestViewCurrentGroups():
    # Load in my token, then use that token to view the groups
    with open("C://Users//Public//Documents//groupmetoken.txt") as f:
        data = f.read()
    # Should have an array of the dicts for the first 500 groups
    returnedArrayOfDicts = ViewCurrentGroups(data)
    print("Full data for all groups")
    for i in range(len(returnedArrayOfDicts)):
        print(returnedArrayOfDicts[i])
    print("Names of all groups")
    for i in range(len(returnedArrayOfDicts)):
        print(returnedArrayOfDicts[i]['name'])
