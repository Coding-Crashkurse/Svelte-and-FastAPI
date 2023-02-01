import scrapetube
import requests

playlists = ["PL-lCrD3QqynWOYATxwjTPSc_qr3iWus_a", "PL-lCrD3QqynX2a2sgXZlvxEGssGg9ZTCa", "PL-lCrD3QqynWL0Ve2zqtABq6cE4BwmVvm", "PL-lCrD3QqynWDYLO6GMzqnZL29y_qe-3v"]

videos = scrapetube.get_playlist("PL-lCrD3QqynWOYATxwjTPSc_qr3iWus_a")
fastapi_url = "http://127.0.0.1:4000/create_entry"
playlist_url = "http://127.0.0.1:4000/create_playlist"


for playlist in playlists:
    playlist_data = {"id": playlist}
    requests.post(playlist_url, json=playlist_data)
    for video in scrapetube.get_playlist(playlist):
        video_id = video['videoId']
        title = video["title"].get("runs")[0].get("text")

        data = {
            "video_id": video_id,
            "title": title,
            "playlist_id": playlist
        }
        response = requests.post(fastapi_url, json=data)
