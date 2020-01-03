data = {
  "pranav3nov@gmail.com": "264976",
  "b.dubey1111@gmail.com": "739768",
  "abhivyakti128@gmail.com": "192798" ,
  "parthsethi1998@gmail.com": "777833",
  "cinekala.jiit128@gmail.com" : "594977",
  "goyal.jahanvi@gmail.com": "424870",
  "princebest3@rediffmail.com": "030535",
  "fortissimojiit128@gmail.com": "332111",
  "ashitagoel10@gmail.com": "247889",
}

def checkPassword(email, password):
  try:
    if data[email] == password:
      return True
    else:
      return False
  except:
    return False