# Simple backend django application to manage images

## How does it work?

- You can pass image or url to image and receive photo attributes like height, width and dominant color in response

### Open this app locally
Go to http://localhost:8000/api/photos or send a post request to that address.
- Title: str
- AlbumId: int ( range (1,2))
- Image: file [optional]
- url: url [optonal]

(It is necessary to pass image or url)

### Both ways the image is going to be stored locally, and you will receive attributes from uploaded image  

