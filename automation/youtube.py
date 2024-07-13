import scrapetube
import requests
import time

time.sleep(10)

playlists = ["PLNVqeXDm5tIqUIPQHLk5Xw5mpisruvsac"]

fastapi_url = "http://api:5000/create_entry"
playlist_url = "http://api:5000/create_playlist"

for playlist in playlists:
    playlist_data = {"id": playlist}
    requests.post(playlist_url, json=playlist_data)

    videos = list(scrapetube.get_playlist(playlist))
    videos.reverse()

    for video in videos:
        video_id = video["videoId"]
        title = video["title"].get("runs")[0].get("text")

        data = {"video_id": video_id, "title": title, "playlist_id": playlist}
        response = requests.post(fastapi_url, json=data)
