# Chapter 2 Using ChatGPT

To run:

`pip install virtualenv`

`python3 -m venv gpt-itam-env`

`source gpt-itam-env/bin/activate`

`pip install -r requirements.txt`


curl -X POST "http://localhost:8000/assets/" -d "{'asset_id':'003', \
'asset_type': 'Server', \
    'manufacturer': 'Dell', \
    'model': 'PowerEdge R740', \
    'purchase_date': '2021-03-01', \
    'warranty_end_date': '2024-03-01', \
    'location': 'London' \
    }"

    '003', , ', 'PowerEdge R740', '2021-03-01', , )

    curl -X PUT -H "Content-Type: application/json" -d '{"asset_id": "12345", "user": "John"}' http://localhost:8000/assets/12345/assign
