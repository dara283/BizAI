from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_service import get_ai_response

app = Flask(__name__)
CORS(app)


@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.json
    user_input = data.get("text")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    summary = get_ai_response(f"Summarise this business data:\n{user_input}")
    insights = get_ai_response(f"Give business insights from this:\n{user_input}")
    recommendations = get_ai_response(f"Give improvement suggestions:\n{user_input}")

    return jsonify({
        "summary": summary,
        "insights": insights,
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(debug=True)