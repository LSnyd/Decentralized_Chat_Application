import asyncio


from kademlia.network import Server




def send(port, chatname, username, message):

    node = Server()
    node.listen(port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))

    chat = loop.run_until_complete(node.get(chatname))
    loop.run_until_complete(node.set(chatname,  str(chat) + "\n" + username + ":  " + message + "\n"))
    new_chat = loop.run_until_complete(node.get(chatname))




    node.stop()

    print("************************************************")
    print(chatname)
    print("************************************************")
    print( "\n"+ new_chat + "\n")
    print("************************************************")


