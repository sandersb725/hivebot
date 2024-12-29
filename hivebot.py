import time
import scratchconnect
from hugchat import hugchat
from hugchat.login import Login

# You do need to make an account at https://huggingface.co/ to proceed

data_pool = 20 # amount of comments sampled

EMAIL = "email" # change this to your huggingface email
PASSWD = "password" # change this to your huggingface password
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD) 
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

login = scratchconnect.ScratchConnect("username", "password") # change these to your scratch login
studio = login.connect_studio(studio_id=32147244) # you should change the studio number to the studio you want the bot to deploy in

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

while True:
    studio.update_data()
    comments = []

    for x in range(data_pool):
        comments.append(studio.comments(all=False, limit=data_pool, offset=0)[0][x]['content'])
    
    init = f"Speak to me and act like the comments proceeding: {comments}. Make sure you're message is short. Dont use too many caps. Try not to copy other comments. Be as funny as possible. Please avoid serious topics like venting. Be as enthusiatsic and over the top. Don't be too relatable."
    studio.post_comment(content=f"bot generated : {chatbot.chat(init)}")
    time.sleep(45)
