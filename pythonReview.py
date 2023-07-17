def create_youtube_video(title,description):
	return {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}

def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1
	return video

def add_comment(video,username,comment_text):
	video["comments"][username]= comment_text
	return video

video=create_youtube_video("Meet","Very fun")
like(video)
dislike(video)
add_comment(video,"Sireen","My Experience")
print(video)

for i in range(495):
	like(video)

prit(video)