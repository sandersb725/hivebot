import time
import scratchconnect
from hugchat import hugchat
from hugchat.login import Login

EMAIL = "bus120610@gmail.com"
PASSWD = "N&YPr3kWr(6dVSm"
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

login = scratchconnect.ScratchConnect("atoke-bf", "N&YPr3kWr(6dVSm")
studio = login.connect_studio(studio_id=32147244)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

while True:
    studio.update_data()
    comments = []

    for x in range(20):
        comments.append(studio.comments(all=False, limit=20, offset=0)[0][x]['content'])
    
    init = f"Speak to me and act like the comments proceeding: {comments}. Make sure you're message is short. Dont use too many caps. Try not to copy other comments. Be as funny as possible. Please avoid serious topics like venting. Be as enthusiatsic and over the top. Don't be too relatable."
    #print(chatbot.chat(init))
    studio.post_comment(content=f"bot generated : {chatbot.chat(init)}")
    time.sleep(45)