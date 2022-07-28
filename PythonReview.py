def create_youtube_video(title,description):
	youtubevid= {"title":title,"description":description,"likes":0,"dislikes":0,"comments":0}
	print(youtubevid)
	return youtubevid

	

def likim(youtubevid):
	key = "likes"
	if key in youtubevid:
		youtubevid["likes"] +=1
		print(youtubevid)
		return youtubevid
	else:
		print("no likes")
		return youtubevid


def dislikim(youtubevid):
	key = "dislikes"
	if key in youtubevid:
		youtubevid["dislikes"] +=1
		print(youtubevid)
		return youtubevid
	else:
		print("no dislikes")
		return youtubevid


def add_comment(youtubevid,username,comment_text):
	youtubevid[username] = comment_text
	print(youtubevid)

myvid = create_youtube_video('yuval' ,'kinggggg')
dislikim(myvid)
add_comment(myvid,'zeno','coolllll')
