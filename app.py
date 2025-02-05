from flask import Flask, render_template, request
from ai import send_prompt_to_AzureOpenAI

app = Flask(__name__)

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")

        if prompt:
            try:
                response_text = send_prompt_to_AzureOpenAI(prompt, "spanish")
                translate_resp = send_prompt_to_AzureOpenAI(response_text, "english")
            except Exception as e:
                response_text = f'Ocurrió un error: {e}'

    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
