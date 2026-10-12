#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder."""
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status code and titles."""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body to posts.csv."""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = [
            {"id": p["id"], "title": p["title"], "body": p["body"]}
            for p in response.json()
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
