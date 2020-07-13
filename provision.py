import pandas
import os
import ast
import twint
import requests


def download(url):
    filename = url.split("/")[-1]
    r = requests.get(url, allow_redirects=True)
    with open("pics/" + filename, "wb") as f:
        f.write(r.content)


# archive @AceYuriBot for images/sources

c = twint.Config()
c.Username = "AceYuriBot"
c.Images = True
c.Store_csv = True
c.Output = "yuribot.csv"
twint.run.Search(c)

os.makedirs("pics", exist_ok=True)
df = pandas.read_csv("yuribot.csv")
source = (
    df["urls"].apply(lambda x: ast.literal_eval(x)).apply(lambda x: x[0] if x else None)
)
file_location = df["photos"].apply(lambda x: os.path.basename(ast.literal_eval(x)[0]))
# save to file where bot will pull data from
pandas.concat([source, file_location], axis=1).to_csv("files.csv")
# download images
df["photos"].apply(lambda x: download(ast.literal_eval(x)[0]))
