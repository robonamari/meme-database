addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
    if (url.hostname === 'robonamari.com') {
    const discordPath = url.pathname
    const discordUrl = `https://cdn.discordapp.com${discordPath}`
        const response = await fetch(discordUrl, {
      method: request.method,
      headers: request.headers,
    })
    return response
  }
  return fetch(request)
}
