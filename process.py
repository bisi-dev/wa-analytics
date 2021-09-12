# import modules
import os
import re
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


class Analyse:

    # Data Cleaning Function
    def raw_to_df(self, file, key):
        global df

        # Time formatting
        split_formats = {
            "12hr": "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[APap][mM]\s-\s",
            "24hr": "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s",
            "custom": "",
        }

        datetime_formats = {
            "12hr": "%m/%d/%y, %I:%M %p - ",
            "24hr": "%m/%d/%y, %H:%M - ",
            "custom": "",
        }

        with open(file, "r", encoding="utf8") as raw_data:

            # Converting the list split by newline char as one whole string
            # As there can be multi-line messages
            raw_string = " ".join(raw_data.read().split("\n"))

            # Splits at all the date-time pattern,
            # resulting in list of all the messages with user names
            user_msg = re.split(split_formats[key], raw_string)[1:]

            # Finds all the date-time patterns
            date_time = re.findall(split_formats[key], raw_string)

            # Export it to a df
            df = pd.DataFrame({"date_time": date_time, "user_msg": user_msg})

        # Converting date-time pattern which is of type String to datetime,
        # Format is to be specified for the whole string
        # where the placeholders are extracted by the method
        df["date_time"] = pd.to_datetime(
            df["date_time"], format=datetime_formats[key]
        )

        # Split user and msg
        usernames = []
        msgs = []
        for i in df["user_msg"]:

            # Lazy pattern match to first {user_name}
            # pattern and splitting each msg from a user
            a = re.split("([\w\W]+?):\s", i)

            # User typed messages
            if a[1:]:
                usernames.append(a[1])
                msgs.append(a[2])

            # Other notifications in the group(someone was added, some left...)
            else:
                usernames.append("grp_notif")
                msgs.append(a[0])

        # Creating new columns
        df["user"] = usernames
        df["msg"] = msgs

        # Dropping the old user_msg col.
        df.drop("user_msg", axis=1, inplace=True)

        # Group Notifications
        grp_notif = df[df["user"] == "grp_notif"]

        # Media
        # no. of images, images are represented by <media omitted>
        media = df[df["msg"] == "<Media omitted> "]

        # removing images
        df.drop(media.index, inplace=True)

        # removing grp_notif
        df.drop(grp_notif.index, inplace=True)

        # Reset Index
        df.reset_index(inplace=True, drop=True)

        return df

    # Function to get total sum of messages in chat.
    def messages_count(self):
        return df.shape[0] - 1

    # Function to get total sum of people with message frequency in chat.
    def users_count(self):
        msgs_per_user = df["user"].value_counts(sort=True)
        df2 = msgs_per_user.to_frame()
        df2.rename({"user": "FREQUENCY"}, axis=1, inplace=True)

        return (df2.shape[0], df2)

    # Function uses Wordcloud lib to create infographics on words used in chat.
    def infographics(self):

        # Version Control - Keep Directory Clean for repeated usage in server
        # Check for Last Image file
        list_of_files = glob.glob("./static/data/*.png")
        latest_file = max(list_of_files, key=os.path.getctime)

        # Get Filename without extension
        basename, fileext = os.path.splitext(latest_file)

        # Increase count
        current = basename[14:]
        v = re.findall("[0-9]+", current)
        version = int(v[0])
        version += 1
        version = str(version)

        # Rename it
        current = re.sub("\d+", "", current)
        current_file = current + version + fileext

        # Delete Previous File
        os.remove(latest_file)

        # Comment out all previous code and switch to remove V.C
        # current_file = "test.png"

        comment_words = " "

        for val in df.msg.values:
            val = str(val)
            tokens = val.split()

            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()

            for words in tokens:
                comment_words = comment_words + words + " "

        wordcloud = WordCloud(
            width=800, height=800, background_color="black", min_font_size=10
        ).generate(comment_words)

        wordcloud.to_file("./static/data/" + current_file)

        return current_file
