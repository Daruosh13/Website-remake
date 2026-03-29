with open('C:/Users/M. Gustave/piksort/resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Replace the redirect gate script with a no-op ──────────────────────
OLD_GATE = '''<!-- Gate -->
<script>
(function(){
  if(localStorage.getItem('piksort_subscribed')!=='true'){
    document.body.style.visibility='hidden';
    window.location.replace('subscribe.html');
  }else{
    document.body.style.visibility='visible';
  }
})();
</script>'''

NEW_GATE = '<!-- Gate handled by modal below -->'

if OLD_GATE not in content:
    print("ERROR: gate script not found"); exit(1)

content = content.replace(OLD_GATE, NEW_GATE, 1)

# ── 2. Modal CSS + HTML + JS to inject just before </body> ─────────────────
MODAL_BLOCK = '''
<!-- ══════════════ SUBSCRIBE MODAL ══════════════ -->
<style>
  /* Backdrop */
  #sub-modal-backdrop {
    position: fixed; inset: 0; z-index: 9000;
    background: rgba(10,10,20,0.7);
    backdrop-filter: blur(4px);
    display: flex; align-items: center; justify-content: center;
    padding: 1rem;
    opacity: 0; transition: opacity 0.3s ease;
    pointer-events: none;
  }
  #sub-modal-backdrop.visible {
    opacity: 1; pointer-events: all;
  }

  /* Modal card */
  #sub-modal {
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    width: 100%;
    max-width: 880px;
    max-height: 92vh;
    overflow-y: auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    box-shadow: 0 32px 80px rgba(0,0,0,0.35);
    transform: translateY(20px) scale(0.98);
    transition: transform 0.3s ease;
  }
  #sub-modal-backdrop.visible #sub-modal {
    transform: translateY(0) scale(1);
  }

  /* Left panel */
  .sm-left {
    background: #0d0d0d;
    padding: 3rem 2.5rem;
    display: flex; flex-direction: column; justify-content: center;
    position: relative; overflow: hidden;
  }
  .sm-left::before {
    content: '';
    position: absolute; inset: 0;
    background: url('https://cdn.prod.website-files.com/691d7e1194f0dd76c4566fff/698bcab485064aec3e71d462_Gemini_Generated_Image_z37ko1z37ko1z37k.webp') center/cover no-repeat;
    opacity: 0.15;
  }
  .sm-left-inner { position: relative; z-index: 1; }
  .sm-badge {
    display: inline-flex; align-items: center; gap: 0.4rem;
    background: rgba(71,108,255,0.15); border: 1px solid rgba(71,108,255,0.3);
    color: #8fa5ff; font-size: 0.68rem; font-weight: 700;
    letter-spacing: 0.08em; text-transform: uppercase;
    padding: 0.3rem 0.75rem; border-radius: 100px; margin-bottom: 1.25rem;
  }
  .sm-left h2 {
    font-size: clamp(1.25rem, 2.5vw, 1.75rem);
    font-weight: 800; color: #fff; line-height: 1.2; margin-bottom: 1rem;
  }
  .sm-left h2 span { color: #8fa5ff; }
  .sm-left p {
    color: rgba(255,255,255,0.6); font-size: 0.85rem;
    line-height: 1.65; margin-bottom: 1.5rem; max-width: 340px;
  }
  .sm-benefits { display: flex; flex-direction: column; gap: 0.6rem; margin-bottom: 1.75rem; }
  .sm-benefit {
    display: flex; align-items: center; gap: 0.65rem;
    color: rgba(255,255,255,0.82); font-size: 0.82rem; font-weight: 500;
  }
  .sm-benefit-icon {
    width: 22px; height: 22px; border-radius: 50%;
    background: rgba(71,108,255,0.22); color: #8fa5ff;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem; flex-shrink: 0;
  }
  .sm-counts {
    display: flex; gap: 1.5rem;
    padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);
  }
  .sm-count-num { font-size: 1.4rem; font-weight: 800; color: #fff; display: block; }
  .sm-count-label { font-size: 0.65rem; color: rgba(255,255,255,0.45); text-transform: uppercase; letter-spacing: 0.06em; }

  /* Right panel */
  .sm-right {
    padding: 3rem 2.5rem;
    display: flex; flex-direction: column; justify-content: center;
    background: #fff;
  }
  .sm-right h3 { font-size: 1.3rem; font-weight: 700; color: #0d0d0d; margin-bottom: 0.3rem; }
  .sm-subtitle { color: #6b6b75; font-size: 0.85rem; margin-bottom: 1.5rem; }

  .sm-form { display: flex; flex-direction: column; gap: 0.9rem; }
  .sm-group { display: flex; flex-direction: column; gap: 0.3rem; }
  .sm-group label {
    font-size: 0.72rem; font-weight: 700; color: #2c2c35;
    letter-spacing: 0.04em; text-transform: uppercase;
  }
  .sm-group input {
    padding: 0.75rem 0.9rem;
    border: 1.5px solid #e4e4ec; border-radius: 0.5rem;
    font-family: 'Montserrat', sans-serif; font-size: 0.875rem;
    color: #0d0d0d; background: #fafafa;
    outline: none; transition: border-color 0.2s, box-shadow 0.2s;
  }
  .sm-group input:focus {
    border-color: #476CFF; background: #fff;
    box-shadow: 0 0 0 3px rgba(71,108,255,0.08);
  }
  .sm-group input.sm-err { border-color: #e53e3e; }
  .sm-field-err { font-size: 0.72rem; color: #e53e3e; display: none; }
  .sm-group.has-error .sm-field-err { display: block; }

  .sm-checkbox-row {
    display: flex; align-items: flex-start; gap: 0.65rem;
    padding: 0.85rem; background: #f3f3f6;
    border: 1px solid #e4e4ec; border-radius: 0.5rem;
  }
  .sm-checkbox-row input[type="checkbox"] {
    width: 15px; height: 15px; margin-top: 2px;
    accent-color: #476CFF; flex-shrink: 0;
  }
  .sm-checkbox-row label { font-size: 0.8rem; color: #2c2c35; line-height: 1.5; cursor: pointer; }
  .sm-checkbox-row label strong { color: #0d0d0d; }

  .sm-submit {
    display: flex; align-items: center; justify-content: center; gap: 0.5rem;
    padding: 0.85rem 1.5rem;
    background: #476CFF; color: #fff;
    font-family: 'Montserrat', sans-serif; font-size: 0.875rem; font-weight: 700;
    border: none; border-radius: 0.5rem; cursor: pointer;
    transition: background 0.2s, box-shadow 0.15s;
  }
  .sm-submit:hover { background: #2d4fd4; box-shadow: 0 4px 16px rgba(71,108,255,0.3); }
  .sm-privacy { font-size: 0.7rem; color: #6b6b75; text-align: center; line-height: 1.5; }

  /* Success state inside modal */
  .sm-success {
    display: none; flex-direction: column;
    align-items: center; text-align: center; gap: 0.85rem; padding: 1rem;
  }
  .sm-success.visible { display: flex; }
  .sm-success-icon {
    width: 56px; height: 56px; background: #e8f0fe; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    color: #476CFF; font-size: 1.4rem;
  }
  .sm-success h3 { font-size: 1.3rem; font-weight: 700; color: #0d0d0d; }
  .sm-success p { color: #6b6b75; font-size: 0.875rem; }
  .sm-success-btn {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: #476CFF; color: #fff; padding: 0.75rem 1.5rem;
    border-radius: 0.5rem; border: none; cursor: pointer;
    font-family: 'Montserrat', sans-serif; font-size: 0.875rem; font-weight: 700;
    transition: background 0.2s;
  }
  .sm-success-btn:hover { background: #2d4fd4; }

  /* Responsive */
  @media (max-width: 700px) {
    #sub-modal { grid-template-columns: 1fr; max-height: 96vh; }
    .sm-left { display: none; }
    .sm-right { padding: 2rem 1.5rem; }
  }
</style>

<div id="sub-modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="sm-title">
  <div id="sub-modal">

    <!-- Left: value prop -->
    <div class="sm-left">
      <div class="sm-left-inner">
        <div class="sm-badge">&#10003; Free Resource Hub</div>
        <h2 id="sm-title">Unlock <span>442 Free Templates</span> &amp; Checklists</h2>
        <p>Curated from real WA construction projects — anonymised, deduplicated, and ready to use.</p>
        <div class="sm-benefits">
          <div class="sm-benefit"><div class="sm-benefit-icon">&#10003;</div><span>77 ITP templates across 8 disciplines</span></div>
          <div class="sm-benefit"><div class="sm-benefit-icon">&#10003;</div><span>365 ITR checklists — RTIO &amp; Daruosh verified</span></div>
          <div class="sm-benefit"><div class="sm-benefit-icon">&#10003;</div><span>Podcast episodes on construction delivery</span></div>
          <div class="sm-benefit"><div class="sm-benefit-icon">&#10003;</div><span>Fully anonymised — no client or project refs</span></div>
          <div class="sm-benefit"><div class="sm-benefit-icon">&#10003;</div><span>New resources added regularly</span></div>
        </div>
        <div class="sm-counts">
          <div><span class="sm-count-num">442</span><span class="sm-count-label">Resources</span></div>
          <div><span class="sm-count-num">8</span><span class="sm-count-label">Disciplines</span></div>
          <div><span class="sm-count-num">100%</span><span class="sm-count-label">Free</span></div>
        </div>
      </div>
    </div>

    <!-- Right: form -->
    <div class="sm-right">

      <div id="sm-form-state">
        <h3>Get Instant Access</h3>
        <p class="sm-subtitle">Enter your details and we\'ll unlock the full library immediately.</p>
        <form class="sm-form" id="sm-form" novalidate>

          <div class="sm-group" id="sm-g-name">
            <label for="sm-name">Full Name</label>
            <input type="text" id="sm-name" placeholder="Jane Smith" autocomplete="name"/>
            <span class="sm-field-err">Please enter your full name.</span>
          </div>

          <div class="sm-group" id="sm-g-email">
            <label for="sm-email">Work Email</label>
            <input type="email" id="sm-email" placeholder="jane@yourcompany.com.au" autocomplete="email"/>
            <span class="sm-field-err">Please use your work email (not Gmail, Hotmail etc.).</span>
          </div>

          <div class="sm-group" id="sm-g-mobile">
            <label for="sm-mobile">Mobile Number</label>
            <input type="tel" id="sm-mobile" placeholder="+61 4xx xxx xxx" autocomplete="tel"/>
            <span class="sm-field-err">Please enter your mobile number.</span>
          </div>

          <div class="sm-group" id="sm-g-role">
            <label for="sm-role">Your Role</label>
            <input type="text" id="sm-role" placeholder="e.g. Project Manager, QA Engineer" autocomplete="organization-title"/>
            <span class="sm-field-err">Please enter your role.</span>
          </div>

          <div class="sm-checkbox-row">
            <input type="checkbox" id="sm-updates" checked/>
            <label for="sm-updates"><strong>Keep me updated</strong> — notify me when Piksort releases new templates, quality tools, and resources.</label>
          </div>

          <button type="submit" class="sm-submit">
            Unlock the Library
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>

          <p class="sm-privacy">&#128274; We respect your privacy. No spam — ever.</p>
        </form>
      </div>

      <div class="sm-success" id="sm-success-state">
        <div class="sm-success-icon">&#10003;</div>
        <h3>You\'re in!</h3>
        <p>The full library is now unlocked. Click below to start browsing.</p>
        <button class="sm-success-btn" id="sm-close-btn">
          Browse the Library
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>

    </div>
  </div>
</div>

<script>
(function () {
  var backdrop  = document.getElementById('sub-modal-backdrop');
  var formState = document.getElementById('sm-form-state');
  var success   = document.getElementById('sm-success-state');
  var form      = document.getElementById('sm-form');

  function closeModal() {
    backdrop.classList.remove('visible');
    document.body.style.overflow = '';
  }

  function openModal() {
    backdrop.classList.add('visible');
    document.body.style.overflow = 'hidden';
  }

  // Show modal if not yet subscribed
  if (localStorage.getItem('piksort_subscribed') !== 'true') {
    openModal();
  }

  function validateEmail(email) {
    var re = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
    if (!re.test(email)) return false;
    var free = ['gmail.com','yahoo.com','hotmail.com','outlook.com','icloud.com','live.com','me.com','msn.com','yahoo.com.au'];
    var domain = email.split('@')[1].toLowerCase();
    return !free.includes(domain);
  }

  function setErr(id, hasErr, msg) {
    var g = document.getElementById(id);
    if (!g) return;
    g.classList.toggle('has-error', hasErr);
    var inp = g.querySelector('input');
    if (inp) inp.classList.toggle('sm-err', hasErr);
    if (msg) { var el = g.querySelector('.sm-field-err'); if (el) el.textContent = msg; }
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name   = document.getElementById('sm-name').value.trim();
    var email  = document.getElementById('sm-email').value.trim();
    var mobile = document.getElementById('sm-mobile').value.trim();
    var role   = document.getElementById('sm-role').value.trim();
    var sub    = document.getElementById('sm-updates').checked;
    var ok = true;

    setErr('sm-g-name', !name);
    if (!name) ok = false;

    var emailOk = validateEmail(email);
    var emailMsg = !email ? 'Please enter your work email.'
      : !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email) ? 'Please enter a valid email.'
      : 'Please use your work email (not Gmail, Hotmail etc.).';
    setErr('sm-g-email', !emailOk, emailMsg);
    if (!emailOk) ok = false;

    var mobOk = mobile.replace(/[\\s\\-\\(\\)]/g,'').length >= 8;
    setErr('sm-g-mobile', !mobOk);
    if (!mobOk) ok = false;

    setErr('sm-g-role', !role);
    if (!role) ok = false;

    if (!ok) return;

    localStorage.setItem('piksort_subscribed', 'true');
    localStorage.setItem('piksort_subscriber', JSON.stringify({
      name: name, email: email, mobile: mobile, role: role,
      subscribe: sub, timestamp: new Date().toISOString()
    }));

    formState.style.display = 'none';
    success.classList.add('visible');
  });

  document.getElementById('sm-close-btn').addEventListener('click', closeModal);

  // Clear errors on type
  ['sm-name','sm-email','sm-mobile','sm-role'].forEach(function(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('input', function() {
      var g = el.closest('.sm-group');
      if (g) { g.classList.remove('has-error'); el.classList.remove('sm-err'); }
    });
  });
})();
</script>
'''

if '</body>' not in content:
    print("ERROR: </body> not found"); exit(1)

content = content.replace('</body>', MODAL_BLOCK + '\n</body>', 1)

with open('C:/Users/M. Gustave/piksort/resources.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done — modal gate injected into resources.html")
