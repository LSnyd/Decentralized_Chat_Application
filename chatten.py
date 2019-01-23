import asyncio
import send
import register

from kademlia.network import Server



def new_user():

    username = input("Please type in a username  ")
    new_userlist = loop.run_until_complete(node.get("userlist"))

    if new_userlist is None:
        new_userlist = "   "
    else:
        new_userlist = new_userlist

    if username in new_userlist:
        print("Your username is taken, please choose a different username")
        new_user()

    else:

        register.user(port, username)
        return username


def new_chat():

    chatname = input("Enter a name for your chat  ")
    new_chatlist = loop.run_until_complete(node.get("chatlist"))


    if new_chatlist is None:
            new_chatlist = "   "
    else:
        new_chatlist = new_chatlist

    if chatname in new_chatlist:
        print("The chat is already existing. Please choose a different chatname")
        new_chat()

    else:
        print("We are creating chat " + chatname)
        register.chat(port, chatname)
        loop.run_until_complete(node.set(chatname, " "))

        return chatname

def join_chat():

    print("You can join the following chats:")
    chatlist = loop.run_until_complete(node.get("chatlist"))


    if chatlist is None:
            print("Their are no chats available. Please create a new one")
            new_chat()

    else:
        print(chatlist)

    joinchat = input("Which chat do you want to join? ")

    if joinchat  in chatlist:
        print("Just type a message to join the chat")

        return joinchat

    else:

        print("The chat is not existing.")
        join_chat()



f = open('chat.txt','r')
stars = f.read()

print(stars)
port = input("Please enter a port ")
join = input("To create a new chat: Type 'new'\nTo join an exisitng chat: Type 'join'\n")


if join == "new":

    # create node, listen to input port
    node = Server()
    node.listen(port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))


    username = new_user()
    chatname = new_chat()
    

    while 1:
        message = input(username + ": >>> ")
        send.send(port, chatname, username, message)





else:
    # create node, listen to input port

    node = Server()
    node.listen(port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))


    username = new_user()
    chatname = join_chat()


    while 1:

        message = input(username + ": >>> ")
        send.send(port, chatname, username, message)
