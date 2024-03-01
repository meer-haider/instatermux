from instaloader import Instaloader
import sys
import datetime

# Check if the username is provided as a command-line argument
if len(sys.argv) != 2:
    print("Please provide the Instagram username as a command-line argument.")
    sys.exit(1)

# Get the username from the command-line argument
profile = sys.argv[1]

# Create an Instaloader instance
loader = Instaloader()

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Download profile pictures with a unique filename
loader.download_profile(profile, profile_pic_only=True, filename_pattern=f"{profile}_{timestamp}_UTC_profile_pic.jpg")