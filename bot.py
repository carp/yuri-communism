from utils import (
    draw_with_border,
    get_colors,
    get_quote,
    messages_multiline,
    randomize_location,
    set_font,
)
from PIL import Image, ImageDraw
from twython import Twython
import csv
import random
import os
from api import consumer_key, consumer_secret, access_token, access_token_secret
from datetime import datetime
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


def post():
    with open("files.csv") as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        source = chosen_row[1]
        file_extension = chosen_row[2].split(".")[1]
        filename = "pics/" + chosen_row[2]

    text = get_quote("texts/quotes.txt")
    image = Image.open(filename)
    font = set_font(image, text)  # get font size based on image size
    draw = ImageDraw.Draw(image)
    lines = messages_multiline(text, font, image)  # split up lines for text wrapping
    colors = get_colors(image.filename)  # get colors

    (x, y,faces) = randomize_location(image, lines, font)  # where to start drawing text

    for line in lines:
        height = font.getsize(line[1])[1]
        draw_with_border(x, y, line, colors[0], colors[1], font, draw)
        y = y + height

    image.save(f"to_tweet.{file_extension}")
    photo = open(f"to_tweet.{file_extension}", "rb")
    response = twitter.upload_media(media=photo)
    message = f"{text} ({source})"
    print(filename, message)
    twitter.update_status(status=message, media_ids=[response["media_id"]])
    photo.close()
    os.remove(photo.name)
    with open("log","a") as f:
        f.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\t{filename}\t({image.size[0]} {image.size[1]})\t{font.size} ({max((font.size // 25), 2)})\t{text}\n")

post()
