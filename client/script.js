document.getElementById('fetch-btn').addEventListener('click', async () => {
  const response = await fetch('/api/data')
  const data = await response.json()
  document.getElementById('output').textContent = JSON.stringify(data, null, 2)
})
