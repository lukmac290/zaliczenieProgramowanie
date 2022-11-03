import jwt

def GenerateToken():
    payload_data = {
        "sub": "6340",
        "name": "Zaliczenie Programowanie",
        "nickname": "LM"
    }
    token = jwt.encode(payload = payload_data, key = 'top_secret')
    return token