import click
import json
from datetime import datetime


# to access or create the json database, returns the object
def file_toucher():
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No database, creating json file...")
        with open("expenses.json", "w") as file:
            data = {
                'entries': [],
                'last id': 0
            }
    return data


@click.group()
def cli():
    pass


# adds entries to the database
@cli.command()
@click.option("-d", "--description", type=str,
              help="Adds a description to a entry. Multiple words must be between \"\"")
@click.option("-a", "--amount", type=int,
              help="Adds expense cost to an entry. Without cents.")
def add(description, amount):

    # validation
    if amount is not None and amount < 0:
        return print("Invalid amount.")

    data = file_toucher()

    # building new entry
    new_entry = {
        "id": (data['last id'] + 1),
        "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "description": description,
        "amount": amount
    }

    # updating database object
    data['entries'].append(new_entry)
    data['last id'] += 1

    # dumping json database
    with open("expenses.json", "w") as file:
        json.dump(data, file)


# deletes entries by id
@cli.command()
@click.argument("id", type=int)
def delete(id):
    # file_toucher with a twist
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return print("Nothing to delete.")

    # loop to find the id, too lazy to introduce an algorithm
    for i, entry in enumerate(data['entries']):
        if entry['id'] == id:
            data['entries'].pop(i)
            with open("expenses.json", "w") as file:
                json.dump(data, file)
            return print("Entry sucessfully deleted.")
    print("ID not found.")


# prints the database
@cli.command()
def list():
    data = file_toucher()
    for entry in data['entries']:
        click.echo(f"ID: {entry['id']} / {entry['date']} / Description: {entry['description']} / Amount: ${entry['amount']}")


# prints the sum of all the expenses, can filter by month
@cli.command()
@click.option("-m", "--month", type=int,
              help="Filters by month number,")
def summary(month):
    data = file_toucher()
    sum = 0

    # case no month was passed
    if month is None:
        for entry in data['entries']:
            sum += entry['amount']
        print(f"Total expenses: {sum}")

    # month validation
    elif month > 12 or month < 1:
        print("Invalid month.")

    # case a valid month was passed
    else:
        for entry in data['entries']:
            if entry['date'][3:5] == str(month) or entry['date'][3:5] == "0" + str(month):
                sum += entry['amount']
        print(f"Total expenses: {sum}")


# everything works because of this, no idea why
if __name__ == "__main__":
    cli()
