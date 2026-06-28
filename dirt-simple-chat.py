# easier versions: host the backend, no usernames
from flask import Flask, request

app = Flask(__name__)
all_messages = []


@app.route("/messages", methods=["POST", "GET"])
def messages():
    if request.method == "POST":
        all_messages.append(request.json)

    return all_messages


@app.route("/")
def index():
    return """
<div>
  Username:
  <form>
    <input />
    <button>Submit</button>
  </form>
</div>

<div>
  <div id="messages"></div>
  <form id="send-message">
    <input />
    <button>Submit</button>
  </form>
</div>

<script>
const renderMessages = (messages) => {
  let result = "";

  for (const message of messages) {
    result += `<div>${message.username}: ${message.message}</div>`;
  }

  document.querySelector("#messages").setHTML(result);
};

const form = document.querySelector("form");
const sendMessageForm = document.querySelector("#send-message");
const username = document.querySelector("input");
let chosenUsername = "anonymous";

form.addEventListener("submit", (event) => {
  event.preventDefault();
  chosenUsername = form.querySelector("input").value;
  form.closest("div").remove();
});

sendMessageForm.addEventListener("submit", (event) => {
  event.preventDefault();
  fetch("messages", {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: chosenUsername,
      message: sendMessageForm.querySelector("input").value,
    }),
  })
    .then((res) => res.json())
    .then((data) => renderMessages(data));
});
setInterval(() => {
  fetch("messages")
    .then((response) => response.json())
    .then((data) => {
      renderMessages(data);
    });
}, 1000);
</script>
"""


app.run(host="0.0.0.0", port=81, debug=True)
