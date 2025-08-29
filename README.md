# Bajaj_PragnaSresta_22BCE1688

## 👩‍💻 Author
- **Name:** Polimera Pragna Sresta  
- **Roll Number:** 22BCE1688  
- **Email:** pragnasresta05@gmail.com  
- **DOB:** 05-05-2005  

---

## 📌 Project Description
This project implements the **BFHL REST API** as per the VIT Full Stack Objective question paper.  
The API accepts an array of strings (numbers, alphabets, special characters) and returns:

- ✅ Status of operation (`is_success`)  
- ✅ User ID (`full_name_ddmmyyyy` format)  
- ✅ Email ID  
- ✅ Roll Number  
- ✅ Array of even numbers (as strings)  
- ✅ Array of odd numbers (as strings)  
- ✅ Array of alphabets (converted to uppercase)  
- ✅ Array of special characters  
- ✅ Sum of all numbers (as string)  
- ✅ Concatenation of all alphabets in reverse order with alternating caps  

---

## 🚀 Hosted URL
- Base URL: [https://bajaj-pragnasresta-22bce1688.onrender.com](https://bajaj-pragnasresta-22bce1688.onrender.com)  
- API Endpoint: [https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl](https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl)  

---

## 📂 API Routes
- `GET /` → Check if API is running  
- `GET /bfhl` → Shows message: *"This endpoint only supports POST. Send a JSON body like: { "data": ["a","1","$"] }"*  
- `POST /bfhl` → Main logic endpoint  

---

## 📜 Example Request & Response

### Request (POST `/bfhl`)
```json
{
  "data": ["2","a","y","4","&","-","*","5","92","b"]
}
```

### Response
```json
{
  "is_success": true,
  "user_id": "polimera_pragna_sresta_05052005",
  "email": "pragnasresta05@gmail.com",
  "roll_number": "22BCE1688",
  "odd_numbers": ["5"],
  "even_numbers": ["2","4","92"],
  "alphabets": ["A","Y","B"],
  "special_characters": ["&","-","*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

---

## 🛠️ How to Test the API

### 1️⃣ Using cURL
```bash
curl -X POST https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data":["2","a","y","4","&","-","*","5","92","b"]}'
```

### 2️⃣ Using Postman
- Method: **POST**
- URL: `https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl`
- Body → Raw → JSON:
```json
{
  "data": ["2","a","y","4","&","-","*","5","92","b"]
}
```

### 3️⃣ Using PowerShell (Windows)
```powershell
$body = '{"data":["2","a","y","4","&","-","*","5","92","b"]}'
Invoke-RestMethod -Method Post -Uri https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl -ContentType 'application/json' -Body $body
```

Expected Output in PowerShell:
```yaml
alphabets          : {A, Y, B}
concat_string      : ByA
email              : pragnasresta05@gmail.com
even_numbers       : {2, 4, 92}
is_success         : True
odd_numbers        : {5}
roll_number        : 22BCE1688
special_characters : {&, -, *}
sum                : 103
user_id            : polimera_pragna_sresta_05052005
```
```powershell
$body = '{"data":["10","21","32","43"]}'
Invoke-RestMethod -Method Post -Uri https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl -ContentType 'application/json' -Body $body
```
Expected Output in PowerShell:
```yaml
alphabets          : {}
concat_string      : 
email              : pragnasresta05@gmail.com
even_numbers       : {10, 32}
is_success         : True
odd_numbers        : {21, 43}
roll_number        : 22BCE1688
special_characters : {}
sum                : 106
user_id            : polimera_pragna_sresta_05052005
```
```powershell
$body = '{"data":["x","y","z"]}'
Invoke-RestMethod -Method Post -Uri https://bajaj-pragnasresta-22bce1688.onrender.com/bfhl -ContentType 'application/json' -Body $body
```
Expected Output in PowerShell:
```yaml
alphabets          : {X, Y, Z}
concat_string      : ZyX
email              : pragnasresta05@gmail.com
even_numbers       : {}
is_success         : True
odd_numbers        : {}
roll_number        : 22BCE1688
special_characters : {}
sum                : 0
user_id            : polimera_pragna_sresta_05052005
```
---

## ⚡ Local Development (Optional)

If you want to run locally:

```bash
# Clone the repo
git clone https://github.com/Pragna-Sresta-5/Bajaj_PragnaSresta_22BCE1688.git
cd Bajaj_PragnaSresta_22BCE1688

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```
App will run at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📄 `requirements.txt`
Copy this into a file named `requirements.txt`:

```
flask
gunicorn
```
*(Flask = web framework, Gunicorn = production server used by Render)*

---

## 📄 `Procfile`
Copy this into a file named `Procfile`:

```
web: gunicorn app:app
```

---

👉 Now your repo will be **exam-ready**:  
- `app.py` (your code)  
- `requirements.txt` (dependencies)  
- `Procfile` (for deployment)  
- `README.md` (documentation + hosted URL + test commands)  

---

**This README ensures evaluators can:**
- Open your GitHub repo
- See your details
- Test the hosted URL instantly
- Verify correctness with examples
