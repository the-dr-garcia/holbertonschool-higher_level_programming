#!/usr/bin/python3
"""Flask app displaying products from JSON, CSV or SQLite."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filepath='products.json'):
    """Read products from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv(filepath='products.csv'):
    """Read products from a CSV file, converting the field types."""
    products = []
    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as file:
            for row in csv.DictReader(file):
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


def read_sql(db_path='products.db'):
    """Read products from the SQLite database. Return None on error."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return rows
    except sqlite3.Error:
        return None


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items list read from items.json."""
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            items_list = json.load(file).get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Display products from the json, csv or sql source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html',
                                   error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            pid = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")
        data = [p for p in data if int(p.get('id', -1)) == pid]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
