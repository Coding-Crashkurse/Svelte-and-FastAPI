import scrapetube
import requests

playlists = ["PL-lCrD3QqynV3jliSJ1VfUu-4Uf0f6krh", "PL-lCrD3QqynWDYLO6GMzqnZL29y_qe-3v", "PL-lCrD3QqynWOYATxwjTPSc_qr3iWus_a", "PL-lCrD3QqynX2a2sgXZlvxEGssGg9ZTCa", "PL-lCrD3QqynWL0Ve2zqtABq6cE4BwmVvm"]

fastapi_url = "http://127.0.0.1:4000/create_entry"
playlist_url = "http://127.0.0.1:4000/create_playlist"

for playlist in playlists:
    playlist_data = {"id": playlist}
    requests.post(playlist_url, json=playlist_data)

    # Convert the generator object to a list and reverse the order of items
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
