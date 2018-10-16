import requests
import json
import sys
def ViewCurrentGroups(userToken):
    # Standard start for the request string for the GroupMe API
    standardBeginning = "https://api.groupme.com/v3/groups"

    # GroupMe API Defines maximum per_page value as 500. We use this value.
    inputParameters = { "per_page" : 500 , "omit" : "memberships"  }

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
    print(jsonInterpretedResponse)
    print(jsonInterpretedResponse['response'][0]) 

def TestViewCurrentGroups():
    with open("C://Users//Public//Documents//groupmetoken.txt") as f:
        data = f.read()
    ViewCurrentGroups(data)


TestViewCurrentGroups()

