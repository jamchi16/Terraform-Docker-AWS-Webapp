from flask import Flask, request
import csv
import random
import os
random_pkmn = ""
PokemonList = 'Pokemon.csv'
y = ""
app = Flask(__name__)

@app.route("/")
def index():
    global y
    global random_pkmn
    y = request.args.get("y", "")
    if y:
        random_pkmn = pkmn_randomizer(y)
    else:
        random_pkmn = ""
    return (
        """<form action="" method="get">
                Would you like to catch a Pokemon? If yes: type 1, If no: type 0. <input type="text" name="y">
                <input type="submit" value="Submit">
            </form>"""
        f"{random_pkmn}"
    )

def pkmn_randomizer(y):
    global random_pkmn
    if y == '1':
        with open(f'{PokemonList}', 'r') as f:
            reader = csv.reader(f)
            data = [row[0] for row in reader]
            random_pkmn = random.choice(data)
            return f"You have caught a {random_pkmn}!"
    else:
        return "Then why did you come here?"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)