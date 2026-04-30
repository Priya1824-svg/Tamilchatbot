
import gradio as gr

chatbot_data = {
    "வணக்கம்": "வணக்கம்! நான் உங்களுக்கு எப்படி உதவ முடியும்?",
    "hello": "வணக்கம்! எப்படி இருக்கீங்க?",
    "hi": "வணக்கம்! நான் உங்களுக்கு எப்படி உதவ முடியும்?",
    "எப்படி இருக்கீங்க": "நான் நன்றாக இருக்கேன், நன்றி! நீங்கள் எப்படி இருக்கீங்க?",
    "உங்கள் பெயர் என்ன": "என் பெயர் தமிழ் சாட்பாட். நான் தமிழில் பேசுவதற்கு இங்கே இருக்கேன்!",
    "நன்றி": "மிக்க நன்றி! வேறு ஏதாவது தேவையா?",
    "bye": "சரி, வணக்கம்! மீண்டும் பேசுவோம்!",
    "what is nlp": "NLP is Natural Language Processing — helping computers understand human language!",
    "what is ai": "AI stands for Artificial Intelligence — teaching computers to think like humans!",
    "who made you": "என்னை N. Priya Dharshini உருவாக்கினார். அவர் Kalasalingam University-ல் PhD ஆராய்ச்சி மாணவர்.",
}

def get_response(user_input):
    user_input = user_input.strip().lower()
    if user_input in chatbot_data:
        return chatbot_data[user_input]
    for key in chatbot_data:
        if key in user_input or user_input in key:
            return chatbot_data[key]
    return "மன்னிக்கவும், எனக்கு புரியவில்லை. தயவுசெய்து வேறு விதமாக கேளுங்க!"

def chat(user_message, history):
    response = get_response(user_message)
    history.append((user_message, response))
    return history, ""

with gr.Blocks(title="Tamil Chatbot") as app:
    gr.Markdown("# 🤖 தமிழ் சாட்பாட் (Tamil Chatbot)")
    gr.Markdown("தமிழிலும் ஆங்கிலத்திலும் பேசுங்க!")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="தமிழில் அல்லது English-ல் தட்டச்சு செய்யுங்க...", label="உங்கள் செய்தி")
    with gr.Row():
        send_btn = gr.Button("அனுப்பு / Send 📤", variant="primary")
        clear_btn = gr.Button("அழி / Clear 🗑️")
    send_btn.click(chat, [msg, chatbot], [chatbot, msg])
    msg.submit(chat, [msg, chatbot], [chatbot, msg])
    clear_btn.click(lambda: ([], ""), None, [chatbot, msg])
    gr.Markdown("*Built by N. Priya Dharshini | PhD Research Scholar | Kalasalingam University*")

app.launch(share=True)
