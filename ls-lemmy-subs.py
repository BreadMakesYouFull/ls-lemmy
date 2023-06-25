#!/usr/bin/env python
"""Export lemmy subscriptions

Login as user and export subscriptions.
Could be useful incase your instance goes down,
to share with another user, or to create a bespoke feed.
"""
import argparse
import getpass
import os
import requests
import sys

def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instance", help="Lemmy instance URL")
    parser.add_argument("username", help="Username")
    return parser

def login(instance, username):
    login_url = instance + "/api/v3/user/login"

    # Create a session
    session = requests.Session()

    # Send login request
    login_payload = {
        "username_or_email": username,
        "password": os.getenv("LEMMY_PASS") or getpass.getpass("Enter your password: ")
    }
    response = session.post(login_url, json=login_payload)

    if response.status_code == 200:
        access_token = response.json()["jwt"]
        session.access_token = access_token
        session.headers.update({"Authorization": f"Bearer {access_token}"})
        return session
    else:
        print("Login failed")
        sys.exit(1)

def subscriptions(session, instance):
    subscriptions = []
    for i in range(100):
        query=f"community/list?page={i}&type_=Subscribed&auth={session.access_token}&limit=50"
        user_url = f"{instance}/api/v3/{query}"
        response = session.get(user_url)
        if response.status_code == 200:
            data = response.json()
            communities = [
                    community.get("community", {}).get("actor_id", "")
                    for community
                    in data.get("communities", [])
            ]
            subscriptions.extend(communities)
            if not communities:
                break
    return sorted(subscriptions, key=lambda s: s.split("/")[-1])


def main():
    args = get_parser().parse_args()
    session = login(args.instance, args.username)
    if session:
        print("\n".join(subscriptions(session, args.instance)))


if __name__ == "__main__":
    main()

