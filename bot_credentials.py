import os

# if os.path.exists(".env"):
#     print("env found")
#     # if we see the .env file, load it
#     from dotenv import load_dotenv
#     load_dotenv()

from dotenv import load_dotenv, find_dotenv
env_path = find_dotenv()
load_dotenv(dotenv_path = env_path)

# now we have them as a handy python strings!

BOT_USERNAME = os.getenv('BOT_USERNAME')
BOT_TOKEN = os.getenv('BOT_TOKEN')

print(BOT_TOKEN)
