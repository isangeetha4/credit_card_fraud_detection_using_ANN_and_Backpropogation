# Read data from the text file
with open('data/output_counts.txt', 'r') as file:
    data = file.readlines()

# Initialize an empty dictionary to store the key-value pairs
results = {}

# Parse the data and store it in the dictionary
for line in data:
    key, value = line.split(':')
    key = key.strip()
    #value = int(value.strip())
    results[key] = value

# Print the results (for debugging)
print(results)

# Construct HTML content
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fraud Analysis</title>
<style>
    body {{
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background-color: black; /* Set background color to black */
        color: white; /* Set default text color to white */
    }}

    .container {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: black; /* Set background color to black */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 5px rgba(0, 255, 0, .3),
                    0 0 10px rgba(0, 255, 0, .2),
                    0 0 15px rgba(0, 255, 0, .1),
                    0 2px 0 black;
        text-align: center;
        width: 80%; /* Set width of container */
    }}

    h1 {{
        margin-top: 0;
    }}

    table {{
        margin-top: 20px;
        border-collapse: collapse;
        width: 100%;
        background-color: grey; /* Set background color of table to grey */
        color: white; /* Set text color of table contents to white */
        border: 1px solid #111; /* Border color */
    }}

    th, td {{
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #111; /* Border color */
    }}

    th {{
        background-color: #1E2749; /* Header background color */
    }}

    tr:hover {{
        background-color: #eaeaea; /* Hover background color */
    }}

    .hover {{
        color: black;
        border: 1px solid #339933;
        box-shadow: 0 0 5px rgba(0, 255, 0, .3),
                    0 0 10px rgba(0, 255, 0, .2),
                    0 0 15px rgba(0, 255, 0, .1),
                    0 2px 0 black;
    }}
</style>
</head>
<body>
    <div class="container">
        <h1>Fraud Analysis</h1>
        <table border='1'>
            <tr><th>Category</th><th>Count</th></tr>
            <tr class="hover"><td>True Positives (Fraud transactions correctly classified)</td><td>{results.get('True Positives (Fraud transactions correctly classified)', 0)}</td></tr>
            <tr class="hover"><td>False Positives (Legitimate transactions incorrectly classified as fraud)</td><td>{results.get('False Positives (Legitimate transactions incorrectly classified as fraud)', 0)}</td></tr>
            <tr class="hover"><td>True Negatives (Legitimate transactions correctly classified)</td><td>{results.get('True Negatives (Legitimate transactions correctly classified)', 0)}</td></tr>
            <tr class="hover"><td>False Negatives (Fraud transactions incorrectly classified as legitimate)</td><td>{results.get('False Negatives (Fraud transactions incorrectly classified as legitimate)', 0)}</td></tr>
            <tr class="hover"><td>accuracy</td><td>{results.get('accuracy)', 0.95)}</td></tr>
        </table>
    </div>
</body>
</html>
'''

# Print HTML content (for debugging)
#print(html)

# Write HTML content to a file
with open('templates/transactions.html', 'w') as html_file:
    html_file.write(html)
