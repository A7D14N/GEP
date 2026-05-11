import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Learn Guitar — Music Of The Spheres",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8" />
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0, maximum-scale=1.0"
/>

<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">

<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  min-height: 100%;
  overflow-x: hidden;
  background: #0d0020;
  font-family: 'Nunito', sans-serif;
  color: white;
}

:root {
  --orange: #ff6b00;
  --pink: #ff1d8e;
  --yellow: #ffe600;
  --teal: #00e5cc;
  --white: #ffffff;
}

body {
  position: relative;
}

.scene {
  width: 100%;
  min-height: 100vh;
  padding: 24px 16px 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.stars,
.notes-float {
  position: fixed;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.star {
  position: absolute;
  background: white;
  border-radius: 50%;
  animation: twinkle var(--dur) ease-in-out infinite var(--delay);
}

.note {
  position: absolute;
  color: var(--yellow);
  opacity: 0;
  animation: floatUp var(--dur) ease-in-out infinite var(--delay);
}

@keyframes twinkle {
  0%,100% {
    opacity: 0.1;
    transform: scale(1);
  }

  50% {
    opacity: 0.9;
    transform: scale(1.5);
  }
}

@keyframes floatUp {
  0% {
    opacity: 0;
    transform: translateY(0);
  }

  20% {
    opacity: 0.7;
  }

  100% {
    opacity: 0;
    transform: translateY(-90vh) rotate(25deg);
  }
}

.card {
  position: relative;
  z-index: 10;

  width: 100%;
  max-width: 560px;

  background: rgba(26,5,51,0.85);
  backdrop-filter: blur(18px);

  border: 2px solid rgba(255,107,0,0.3);

  border-radius: 28px;

  padding: 42px 32px;

  box-shadow:
    0 0 40px rgba(255,29,142,0.15),
    0 0 90px rgba(255,107,0,0.1);
}

.logo-ring {
  width: 74px;
  height: 74px;

  margin: 0 auto 20px;

  border-radius: 50%;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 34px;

  background: linear-gradient(
    135deg,
    var(--orange),
    var(--pink)
  );

  animation: pulse 2.5s ease-in-out infinite;
}

@keyframes pulse {

  0%,100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.06);
  }
}

.school-name {
  text-align: center;
  color: var(--orange);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 8px;
}

h1 {
  font-family: 'Pacifico', cursive;
  font-size: 38px;
  text-align: center;
  line-height: 1.15;
  margin-bottom: 12px;

  background: linear-gradient(
    135deg,
    white,
    var(--yellow),
    var(--orange)
  );

  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tagline {
  text-align: center;
  color: rgba(255,255,255,0.6);
  font-size: 14px;
  margin-bottom: 34px;
}

.form-group {
  margin-bottom: 18px;
}

label {
  display: block;
  margin-bottom: 8px;

  color: var(--orange);

  font-size: 12px;
  font-weight: 800;

  text-transform: uppercase;
  letter-spacing: 0.1em;
}

input,
textarea {
  width: 100%;

  background: rgba(255,255,255,0.06);

  border: 1.5px solid rgba(255,255,255,0.12);

  border-radius: 14px;

  padding: 15px 16px;

  color: white;

  font-size: 16px;

  outline: none;

  transition: 0.2s;
}

textarea {
  min-height: 120px;
  resize: vertical;
}

input:focus,
textarea:focus {
  border-color: var(--orange);

  background: rgba(255,107,0,0.08);

  box-shadow: 0 0 0 3px rgba(255,107,0,0.15);
}

input::placeholder,
textarea::placeholder {
  color: rgba(255,255,255,0.3);
}

.divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 28px 0;
}

.divider-line {
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,0.1);
}

.divider-text {
  font-size: 11px;
  color: rgba(255,255,255,0.3);
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.skill-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.skill-option {
  display: flex;
  align-items: center;
  gap: 12px;

  background: rgba(255,255,255,0.05);

  border: 1.5px solid rgba(255,255,255,0.08);

  border-radius: 14px;

  padding: 14px 16px;

  cursor: pointer;

  transition: 0.2s;
}

.skill-option:hover {
  border-color: rgba(255,107,0,0.4);
  background: rgba(255,107,0,0.08);
}

.skill-option.selected {
  border-color: var(--orange);
  background: rgba(255,107,0,0.14);
}

.skill-option input {
  display: none;
}

.skill-dots {
  min-width: 80px;
}

.skill-label {
  font-size: 14px;
  font-weight: 700;
}

.skill-sub {
  margin-left: auto;
  font-size: 11px;
  color: rgba(255,255,255,0.45);
}

.submit-btn {
  width: 100%;

  margin-top: 30px;

  border: none;
  border-radius: 16px;

  padding: 18px;

  cursor: pointer;

  font-size: 18px;
  font-family: 'Pacifico', cursive;

  color: white;

  background: linear-gradient(
    135deg,
    var(--orange),
    var(--pink)
  );

  box-shadow: 0 10px 30px rgba(255,29,142,0.35);

  transition: 0.2s;
}

.submit-btn:hover {
  transform: translateY(-2px);
}

.footer-note {
  margin-top: 20px;
  text-align: center;
  font-size: 12px;
  color: rgba(255,255,255,0.35);
}

.success-msg {
  display: none;
  text-align: center;
  padding: 24px 0;
}

.success-msg h2 {
  margin: 16px 0 10px;
  color: var(--yellow);
  font-family: 'Pacifico', cursive;
}

.success-msg p {
  color: rgba(255,255,255,0.6);
}

.big-emoji {
  font-size: 62px;
}

@media (max-width: 640px) {

  .scene {
    padding: 14px 12px 40px;
    align-items: flex-start;
  }

  .card {
    padding: 28px 20px;
    border-radius: 24px;
  }

  h1 {
    font-size: 30px;
  }

  .skill-option {
    flex-direction: column;
    align-items: flex-start;
  }

  .skill-sub {
    margin-left: 0;
  }

  .submit-btn {
    font-size: 16px;
  }
}

</style>
</head>

<body>

<div class="stars" id="stars"></div>
<div class="notes-float" id="notes"></div>

<div class="scene">

<div class="card">

<div class="logo-ring">🎸</div>

<p class="school-name">
Music Of The Spheres
</p>

<h1>Learn Guitar!</h1>

<p class="tagline">
School of Improvisation ✦ Enquire Below
</p>

<div id="form-content">

<form id="guitar-form">

<div class="form-group">
<label>Your Name</label>

<input
type="text"
id="name"
placeholder="Enter your name"
required
>
</div>

<div class="form-group">
<label>Email Address</label>

<input
type="email"
id="email"
placeholder="yourname@example.com"
required
>
</div>

<div class="form-group">
<label>Phone Number</label>

<input
type="tel"
id="phone"
placeholder="+44 7000 000000"
required
>
</div>

<div class="form-group">
<label>Notes</label>

<textarea
id="notesInput"
placeholder="Anything you'd like me to know?"
></textarea>
</div>

<div class="divider">
<div class="divider-line"></div>

<div class="divider-text">
Your Guitar Level
</div>

<div class="divider-line"></div>
</div>

<div class="skill-options">

<label class="skill-option">
<input type="radio" name="skill" value="beginner">

<span class="skill-dots">🎸</span>

<span class="skill-label">
Total Beginner
</span>

<span class="skill-sub">
Never played!
</span>
</label>

<label class="skill-option">
<input type="radio" name="skill" value="novice">

<span class="skill-dots">🎸🎸</span>

<span class="skill-label">
Know a Few Chords
</span>

<span class="skill-sub">
G, C & D squad
</span>
</label>

<label class="skill-option">
<input type="radio" name="skill" value="intermediate">

<span class="skill-dots">🎸🎸🎸</span>

<span class="skill-label">
Intermediate Jammer
</span>

<span class="skill-sub">
Campfire hero
</span>
</label>

<label class="skill-option">
<input type="radio" name="skill" value="advanced">

<span class="skill-dots">🎸🎸🎸🎸</span>

<span class="skill-label">
Advanced Player
</span>

<span class="skill-sub">
Solos & scales
</span>
</label>

<label class="skill-option">
<input type="radio" name="skill" value="god">

<span class="skill-dots">🎸🎸🎸🎸🎸</span>

<span class="skill-label">
Shredding God
</span>

<span class="skill-sub">
Why are you here?!
</span>
</label>

</div>

<button type="submit" class="submit-btn">
🎵 Send My Enquiry!
</button>

<p class="footer-note">
Music Of The Spheres ✦ We'll reply ASAP
</p>

</form>
</div>

<div class="success-msg" id="success-msg">

<div class="big-emoji">
🎸
</div>

<h2>
You're a Rock Star!
</h2>

<p>
Your enquiry has been sent.
<br>
We'll be in touch soon.
</p>

</div>
</div>
</div>

<script>

const starsEl = document.getElementById('stars');

for (let i = 0; i < 80; i++) {

  const s = document.createElement('div');

  s.className = 'star';

  const size = Math.random() * 3 + 1;

  s.style.cssText = `
    width:${size}px;
    height:${size}px;
    left:${Math.random()*100}%;
    top:${Math.random()*100}%;
    --dur:${2+Math.random()*4}s;
    --delay:${Math.random()*5}s;
  `;

  starsEl.appendChild(s);
}

const notesEl = document.getElementById('notes');

const noteSymbols = ['♪','♫','♩','♬'];

for (let i = 0; i < 12; i++) {

  const n = document.createElement('div');

  n.className = 'note';

  n.textContent =
    noteSymbols[
      Math.floor(Math.random()*noteSymbols.length)
    ];

  n.style.cssText = `
    left:${Math.random()*100}%;
    top:${70+Math.random()*30}%;
    font-size:${18+Math.random()*18}px;
    --dur:${6+Math.random()*8}s;
    --delay:${Math.random()*8}s;
  `;

  notesEl.appendChild(n);
}

document
.querySelectorAll('.skill-option')
.forEach(opt => {

  opt.addEventListener('click', () => {

    document
    .querySelectorAll('.skill-option')
    .forEach(o => o.classList.remove('selected'));

    opt.classList.add('selected');

    opt.querySelector('input').checked = true;
  });
});

document
.getElementById('guitar-form')
.addEventListener('submit', function(e) {

  e.preventDefault();

  const name =
    document.getElementById('name').value;

  const email =
    document.getElementById('email').value;

  const phone =
    document.getElementById('phone').value;

  const notes =
    document.getElementById('notesInput').value;

  const skill =
    document.querySelector(
      'input[name="skill"]:checked'
    );

  const skillLabels = {
    beginner: 'Total Beginner 🎸',
    novice: 'Know a Few Chords 🎸🎸',
    intermediate: 'Intermediate Jammer 🎸🎸🎸',
    advanced: 'Advanced Player 🎸🎸🎸🎸',
    god: 'Shredding God 🎸🎸🎸🎸🎸'
  };

  const skillText =
    skill
    ? skillLabels[skill.value]
    : 'Not specified';

  const subject = encodeURIComponent(
    `Guitar Lesson Enquiry — ${name}`
  );

  const body = encodeURIComponent(

`Hello Music Of The Spheres!

I'd love to enquire about guitar lessons.

Name: ${name}
Email: ${email}
Phone: ${phone}

Guitar Skill Level:
${skillText}

Notes:
${notes}

Best wishes,
${name}`

  );

  window.location.href =
`mailto:mizarolli@icloud.com?subject=${subject}&body=${body}`;

  document.getElementById(
    'form-content'
  ).style.display = 'none';

  document.getElementById(
    'success-msg'
  ).style.display = 'block';
});

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=1400,
    scrolling=True
)