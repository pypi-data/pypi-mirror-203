from arkdriver.presentation.presentation import main as presentation
from arkdriver.driver.application import Application
from arkdriver.driver import Driver
from arklibrary.admin import Admin
from pathlib import Path
from arklibrary import Ini
from time import sleep
import requests

URL = 'https://api.loadingproductions.com'
TEST_URL = 'http://127.0.0.1:5000'
TEST_CLOUD_URL = 'http://3.137.160.113'


def ping(url: str):
    count = 0
    while count < 10:
        try:
            res = requests.get(url)
            assert res.status_code == 200, f"Url returned status code: {res.status_code}"
            assert res.json()['connection'] == "successful", "Connection was not successful"
            return
        except Exception as e:
            print(e)
        count += 1
    raise Exception("Unable to get a response from the server: ping")


def get_new_commands(domain: str):
    count = 0
    while count < 10:
        try:
            return requests.get(domain + "/command/new")
        except Exception as e:
            print(e)
        count += 1
    raise Exception("Unable to get a response from the server: get new commands")


def set_command_as_executed(domain: str, command_id: int):
    count = 0
    while count < 10:
        try:
            res = requests.patch(domain + f'/command/{command_id}', json={'executed': True}, headers={'mime': 'application/json'})
            if res.status_code != 200:
                raise Exception("failed to update command as executed [command_id]:", command_id)
            return
        except Exception as e:
            print(e)
        count += 1
    raise Exception("Unable to get a response from the server: update command")


def config():
    path = Path.cwd() / Path('config.ini')
    if not path.exists():
        return
    config = Ini(path)
    if not 'ADMIN' in config:
        return
    admin_password = config['ADMIN']['password']
    admin_player_id = config['ADMIN']['player_id']
    return {'admin_password': admin_password, 'admin_player_id': admin_player_id}


def fetch_commands(url: str, interval=10, wait=5):
    while True:
        res = get_new_commands(url)
        data = []
        try:
            data = [c for c in res.json()]
            print(f"FETCHED: {len(data)}")
        except:
            print(f"[Error] Request to api crashed, response: {res = }")
        if len(data) == 0:
            sleep(wait)
            continue
        i = 0
        while i < len(data):
            print(f"DATA[{i}: {min(i+interval, len(data))}]: {data}")
            yield data[i:i+interval]
            i += interval


def run(url: str):
    commands_per_line = input("How many commands per line should the admin submit at once? Enter a number: ")
    while not commands_per_line.isnumeric():
        print("ERROR: You must input a number.")
        commands_per_line = input("How many commands per line should the admin submit at once? Enter a number: ")
    print()

    wait_time = input("How long should the admin wait before submitting another command sequence? Enter number in seconds: ")
    while not wait_time.isnumeric():
        print("ERROR: You must enter a number.")
        wait_time = input("How long should the admin wait before submitting another command sequence? Enter number in seconds: ")
    print()

    print("Sign into the server.")
    input("Press enter to continue...")
    print()

    print("Create your character and spawn without dying.")
    input("Press enter to continue...")
    print()
    admin_credentials = config()
    if admin_credentials is None:
        password = input("What is the server ADMIN PASSWORD: ")
        while len(password) == 0:
            print("ERROR: The admin password must be longer than 0 characters.")
            password = input("What is the server's ADMIN PASSWORD: ")
        print()

        admin_id = input("What is the ADMIN specimen implant id: ")
        while len(admin_id) != 9 or not admin_id.isnumeric():
            print("ERROR: The specimen implant id must be length 9 and all numbers.")
            admin_id = input("What is the ADMIN specimen implant id: ")
        print()
    else:
        password = admin_credentials['admin_password'].upper()
        admin_id = admin_credentials['admin_player_id']
    print("Close any menu on the screen.",
          "\nMake sure your character's inventory is closed.",
          "\nThe command prompt should not be open.",
          "\nWait until all cutscenes are over.\n")
    input("Press enter to continue...")

    driver = Driver()
    admin = Admin(driver=driver, password=password, player_id=admin_id)
    admin.enable_admin()
    admin.execute()
    for commands in fetch_commands(url, interval=int(commands_per_line), wait=int(wait_time)):
        for command in commands:
            admin.command_list.append(command['code'])
            command['executed'] = True
            set_command_as_executed(url, command['id'])
        admin.execute()


def executable():
    ping(URL)
    run(URL)


def main():
    print("[1] Run driver with official API")
    print("[2] Test driver with local API")
    print("[3] Test driver with cloud API")
    print("[4] Ragnarok Presentation")
    print("[0] To exit")
    response = input("What would you like to run? ")
    choices = ['0', '1', '2', '3', '4']
    while response not in choices:
        print(f"ERROR: your response should be a choice of: {choices}")
        print("[1] Run driver with official API")
        print("[2] Test driver with local API")
        print("[3] Test driver with cloud API")
        print("[4] Ragnarok Presentation")
        print("[0] To exit")
        response = input("What would you like to run? ")

    print()

    if response == '0':
        return

    Application().open_ark()

    if response == '1':
        ping(URL + '/ping')
        run(URL)
    elif response == '2':
        ping(TEST_URL + '/ping')
        run(TEST_URL)
    elif response == '3':
        ping(TEST_CLOUD_URL + '/ping')
        run(TEST_CLOUD_URL)
    elif response == '4':
        presentation()


if __name__ == "__main__":
    main()
