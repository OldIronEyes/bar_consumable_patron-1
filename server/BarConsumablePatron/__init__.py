from flask import Flask, jsonify, make_response, request
import json

from BarConsumablePatron import database

app = Flask(__name__)

#get all bars
@app.route('/api/bar', methods=["GET"])
def get_bars():
	return jsonify(database.get_bars())

#find bar with given license
@app.route("/api/bar/<license>", methods=["GET"])
def find_bar(license):
	try:
		if license is None:
			raise ValueError("Please specify Bar.")
		bar = database.find_bar(license)
		if bar is None:
			return make_response("No matching bar was found.", 404)
		return jsonify(bar)
	except ValueError as err:
		return make_response(str(err), 400)
	except Exception as e:
		return make_response(str(e), 500)

#find all beers this bar sells
#@app.route("/api/menu/beer/<license>", methods=["GET"])

#find all foods this bar sells
@app.route("/api/menu/food/<license>", methods=["GET"])
def get_food_menu(license):
	try:
		if license is None:
			raise ValueError("Please specify Bar.")
		res = database.get_food_menu(license)
		if res is None:
			return make_response("Bar does not sell any food.", 404)
		return jsonify(res)
	except ValueError as err:
		return make_response(str(err), 400)
	except Exception as e:
		return make_response(str(e), 500)

#find all sodas this bar sells
#@app.route("/api/menu/soda/<license>", methods=["GET"])

#get all patrons
@app.route('/api/patrons', methods=["GET"])
def get_patrons():
    return jsonify(database.get_patrons())

#find patron with given phone number
@app.route("/api/patrons/<phone>", methods=["GET"])
def find_patron(phone):
    try:
        if phone is None:
            raise ValueError("Patron not specified")
        patron = database.find_patron(phone)
        if patron is None:
            return make_response("No Patron with that phone number", 404)
        return jsonify(patron)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

#get all beers
@app.route('/api/beer', methods=["GET"])
def get_beers():
	return jsonify(database.get_beers())
	
#find beer with given name
@app.route("/api/beer/<name>", methods=["GET"])
def find_beer(name):
	try:
		if name is None:
			raise ValueError("Please specify beer.")
		beer = database.find_beer(name)
		if beer is None:
			return make_response("No matching beer was found.", 404)
		return jsonify(beer)
	except ValueError as err:
		return make_response(str(err), 400)
	except Exception as e:
		return make_response(str(e), 500)

#find beers cheaper than given price
@app.route("/api/find_beers_less_than", methods=["POST"])
def find_beers_less_than():
	body = json.loads(request.data)
	max_price = body['maxPrice']
	return jsonify(database.find_beers_less_than[max_price])
	
