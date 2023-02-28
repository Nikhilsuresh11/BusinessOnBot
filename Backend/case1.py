from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/search')
def search_banks():
    q = request.args.get('q')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    conn = sqlite3.connect('bank_details.db')
    cursor = conn.cursor()

    query = """
        SELECT * FROM bank_details
        WHERE bank_name LIKE ? OR ifsc LIKE ? OR branch LIKE ? OR address LIKE ? OR city LIKE ? OR district LIKE ? OR state LIKE ?
        ORDER BY ifsc ASC
        LIMIT ? OFFSET ?
    """

    search_term = f"%{q}%"
    params = (search_term, search_term, search_term, search_term, search_term, search_term, search_term, limit, offset)
    cursor.execute(query, params)

    results = cursor.fetchall()
    banks = []

    for row in results:
        bank = {
            'ifsc': row[0],
            'bank_id': row[1],
            'branch': row[2],
            'address': row[3],
            'city': row[4],
            'district': row[5],
            'state': row[6],
            'bank_name': row[7]
        }
        banks.append(bank)

    conn.close()

    return jsonify({'banks': banks})