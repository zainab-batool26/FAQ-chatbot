const messagesEl = document.getElementById('messages')
const form = document.getElementById('chat-form')
const input = document.getElementById('user-input')

function addMessage(text, sender) {
  const div = document.createElement('div')
  div.className = `message ${sender}`
  div.textContent = text
  messagesEl.appendChild(div)
  messagesEl.scrollTop = messagesEl.scrollHeight
  return div
}

async function sendMessage(text) {
  addMessage(text, 'user')
  const typing = addMessage('Typing...', 'bot')
  typing.classList.add('typing')

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text }),
    })
    const data = await response.json()
    typing.classList.remove('typing')
    typing.textContent = data.answer
  } catch (err) {
    typing.classList.remove('typing')
    typing.textContent = 'Sorry, the chat server is not responding. Check that app.py is running.'
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  const text = input.value.trim()
  if (!text) return
  input.value = ''
  sendMessage(text)
})

document.querySelectorAll('.suggestions button').forEach((btn) => {
  btn.addEventListener('click', () => sendMessage(btn.textContent))
})

addMessage('Hi! Ask me anything about our services.', 'bot')