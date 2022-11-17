def solution(id_pw, db):
    _id = id_pw[0]
    _pw = id_pw[1]
    
    for i in range(len(db)) :
        if db[i][0] == _id :
            if db[i][1] == _pw :
                return "login"
            else :
                return "wrong pw"

    return "fail"