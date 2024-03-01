from instaloader import Instaloader

# Create an Instaloader instance
loader = Instaloader()

# Replace 'your_username' with the Instagram username you want to download
profile = 'your_username'

# Download profile pictures
loader.download_profile(profile, profile_pic_only=True)
