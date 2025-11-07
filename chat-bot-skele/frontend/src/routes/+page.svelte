<script lang="ts">
	import { onMount } from 'svelte';

	let message = '';
	let messages: { role: string; content: string }[] = [];

	async function sendMessage() {
		if (!message.trim()) return;

		const userMsg = { role: 'user', content: message };
		messages = [...messages, userMsg];

		const res = await fetch('http://127.0.0.1:8000/chat', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ message })
		});

		const data = await res.json();
		const botMsg = { role: 'assistant', content: data.reply };
		messages = [...messages, botMsg];
		message = '';
	}
</script>

<div class="flex h-screen flex-col bg-gray-50">
	<!-- Header -->
	<header class="border-b bg-white p-4 shadow-sm">
		<h1 class="text-xl font-semibold text-gray-700">Ollama Chat</h1>
	</header>

	<!-- Chat Messages -->
	<main class="flex-1 space-y-3 overflow-y-auto p-4">
		{#each messages as msg}
			<div class={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
				<div
					class={`max-w-xs rounded-2xl px-4 py-2 text-sm md:max-w-md
          ${
						msg.role === 'user'
							? 'rounded-br-none bg-blue-500 text-white'
							: 'rounded-bl-none bg-gray-200 text-gray-800'
					}`}
				>
					{msg.content}
				</div>
			</div>
		{/each}
	</main>

	<!-- Input Area -->
	<footer class="border-t bg-white p-4">
		<form on:submit|preventDefault={sendMessage} class="flex items-center gap-2">
			<input
				type="text"
				bind:value={message}
				placeholder="Type a message..."
				class="flex-1 rounded-full border border-gray-300 px-4 py-2 focus:ring-2 focus:ring-blue-400 focus:outline-none"
			/>
			<button
				type="submit"
				class="rounded-full bg-blue-500 px-4 py-2 text-white transition hover:bg-blue-600"
			>
				Send
			</button>
		</form>
	</footer>
</div>
