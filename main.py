import requests

############################################################################################################################################################
# Movie Script: https://gist.githubusercontent.com/ElliotGluck/64b0b814293c09999f765e265aaa2ba1/raw/79f24f9f87654d7ec7c2f6ba83e927852cdbf9a5/gistfile1.txt #
############################################################################################################################################################
# Big THX to @ElliotGluck for uploading the Bee Movie Script to GitHub. #
# It was exactly what we missed. UwU.                                   #
#########################################################################

url = "https://gist.githubusercontent.com/ElliotGluck/64b0b814293c09999f765e265aaa2ba1/raw/79f24f9f87654d7ec7c2f6ba83e927852cdbf9a5/gistfile1.txt"
r = requests.get(url)
bee_movie_script = r.text
print(bee_movie_script)
