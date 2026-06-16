"""Music Of The Spheres - Guitar Lesson Enquiry Form."""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Learn Guitar - Music Of The Spheres",
    page_icon="\U0001F3B8",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu, header, footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"] { display: none !important; }
        .block-container { padding: 0 !important; max-width: 100% !important; gap: 0 !important; }
        .stApp { background: #0d0020; }
        section.main > div:first-child { padding-top: 0 !important; padding-bottom: 0 !important; }
        iframe { width: 100% !important; border: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=5.0">
<meta name="theme-color" content="#0d0020">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="format-detection" content="telephone=no">
<title>Learn Guitar - Music Of The Spheres</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

:root {
    --deep: #0d0020; --orange: #ff6b00; --pink: #ff1d8e; --yellow: #ffe600;
    --safe-top:    env(safe-area-inset-top, 0px);
    --safe-bottom: env(safe-area-inset-bottom, 0px);
    --safe-left:   env(safe-area-inset-left, 0px);
    --safe-right:  env(safe-area-inset-right, 0px);
}

html { width: 100%; -webkit-text-size-adjust: 100%; -webkit-overflow-scrolling: touch; scroll-behavior: smooth; }

body {
    width: 100%;
    min-height: 100vh; min-height: 100dvh;
    background: var(--deep);
    font-family: 'Nunito', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    color: white; overflow-x: hidden; position: relative;
    -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
    overscroll-behavior-y: contain; touch-action: manipulation;
    padding: var(--safe-top) var(--safe-right) var(--safe-bottom) var(--safe-left);
}

.stars { position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 0; }
.star {
    position: absolute; background: white; border-radius: 50%;
    animation: twinkle var(--dur) ease-in-out infinite var(--delay);
    will-change: opacity, transform;
}
@keyframes twinkle { 0%, 100% { opacity: 0.1; transform: scale(1); } 50% { opacity: 0.9; transform: scale(1.5); } }

.scene {
    position: relative; width: 100%;
    min-height: calc(100vh - var(--safe-top) - var(--safe-bottom));
    min-height: calc(100dvh - var(--safe-top) - var(--safe-bottom));
    padding: 20px 14px 50px;
    display: flex; justify-content: center; align-items: flex-start; z-index: 1;
}

.card {
    position: relative; width: 100%; max-width: 560px;
    background: rgba(26, 5, 51, 0.88);
    -webkit-backdrop-filter: blur(18px); backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 107, 0, 0.25); border-radius: 28px; padding: 42px 32px;
    box-shadow: 0 0 40px rgba(255, 29, 142, 0.12), 0 0 90px rgba(255, 107, 0, 0.08);
    animation: cardIn 0.6s ease-out;
}
@keyframes cardIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

.logo-ring {
    width: 74px; height: 74px; margin: 0 auto 20px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center; font-size: 34px;
    background: linear-gradient(135deg, var(--orange), var(--pink));
    box-shadow: 0 8px 24px rgba(255, 29, 142, 0.4);
    animation: pulse 3s ease-in-out infinite;
}
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }

.school-name { text-align: center; color: var(--orange); font-size: 12px; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 8px; }

h1 {
    font-family: 'Pacifico', cursive; font-size: 38px; text-align: center; line-height: 1.15; margin-bottom: 12px;
    background: linear-gradient(135deg, white, var(--yellow), var(--orange));
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}

.tagline { text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 14px; margin-bottom: 34px; }

.form-group { margin-bottom: 18px; }
label { display: block; margin-bottom: 8px; color: var(--orange); font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; }

input, textarea {
    width: 100%; border: 1px solid rgba(255, 255, 255, 0.12); background: rgba(255, 255, 255, 0.06);
    border-radius: 14px; padding: 15px 16px; color: white; font-size: 16px;
    font-family: inherit; outline: none; -webkit-appearance: none; appearance: none;
    transition: border-color 0.2s, background 0.2s, box-shadow 0.2s; touch-action: manipulation;
}
input:focus, textarea:focus { border-color: var(--orange); background: rgba(255, 255, 255, 0.08); box-shadow: 0 0 0 3px rgba(255, 107, 0, 0.15); }
input::placeholder, textarea::placeholder { color: rgba(255, 255, 255, 0.35); }
textarea { min-height: 120px; resize: vertical; }

.skill-options { display: flex; flex-direction: column; gap: 10px; margin-top: 20px; }
.skill-option {
    display: flex; align-items: center; gap: 12px; padding: 14px 16px; min-height: 52px;
    border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.05); cursor: pointer;
    transition: transform 0.15s, border-color 0.2s, background 0.2s;
    -webkit-user-select: none; user-select: none; touch-action: manipulation; position: relative;
}
.skill-option:active { transform: scale(0.98); }
.skill-option.selected { border-color: var(--orange); background: rgba(255, 107, 0, 0.14); box-shadow: inset 0 0 0 1px var(--orange); }
.skill-option input { position: absolute; opacity: 0; pointer-events: none; width: 1px; height: 1px; margin: 0; }
.skill-option span { flex: 1; }

.submit-btn {
    width: 100%; margin-top: 30px; border: none; border-radius: 16px; padding: 18px; cursor: pointer;
    font-size: 18px; font-family: 'Pacifico', cursive; color: white;
    background: linear-gradient(135deg, var(--orange), var(--pink));
    -webkit-appearance: none; appearance: none; min-height: 56px; touch-action: manipulation;
    transition: transform 0.15s, opacity 0.2s, box-shadow 0.2s;
    box-shadow: 0 8px 24px rgba(255, 29, 142, 0.3); position: relative;
}
.submit-btn:active:not(:disabled) { transform: scale(0.98); }
.submit-btn:disabled { opacity: 0.7; cursor: not-allowed; }
.submit-btn.loading::after {
    content: ''; position: absolute; right: 20px; top: 50%; width: 20px; height: 20px; margin-top: -10px;
    border: 2px solid rgba(255, 255, 255, 0.3); border-top-color: white; border-radius: 50%;
    animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.footer-note { margin-top: 20px; text-align: center; font-size: 12px; color: rgba(255, 255, 255, 0.35); }

.thank-you {
    position: fixed; inset: 0; z-index: 9999;
    background: rgba(13, 0, 32, 0.95);
    -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px);
    display: flex; align-items: center; justify-content: center;
    padding: max(24px, var(--safe-top)) max(24px, var(--safe-right)) max(24px, var(--safe-bottom)) max(24px, var(--safe-left));
    opacity: 0; pointer-events: none; transition: opacity 0.4s;
}
.thank-you.show { opacity: 1; pointer-events: auto; }
.thank-you-content { text-align: center; max-width: 400px; width: 100%; animation: popIn 0.5s ease-out; }
@keyframes popIn { 0% { transform: scale(0.5); opacity: 0; } 60% { transform: scale(1.05); opacity: 1; } 100% { transform: scale(1); opacity: 1; } }
.thank-you-icon { font-size: 80px; margin-bottom: 20px; display: inline-block; animation: bounce 1.5s ease-in-out infinite; }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
.thank-you h2 {
    font-family: 'Pacifico', cursive; font-size: 32px; margin-bottom: 16px; line-height: 1.2;
    background: linear-gradient(135deg, white, var(--yellow), var(--orange));
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.thank-you p { color: rgba(255, 255, 255, 0.85); font-size: 16px; line-height: 1.5; margin-bottom: 12px; }
.thank-you p strong { color: white; font-weight: 800; }
.redirect-note { color: var(--orange) !important; font-size: 14px; font-weight: 700; margin-top: 24px !important; }
.progress-bar { width: 100%; max-width: 240px; height: 4px; background: rgba(255, 255, 255, 0.1); border-radius: 2px; margin: 20px auto 0; overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--orange), var(--pink)); border-radius: 2px; transform-origin: left; animation: progress 2.5s linear forwards; }
@keyframes progress { from { transform: scaleX(0); } to { transform: scaleX(1); } }

@media (max-width: 640px) {
    .card { padding: 26px 18px; border-radius: 22px; }
    h1 { font-size: 30px; }
    .scene { padding: 14px 12px 40px; }
    .logo-ring { width: 64px; height: 64px; font-size: 28px; }
    .skill-option { padding: 12px 14px; min-height: 48px; }
    .submit-btn { font-size: 17px; padding: 16px; }
    .thank-you h2 { font-size: 26px; }
    .thank-you-icon { font-size: 64px; }
}
@media (max-width: 380px) {
    .card { padding: 22px 14px; }
    h1 { font-size: 26px; }
    .skill-option { font-size: 14px; }
    .tagline { font-size: 13px; }
}
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
</style>
</head>
<body>
<div class="stars" id="stars"></div>
<div class="scene">
    <div class="card">
        <div class="logo-ring" aria-hidden="true">&#127928;</div>
        <p class="school-name">Music Of The Spheres</p>
        <h1>Learn Guitar!</h1>
        <p class="tagline">School of Improvisation &#10022; Enquire Below</p>

        <form id="guitar-form"
              action="https://formsubmit.co/your-email@example.com"
              method="POST"
              autocomplete="on">

            <input type="hidden" name="_next" value="https://www.mizarolli.net/">
            <input type="hidden" name="_subject" value="New Guitar Lesson Enquiry">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_captcha" value="false">

            <div class="form-group">
                <label for="name">Your Name</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required autocomplete="name" autocapitalize="words">
            </div>

            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="yourname@example.com" required autocomplete="email" inputmode="email" autocapitalize="none" spellcheck="false">
            </div>

            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="+44 7000 000000" required autocomplete="tel" inputmode="tel">
            </div>

            <div class="form-group">
                <label for="notes">Notes</label>
                <textarea id="notes" name="notes" placeholder="Anything you'd like me to know?" autocomplete="off"></textarea>
            </div>

            <div class="skill-options" role="radiogroup" aria-label="Skill level">
                <label class="skill-option"><input type="radio" name="skill" value="Total Beginner" required><span>&#127928; Total Beginner</span></label>
                <label class="skill-option"><input type="radio" name="skill" value="Know a Few Chords"><span>&#127928;&#127928; Know a Few Chords</span></label>
                <label class="skill-option"><input type="radio" name="skill" value="Intermediate Jammer"><span>&#127928;&#127928;&#127928; Intermediate Jammer</span></label>
                <label class="skill-option"><input type="radio" name="skill" value="Advanced Player"><span>&#127928;&#127928;&#127928;&#127928; Advanced Player</span></label>
                <label class="skill-option"><input type="radio" name="skill" value="Shredding God"><span>&#127928;&#127928;&#127928;&#127928;&#127928; Shredding God</span></label>
            </div>

            <button type="submit" class="submit-btn" id="submit-btn">&#127925; Send My Enquiry!</button>
            <p class="footer-note">Music Of The Spheres &#10022; We'll reply ASAP</p>
        </form>
    </div>
</div>

<div class="thank-you" id="thank-you" role="alertdialog" aria-live="assertive" aria-labelledby="thank-you-title">
    <div class="thank-you-content">
        <div class="thank-you-icon" aria-hidden="true">&#127881;</div>
        <h2 id="thank-you-title">Thank You Very Much!</h2>
        <p><strong>Mizarolli will contact you</strong> as soon as possible.</p>
        <p>Get ready to start your guitar journey! &#127928;</p>
        <p class="redirect-note">Redirecting you to mizarolli.net...</p>
        <div class="progress-bar" aria-hidden="true"><div class="progress-fill"></div></div>
    </div>
</div>

<script>
(function () {
    'use strict';

    var FORM_ENDPOINT     = 'https://formsubmit.co/ajax/your-email@example.com';
    var REDIRECT_URL      = 'https://www.mizarolli.net/';
    var REDIRECT_DELAY_MS = 2800;

    var starsEl     = document.getElementById('stars');
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var STAR_COUNT   = reduceMotion ? 25 : 80;

    for (var i = 0; i < STAR_COUNT; i++) {
        var s    = document.createElement('div');
        s.className = 'star';
        var size = Math.random() * 3 + 1;
        s.style.cssText =
            'width:' + size + 'px;' +
            'height:' + size + 'px;' +
            'left:' + (Math.random() * 100) + '%;' +
            'top:' + (Math.random() * 100) + '%;' +
            '--dur:' + (2 + Math.random() * 4) + 's;' +
            '--delay:' + (Math.random() * 5) + 's;';
        starsEl.appendChild(s);
    }

    var skillOptions = document.querySelectorAll('.skill-option');
    skillOptions.forEach(function (opt) {
        opt.addEventListener('click', function (e) {
            e.preventDefault();
            skillOptions.forEach(function (o) { o.classList.remove('selected'); });
            opt.classList.add('selected');
            var radio = opt.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

    var form      = document.getElementById('guitar-form');
    var submitBtn = document.getElementById('submit-btn');
    var thankYou  = document.getElementById('thank-you');

    form.addEventListener('submit', async function (e) {
        if (!form.checkValidity()) { form.reportValidity(); return; }
        e.preventDefault();

        if (!form.querySelector('input[name="skill"]:checked')) {
            var firstOpt = skillOptions[0];
            if (firstOpt) {
                firstOpt.scrollIntoView({ behavior: 'smooth', block: 'center' });
                skillOptions.forEach(function (o) {
                    o.style.transition = 'border-color 0.3s';
                    o.style.borderColor = '#ff1d8e';
                    setTimeout(function () { o.style.borderColor = ''; }, 1200);
                });
            }
            return;
        }

        submitBtn.classList.add('loading');
        submitBtn.disabled = true;
        submitBtn.setAttribute('aria-busy', 'true');
        submitBtn.textContent = 'Sending...';

        var data = {};
        new FormData(form).forEach(function (v, k) { data[k] = v; });

        try {
            await fetch(FORM_ENDPOINT, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify(data)
            });
        } catch (err) {
            console.warn('Form submit warning:', err);
        }

        thankYou.classList.add('show');
        document.body.style.overflow = 'hidden';
        setTimeout(function () { navigateTo(REDIRECT_URL); }, REDIRECT_DELAY_MS);
    });

    function navigateTo(url) {
        try { window.top.location.replace(url); return; }    catch (e) {}
        try { window.parent.location.replace(url); return; } catch (e) {}
        try { window.location.replace(url); return; }         catch (e) {}
        var a = document.createElement('a');
        a.href = url;
        a.textContent = 'Tap here to continue ->';
        a.style.cssText = 'display:inline-block;margin-top:20px;color:#ff6b00;font-weight:800;text-decoration:none;padding:14px 22px;border:1px solid #ff6b00;border-radius:12px;';
        thankYou.querySelector('.thank-you-content').appendChild(a);
    }

    function setupStreamlitKeepAlive() {
        try {
            if (window.parent && window.parent !== window) {
                setInterval(function () {
                    fetch('/_stcore/health', { cache: 'no-store' }).catch(function () {});
                }, 25000);
            }
        } catch (e) {}
    }
    setupStreamlitKeepAlive();
})();
</script>
</body>
</html>"""

components.html(HTML, height=1000, scrolling=True)
