from flask import Flask, request, jsonify

app = Flask(__name__)

# Your details
FULL_NAME = "Polimera Pragna Sresta"
DOB = "05052005"
EMAIL = "pragnasresta05@gmail.com"
ROLL_NUMBER = "22BCE1688"

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json()
        input_array = data.get("data", [])
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0
        concat_alpha = []
        for item in input_array:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_alpha.append(item)
            else:
                special_chars.append(item)
        concat_alpha_str = "".join(concat_alpha)[::-1]
        alt_caps_str = ""
        for i, ch in enumerate(concat_alpha_str):
            alt_caps_str += ch.upper() if i % 2 == 0 else ch.lower()
        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": alt_caps_str
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400
@app.route("/", methods=["GET"])
def home():
    return {"message": "BFHL API is running. Use POST /bfhl to test."}, 200

if __name__ == "__main__":
    app.run(debug=True)

