from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        response = client.chat.completions.create(
            model="grok-4",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        answer = response.choices[0].message.content

        return jsonify({
            "success": True,
            "reply": answer
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "reply": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)