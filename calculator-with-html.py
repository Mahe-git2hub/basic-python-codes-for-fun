from flask import Flask, request, render_template_string

app = Flask(__name__)

def get_template():
    # HTML template with embedded CSS and JavaScript for the calculator UI
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Calculator</title>
      <style>
        body { text-align: center; padding-top: 50px; }
        .container { display: inline-block; }
        input, button { font-size: 20px; }
        input[type="text"] { width: 200px; }
        .operator { font-size: 24px; }
      </style>
      <script>
        document.addEventListener('DOMContentLoaded', function() {
          document.addEventListener('keydown', function(event) {
            if(event.key === '+') {
              document.querySelector('button[value="add"]').click();
            } else if(event.key === '-') {
              document.querySelector('button[value="subtract"]').click();
            } else if(event.key === '*') {
              document.querySelector('button[value="multiply"]').click();
            } else if(event.key === '/') {
              document.querySelector('button[value="divide"]').click();
            }
          });
        });
      </script>
    </head>
    <body>
      <div class="container">
        <form method="post" action="/calculate">
          <input type="text" name="operand1" id="operand1" required="required" />
          <span class="operator">{{ operator }}</span>
          <input type="text" name="operand2" id="operand2" required="required" />
          <br><br>
          <button type="submit" name="operation" value="add">+</button>
          <button type="submit" name="operation" value="subtract">-</button>
          <button type="submit" name="operation" value="multiply">*</button>
          <button type="submit" name="operation" value="divide">/</button>
        </form>
        {% if result is not none %}
        <p>Result: {{ result }}</p>
        {% endif %}
      </div>
    </body>
    </html>
    """


# Route for the main page
@app.route("/", methods=["GET"])
def index():
    template = get_template()
    return render_template_string(template, operator='+', result=None)

# Route to handle calculation requests
@app.route("/calculate", methods=["POST"])
def calculate():
    template = get_template()
    # Extract operands and operation from the form
    operand1 = request.form.get("operand1", type=float)
    operand2 = request.form.get("operand2", type=float)
    operation = request.form.get("operation", type=str)
    
    # Perform the operation
    result = None
    if operation == "add":
        result = operand1 + operand2
    elif operation == "subtract":
        result = operand1 - operand2
    elif operation == "multiply":
        result = operand1 * operand2
    elif operation == "divide":
        # Handle division by zero
        result = "Error" if operand2 == 0 else operand1 / operand2
    
    # Render the page with the result
    return render_template_string(template, operator='+', result=result)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)

