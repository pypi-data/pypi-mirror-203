import sys
import argparse
from mc_uuid_check import mc_offline_uuid as offmcuuid
from mc_uuid_check import mc_online_uuid as onmcuuid
from mc_uuid_check import helperfunctions as helper


parser = argparse.ArgumentParser(
    prog='mc-uuid-check',
    description='Get the Offline / Online UUID of a Player')
parser.add_argument("-o", "--online", action="store_true", help="Check Mojang API for UUID")
parser.add_argument("-r", "--without-hyphen", dest="wouthyph", action="store_true", help="Removes Hyphen from UUID String")
parser.add_argument("username", type=str, help="Username of the Player")
args = parser.parse_args()

username = args.username


def main():
    #Getting argument from command line as username to convert
    #Printing UUID
    if args.online:
        stringinput = helper.format_json(onmcuuid.get_uuid_api(username))
        if args.wouthyph:
            print(helper.rem_hyphen(stringinput))
        else:
            print(stringinput)
    else:
        if args.wouthyph:
            print(helper.rem_hyphen(offmcuuid.get_uuid_offline(username)))
        else:
            print(offmcuuid.get_uuid_offline(username))


if __name__ == "__main__":
    main(username)

