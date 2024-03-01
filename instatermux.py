from instaloader import Instaloader
import sys

# Check if the username is provided as a command-line argument
if len(sys.argv) != 2:
    print("Please provide the Instagram username as a command-line argument.")
    sys.exit(1)

# Get the username from the command-line argument
profile = sys.argv[1]

# Create an Instaloader instance
loader = Instaloader()

# Download profile pictures
loader.download_profile(profile, profile_pic_only=True)