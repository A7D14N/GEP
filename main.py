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
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">

<style>

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --purple: #1a0533;
  --deep: #0d0020;
  --orange: #ff6b00;
  --pink: #ff1d8e;
  --yellow: #ffe600;
  --teal: #00e5cc;
  --white: #ffffff;
}

body {
  background: var(--deep);
  font-family: 'Nunito', sans-serif;
  min-height: 100vh;
  overflow-x: hidden;
  color: var(--white);
}

.scene {
  position: relative;
  min-height: 100vh;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 40px 20px;
}

.stars,
.notes-float {
  position: fixed;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
}

.star {
  position: absolute;
  border-radius: 50%;
  background: white;

  animation:
    twinkle var(--dur, 3s)
    ease-in-out infinite
    var(--delay, 0s);
}

.note {
  position: absolute;
  color: var(--yellow);
  opacity: 0;

  animation:
    floatUp var(--dur, 8s)
    ease-in-out infinite
    var(--delay, 0s);
}

@keyframes twinkle {
  0%,100% {
    opacity: 0.1;
    transform: scale(1);
  }

  50% {
    opacity: 0.9;
    transform: scale(1.4);
  }
}

@keyframes floatUp {
  0% {
    opacity: 0;
    transform: translateY(0) rotate(0deg);
  }

  20% {
    opacity: 0.7;
  }

  80% {
    opacity: 0.3;
  }

  100% {
    opacity: 0;
    transform: translateY(-80vh) rotate(30deg);
  }
}

.card {
  position: relative;
  z-index: 10;

  width: 100%;
  max-width: 580px;

  padding: 48px 52px;

  border-radius: 32px;

  background: rgba(26, 5, 51, 0.82);

  border: 2px solid rgba(255, 107, 0, 0.35);

  backdrop-filter: blur(18px);

  box-shadow:
    0 0 60px rgba(255, 29, 142, 0.15),
    0 0 120px rgba(255, 107, 0, 0.08);
}

.logo-ring {
  width: 76px;
  height: 76px;

  margin: 0 auto 20px;

  border-radius: 50%;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 34px;

  background:
    linear-gradient(
      135deg,
      var(--orange),
      var(--pink)
    );

  animation: pulse 2.5s ease-in-out infinite;
}

@keyframes pulse {

  0%,100% {
    transform: scale(1);

    box-shadow:
      0 0 20px rgba(255,107,0,0.4);
  }

  50% {
    transform: scale(1.05);

    box-shadow:
      0 0 50px rgba(255,107,0,0.7),
      0 0 80px rgba(255,29,142,0.25);
  }
}

.school-name {
  text-align: center;

  color: var(--orange);

  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;

  margin-bottom: 6px;

  font-family: 'Pacifico', cursive;
}

h1 {
  text-align: center;

  margin-bottom: 10px;

  font-size: 38px;
  line-height: 1.2;

  font-family: 'Pacifico', cursive;

  background:
    linear-gradient(
      135deg,
      #fff 0%,
      var(--yellow) 50%,
      var(--orange) 100%
    );

  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tagline {
  text-align: center;

  margin-bottom: 36px;

  color: rgba(255,255,255,0.55);

  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;

  margin-bottom: 8px;

  color: var(--orange);

  font-size: 12px;
  font-weight: 800;

  text-transform: uppercase;
  letter-spacing: 0.12em;
}

input,
textarea {
  width: 100%;

  border: 1.5px solid rgba(255,255,255,0.15);
  border-radius: 14px;

  background: rgba(255,255,255,0.06);

  color: white;

  font-family: 'Nunito', sans-serif;
  font-size: 15px;
  font-weight: 600;

  padding: 14px 18px;

  outline: none;

  transition:
    border-color 0.25s,
    background 0.25s,
    box-shadow 0.25s;
}

textarea {
  min-height: 120px;
  resize: vertical;
}

input::placeholder,
textarea::placeholder {
  color: rgba(255,255,255,0.3);
}

input:focus,
textarea:focus {
  border-color: var(--orange);

  background: rgba(255,107,0,0.08);

  box-shadow:
    0 0 0 3px rgba(255,107,0,0.15);
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
  color: rgba(255,255,255,0.25);

  font-size: 11px;
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

  padding: 12px 16px;

  border-radius: 14px;

  border: 1.5px solid rgba(255,255,255,0.1);

  background: rgba(255,255,255,0.05);

  cursor: pointer;

  transition: all 0.2s;
}

.skill-option:hover {
  transform: translateX(4px);

  background: rgba(255,107,0,0.1);

  border-color: rgba(255,107,0,0.35);
}

.skill-option.selected {
  background: rgba(255,107,0,0.16);

  border-color: var(--orange);

  box-shadow:
    0 0 15px rgba(255,107,0,0.2);
}

.skill-option input {
  display: none;
}

.skill-dots {
  min-width: 90px;
}

.skill-label {
  font-size: 13px;
  font-weight: 800;
}

.skill-sub {
  margin-left: auto;

  color: rgba(255,255,255,0.45);

  font-size: 11px;
  font-weight: 700;

  text-align: right;
}

.submit-btn {
  width: 100%;

  margin-top: 30px;

  padding: 18px;

  border: none;
  border-radius: 16px;

  cursor: pointer;

  color: white;

  font-family: 'Pacifico', cursive;
  font-size: 20px;

  background:
    linear-gradient(
      135deg,
      var(--orange),
      var(--pink)
    );

  box-shadow:
    0 8px 30px rgba(255,29,142,0.35);

  transition:
    transform 0.2s,
    box-shadow 0.2s;
}

.submit-btn:hover {
  transform: translateY(-3px) scale(1.02);

  box-shadow:
    0 14px 40px rgba(255,29,142,0.45);
}

.footer-note {
  margin-top: 20px;

  text-align: center;

  color: rgba(255,255,255,0.3);

  font-size: 12px;
  font-weight: 700;
}

.footer-note span {
  color: var(--teal);
}

.success-msg {
  display: none;

  text-align: center;

  padding: 24px;
}

.success-msg .big-emoji {
  display: block;

  margin-bottom: 16px;

  font-size: 64px;
}

.success-msg h2 {
  margin-bottom: 8px;

  color: var(--yellow);

  font-size: 30px;

  font-family: 'Pacifico', cursive;
}

.success-msg p {
  color: rgba(255,255,255,0.6);

  font-size: 15px;
  font-weight: 700;
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

    <h1>
      Learn Guitar!
    </h1>

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
            id="notes-input"
            placeholder="Anything you would like me to know?"
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
          Enquiries go to
          <span>Music Of The Spheres</span>
          ✦ We'll get back to you ASAP!
        </p>

      </form>

    </div>

    <div class="success-msg" id="success-msg">

      <span class="big-emoji">🎸</span>

      <h2>
        You're a Rock Star!
      </h2>

      <p>
        Your enquiry is on its way to Music Of The Spheres.
        <br>
        We'll be in touch super soon!
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
    --delay:${Math.random()*5}s
  `;

  starsEl.appendChild(s);
}

const noteSymbols = ['♪', '♫', '♩', '♬', '♭', '♮'];

const notesEl = document.getElementById('notes');

for (let i = 0; i < 12; i++) {

  const n = document.createElement('div');

  n.className = 'note';

  n.textContent =
    noteSymbols[
      Math.floor(Math.random() * noteSymbols.length)
    ];

  n.style.cssText = `
    left:${5+Math.random()*90}%;
    top:${60+Math.random()*40}%;
    --dur:${6+Math.random()*8}s;
    --delay:${Math.random()*8}s;
    font-size:${18+Math.random()*20}px
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
    document.getElementById('notes-input').value;

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
    `Hello Music Of The Spheres!\n\n` +

    `I'd love to enquire about guitar lessons.\n\n` +

    `Name: ${name}\n` +
    `Email: ${email}\n` +
    `Phone: ${phone}\n` +
    `Guitar Skill Level: ${skillText}\n` +
    `Notes: ${notes}\n\n` +

    `Please get in touch at your earliest convenience!\n\n` +

    `Best wishes,\n${name}`
  );

  window.location.href =
    `mailto:hiokardian@gmail.com?subject=${subject}&body=${body}`;

  document.getElementById('form-content').style.display = 'none';

  document.getElementById('success-msg').style.display = 'block';
});

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=1400,
    scrolling=False
)