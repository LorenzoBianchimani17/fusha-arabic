# Fusha - Modern Standard Arabic

One self-contained page. No build step, no dependencies, no server code.

## Putting it online

Any static host works. The only thing that matters is that it is served
as a normal page over HTTPS, not embedded in someone else's iframe,
because the microphone is refused inside a frame.

**Render** - New > Static Site > connect this repo.
  Build command: leave empty.
  Publish directory: `.`

**Netlify Drop** - drag this folder onto https://app.netlify.com/drop.
  No account needed, no repo needed.

**GitHub Pages** - push, then Settings > Pages > deploy from branch, root.

## What needs what

- Reading, games, conversations, progress: nothing. Works offline once loaded.
- Hearing the phrases: an Arabic voice installed on the device.
- Speaking into it: HTTPS, a top-level page, and Safari or Chrome.
  On iOS also check Settings > General > Keyboard > Enable Dictation.

Progress lives in the browser's local storage. The backup code at the
bottom of the home screen moves it between devices.
