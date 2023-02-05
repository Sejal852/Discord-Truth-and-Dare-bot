# To be implemented with the help of replit

import os
import discord
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

starter_truth = []

starter_dare = ["go and drink water"]

starter_wyd = []

starter_nhie = []


def update_truth(truth_message):
    if "truth" in db.keys():
        truth = db["truth"]
        truth.append(truth_message)
        db["truth"] = truth
    else:
        db["truth"] = [truth_message]


def update_dare(dare_message):
    if "dare" in db.keys():
        dare = db["dare"]
        dare.append(dare_message)
        db["dare"] = dare
    else:
        db["dare"] = [dare_message]


def update_wyd(wyd_message):
    if "wyd" in db.keys():
        wyd = db["wyd"]
        wyd.append(wyd_message)
        db["wyd"] = wyd
    else:
        db["wyd"] = [wyd_message]


def update_nhie(nhie_message):
    if "nhie" in db.keys():
        nhie = db["nhie"]
        nhie.append(nhie_message)
        db["nhie"] = nhie
    else:
        db["nhie"] = [nhie_message]


def delete_truth(index):
    truth = db["truth"]
    if len(truth) > index:
        del truth[index]
        db["truth"] = truth


def delete_dare(index):
    dare = db["dare"]
    if len(dare) > index:
        del dare[index]
        db["dare"] = dare


def delete_wyd(index):
    wyd = db["wyd"]
    if len(wyd) > index:
        del wyd[index]
        db["wyd"] = wyd


def delete_nhie(index):
    nhie = db["nhie"]
    if len(nhie) > index:
        del nhie[index]
        db["nhie"] = nhie


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    #start for the code of true command

    options = starter_truth
    if "truth" in db.keys():
        options = options + list(db['truth'])

    if msg.startswith(".true"):
        await message.channel.send(random.choice(options))

    if msg.startswith(".addingtrue"):
        truth_message = msg.split(".addingtrue ", 1)[1]
        update_truth(truth_message)
        await message.channel.send("Your message added.")

    if msg.startswith(".deltruth"):
        truth = []
        if "truth" in db.keys():
            index = int(msg.split(".deltruth", 1)[1])
            delete_truth(index)
            truth = db["truth"]
        await message.channel.send(truth)

    if msg.startswith(".tlist"):
            truth = []
            if "truth" in db.keys():
                truth = db["truth"]
            await message.channel.send(truth)
#start for the code of dare command
    optiond = starter_dare
    if "dare" in db.keys():
        optiond = optiond + list(db['dare'])

    if msg.startswith(".addingdare"):
        dare_message = msg.split(".addingdare", 1)[1]
        update_dare(dare_message)
        await message.channel.send("Your message added.")

    if msg.startswith(".dare"):
        await message.channel.send(random.choice(optiond))

    if msg.startswith(".deldare"):
        dare = []
        if "dare" in db.keys():
            index = int(msg.split(".deldare", 1)[1])
            delete_dare(index)
            dare = db["dare"]
        await message.channel.send(dare)

    if msg.startswith(".dlist"):
        dare = []
        if "dare" in db.keys():
            dare = db["dare"]
        await message.channel.send(dare)

#Start of would you rather command

    optionw = starter_wyd
    if "wyd" in db.keys():
        optionw = optionw + list(db['wyd'])

    if msg.startswith(".wyr"):
        await message.channel.send(random.choice(optionw))

    if msg.startswith(".awyd"):
        wyd_message = msg.split(".awyd ", 1)[1]
        update_wyd(wyd_message)
        await message.channel.send("Your message added.")

    if msg.startswith(".delwyd"):
        wyd = []
        if "wyd" in db.keys():
            index = int(msg.split(".delwyd", 1)[1])
            delete_wyd(index)
            wyd = db["wyd"]
        await message.channel.send(wyd)

    if msg.startswith(".wlist"):
        wyd = []
        if "wyd" in db.keys():
            wyd = db["wyd"]
        await message.channel.send(wyd)


#Start of would you rather command

    optionn = starter_wyd
    if "nhie" in db.keys():
        optionn = optionn + list(db['nhie'])

    if msg.startswith(".nhie"):
        await message.channel.send(random.choice(optionn))

    if msg.startswith(".anhie"):
        nhie_message = msg.split(".anhie ", 1)[1]
        update_nhie(nhie_message)
        await message.channel.send("Your message added.")

    if msg.startswith(".delnhie"):
        nhie = []
        if "nhie" in db.keys():
            index = int(msg.split(".delnhie", 1)[1])
            delete_nhie(index)
            nhie = db["nhie"]
        await message.channel.send(nhie)

    if msg.startswith(".nlist"):
        nhie = []
        if "nhie" in db.keys():
            nhie = db["nhie"]
        await message.channel.send(nhie)

#help
    if msg.startswith(".help"):
       await message.channel.send("  .true to get truth \n .dare to get dare \n .wyr to get woukd you rather \n .nhie to get never have i ever")
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
