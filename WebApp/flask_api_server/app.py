import json
import random

from flask import Flask, request
from flask_cors import CORS, cross_origin

sessions: dict = {

}

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/register')
@cross_origin()
def register():
    post_body = request.get_json()
    users = json.loads(open('static/users.json').read())
    if any(user['email'] == post_body['email'] for user in users):
        return {"success": False, "error": "E-Mail already registered.", "code": 1}
    if any(user['username'] == post_body['username'] for user in users):
        return {"success": False, "error": "Username already exists.", "code": 2}
    post_body['id'] = len(users) + 1
    users.append(post_body)
    with open('static/users.json', 'w') as f:
        f.write(json.dumps(users, indent=4))
    if post_body['username'] in sessions.values():
        # session already exists. session is key, username is value
        session = list(sessions.keys())[list(sessions.values()).index(post_body['username'])]
        print(session)
        return {'session': session}
    else:
        # create new session
        sessions[str(random.randint(1000000, 9999999))] = post_body['username']
    session = list(sessions.keys())[list(sessions.values()).index(post_body['username'])]
    print(session)
    return {'session':session}

@app.post('/login')
@cross_origin()
def login():
    print('login')
    post_body = request.get_json()
    users = json.loads(open('static/users.json').read())
    for user in users:
        if user['username'] == post_body['username'] and user['password'] == post_body['password']:
            if post_body['username'] in sessions.values():
                # session already exists. session is key, username is value
                session = list(sessions.keys())[list(sessions.values()).index(post_body['username'])]
                print(session)
                return {'session': session}
            else:
                # create new session
                sessions[str(random.randint(1000000, 9999999))] = post_body['username']
            session = list(sessions.keys())[list(sessions.values()).index(post_body['username'])]
            print(session)
            return {'session': session}
    return {"success": False, "error": "No User found", "code": 3}

@app.post('/logout')
@cross_origin()
def logout():
    print('logout')
    post_body = request.get_json()
    session = post_body['session']
    print(session)
    # remove session
    if session in sessions.keys():
        sessions.pop(session)
        return {'success':True}

@app.post('/cameras')
@cross_origin()
def cameras():
    print('cameras')
    post_body = request.get_json()
    print(post_body)
    session = post_body['session']
    if session not in sessions.keys():
        return {"success": False, "error": "Unauthorized", "code": 4}
    print(session)
    cameras = json.loads(open('static/cameras.json', encoding='utf-8').read())
    users= json.loads(open('static/users.json', encoding='utf-8').read())
    owned_cameras = list(filter(lambda user: user['username'] ==sessions[post_body['session']], users))[0]['cameras']
    print(owned_cameras)
    return {'cameras': list(filter(lambda camera: camera['id'] in owned_cameras, cameras))}

@app.post('/camera/<int:id>')
@cross_origin()
def camera(id:int):
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        return {"success": False, "error": "Unauthorized", "code": 4}
    cameras = json.loads(open('static/cameras.json').read())
    users= json.loads(open('static/users.json').read())
    owned_cameras = list(filter(lambda user: user['username'] ==sessions[post_body['session']], users))[0]['cameras']
    if id not in owned_cameras:
        return {"success": False, "error": "Unauthorized", "code": 4}
    return list(filter(lambda camera: camera['id'] == id, cameras))[0]

@app.post('/advancedSettings')
@cross_origin()
def advancedSettings():
    """
    Bleiben die gleich für alle Kameras? weil dann kann man die ID sich sparen.
    :return:
    """
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        print("not in keys")
        print(session)
        print(sessions.keys())
        return {"success": False, "error": "Unauthorized", "code": 4}
    camera_id = post_body['id']
    users = json.loads(open('static/users.json').read())
    owned_cameras = list(filter(lambda user: user['username'] == sessions[post_body['session']], users))[0]['cameras']
    if camera_id not in owned_cameras:
        print("not in owned cameras")
        return {"success": False, "error": "Unauthorized", "code": 4}
    return json.loads(open('static/advancedSettings.json').read())

@app.put('/advancedSettings')
@cross_origin()
def advancedSettingsPut():
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        return {"success": False, "error": "Unauthorized", "code": 4}
    camera_id = post_body['id']
    users = json.loads(open('static/users.json').read())
    owned_cameras = list(filter(lambda user: user['username'] == sessions[post_body['session']], users))[0]['cameras']
    if camera_id not in owned_cameras:
        return {"success": False, "error": "Unauthorized", "code": 4}

    advanced_settings = json.loads(open('static/advancedSettings.json').read())
    # omg ist das schiach
    for section in post_body['settings']:
        section_name = section['sectionName']
        section_settings = {setting['name']: setting['value'] for setting in section['sectionSettings']}

        for advanced_section in advanced_settings:
            if advanced_section['sectionName'] == section_name:
                for advanced_setting in advanced_section['sectionSettings']:
                    if advanced_setting['name'] in section_settings:
                        advanced_setting['value'] = section_settings[advanced_setting['name']]

    # nicht gut, sollte für alle getrennt sein
    # keine lust es umzusetzen
    with open('static/advancedSettings.json', 'w') as f:
        f.write(json.dumps(advanced_settings, indent=4))
    return {"succsess": True}

@app.post('/imageSearchSettings')
@cross_origin()
def imageSearchSettings():
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        return {"success": False, "error": "Unauthorized", "code": 4}
    users = json.loads(open('static/users.json').read())
    owned_cameras = list(filter(lambda user: user['username'] ==sessions[post_body['session']], users))[0]['cameras']
    print(owned_cameras)
    # get names for the cameras
    cameras = json.loads(open('static/cameras.json', encoding='utf-8').read())
    camera_names = list(map(lambda camera: camera['name'], list(filter(lambda camera: camera['id'] in owned_cameras, cameras))))
    print(camera_names)
    bare_settings:dict= json.loads(open('static/imageSearchSettings.json').read())
    l= [json.loads('''{
    "type": "boolean",
    "name": "'''+str(x)+'''",
    "value": true,
    "required": true
  }''') for x in camera_names]
    print(l)
    bare_settings[1]['sectionSettings'] = l
    print(bare_settings)
    return bare_settings

@app.post('/imageSearch')
@cross_origin()
def imageSearch():
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        return {"success": False, "error": "Unauthorized", "code": 4}
    imageSearchSettings= post_body['imageSearchSettings']
    page= post_body['page']
    print(imageSearchSettings)
    print(page)
    # wow
    if page==0:
        return json.loads(open('static/images.json', encoding='utf-8').read())
    else:
        return json.loads(open('static/images2.json', encoding='utf-8').read())
    # return json.loads(open('static/images.json', encoding='utf-8').read())

@app.post('/checkSession')
@cross_origin()
def checkSession():
    post_body = request.get_json()
    session = post_body['session']
    if session not in sessions.keys():
        print('Unauthorized')
        return {"success": True, "authorized": False}
    return {"success": True, "authorized": True}


if __name__ == '__main__':
    app.run()
