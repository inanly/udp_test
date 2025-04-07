# curl -fsSL https://ollama.ai/install.sh | sh
# nohup ollama serve &
# ollama pull gemma3
# pip install gradio
# pip install openai

import gradio as gr
import openai  # 修正引用

# 設定 OpenAI API (用 Ollama)
openai.api_key = "ollama"
openai.api_base = "http://localhost:11434/v1"

# 定義不同人設
personalities = {
    "溫暖治癒型": "你是一個非常溫暖的對話機器人，回應像好朋友一樣，有同理心鼓勵使用者，盡量不要超過二十個字，請用台灣習慣的中文回應，並加上適當的 emoji。",
    "搞笑幽默型": "你是一個搞笑的對話機器人，喜歡用幽默又可愛的方式回應，經常使用台灣用語和 emoji。",
    "哲學思考型": "你是一個喜歡哲學思考的機器人，用詩意或哲理的方式回應，鼓勵使用者思考人生。",
    "欣賞型": "你是一個專門誇獎使用者的機器人，無論使用者說什麼都給予正面誇獎和鼓勵，並加上 emoji。"
}

description = "你好，我是你的 AI 好友拍拍機器人！選擇風格開始聊天吧 :)"
model = "gemma3"

# 初始對話設定
def get_initial_messages(personality):
    return [{"role": "system", "content": personalities[personality]},
            {"role": "assistant", "content": description}]

# 對話邏輯
def pipi(prompt, messages, personality):
    messages.append({"role": "user", "content": prompt})

    # 加入彩蛋關鍵字回應
    if "我好累" in prompt:
        reply = "休息一下吧！你已經很棒了 🛌✨"
    else:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
        )
        reply = chat_completion.choices[0].message.content

        # 自動追加追問
        follow_up = "你願意多跟我分享嗎？😊"
        reply += f"\n\n{follow_up}"

    messages.append({"role": "assistant", "content": reply})
    return messages, messages

# Gradio 介面
with gr.Blocks(title="拍拍機器人 升級版") as demo:
    gr.Markdown(f"## 🤖 拍拍機器人 升級版\n{description}")

    personality_selector = gr.Radio(
        list(personalities.keys()), label="選擇你的機器人風格", value="溫暖治癒型"
    )
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(label="輸入訊息")
    state = gr.State(get_initial_messages("溫暖治癒型"))

    def change_personality(personality):
        return get_initial_messages(personality)

    personality_selector.change(fn=change_personality, inputs=personality_selector, outputs=state)
    msg.submit(fn=pipi, inputs=[msg, state, personality_selector], outputs=[chatbot, state])

demo.launch(share=True, debug=True)
