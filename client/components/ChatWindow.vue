<template>
  <div class="chat-window">
    <div class="messages">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="msg.sender === 'User' ? 'user-messages' : 'bot-messages'"
        class="message"
        ref="lastMessage"
      >
        <strong>{{ msg.sender }}:</strong>
        <div v-if="msg.sender === 'Bot'" v-html="parseMarkdown(msg.text)" />
        <div v-else>{{ msg.text }}</div>
      </div>
    </div>

    <input
      v-model="userInput"
      @keyup.enter="sendMessage"
      placeholder="type your message..."
      class="chat-input"
    />

    <button @click="sendMessage" class="send-button">Send</button>
  </div>
</template>

<script setup lang="ts">
import { marked } from "marked";
import { useRuntimeConfig } from "nuxt/app";
import { nextTick, ref } from "vue";

interface Message {
	sender: string;
	text: string;
}

// define messages list and input var
const messages = ref<Message[]>([]);
const userInput = ref<string>("");
const lastMessage = ref<HTMLElement | null>(null);

const config = useRuntimeConfig();
const apiBase = config.public.apiBase;

const sendMessage = async () => {
	// assign userInput.vaue to tmp var to clear input field and preserve msg
	let msg = userInput.value;

	// clear input field and scroll to bottom
	userInput.value = "";

	// handle empty messages
	if (msg.trim() === "") return;

	// push json message obj to messages list
	messages.value.push({ sender: "User", text: msg });

	// scroll to bottom after user posts message
	await nextTick();
	scrollToBottom;

	// post to server api endpoint
	try {
		console.log(`${apiBase}/send-chat`);
		const response = await fetch(`${apiBase}/send-chat`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ userMsg: msg }),
		});

		// handle no response case
		if (!response.ok) {
			throw new Error("Network response not ok");
		}

		const data = await response.json();

		// if message, push message object to messages list, else console log error
		messages.value.push({ sender: "Bot", text: data.bot_response });

		// scroll to bottom after bot posts message
		await nextTick();
		scrollToBottom();
	} catch (error) {
		messages.value.push({ sender: "System", text: "Network error" });
	}
};

// markdown to text conversion
const parseMarkdown = (markdownText: string) => {
	if (!markdownText) {
		return "";
	}
	return marked(markdownText);
};

// smooth scroll to bottom of chat window
const scrollToBottom = () => {
	const messagesContainer = document.querySelector(".messages");
	if (messagesContainer) {
		messagesContainer.scrollTop = messagesContainer.scrollHeight;
	}
};
</script>

<style scoped>
.chat-window {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  width: 400px;
  max-height: 500px;
  display: flex;
  flex-direction: column;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  min-height: 50vh;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 8px;
  color: black;
}

.message {
  margin: 8px 0;
}

.user-messages {
  background-color: lightblue;
  padding: 8px;
  border-radius: 4px;
  text-align: right;
  margin-left: 4rem;
}

.bot-messages {
  background-color: white;
  padding: 8px;
  border-radius: 4px;
  text-align: left;
  margin-right: 4rem;
}

.chat-input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  flex: 0;
}

.send-button {
  padding: 8px 16px;
  cursor: pointer;
  margin-left: auto;
  margin-top: 1rem;
  margin-right: auto;
  background-color: lightblue;
  color: black;
  font-weight: bold;
}
</style>
