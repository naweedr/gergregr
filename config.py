from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBWyb-WPlywKT4pr-KYdG65dR00NwxOH3UfuZ_5gO4BJ0Zm3OSTfDelRt7Y5VJQrLDZn-cVOQ25JJYzo9yuqw4tjn_-RSuFLtv-WDKuIgZEJNl_ZGuetf9XCjBY--y_92lETcagfrx5BlCJMTARh0jv1RyKED-W-XBO9pqXdLbdn6EirAy0hLlySNKYuoBDUWdNLpX8o7lXCJVqeETq4AqKXzBqP4M4PlDcSkE4-k0dLCA4jYjqvtyieGRb0IuCxpJW2zMBmkKnXcO2CgotFuHEBCGUSUZDlVP8zCJv7FqLWN-93LCwI7_FcpTyDiL9n9Lrye19TITdZxi-wnBBk2azX9eSewA")
BOT_TOKEN = getenv("BOT_TOKEN", "2096185149:AAGir_iyj1q4g35ePOorRl_twGdCHZ_Jk5I")
BOT_USERNAME = getenv("BOT_USERNAME", "MuslcPlayer_bot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "padeshatoon")
admins = {}
API_ID = int(getenv("API_ID"), "164723")
API_HASH = getenv("API_HASH", "dabd3508016970f6c78c43ab208415da")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1769401739").split()))



