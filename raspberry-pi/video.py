from subprocess import Popen

def play_video(path_to_video):
	omxp= Popen(['omxplayer',path_to_video])

def main():
	play_video("videos/test.mp4")
	print("---")

main()
