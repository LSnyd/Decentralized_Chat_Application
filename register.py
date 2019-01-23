import logging
import asyncio
import sys
import datetime

from kademlia.network import Server



def user(port, username):

    node = Server()
    node.listen(port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))


    userlist = loop.run_until_complete(node.get("userlist"))
    loop.run_until_complete(node.set("userlist",  str(userlist) + "\n" + username + "\n"))


    node.stop()


def chat(port, chatname):

    node = Server()
    node.listen(port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.bootstrap([("0.0.0.0", 8468)]))


    chatlist = loop.run_until_complete(node.get("chatlist"))
    loop.run_until_complete(node.set("chatlist",  str(chatlist) + "\n" + chatname + "\n"))


    node.stop()






