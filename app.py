from flask import Flask,render_template,request
from groq import Groq


app=Flask(__name__)
client = Groq(api_key = "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")
#Groq.api_key = "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"
chat_history = []
@app.route("/",methods=["GET", "POST"])
def chat():
    global chat_history
    if request.method == "POST":
        user_input= request.form["user_input"]
        chat_history.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model ="mistral-saba-24b",
            messages=chat_history,
        )
        assistant_response = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": assistant_response})
          

    return render_template("index.html", chat_history=chat_history)
if __name__ == "__main__":
    app.run(debug=True)
