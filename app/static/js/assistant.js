const assistantBtn = document.getElementById("assistantBtn");
const assistantBox = document.getElementById("assistantBox");
const assistantForm = document.getElementById("assistantForm");
const assistantInput = document.getElementById("assistantInput");
const assistantMessages = document.getElementById("assistantMessages");

// Toggle chat window
assistantBtn.addEventListener("click", () => {

    if (assistantBox.style.display === "block") {

        assistantBox.style.display = "none";

    } else {

        assistantBox.style.display = "block";

        assistantInput.focus();

    }

});

// Send message
assistantForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const message = assistantInput.value.trim();

    if (!message) return;

    assistantMessages.innerHTML += `
        <div class="assistant-message user-message">
            <strong>You:</strong> ${message}
        </div>
    `;

    assistantInput.value = "";

    assistantMessages.innerHTML += `
        <div class="assistant-message ai-message" id="typing">
            🤖 Thinking...
        </div>
    `;

    assistantMessages.scrollTop = assistantMessages.scrollHeight;

    try {

        const response = await fetch("/assistant", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await response.json();

        document.getElementById("typing").remove();

        assistantMessages.innerHTML += `
            <div class="assistant-message ai-message">
                <strong>AI:</strong> ${data.response}
            </div>
        `;

    } catch (err) {

        document.getElementById("typing").remove();

        assistantMessages.innerHTML += `
            <div class="assistant-message ai-message">
                ❌ Error contacting AI.
            </div>
        `;

    }

    assistantMessages.scrollTop = assistantMessages.scrollHeight;

});