import logging
import threading
import time
import simplejson as json
from django.conf import settings
from channels import Group
from channels import Channel
from channels.sessions import channel_session, enforce_ordering
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import views
import sweetify

# Django Matchmaking Engine

# Get an instnace of a logger
logger = logging.getLogger(__name__)

# Connect to websocket.connect
@enforce_ordering
@channel_session
@channel_session_user_from_http
def ws_connect(message):
    # Work out game name from path (ignore slashes)
    game = message.content['path'].strip("/")
    session_id = message.channel_session.session_key
    reply_channel = message.reply_channel
    http_user = message.user

    #log name of game
    logger.info('path: ' + message.content['path'])
    logger.info('game name: ' + game)

    # Save game in session and add us to the group
    message.channel_session['game'] = game
    Group("chat-%s" % game).add(message.reply_channel)

    settings.MATCH_MAKING_QUEUE.append({'session': session_id,
                                      'game': game,
                                      'reply_channel': reply_channel,
                                      'user': http_user})

    reply_channel.send({'text': 'Finding players...'})

    # Get the user information to display via json
    reply_channel.send({'text': json.dumps({
            'imageurl': http_user.profile.image.url,
            'rank': http_user.profile.rank,
            "username": http_user.username,
            'membersince': http_user.date_joined.year,
            'wins': http_user.profile.wins,
            'losses': http_user.profile.losses,
            'wlratio': http_user.profile.wlratio,
            'kills': http_user.profile.kills,
            'deaths': http_user.profile.deaths,
            'kdratio': http_user.profile.kdratio,
        }, use_decimal=True),
    })


    # whenever a user connects, check if we have 10 users to start a given game
    matching_players = []
    for player in settings.MATCH_MAKING_QUEUE:
        if player['game'] == game:
            matching_players.append(player)


    # Length of queue
    if len(matching_players) >= 10:
        make_match(matching_players)




# Connected to websocket.receive
@enforce_ordering
@channel_session
@channel_session_user
def ws_message(message):
    # TODO: if it's polling message, check if the user is already in queue
    # TODO: if so, check if we have 10 users to start a given game
    # TODO: if so send both a message and remove them from queue
    # TODO: else do nothing
    Group("chat-%s" % message.channel_session['game']).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
# @enforce_ordering(slight=True)
@enforce_ordering
@channel_session
@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['game']).discard(message.reply_channel)

    # remove user from matchmaking queue in case of disconnect
    session_id = message.channel_session.session_key
    reply_channel = message.reply_channel
    try:
        settings.MATCH_MAKING_QUEUE.remove({'session': session_id,
                                            'game': message.channel_session['game'],
                                            'reply_channel': reply_channel})
    except:
        # the user might have been removed because the game started
        logger.info('Item already removed from matchmaking queue')


# declare synchronized decorator
def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


# synchronized match making function
@synchronized
def make_match(matching_players):
    for indx, player in enumerate(matching_players):
        if indx < 10:
            # take first 10 matching players out of queue
            settings.MATCH_MAKING_QUEUE.remove(player)
            # send game starting message
            player['reply_channel'].send({'text': 'Players found! The match is about to start...'})
