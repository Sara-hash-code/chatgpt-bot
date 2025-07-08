from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os


app = Flask(__name__)
CORS(app)


openai.api_key = os.getenv(" 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")


@app.route('/')
def home():
    return " ChatGPT Flask Server is Running!"

# روت چت برای دریافت پیام و پاسخ
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "Message not provided"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # اگر اکانتت GPT-4 داره، اینو تغییر بده
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=100,
            temperature=0.7
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
