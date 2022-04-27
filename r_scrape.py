import praw
import pandas as pd
import json

r = praw.Reddit(client_id="<YOUR_CLIENT_ID_HERE>",
                client_secret="<YOUR_CLIENT_SECRET_HERE>",
                user_agent="<YOUR_USER_AGENT>",
                )


# search parameters
q='bitcoin'
sub='CryptoCurrency'
sort = "top"
limit = 50


top_posts = r.subreddit(sub).search(q, sort=sort, limit=limit)

print('TYPE', type(top_posts.params))

total_posts = list()

count=0
for post in top_posts:
    # print('type', vars(post)) # print all properties
    Title=post.title,
    Score = post.score,
    Number_Of_Comments = post.num_comments,
    Publish_Date = post.created,
    Link = post.permalink,
    count=count+1
    data_set = {"Count":count,"Title":Title[0],"Score":Score[0], "Number_Of_Comments":Number_Of_Comments[0],"Publish_Date":Publish_Date[0],"Link":'https://www.reddit.com'+Link[0]}
    total_posts.append(data_set)

# create csv file
df = pd.DataFrame(total_posts)
df.to_csv('data.csv', sep=',', index=False)

#create json file
json_string = json.dumps(total_posts)
jsonFile = open("data.json", "w")
jsonFile.write(json_string)
jsonFile.close()









