import os
import telethon
from telethon.sync import TelegramClient
from telethon import functions
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors import SessionPasswordNeededError
import getpass
import time
from telethon import errors
list_accounts=[]
def random_username():
    user=""
    string="qwertyuiopasdfghjklzxcvbnm1234567890"
    number="123456798"
  
    for i in range(10):
        user=string[random.randint(0,len(string)-1)]+user
        
    print(user)
    try:
        client(UpdateUsernameRequest(user))
    except:
        print("error username")
        try:
            for i in range(10):
                user=number[random.randint(0,len(number)-1)]+user
            client(UpdateUsernameRequest(user))
        except:
            print(user)
            print("error 2")
def get_msg():
    for chat in client.iter_dialogs():
        getmessage = client.get_messages(chat.id, limit=1)
        if(chat.name=="Telegram"):
            for message in getmessage:
                print(message.message)

api_id ="11240336"
api_hash ="55a5f408129ae4208dabfe5ca9bffe75"
phone ="+5547984290160"
def check_all_bots():
    with open("old_phones","+r") as e:
       for i in e.readlines():
           try:
            print(i)
            client = TelegramClient(i.strip("\n").split(":")[0], i.strip("\n").split(":")[1], i.strip("\n").split(":")[2])
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(phone)
                client.sign_in(phone)
                try:
                        client.sign_in(code=input('Enter code: '))
                except SessionPasswordNeededError:
                        client.sign_in(password="dali123")
                
            print("succesfly connected to ",i.strip("\n").split(":")[0])
            list_accounts.append(i)
           except errors.PhoneNumberBannedError as e:
            print(e)
            print("phone banned ",i.strip("\n").split(":")[0])            
           time.sleep(5)
       
        
       
       print("done")
       with open("phones.txt","+w") as f:
        for i in list_accounts:
           f.write(i)
            
            
           
    

# Your Api ID
# Your Api Hash
# Your Phone Number With Country Code.

client = TelegramClient(phone, api_id, api_hash)
client.connect()

chats = []
last_date = None
chunk_size = 1000
groups = []
empty=""
dc=0

def send_msg_to_group():
    d = ""
    messa=""
    count = 0
    # msg1=open("msg.txt","+r")

    for dialog in client.iter_dialogs():
        ##print(dialog.title)
            if dialog.title=="poorguy marketplace":
                print("found")
                messa=client.get_messages(dialog.id,limit=1)
                print(messa)
                input()

    while True:
        count = count + 1
        
        print("cycle number " + str(count))
        for dialog in client.iter_dialogs():
            if dialog.title=="CHinatown v1.1":
                pass
            else:
                try:
                    print(messa)
                    client.forward_messages(client.get_entity(dialog.id),messages=messa)
                    print(f'Sent==> {dialog.title}')
                    time.sleep(int(t1))

                except errors.FloodWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds')
                    time.sleep(e.seconds+800)
                except errors.ChatWriteForbiddenError as e:
                    print("frobiden to write in ",dialog.title)
                except errors.UserBannedInChannelError as e :
                    print("banned")
                except errors.SlowModeWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds')
                    time.sleep(e.seconds)
                except errors.ChatAdminRequiredError as e:
                    pass
                except errors.InputUserDeactivatedError as e:
                    pass
                except errors.UsernameInvalidError as e:
                    pass
                
                
                
            print("waiting the timeout")
            time.sleep(int(t2))


def group_scanner():
    chats = []
    last_date = None
    chunk_size = 1000
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=3000,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=3000
    ))
    chats.extend(result.chats)
    f2 = open("groups.txt", "a")
    d = 0
    test = []
    for chat in chats:
        if chat.title not in test:
            try:
                # print(chat)
                test.append(chat.title)

                f2.write(str(chat.title) + '\n')

                # if chat.megagroup== True:
            except:
                continue

    f2.close()

def inv():
    file = open("groups.txt", "+r")
    test=""
    for x in file:
        try:

            name = client.get_entity(x)
            
            d = (client(functions.channels.JoinChannelRequest(name)))
            print("added ==>" + x)
            time.sleep(50)
        except errors.FloodWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds')
                    time.sleep(e.seconds+800)
        except errors.ChatWriteForbiddenError as e:
                    print("frobiden to write in ",x)
        except errors.UserBannedInChannelError as e :
                    print("banned")
        except errors.SlowModeWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds')
                    time.sleep(e.seconds)
        except errors.ChatAdminRequiredError as e:
                    pass
        except errors.InputUserDeactivatedError as e:
                    pass
        except errors.ChannelPrivateError as e:
                    pass
        except errors.UsernameNotOccupiedError as e:
                    pass
        except errors.UsernameNotOccupiedError as e:
                    pass


# print(str(i) + '- ' + g.title)
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone)
    try:
        client.sign_in(code=input('Enter code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=getpass())

t1 = 5
t2 = 10
def menu():
    print("""choose what options \n 
          1-join groups \n
          2- forward msg \n
          3- get last msg from telegram\n
          4- change to ramdom username\n
          """)
    a=input("please choose a options")
    if a=='1':
        inv()
    if a=='2':
        send_msg_to_group()
    if a=='3':
        get_msg()
    if a=='4':
        random_username()


menu()
