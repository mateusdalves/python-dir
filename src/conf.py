from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    DIR = os.getenv('ROOT_DIR')