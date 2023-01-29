import scrapetube
import requests

videos = scrapetube.get_channel("UCikLKUS0DZWMkukbkYDG49Q")
fastapi_url = "http://127.0.0.1:4000/create_entry"

for video in videos:
    video_id = video['videoId']
    title = video["title"].get("runs")[0].get("text")
    description = video["descriptionSnippet"].get("runs")[0].get("text")

    data = {
        "video_id": video_id,
        "title": title,
        "description": description
    }
    response = requests.post(fastapi_url, json=data)
    print(response.status_code)