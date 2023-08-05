import json
import requests

class Cronuseo:

    def __init__(self, endpoint, organization, token):
        
        self.__endpoint = endpoint
        self.__organization = organization
        self.__token = token

    def checkPermission(self,username, action, resource):

        url = f"{self.__endpoint}/{self.__organization}/permission/check"
        data = json.dumps({"username": username, "action": action, "resource": resource})
        try: 
            response = requests.post(url, 
                                data= data, 
                                headers={"API_KEY": f"{self.__token}",
                                        "Content-Type": "application/json"}
                            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)