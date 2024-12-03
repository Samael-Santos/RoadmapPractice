import requests


def GHUA():
    user = "Samael-Santos"  # input("Enter username: ")
    r = requests.get(f"https://api.github.com/users/{user}/events")
    response = r.json()
    for event in response:
        output = f"- ({str(event['created_at']).replace('T', ' ')[:-1]})"

        if event['type'] == "CreateEvent":
            output += " Created a"
            output += f" ({event['payload']['ref_type']})"
            if event['payload']['ref_type'] == 'branch':
                output += f" called ({event['payload']['ref']})"
            output += f" at ({event['repo']['name']})"
            print(output)
            continue

        if event['type'] == "PushEvent":
            output += " Pushed a commit to"
            output += f" ({event['repo']['name']})"
            output += f" Message: ({event['payload']['commits'][0]['message']})"
            print(output)
            continue


GHUA()
