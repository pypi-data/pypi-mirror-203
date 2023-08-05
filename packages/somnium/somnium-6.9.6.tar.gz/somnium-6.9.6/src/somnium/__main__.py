import json
import time
import requests

#Main class
class Somnium():
    """"Somnium class
    
    Somnium objects are responsible of Generating artworks & getting artstyles.
    
    Available options:
        - Styles(): --> list                 Get all art-styles list.
        - Generate(prompt, style): --> url   Generate Artwork using prompt.
    Example:
        - Somnium.Generate('Girl', 79)
    """
    #Get All Styles
    @classmethod
    def Styles(cls):
        r = requests.get("https://paint.api.wombo.ai/api/styles")
        return {style["name"]: style["id"] for style in r.json() if not style["is_premium"]}

    #Generate Art
    @classmethod
    def Generate(cls, text: str, style: int):
        #FireBase
        s = requests.Session()
        API = "AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw"
        api_header = {"Content-Type": "application/json", "x-goog-api-key": API}
        api_json = {"appId": "1:181681569359:web:277133b57fecf57af0f43a", "authVersion": "FIS_v2", "sdkVersion": "w:0.5.1"}
        r = s.post("https://firebaseinstallations.googleapis.com/v1/projects/paint-prod/installations", headers=api_header, json=api_json)
        r2 = s.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API}")
        Token = r2.json()['idToken'] if r.status_code == 200 else None
        
        #Headers
        headers = {
            'authority': 'paint.api.wombo.ai',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authorization': f'bearer {Token}',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://dream.ai',
            'referer': 'https://dream.ai/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
            'x-app-version': 'WEB-1.90.1',
        }
        
        data = {
            "is_premium": False,
            "input_spec": {
                "prompt": text,
                "style": style,
                "display_freq": 10
            }
        }
        
        gen_response = requests.post('https://paint.api.wombo.ai/api/v2/tasks', headers=headers, data=json.dumps(data))

        try:
            image_id = gen_response.json()["id"]
            for i in range(10):
                response = requests.get(f'https://paint.api.wombo.ai/api/v2/tasks/{image_id}', headers=headers)
                time.sleep(3)
                try:
                    img = response.json()["result"]["final"]
                    return img
                    break
                except:
                    continue
        except Exception as e:
            return 'Process failed or contains NSFW.'
