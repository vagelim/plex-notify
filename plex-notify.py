#!/usr/bin/env python2.7
from flask import Flask, request
import json

from keys import API_KEY, USER_KEY

from pushover import Client

client = Client(USER_KEY, api_token=API_KEY)

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def main():
    data = dict(request.form)
    data = data['payload'][0]
    data = dict(json.loads(data))
    print data

    event = data['event']
    user = data['Account']['title']
    server = data['Server']['title']
    show = data['Metadata']['grandparentTitle']
    episode = data['Metadata']['title']
    summary = data['Metadata']['summary']

    title = "{} by {}@{}".format(event, user, server)
    body = "{}-{}\n{}".format(show, episode, summary)
    client.send_message(body, title=title)
    return "OK"

if __name__ == '__main__':
   app.run()
