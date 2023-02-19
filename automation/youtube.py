import scrapetube
import requests
import time

time.sleep(10)

playlists = ["PL-lCrD3QqynV3jliSJ1VfUu-4Uf0f6krh", "PL-lCrD3QqynWDYLO6GMzqnZL29y_qe-3v", "PL-lCrD3QqynWOYATxwjTPSc_qr3iWus_a", "PL-lCrD3QqynX2a2sgXZlvxEGssGg9ZTCa", "PL-lCrD3QqynWL0Ve2zqtABq6cE4BwmVvm"]

fastapi_url = "http://api:5000/create_entry"
playlist_url = "http://api:5000/create_playlist"

for playlist in playlists:
    playlist_data = {"id": playlist}
    requests.post(playlist_url, json=playlist_data)

    videos = list(scrapetube.get_playlist(playlist))
    videos.reverse()

    for video in videos:
        video_id = video['videoId']
        title = video["title"].get("runs")[0].get("text")

        data = {
            "video_id": video_id,
            "title": title,
            "playlist_id": playlist
        }
        response = requests.post(fastapi_url, json=data)
