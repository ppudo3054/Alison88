LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" id="htmlRoot">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ALISON | Login</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&family=Estedad:wght@400;500;600;700;800;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700;800&family=Shabnam:wght@400;500;700&family=Yekan+Bakh:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#08050f;--panel:rgba(255,255,255,.035);--line:rgba(255,255,255,.09);--line2:rgba(255,255,255,.16);
  --accent:#a855f7;--accent2:#7c3aed;--accent3:#22c55e;
  --text:#f3f0fa;--sub:#9c93b5;--sub2:#655d7e;
  --font-fa:'Vazirmatn',sans-serif;--font-en:'Inter',sans-serif;
}
html,body{background:var(--bg);color:var(--text);min-height:100%;font-family:var(--font-fa)}
html[data-lang="en"] body{font-family:var(--font-en)}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}
body{
  min-height:100vh;min-height:100svh;min-height:100dvh;display:flex;align-items:center;justify-content:center;position:relative;overflow-x:hidden;overflow-y:auto;padding:24px;
  background:
    radial-gradient(48% 40% at 50% 8%, rgba(168,85,247,.30), transparent 60%),
    radial-gradient(40% 35% at 12% 85%, rgba(124,58,237,.22), transparent 60%),
    radial-gradient(40% 35% at 90% 80%, rgba(34,197,94,.10), transparent 60%),
    #08050f;
}
/* روی صفحات کوتاه (موبایل، زوم بالا، پنجره کوچک) اجازه می‌ده کاربر اسکرول کنه
   تا کل کارت (شامل دکمه‌ی «ثبت‌نام ادمینی» زیر کارت ورود) قابل دیدن و کلیک باشه؛
   وقتی محتوا داخل صفحه جا می‌شه ظاهر صفحه دقیقاً مثل قبل باقی می‌مونه. */
@media (max-height:760px){
  body{align-items:flex-start;padding-top:28px;padding-bottom:28px}
}
.grid-bg{position:absolute;inset:0;opacity:.35;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:38px 38px;mask-image:radial-gradient(65% 55% at 50% 30%,#000 20%,transparent 85%)}
 .grid-bg:before{content:"";position:absolute;inset:-2%;background:conic-gradient(from 0deg,transparent 0deg,rgba(168,85,247,.12) 65deg,transparent 130deg,rgba(62,166,255,.10) 210deg,transparent 290deg);filter:blur(24px);animation:ambientSpin 18s linear infinite;will-change:transform;contain:strict}
@keyframes ambientSpin{to{transform:rotate(360deg)}}
.scanline{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,transparent 0%,rgba(255,255,255,.025) 48%,transparent 52%);background-size:100% 180px;animation:scan 7s linear infinite;mix-blend-mode:screen}
@keyframes scan{to{background-position:0 180px}}
.ambient-orb{position:absolute;border-radius:50%;filter:blur(2px);opacity:.45;animation:floatOrb 9s ease-in-out infinite}
.ambient-orb.a{width:180px;height:180px;right:9%;top:12%;background:radial-gradient(circle,rgba(168,85,247,.35),transparent 70%)}
.ambient-orb.b{width:240px;height:240px;left:3%;bottom:3%;background:radial-gradient(circle,rgba(62,166,255,.22),transparent 70%);animation-delay:-3s}
@keyframes floatOrb{0%,100%{transform:translate3d(0,0,0)}50%{transform:translate3d(0,-18px,0)}}
.dot{position:absolute;width:3px;height:3px;border-radius:50%;background:#c9a8ff;opacity:.6;animation:twinkle 3.4s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:.15;transform:scale(1)}50%{opacity:.9;transform:scale(1.6)}}

.lang-switch{position:absolute;top:22px;left:22px;z-index:5;display:flex;background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:100px;padding:3px;gap:2px}
html[dir="rtl"] .lang-switch{left:auto;right:22px}
.lang-switch button{padding:6px 14px;border:0;background:transparent;color:var(--sub);font-size:12px;font-weight:700;border-radius:100px;transition:.15s}
.lang-switch button.on{background:linear-gradient(90deg,var(--accent2),var(--accent));color:#fff}

.wrap{position:relative;z-index:1;width:100%;max-width:420px;display:flex;flex-direction:column;align-items:center;animation:rise .55s cubic-bezier(.2,.8,.2,1) both}
.wrap{position:relative;z-index:1;width:100%;max-width:470px;display:flex;flex-direction:column;align-items:center;animation:rise .65s cubic-bezier(.2,.8,.2,1) both}
.login-status{display:flex;align-items:center;gap:8px;margin:0 0 12px;padding:7px 11px;border-radius:999px;border:1px solid rgba(62,166,255,.18);background:rgba(10,18,32,.58);box-shadow:0 8px 30px rgba(0,0,0,.18);font-size:9px;letter-spacing:.12em;color:#9ecfff;text-transform:uppercase}.login-status .live{width:7px;height:7px;border-radius:50%;background:#34d399;box-shadow:0 0 0 5px rgba(52,211,153,.08),0 0 14px rgba(52,211,153,.8);animation:statusPulse 1.8s ease-in-out infinite}@keyframes statusPulse{50%{transform:scale(1.25);opacity:.65}}
.security-strip{display:flex;justify-content:center;gap:7px;flex-wrap:wrap;margin-top:14px}.security-strip span{font-size:8.5px;color:var(--sub);padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:rgba(255,255,255,.025)}.security-strip i{color:#8fd9ff;margin-left:3px}
.login-card-glow{position:absolute;inset:-1px;border-radius:23px;background:conic-gradient(from 180deg,rgba(168,85,247,.0),rgba(168,85,247,.55),rgba(62,166,255,.35),rgba(168,85,247,.0));filter:blur(8px);opacity:.18;z-index:-1;animation:cardGlow 8s linear infinite;will-change:transform;contain:strict}@keyframes cardGlow{to{transform:rotate(360deg)}}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}

.badge-wrap{position:relative;width:92px;height:92px;margin:14px 0 30px}
.orbit-ring{position:absolute;inset:-24px;border-radius:50%;border:1px dashed rgba(168,85,247,.35);animation:orbitspin 7s linear infinite}
.orbit-ring2{position:absolute;inset:-38px;border-radius:50%;border:1px dashed rgba(62,166,255,.20);animation:orbitspin 12s linear infinite reverse}
.planet{position:absolute;top:-5px;left:50%;width:10px;height:10px;margin-left:-5px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#c9f0ff,#3ea6ff 55%,#1c5fa8 100%);box-shadow:0 0 12px 2px rgba(62,166,255,.85)}
.planet2{position:absolute;bottom:-4px;left:50%;width:6px;height:6px;margin-left:-3px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#f3d9ff,#a855f7 60%,#6425d6 100%);box-shadow:0 0 9px 2px rgba(168,85,247,.85)}
@keyframes orbitspin{to{transform:rotate(360deg)}}
.badge-glow{position:absolute;inset:-14px;border-radius:50%;background:radial-gradient(circle,rgba(168,85,247,.55),transparent 70%);filter:blur(6px);animation:pulseGlow 2.6s ease-in-out infinite;will-change:transform,opacity;contain:strict}
@keyframes pulseGlow{0%,100%{opacity:.6;transform:scale(1)}50%{opacity:1;transform:scale(1.08)}}
.badge{position:relative;width:92px;height:92px;border-radius:50%;overflow:hidden;border:2px solid rgba(255,255,255,.18);box-shadow:0 10px 40px -6px rgba(168,85,247,.7);background:#150c26;display:flex;align-items:center;justify-content:center}
.badge img{width:100%;height:100%;object-fit:cover}

.brand-caps{font-size:12px;font-weight:800;letter-spacing:.32em;color:#c9a8ff;margin-bottom:14px}
h1{font-size:29px;font-weight:900;text-align:center;line-height:1.5;color:var(--text)}
h1 .g{background:linear-gradient(90deg,#c9a8ff,#a855f7,#8fd9ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.subtitle{margin-top:10px;font-size:13.5px;color:var(--sub);text-align:center;line-height:1.9;max-width:340px}

.card{position:relative;
  width:100%;margin-top:28px;padding:30px 28px;border-radius:24px;
  background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
  border:1px solid var(--line);backdrop-filter:none;
  box-shadow:0 36px 100px -26px rgba(0,0,0,.62), inset 0 1px 0 rgba(255,255,255,.05);
}
.field{margin-bottom:16px}
.field label{display:block;font-size:12px;font-weight:700;color:var(--sub);margin-bottom:8px}
.inp{position:relative}
.inp input{width:100%;padding:14px 44px;border-radius:12px;border:1px solid var(--line);background:rgba(0,0,0,.28);color:var(--text);font-size:14px;outline:none;transition:.15s;font-family:inherit}
.inp input::placeholder{color:var(--sub2)}
.inp input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(168,85,247,.20)}
.inp i.i-lead{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--sub);font-size:16px;pointer-events:none}
html[dir="ltr"] .inp i.i-lead{right:auto;left:14px}
html[dir="ltr"] .inp input{padding:13px 42px}
.toggle-eye{position:absolute;left:12px;top:50%;transform:translateY(-50%);background:none;border:0;color:var(--sub);font-size:16px;padding:4px;border-radius:6px;transition:.15s}
html[dir="ltr"] .toggle-eye{left:auto;right:12px}
.toggle-eye:hover{color:var(--text);background:rgba(255,255,255,.07)}
.remember{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--sub);margin:2px 0 20px;user-select:none;cursor:pointer}
.remember input{accent-color:var(--accent);width:15px;height:15px}
.error{display:flex;gap:8px;align-items:center;background:rgba(239,68,68,.10);border:1px solid rgba(239,68,68,.30);color:#ff9b9b;border-radius:11px;padding:11px 13px;font-size:12.5px;margin-bottom:16px}
.error::before{content:"\ea87";font-family:"tabler-icons";font-size:15px;flex-shrink:0}
.btn-main{width:100%;padding:15px;border:0;border-radius:12px;background:linear-gradient(90deg,var(--accent2),var(--accent));color:#fff;font-weight:800;font-size:14.5px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;transition:.18s;box-shadow:0 14px 30px -10px rgba(168,85,247,.65)}
.btn-main:hover{filter:brightness(1.08);transform:translateY(-1px)}
.btn-main:active{transform:translateY(0)}
@keyframes spin{to{transform:rotate(360deg)}}
.spin{animation:spin .7s linear infinite}
.foot{margin-top:22px;text-align:center;font-size:11.5px;color:var(--sub2)}
.admin-reg-row{margin-top:16px;padding-top:14px;border-top:1px dashed var(--line);text-align:center}
.admin-reg-btn{width:100%;background:rgba(255,255,255,.03);border:1px dashed var(--line2);color:var(--sub);padding:11px;border-radius:12px;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;transition:.15s}
.admin-reg-btn:hover{color:var(--text);border-color:var(--accent);background:rgba(168,85,247,.07)}
.areg-overlay{position:fixed;inset:0;z-index:50;display:none;align-items:center;justify-content:center;background:rgba(4,2,10,.72);backdrop-filter:blur(3px);padding:18px}
.areg-overlay.show{display:flex}
.areg-box{width:100%;max-width:420px;max-height:88vh;overflow:auto;padding:24px;border-radius:20px;background:#100a1e;border:1px solid var(--line2);box-shadow:0 40px 100px -20px rgba(0,0,0,.7);animation:rise .35s ease both}
.areg-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;margin-bottom:16px}
.areg-badge{display:inline-flex;align-items:center;gap:6px;font-size:9.5px;font-weight:800;color:#c9a8ff;background:rgba(168,85,247,.12);border:1px solid rgba(168,85,247,.25);padding:5px 10px;border-radius:999px;margin-bottom:9px}
.areg-head h3{font-size:17px;font-weight:900;margin:0 0 6px}
.areg-head p{font-size:11.5px;color:var(--sub);line-height:1.8;margin:0;max-width:300px}
.areg-close{background:rgba(255,255,255,.06);border:1px solid var(--line);color:var(--sub);width:32px;height:32px;border-radius:10px;flex-shrink:0;display:grid;place-items:center}
.areg-close:hover{color:var(--text)}
.areg-msg{font-size:12px;border-radius:10px;padding:10px 12px;margin-bottom:14px;line-height:1.8}
.areg-msg.ok{background:rgba(34,197,94,.10);border:1px solid rgba(34,197,94,.28);color:#7cf0a8}
.areg-msg.err{background:rgba(239,68,68,.10);border:1px solid rgba(239,68,68,.30);color:#ff9b9b}
.areg-hint{margin-top:14px;font-size:10.5px;color:var(--sub2);line-height:1.9;text-align:center}
@media(max-width:480px){h1{font-size:24px}.card{padding:22px 18px}.login-status{font-size:7.5px}.security-strip span{font-size:7.5px}}
@media (prefers-reduced-motion: reduce){
  .grid-bg:before,.scanline,.ambient-orb,.dot,.login-card-glow,.orbit-ring,.orbit-ring2,.badge-glow,.login-status .live,.wrap{animation:none!important}
}
@media (max-width:820px), (pointer:coarse){
  /* Phones/low-end GPUs: the jank came from the blurred/filtered layers being
     repainted every frame (conic-gradient + blur, glow blur, scanline gradient
     shift) — those are the expensive ones and stay off on touch/small screens.
     .orbit-ring / .orbit-ring2 (the spinning "planet" rings) only animate a
     `transform`, which the compositor handles almost for free, so they keep
     spinning on mobile instead of being frozen along with the heavy effects. */
  .grid-bg:before,.scanline,.ambient-orb,.login-card-glow,.badge-glow{animation:none!important}
  .grid-bg:before{filter:blur(14px)}
  .login-card-glow{filter:blur(5px)}
  .badge-glow{filter:blur(4px)}
  .orbit-ring,.orbit-ring2{will-change:transform}
}

/* ================= ALISON // VISUAL IDENTITY ================= */
:root{
  --bg:#030806; --panel:rgba(7,18,16,.82); --line:rgba(112,255,230,.13); --line2:rgba(112,255,230,.26);
  --accent:#55f7d8; --accent2:#00b8ff; --accent3:#8dff6a;
  --text:#effffb; --sub:#8ba9a4; --sub2:#4c6762;
}
body{
  background:
    radial-gradient(70% 55% at 50% 0%,rgba(0,184,255,.14),transparent 68%),
    radial-gradient(55% 50% at 10% 100%,rgba(85,247,216,.12),transparent 70%),
    radial-gradient(45% 45% at 95% 75%,rgba(141,255,106,.07),transparent 70%),
    #030806 !important;
}
.grid-bg{
  opacity:.24;
  background-image:linear-gradient(rgba(112,255,230,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(112,255,230,.045) 1px,transparent 1px);
  background-size:42px 42px;
}
.grid-bg:before{background:conic-gradient(from 90deg,transparent,rgba(85,247,216,.10),transparent 28%,rgba(0,184,255,.10),transparent);filter:blur(32px)}
.login-status{border-color:rgba(85,247,216,.20);background:rgba(4,22,19,.72);color:#9fffee}
.login-status .live{background:#55f7d8;box-shadow:0 0 0 5px rgba(85,247,216,.08),0 0 16px rgba(85,247,216,.75)}
.badge-wrap{margin-bottom:26px}
.orbit-ring{border-color:rgba(85,247,216,.35)}
.orbit-ring2{border-color:rgba(0,184,255,.22)}
.badge-glow{background:radial-gradient(circle,rgba(85,247,216,.42),transparent 70%)}
.badge{border-color:rgba(112,255,230,.35);box-shadow:0 12px 55px -8px rgba(0,184,255,.42);background:#061411}
.brand-caps{color:#72ffe4;letter-spacing:.42em}
h1 .g{background:linear-gradient(90deg,#effffb,#55f7d8,#00b8ff);-webkit-background-clip:text;background-clip:text}
.card{
  background:linear-gradient(145deg,rgba(10,29,25,.88),rgba(3,10,9,.88)) !important;
  border:1px solid rgba(112,255,230,.16) !important;
  box-shadow:0 40px 120px -35px rgba(0,0,0,.86),inset 0 1px 0 rgba(255,255,255,.045),0 0 70px rgba(0,184,255,.035);
}
.inp input{background:rgba(1,8,7,.72);border-color:rgba(112,255,230,.12)}
.inp input:focus{border-color:#55f7d8;box-shadow:0 0 0 3px rgba(85,247,216,.10),0 0 22px rgba(85,247,216,.08)}
.lang-switch{background:rgba(3,14,12,.80);border-color:rgba(112,255,230,.14)}
.lang-switch button.on{background:linear-gradient(90deg,#00a8d9,#27d8bd);box-shadow:0 4px 18px rgba(0,184,255,.18)}
.security-strip span{border-color:rgba(112,255,230,.11);background:rgba(112,255,230,.025)}
.security-strip i{color:#6fffe9}
button[type="submit"],.btn-primary,.login-submit{background:linear-gradient(110deg,#10bda6,#008fd0) !important;box-shadow:0 12px 32px rgba(0,184,255,.16),inset 0 1px 0 rgba(255,255,255,.2)}
.login-card-glow{background:conic-gradient(from 180deg,transparent,#55f7d8, #00b8ff,transparent);opacity:.18}
.foot{color:#506b66 !important}

/* ================= ALISON // NEON OPS CONSOLE ================= */
:root{
  --bg:#030806 !important;--panel:#07120f !important;--panel2:#091814 !important;
  --line:rgba(112,255,230,.11) !important;--line2:rgba(112,255,230,.22) !important;
  --accent:#55f7d8 !important;--accent2:#00b8ff !important;--accent3:#8dff6a !important;
  --text:#effffb !important;--sub:#8ba9a4 !important;--sub2:#4c6762 !important;
}
html,body{background:#030806 !important}
body{
  background:
    radial-gradient(700px 400px at 72% -8%,rgba(0,184,255,.09),transparent 68%),
    radial-gradient(650px 420px at 12% 100%,rgba(85,247,216,.07),transparent 68%),
    #030806 !important;
}
body:before{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.18;
  background-image:linear-gradient(rgba(112,255,230,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(112,255,230,.035) 1px,transparent 1px);
  background-size:44px 44px;mask-image:linear-gradient(to bottom,#000,transparent 92%);
}
.sidebar{
  background:linear-gradient(180deg,rgba(5,17,14,.97),rgba(3,10,9,.98)) !important;
  border-color:rgba(112,255,230,.10) !important;
  box-shadow:18px 0 80px rgba(0,0,0,.32);
}
.sidebar-brand{border-bottom-color:rgba(112,255,230,.08) !important}
.sidebar-brand:after{
  content:"ALISON";display:block;position:absolute;opacity:0;pointer-events:none;
}
.sidebar-brand span,.sidebar-brand [data-i18n="brand"]{color:#eafff9 !important}
.sidebar-brand small{color:#5ed9c5 !important;letter-spacing:.16em;text-transform:uppercase}
.tabnav{gap:6px !important}
.tab{
  border:1px solid transparent !important;border-radius:13px !important;color:#78948e !important;
  transition:.18s ease !important;
}
.tab:hover{background:rgba(85,247,216,.045) !important;color:#c8fff5 !important;border-color:rgba(112,255,230,.08) !important}
.tab.on{
  color:#eafff9 !important;background:linear-gradient(100deg,rgba(85,247,216,.10),rgba(0,184,255,.055)) !important;
  border-color:rgba(85,247,216,.18) !important;box-shadow:inset 3px 0 #55f7d8,0 8px 28px rgba(0,0,0,.18) !important;
}
.pg-head h1,.pg-head h2{letter-spacing:-.02em}
.eyebrow{color:#5de4ce !important;letter-spacing:.16em}
.live-dot{background:#55f7d8 !important;box-shadow:0 0 0 5px rgba(85,247,216,.08),0 0 15px rgba(85,247,216,.6) !important}
.card,.stat-card,.resource-card,.traffic-card,.connection-card,.settings-card,.admin-card,.mini-panel{
  background:linear-gradient(145deg,rgba(8,24,20,.88),rgba(4,12,10,.92)) !important;
  border:1px solid rgba(112,255,230,.10) !important;
  box-shadow:0 24px 70px rgba(0,0,0,.25),inset 0 1px 0 rgba(255,255,255,.025) !important;
  border-radius:18px !important;
}
.card:hover,.stat-card:hover,.ib-card:hover{border-color:rgba(85,247,216,.18) !important}
.btn{
  border-color:rgba(112,255,230,.12) !important;background:rgba(8,23,19,.72) !important;color:#b9e9df !important;
  border-radius:11px !important;
}
.btn:hover{border-color:rgba(85,247,216,.28) !important;background:rgba(85,247,216,.07) !important;color:#effffb !important}
.btn-primary,.primary,.btn.success{
  background:linear-gradient(110deg,#0caa98,#007fbd) !important;border-color:transparent !important;color:#fff !important;
  box-shadow:0 10px 30px rgba(0,184,255,.13) !important;
}
input,select,textarea{
  background:rgba(1,8,7,.72) !important;border-color:rgba(112,255,230,.10) !important;color:#eafff9 !important;
  border-radius:11px !important;
}
input:focus,select:focus,textarea:focus{border-color:#55f7d8 !important;box-shadow:0 0 0 3px rgba(85,247,216,.08) !important}
.badge,.tag,.chip{border-color:rgba(112,255,230,.13) !important}
.badge.green,.live-tag,.ib-live-tag{color:#7dffdc !important;background:rgba(85,247,216,.07) !important;border-color:rgba(85,247,216,.18) !important}
.ib-grid{gap:14px !important}
.ib-card{
  position:relative !important;overflow:hidden !important;
  background:linear-gradient(150deg,rgba(9,28,23,.94),rgba(3,12,10,.98)) !important;
  border:1px solid rgba(112,255,230,.11) !important;border-radius:20px !important;
  box-shadow:0 22px 65px rgba(0,0,0,.28) !important;
}
.ib-card:before{
  content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(120deg,rgba(85,247,216,.06),transparent 35%,rgba(0,184,255,.035) 75%,transparent);
}
.ib-card-head{border-bottom-color:rgba(112,255,230,.08) !important}
.ib-icon{
  background:linear-gradient(135deg,rgba(85,247,216,.14),rgba(0,184,255,.08)) !important;
  border-color:rgba(85,247,216,.18) !important;color:#75ffe6 !important;
  box-shadow:0 0 30px rgba(85,247,216,.06);
}
.ib-status-dot{box-shadow:0 0 12px currentColor !important}
.ib-section{
  background:rgba(4,14,12,.58) !important;border-color:rgba(112,255,230,.08) !important;
  border-radius:16px !important;
}
.ib-section-head{border-bottom-color:rgba(112,255,230,.07) !important}
.ib-step .num{
  background:linear-gradient(135deg,#0db59f,#008fc7) !important;color:#fff !important;
  box-shadow:0 7px 20px rgba(0,184,255,.14) !important;
}
.ib-opt{
  background:rgba(6,20,17,.75) !important;border-color:rgba(112,255,230,.09) !important;border-radius:13px !important;
}
.ib-opt:hover,.ib-opt.active,.ib-opt.selected{
  border-color:rgba(85,247,216,.32) !important;background:rgba(85,247,216,.065) !important;
  box-shadow:0 0 0 1px rgba(85,247,216,.08),0 12px 30px rgba(0,0,0,.18) !important;
}
.ib-summary{
  background:linear-gradient(135deg,rgba(85,247,216,.07),rgba(0,184,255,.045)) !important;
  border-color:rgba(85,247,216,.12) !important;border-radius:16px !important;
}
.ib-progress{background:rgba(112,255,230,.08) !important}
.ib-progress > *{background:linear-gradient(90deg,#55f7d8,#00b8ff) !important}
table{border-color:rgba(112,255,230,.08) !important}
th{color:#67d8c5 !important;background:rgba(85,247,216,.025) !important}
td{border-color:rgba(112,255,230,.06) !important}
tr:hover td{background:rgba(85,247,216,.025) !important}
.modal,.dialog,.overlay-panel{
  background:linear-gradient(145deg,#071713,#030b09) !important;border-color:rgba(112,255,230,.15) !important;
  box-shadow:0 40px 120px rgba(0,0,0,.72) !important;
}
::-webkit-scrollbar{width:7px;height:7px}
::-webkit-scrollbar-track{background:#020706}
::-webkit-scrollbar-thumb{background:#164b43;border-radius:20px}
::-webkit-scrollbar-thumb:hover{background:#237d6d}
</style>
<style>
.perm-grid,.bot-text-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}.perm-item{display:flex;align-items:center;gap:9px;padding:11px 12px;border:1px solid var(--line);background:var(--panel2);border-radius:13px;font-size:12px}.perm-item input{accent-color:var(--accent)}.bot-text-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.bot-text-grid textarea{width:100%;resize:vertical;min-height:90px;background:var(--panel2);border:1px solid var(--line);color:var(--text);border-radius:12px;padding:11px;font:inherit;line-height:1.8}@media(max-width:700px){.perm-grid,.bot-text-grid{grid-template-columns:1fr}}
.tpl-studio-head{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;flex-wrap:wrap}
.tpl-badge{display:flex;align-items:center;gap:6px;padding:6px 11px;border-radius:99px;background:rgba(148,85,255,.12);color:#b79bff;border:1px solid rgba(148,85,255,.22);font-size:10.5px;font-weight:800;white-space:nowrap}
.tpl-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:14px;margin-top:14px}
.tpl-fields{display:flex;flex-direction:column;gap:8px}
.tpl-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:11px 13px;border:1px solid var(--line);background:var(--panel2);border-radius:13px;cursor:pointer;transition:border-color .12s ease}
.tpl-row:hover{border-color:var(--line2)}
.tpl-row-main{display:flex;align-items:center;gap:10px;min-width:0}
.tpl-row-main i{width:32px;height:32px;flex-shrink:0;display:grid;place-items:center;border-radius:9px;background:rgba(148,85,255,.12);color:#a997ff;font-size:15px}
.tpl-row-main b{display:block;font-size:12px}
.tpl-row-main small{display:block;color:var(--sub2);font-size:9.5px;margin-top:2px}
input.tpl-switch{appearance:none;-webkit-appearance:none;width:36px;height:20px;border-radius:99px;background:var(--line2);border:1px solid var(--line);position:relative;cursor:pointer;flex-shrink:0;margin:0;transition:background-color .16s ease}
input.tpl-switch:after{content:'';position:absolute;width:14px;height:14px;top:2px;right:2px;border-radius:50%;background:#fff;transition:right .16s ease;box-shadow:0 1px 3px rgba(0,0,0,.3)}
input.tpl-switch:checked{background:linear-gradient(90deg,var(--accent),var(--accent-d));border-color:transparent}
input.tpl-switch:checked:after{right:18px}
.tpl-preview{padding:14px;border:1px dashed var(--line2);border-radius:14px;background:linear-gradient(155deg,rgba(148,85,255,.06),rgba(255,255,255,.015))}
.tpl-preview-label{display:flex;align-items:center;gap:7px;font-size:10.5px;color:var(--sub);font-weight:700;margin-bottom:10px}
.tpl-preview-row{display:flex;align-items:center;gap:9px;padding:11px 12px;border-radius:12px;background:var(--panel);border:1px solid var(--line)}
.tpl-preview-dot{width:9px;height:9px;border-radius:50%;background:var(--good);box-shadow:0 0 0 3px rgba(34,197,139,.18);flex-shrink:0}
.tpl-preview-text{flex:1;min-width:0;font-size:12px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;direction:ltr;text-align:left}
.tpl-preview-proto{font-size:9px;font-weight:800;color:var(--accent);background:rgba(148,85,255,.12);padding:3px 8px;border-radius:99px;flex-shrink:0}
@media(max-width:760px){.tpl-grid{grid-template-columns:1fr}}
.admin-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.admin-card{position:relative;overflow:hidden;padding:18px;border:1px solid var(--line);background:linear-gradient(155deg,var(--panel) 0%,var(--panel2) 100%);border-radius:18px;box-shadow:var(--shadow-sm);transition:transform .15s ease,box-shadow .15s ease,border-color .15s ease}
.admin-card:hover{transform:translateY(-2px);box-shadow:var(--shadow-md);border-color:var(--line2)}
.admin-card.is-owner{border-color:rgba(245,165,36,.35);background:linear-gradient(155deg,rgba(245,165,36,.08) 0%,var(--panel2) 60%)}
.admin-card.is-inactive{opacity:.62}
.admin-card-top{display:flex;align-items:flex-start;justify-content:space-between;gap:10px}
.admin-id{display:flex;align-items:center;gap:11px;min-width:0}
.admin-avatar{flex:none;width:42px;height:42px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent-d));box-shadow:0 6px 16px rgba(148,85,255,.28)}
.admin-card.is-owner .admin-avatar{background:linear-gradient(135deg,#f5a524,#c9820a);box-shadow:0 6px 16px rgba(245,165,36,.3)}
.admin-meta{min-width:0}
.admin-meta .admin-name{font-size:14px;font-weight:800;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.admin-meta .admin-sub{display:flex;align-items:center;gap:6px;margin-top:3px;font-size:11px;color:var(--sub)}
.admin-role-badge{flex:none;display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:999px;font-size:10px;font-weight:700;letter-spacing:.02em}
.admin-role-badge.owner{color:#f5a524;background:rgba(245,165,36,.14);border:1px solid rgba(245,165,36,.3)}
.admin-role-badge.admin{color:var(--accent);background:rgba(148,85,255,.12);border:1px solid rgba(148,85,255,.28)}
.admin-status-dot{width:7px;height:7px;border-radius:50%;background:var(--good);box-shadow:0 0 0 3px rgba(34,197,139,.15)}
.admin-card.is-inactive .admin-status-dot{background:var(--bad);box-shadow:0 0 0 3px rgba(242,73,85,.15)}
.admin-perm-row{display:flex;flex-wrap:wrap;gap:5px;margin-top:14px}
.admin-perm-chip{font-size:10px;padding:3px 8px;border-radius:8px;background:var(--panel2);border:1px solid var(--line);color:var(--sub)}
.admin-perm-chip.all{color:#f5a524;border-color:rgba(245,165,36,.3);background:rgba(245,165,36,.1)}
.admin-card-foot{display:flex;align-items:center;justify-content:space-between;margin-top:16px;padding-top:12px;border-top:1px dashed var(--line)}
.admin-card-foot .admin-login{font-size:10.5px;color:var(--sub2)}
.admin-card-foot .row-actions{gap:6px}
.admins-hero{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:center;margin-bottom:14px;padding:20px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(135deg,rgba(124,92,255,.11),rgba(57,214,255,.035));box-shadow:var(--shadow-sm)}.admins-hero h2{font-size:18px;margin:0 0 5px}.admins-hero p{font-size:10px;color:var(--sub);margin:0;line-height:1.9}.admins-summary{display:flex;gap:8px;flex-wrap:wrap}.admins-summary .sum{min-width:92px;padding:11px 13px;border:1px solid var(--line);border-radius:13px;background:rgba(255,255,255,.025);text-align:center}.admins-summary b{display:block;font-size:18px}.admins-summary small{display:block;color:var(--sub2);font-size:8px;margin-top:3px}.admin-card{min-height:188px;display:flex;flex-direction:column}.admin-card-top{padding-bottom:13px;border-bottom:1px dashed var(--line)}.admin-id{flex:1}.admin-avatar{position:relative;overflow:hidden}.admin-avatar:after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,transparent 35%,rgba(255,255,255,.18) 50%,transparent 65%);transform:translateX(-130%);transition:transform .55s ease}.admin-card:hover .admin-avatar:after{transform:translateX(130%)}.admin-perm-row{min-height:45px;align-content:flex-start}.admin-perm-chip{transition:.15s ease}.admin-perm-chip:hover{border-color:var(--line2);color:var(--text)}.admin-card-foot{margin-top:auto}.admin-login{direction:ltr;text-align:left}.admin-actions-label{display:none}.admin-card-foot .row-actions{gap:8px}.admin-card-foot .iconbtn{width:38px;height:34px;border-radius:11px;font-size:15px;background:linear-gradient(145deg,var(--panel2),rgba(124,92,255,.08));border-color:var(--line2);box-shadow:0 7px 18px rgba(0,0,0,.10)}.admin-card-foot .iconbtn.danger{color:var(--bad)}.admin-card-foot .iconbtn.power{color:var(--accent)}.admin-card-foot .iconbtn:hover{transform:translateY(-1px);box-shadow:0 10px 24px rgba(124,92,255,.18)}.access-command-copy{min-width:0}.command-badge{display:inline-flex;align-items:center;gap:7px;padding:6px 10px;border-radius:999px;border:1px solid rgba(124,92,255,.28);background:rgba(124,92,255,.10);color:var(--accent);font-size:9px;font-weight:900;letter-spacing:.08em}.access-command-copy h2{font-size:22px;margin:12px 0 7px;letter-spacing:-.02em}.access-command-copy p{max-width:760px}.command-points{display:flex;flex-wrap:wrap;gap:7px;margin-top:13px}.command-points span{display:inline-flex;align-items:center;gap:5px;padding:6px 9px;border:1px solid var(--line);border-radius:9px;background:rgba(255,255,255,.025);font-size:9px;color:var(--sub)}.command-points i{color:var(--good)}.admin-directory{overflow:hidden}.directory-live{display:inline-flex;align-items:center;gap:6px;font-size:9px;color:var(--good);font-weight:800}.directory-live i{width:6px;height:6px;border-radius:50%;background:var(--good);box-shadow:0 0 0 4px rgba(34,197,139,.12)}.admin-directory .panel-head{border-bottom:1px solid var(--line)}@media(max-width:700px){.access-command-copy h2{font-size:18px}.command-points{display:grid;grid-template-columns:1fr}}.admin-login-block{display:flex;flex-direction:column;gap:4px}.admin-login-label{font-size:8px;color:var(--sub2)}.admin-card{position:relative;overflow:hidden}.admin-card:before{content:"";position:absolute;inset:0 0 auto 0;height:2px;background:linear-gradient(90deg,var(--accent),transparent);opacity:.7}.admin-card.is-owner:before{background:linear-gradient(90deg,#f5a524,transparent)}.feature-lock{text-align:center;padding:16px 6px 8px}.feature-lock-icon{width:68px;height:68px;margin:0 auto 14px;display:grid;place-items:center;border-radius:20px;background:linear-gradient(145deg,rgba(124,92,255,.18),rgba(53,214,255,.08));border:1px solid rgba(124,92,255,.28);font-size:28px;color:var(--accent)}.feature-lock h3{margin:0 0 8px;font-size:18px}.feature-lock p{margin:0 auto;max-width:520px;line-height:2;color:var(--sub);font-size:11px}.feature-lock-note{display:inline-flex;gap:7px;align-items:center;margin-top:16px;padding:8px 11px;border-radius:999px;border:1px solid var(--line);background:var(--panel2);font-size:9px;color:var(--sub2)}@media(max-width:700px){.admins-hero{grid-template-columns:1fr}.admins-summary{justify-content:flex-start}}
.areq-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:13px 14px;border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.02);margin-bottom:10px}
.areq-row:last-child{margin-bottom:0}
.areq-info{display:flex;flex-direction:column;gap:3px;min-width:0}
.areq-name{font-weight:800;font-size:12.5px}
.areq-meta{font-size:10px;color:var(--sub2);display:flex;gap:10px;flex-wrap:wrap}
.areq-meta span{display:inline-flex;align-items:center;gap:4px}
.areq-note{font-size:10.5px;color:var(--sub);margin-top:2px}
.areq-actions{display:flex;gap:8px;flex-shrink:0}
.areq-empty{text-align:center;padding:22px 10px;color:var(--sub2);font-size:11px}
.areq-status{font-size:9px;font-weight:800;padding:4px 9px;border-radius:999px}
.areq-status.approved{background:rgba(34,197,94,.10);color:#7cf0a8;border:1px solid rgba(34,197,94,.25)}
.areq-status.rejected{background:rgba(239,68,68,.10);color:#ff9b9b;border:1px solid rgba(239,68,68,.25)}
@media(max-width:700px){.admin-grid{grid-template-columns:1fr}}
</style></head>
<style id="alison-original-ui">
/* ALISON // ORIGINAL COMMAND UI — visual system intentionally redesigned */
:root{--al-bg:#020706;--al-surface:#071310;--al-surface2:#0a1b17;--al-line:#14342d;--al-cyan:#38f2d0;--al-blue:#38bdf8;--al-lime:#b8ff6a;--al-red:#ff647c;--al-text:#eafff9;--al-muted:#78958e;--al-radius:22px}
*{scrollbar-width:thin;scrollbar-color:#16443a transparent}
html,body{background:var(--al-bg)!important;color:var(--al-text)!important}
body{background-image:radial-gradient(900px 500px at 75% -10%,#0d5b5140,transparent 70%),radial-gradient(700px 500px at 0 100%,#063f5430,transparent 70%),linear-gradient(180deg,#020706,#030a08 45%,#020504)!important}
body:after{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1;opacity:.16;background:linear-gradient(rgba(56,242,208,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(56,242,208,.035) 1px,transparent 1px);background-size:48px 48px;mask-image:linear-gradient(#000,transparent 90%)}
.sidebar{width:272px!important;background:linear-gradient(180deg,#06110e 0%,#030806 100%)!important;border-right:1px solid #12352e!important;box-shadow:25px 0 90px #0009!important}
.sidebar-brand{height:94px!important;padding:20px!important;border-bottom:1px solid #12352e!important}
.sidebar-brand img{width:42px!important;height:42px!important;filter:drop-shadow(0 0 16px #38f2d060)!important}
.sidebar-brand span{font-size:21px!important;letter-spacing:.12em!important;color:#eafff9!important}
.sidebar-brand small{color:#38f2d0!important;letter-spacing:.22em!important;font-size:8px!important}
.tabnav{padding:16px 12px!important;gap:7px!important}
.tab{height:48px!important;border:1px solid transparent!important;border-radius:15px!important;padding:0 13px!important;color:#69857f!important;background:transparent!important;position:relative!important;overflow:hidden!important}
.tab i{font-size:20px!important;width:27px!important;color:#50736b!important}
.tab:hover{background:#0a211b!important;color:#cffff5!important;border-color:#17483d!important;transform:translateX(-2px)}
.tab:hover i{color:#38f2d0!important}
.tab.on{background:linear-gradient(100deg,#0c2b24,#071914)!important;border-color:#1d594b!important;color:#eafff9!important;box-shadow:inset 3px 0 #38f2d0,0 10px 28px #0006!important}
.tab.on:after{content:"";position:absolute;right:12px;width:5px;height:5px;border-radius:50%;background:#38f2d0;box-shadow:0 0 12px #38f2d0}
.bd{background:#0e3028!important;border:1px solid #1b5145!important;color:#8fffe8!important}
.sidebar-foot{border-top:1px solid #12352e!important;padding:14px!important}
.user-chip{background:#071a15!important;border:1px solid #16463b!important;border-radius:16px!important;padding:10px!important}
.user-chip .av{background:linear-gradient(135deg,#38f2d0,#168fd0)!important;color:#02100c!important;box-shadow:0 0 20px #38f2d044!important}
.main-col{background:transparent!important}
.topbar{height:82px!important;background:#030b09d9!important;border-bottom:1px solid #10342c!important;backdrop-filter:blur(18px)!important}
.hamburger{border:1px solid #17453b!important;background:#071713!important;color:#8feadd!important;border-radius:12px!important}
.page-title{font-weight:900!important;letter-spacing:-.03em!important}
.top-right .icon-btn{background:#071713!important;border:1px solid #16463b!important;color:#8aa9a2!important;border-radius:12px!important}
.top-right .icon-btn:hover{color:#38f2d0!important;border-color:#2b8c78!important}
.body-wrap{padding:28px!important;max-width:1600px!important}
.pg-head{padding:4px 2px 24px!important}
.pg-head h1{font-size:34px!important;letter-spacing:-.05em!important}
.pg-head p{color:#718f88!important}
.eyebrow{color:#38f2d0!important;letter-spacing:.18em!important;font-size:9px!important}
.live-dot{background:#38f2d0!important;box-shadow:0 0 0 5px #38f2d014,0 0 18px #38f2d0!important}
.card,.resource-card,.stat-card,.traffic-card,.connection-card,.mini-panel,.ib-card,.settings-card,.admin-card,.resource-grid>div{background:linear-gradient(145deg,#091b17f2,#040b09f2)!important;border:1px solid #143c34!important;border-radius:22px!important;box-shadow:0 24px 80px #0007,inset 0 1px #ffffff08!important}
.card:hover,.resource-card:hover,.ib-card:hover{border-color:#267b68!important;box-shadow:0 28px 90px #0009,0 0 35px #38f2d00d!important;transform:translateY(-2px)}
.resource-grid{gap:14px!important}
.resource-card{min-height:145px!important;padding:20px!important;position:relative!important;overflow:hidden!important}
.resource-card:before{content:"";position:absolute;inset:auto -20% -55% 20%;height:100px;background:radial-gradient(circle,#38f2d014,transparent 65%);pointer-events:none}
.rc-head b{font-size:26px!important;color:#eafff9!important}
.rc-head i{color:#38f2d0!important}
.spark{opacity:.9!important}
.traffic-layout{gap:14px!important}
.panel-head{border-bottom:1px solid #12352d!important;padding-bottom:14px!important}
.panel-head b{letter-spacing:.08em!important;font-size:11px!important}
.traffic-legend b,.connection-number{color:#38f2d0!important}
.connection-card{background:radial-gradient(circle at 70% 25%,#0b4a3c55,transparent 35%),linear-gradient(145deg,#091b17,#040b09)!important}
.btn{border-radius:13px!important;border:1px solid #18483e!important;background:#071813!important;color:#a8c9c2!important;box-shadow:none!important}
.btn:hover{background:#0b271f!important;border-color:#2a8b74!important;color:#eafff9!important}
.btn.primary,.btn.success,.primary{background:linear-gradient(110deg,#13b89f,#087bb3)!important;border:0!important;color:#fff!important;box-shadow:0 12px 30px #0a9d8740!important}
.btn-inbound{background:linear-gradient(110deg,#0da98f,#087db7)!important}
.search input,.sel,input,select,textarea{background:#030a08!important;border:1px solid #153b33!important;color:#eafff9!important;border-radius:13px!important}
.search input:focus,input:focus,select:focus,textarea:focus{border-color:#38f2d0!important;box-shadow:0 0 0 3px #38f2d012!important}
.ib-grid{grid-template-columns:repeat(auto-fill,minmax(310px,1fr))!important;gap:16px!important}
.ib-card{min-height:250px!important;padding:0!important;overflow:hidden!important}
.ib-card:before{background:linear-gradient(120deg,#38f2d008,transparent 45%,#38bdf808)!important}
.ib-card-head{padding:18px!important;background:#071713!important;border-bottom:1px solid #12352d!important}
.ib-icon{width:48px!important;height:48px!important;border-radius:15px!important;background:linear-gradient(135deg,#0b332a,#082336)!important;border:1px solid #267565!important;color:#38f2d0!important}
.ib-live-tag,.badge.green{background:#08362c!important;color:#7dffe5!important;border-color:#1b6b58!important}
.badge{border-radius:999px!important}
.ov-quickstats{gap:14px!important}
.ov-quickstats>div{background:#071713!important;border:1px solid #143c34!important;border-radius:18px!important}
.health-row{border-bottom:1px solid #103129!important}
.mono{color:#72ffe5!important}
.modal,.drawer,.overlay{backdrop-filter:blur(18px)!important}
.drawer{background:#06110e!important;border-left:1px solid #17483d!important;box-shadow:-30px 0 90px #0009!important}
.toast{background:#071a15!important;border:1px solid #1c5c4d!important}
/* distinct page compositions */
#pg-overview .resource-grid{grid-template-columns:repeat(4,1fr)!important}
#pg-overview .traffic-layout{grid-template-columns:minmax(0,1.65fr) minmax(300px,.7fr)!important}
#pg-links .pg-head{background:linear-gradient(90deg,#071713aa,transparent)!important;padding:20px!important;border-radius:20px!important;border:1px solid #10382f!important;margin-bottom:18px!important}
#pg-links .ib-card{border-radius:24px!important}
@media(max-width:1000px){#pg-overview .resource-grid{grid-template-columns:repeat(2,1fr)!important}#pg-overview .traffic-layout{grid-template-columns:1fr!important}}
@media(max-width:700px){.sidebar{width:285px!important}.body-wrap{padding:17px!important}.pg-head h1{font-size:28px!important}.resource-grid{grid-template-columns:1fr 1fr!important}.ib-grid{grid-template-columns:1fr!important}.topbar{height:70px!important}}
</style>
<body>
<div class="grid-bg"></div><div class="scanline"></div><div class="ambient-orb a"></div><div class="ambient-orb b"></div>
<div class="dot" style="top:14%;left:20%"></div>
<div class="dot" style="top:22%;left:78%;animation-delay:-1s"></div>
<div class="dot" style="top:62%;left:10%;animation-delay:-2s"></div>
<div class="dot" style="top:70%;left:88%;animation-delay:-1.6s"></div>
<div class="dot" style="top:40%;left:6%;animation-delay:-2.4s"></div>
<div class="dot" style="top:85%;left:45%;animation-delay:-.6s"></div>

<div class="lang-switch">
  <button id="langFa" class="on" onclick="setLang('fa')">فارسی</button>
  <button id="langEn" onclick="setLang('en')">EN</button>
</div>

<div class="wrap">
  <div class="badge-wrap">
    <div class="orbit-ring2"></div>
    <div class="orbit-ring"><span class="planet"></span><span class="planet2"></span></div>
    <div class="badge-glow"></div>
    <div class="badge"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20256%20256%22%3E%0A%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20stop-color%3D%22%236fffe9%22%2F%3E%3Cstop%20offset%3D%22.48%22%20stop-color%3D%22%2325d9c3%22%2F%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%230aa4ff%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%0A%3Crect%20width%3D%22256%22%20height%3D%22256%22%20rx%3D%2262%22%20fill%3D%22%2307110f%22%2F%3E%0A%3Cpath%20d%3D%22M128%2035%20214%2078v100l-86%2043-86-43V78z%22%20fill%3D%22none%22%20stroke%3D%22url%28%23g%29%22%20stroke-width%3D%2210%22%2F%3E%0A%3Cpath%20d%3D%22m79%20169%2043-88h14l43%2088h-25l-9-20H111l-9%2020zm40-40h18l-9-22z%22%20fill%3D%22url%28%23g%29%22%2F%3E%0A%3Ccircle%20cx%3D%22193%22%20cy%3D%2264%22%20r%3D%227%22%20fill%3D%22%238ffff1%22%2F%3E%0A%3C%2Fsvg%3E" alt="logo"></div>
  </div>
  <div class="brand-caps">ALISON</div>
  <h1 data-i18n="h1"></h1>
  <p class="subtitle" data-i18n="subtitle"></p>

  <div class="login-status"><span class="live"></span><span>ALISON · SECURE ADMIN CONSOLE</span><span style="margin-right:auto;color:#6ee7b7">ONLINE</span></div>
  <div class="card">
    <div class="login-card-glow"></div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px"><div><div style="font-size:10px;letter-spacing:.16em;color:#8fa1c0;font-weight:800">SECURE ADMIN</div><div style="font-size:16px;font-weight:900;margin-top:4px">ورود به مرکز کنترل</div></div><div style="width:38px;height:38px;border-radius:12px;display:grid;place-items:center;border:1px solid rgba(143,217,255,.18);background:rgba(62,166,255,.08);color:#8fd9ff;box-shadow:0 0 25px rgba(62,166,255,.12)"><i class="ti ti-shield-lock" style="font-size:18px"></i></div></div>
    <form method="post" action="/login" id="loginForm">
      <div class="field">
        <label data-i18n="emailLabel"></label>
        <div class="inp">
          <input type="text" name="username" id="username" data-i18n-placeholder="emailPh" autocomplete="username">
          <i class="ti ti-user-shield i-lead"></i>
        </div>
      </div>
      <div class="field">
        <label data-i18n="passLabel"></label>
        <div class="inp">
          <input type="password" name="password" id="password" placeholder="••••••••" autocomplete="current-password" required>
          <i class="ti ti-lock i-lead"></i>
          <button type="button" class="toggle-eye" onclick="togglePw()" id="pwToggle" tabindex="-1"><i class="ti ti-eye"></i></button>
        </div>
        <div id="capsWarn" style="display:none;align-items:center;gap:5px;margin-top:7px;font-size:11px;color:#fbbf24"><i class="ti ti-alert-triangle"></i> Caps Lock فعال است</div>
      </div>
      <label class="remember"><input type="checkbox" name="remember" value="1"><span data-i18n="remember"></span></label>
      <button class="btn-main" type="submit" id="submitBtn"><i class="ti ti-login-2"></i><span data-i18n="submit"></span></button>
    </form>
    <div class="security-strip"><span><i class="ti ti-shield-check"></i>Protected Session</span><span><i class="ti ti-lock"></i>Secure Cookie</span><span><i class="ti ti-activity"></i>System Monitor</span></div>
    <div class="admin-reg-row"><button type="button" class="admin-reg-btn" onclick="openAdminReg()"><i class="ti ti-user-scan"></i><span data-i18n="adminRegBtn"></span></button></div>
  </div>
  <div class="foot">ALISON Control Suite &copy; <span data-i18n="rights"></span></div>
</div>

<div class="areg-overlay" id="aregOverlay" onclick="if(event.target===this)closeAdminReg()">
  <div class="areg-box">
    <div class="areg-head">
      <div>
        <div class="areg-badge"><i class="ti ti-user-shield"></i><span data-i18n="adminRegBadge"></span></div>
        <h3 data-i18n="adminRegTitle"></h3>
        <p data-i18n="adminRegDesc"></p>
      </div>
      <button type="button" class="areg-close" onclick="closeAdminReg()"><i class="ti ti-x"></i></button>
    </div>
    <div class="field">
      <label data-i18n="adminRegNameLabel"></label>
      <div class="inp"><input type="text" id="aregName" data-i18n-placeholder="adminRegNamePh"><i class="ti ti-id i-lead"></i></div>
    </div>
    <div class="field">
      <label data-i18n="adminRegTgLabel"></label>
      <div class="inp"><input type="text" id="aregTg" dir="ltr" data-i18n-placeholder="adminRegTgPh"><i class="ti ti-brand-telegram i-lead"></i></div>
    </div>
    <div class="field">
      <label data-i18n="adminRegNoteLabel"></label>
      <div class="inp"><input type="text" id="aregNote" data-i18n-placeholder="adminRegNotePh"><i class="ti ti-message i-lead"></i></div>
    </div>
    <div id="aregMsg" class="areg-msg" style="display:none"></div>
    <button class="btn-main" type="button" id="aregSubmitBtn" onclick="submitAdminReg()"><i class="ti ti-send"></i><span data-i18n="adminRegSubmit"></span></button>
    <p class="areg-hint" data-i18n="adminRegHint"></p>
  </div>
</div>

<script>
var I18N = {
  fa: {
    title: "ورود | ALISON",
    h1: 'ورود به <span class="g">ALISON</span>',
    subtitle: "کنسول امن ALISON برای مدیریت سرویس‌ها و شبکه",
    emailLabel: "نام کاربری",
    emailPh: "admin",
    passLabel: "رمز عبور",
    remember: "مرا به خاطر بسپار",
    submit: "ورود به پنل",
    rights: "همه‌ی حقوق محفوظ است",
    adminRegBtn: "ثبت‌نام ادمینی",
    adminRegBadge: "درخواست دسترسی",
    adminRegTitle: "درخواست دسترسی ALISON",
    adminRegDesc: "اطلاعاتت رو بفرست، مالک پنل درخواستت رو بررسی می‌کنه و اگر تایید بشه، نام کاربری و رمز از طریق تلگرام برات ارسال می‌شه.",
    adminRegNameLabel: "نام و نام خانوادگی",
    adminRegNamePh: "مثلاً: علی رضایی",
    adminRegTgLabel: "آیدی تلگرام",
    adminRegTgPh: "@username",
    adminRegNoteLabel: "توضیح (اختیاری)",
    adminRegNotePh: "چرا می‌خوای ادمین بشی؟",
    adminRegSubmit: "ارسال درخواست",
    adminRegHint: "پس از تایید مالک، اطلاعات ورود از طریق آیدی تلگرامی که وارد کردی برایت ارسال خواهد شد.",
    adminRegSent: "درخواست شما ثبت شد ✓ منتظر تایید مالک پنل بمانید.",
    adminRegNameErr: "نام و نام خانوادگی را کامل وارد کنید",
    adminRegTgErr: "آیدی تلگرام معتبر وارد کنید"
  },
  en: {
    title: "Login | ALISON",
    h1: 'Sign in to <span class="g">ALISON</span>',
    subtitle: "Secure ALISON control center for services and network",
    emailLabel: "Username",
    emailPh: "admin",
    passLabel: "Password",
    remember: "Remember me",
    submit: "Sign in",
    rights: "All rights reserved",
    adminRegBtn: "Register as admin",
    adminRegBadge: "Access request",
    adminRegTitle: "ALISON Admin Access",
    adminRegDesc: "Send your details. The panel owner will review your request and, if approved, send you a username and password via Telegram.",
    adminRegNameLabel: "Full name",
    adminRegNamePh: "e.g. John Smith",
    adminRegTgLabel: "Telegram ID",
    adminRegTgPh: "@username",
    adminRegNoteLabel: "Note (optional)",
    adminRegNotePh: "Why do you want to be an admin?",
    adminRegSubmit: "Send request",
    adminRegHint: "Once approved by the owner, your login details will be sent to the Telegram ID you provided.",
    adminRegSent: "Your request was submitted ✓ wait for the owner's approval.",
    adminRegNameErr: "Please enter your full name",
    adminRegTgErr: "Please enter a valid Telegram ID"
  }
};
function applyLang(lang){
  var d = I18N[lang];
  document.querySelectorAll('[data-i18n]').forEach(function(el){
    var k = el.getAttribute('data-i18n');
    if(d[k] !== undefined) el.innerHTML = d[k];
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el){
    var k = el.getAttribute('data-i18n-placeholder');
    if(d[k] !== undefined) el.setAttribute('placeholder', d[k]);
  });
  document.title = d.title;
  var html = document.getElementById('htmlRoot');
  html.setAttribute('lang', lang);
  html.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');
  html.setAttribute('data-lang', lang);
  document.getElementById('langFa').classList.toggle('on', lang==='fa');
  document.getElementById('langEn').classList.toggle('on', lang==='en');
}
function setLang(lang){
  try{ localStorage.setItem('vw_lang', lang); }catch(e){}
  applyLang(lang);
}
(function(){
  var saved = 'fa';
  try{ saved = localStorage.getItem('vw_lang') || 'fa'; }catch(e){}
  applyLang(saved);
})();
function togglePw(){
  var inp = document.getElementById('password');
  var icon = document.getElementById('pwToggle').querySelector('i');
  if(inp.type === 'password'){ inp.type = 'text'; icon.className = 'ti ti-eye-off'; }
  else { inp.type = 'password'; icon.className = 'ti ti-eye'; }
}
(function(){
  var pwInput = document.getElementById('password');
  var warn = document.getElementById('capsWarn');
  if(!pwInput || !warn) return;
  function checkCaps(e){
    var isCaps = typeof e.getModifierState === 'function' && e.getModifierState('CapsLock');
    warn.style.display = isCaps ? 'flex' : 'none';
  }
  pwInput.addEventListener('keyup', checkCaps);
  pwInput.addEventListener('keydown', checkCaps);
})();
document.getElementById('loginForm').addEventListener('submit', function(){
  var btn = document.getElementById('submitBtn');
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader-2 spin"></i>';
});
function curLang(){ try{ return localStorage.getItem('vw_lang') || 'fa'; }catch(e){ return 'fa'; } }
function openAdminReg(){
  document.getElementById('aregMsg').style.display = 'none';
  document.getElementById('aregOverlay').classList.add('show');
}
function closeAdminReg(){
  document.getElementById('aregOverlay').classList.remove('show');
}
function aregShowMsg(text, ok){
  var el = document.getElementById('aregMsg');
  el.textContent = text;
  el.className = 'areg-msg ' + (ok ? 'ok' : 'err');
  el.style.display = 'block';
}
async function submitAdminReg(){
  var d = I18N[curLang()];
  var name = document.getElementById('aregName').value.trim();
  var tg = document.getElementById('aregTg').value.trim().replace(/^@/, '');
  var note = document.getElementById('aregNote').value.trim();
  if(name.length < 3){ aregShowMsg(d.adminRegNameErr, false); return; }
  if(tg.length < 3){ aregShowMsg(d.adminRegTgErr, false); return; }
  var btn = document.getElementById('aregSubmitBtn');
  btn.disabled = true;
  var originalHtml = btn.innerHTML;
  btn.innerHTML = '<i class="ti ti-loader-2 spin"></i>';
  try{
    var res = await fetch('/api/admin-requests', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({full_name: name, telegram_id: tg, note: note})
    });
    var data = {};
    try{ data = await res.json(); }catch(e){}
    if(!res.ok) throw new Error(data.detail || 'خطا');
    aregShowMsg(d.adminRegSent, true);
    document.getElementById('aregName').value = '';
    document.getElementById('aregTg').value = '';
    document.getElementById('aregNote').value = '';
  }catch(e){
    aregShowMsg(e.message || 'خطا', false);
  }finally{
    btn.disabled = false;
    btn.innerHTML = originalHtml;
  }
}
</script>
</body>
</html>
"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ALISON Control Suite</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&family=Estedad:wght@400;500;600;700;800;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700;800&family=Shabnam:wght@400;500;700&family=Yekan+Bakh:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:var(--font-ui,'Vazirmatn'),sans-serif}
:root{
  --bg:#0b0e14;--panel:#111623;--panel2:#161c2b;--line:#212838;--line2:#2a3348;
  --accent:#9455ff;--accent-d:#7b3ff0;--good:#22c58b;--warn:#f5a524;--bad:#f24955;
  --text:#e7ebf3;--sub:#8792a8;--sub2:#5b6478;
  --shadow-sm:0 2px 8px rgba(0,0,0,.18);--shadow-md:0 10px 28px rgba(0,0,0,.28);
}
[data-theme="light"]{
  --bg:#ffffff;--panel:#ffffff;--panel2:#f7f8fb;--line:#e5e7eb;--line2:#d1d5db;
  --accent:#7c3aed;--accent-d:#6425d6;--good:#17a673;--warn:#c9820a;--bad:#e0324a;
  --text:#191c2b;--sub:#666f8a;--sub2:#98a1b8;
  --shadow-sm:0 2px 8px rgba(30,34,60,.05);--shadow-md:0 14px 32px rgba(30,34,60,.08);
}
html{transition:background-color .2s ease}
html,body{background:var(--bg);color:var(--text);height:100%}
html{scrollbar-gutter:stable;overflow-anchor:none}
.body-wrap{overflow-anchor:none}
@media (prefers-reduced-motion: no-preference){
  /* Keep the original look, but avoid expensive perpetual compositor work. */
}
@media (max-width:1100px){
  *{scroll-behavior:auto!important}
}

/* Performance: never animate the entire DOM. Only interactive controls transition. */
button,.btn,.tab,.nav-btn,.icon-btn,input,select,textarea,.card,.drawer,.toast{
  transition:background-color .14s ease,border-color .14s ease,color .14s ease,box-shadow .14s ease;
}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-thumb{background:var(--line2);border-radius:8px}

/* ===== Shell ===== */
#app{display:flex;height:100vh;position:relative}

/* ============ SIDEBAR ============ */
.sidebar{
  width:252px;flex-shrink:0;height:100vh;display:flex;flex-direction:column;
  background:var(--panel);border-left:1px solid var(--line);position:relative;z-index:30;
  transition:transform .22s ease;
}
.sidebar-brand{display:flex;align-items:center;gap:10px;padding:20px 18px;border-bottom:1px solid var(--line)}
.sidebar-brand img{width:34px;height:34px;border-radius:9px;box-shadow:0 4px 14px rgba(148,85,255,.35)}
.sidebar-brand div{font-weight:800;font-size:14.5px}
.sidebar-brand small{display:block;font-weight:400;font-size:10.5px;color:var(--sub)}
.tabnav{flex:1;display:flex;flex-direction:column;gap:2px;padding:14px 12px;overflow-y:auto}
.tab{
  padding:10px 13px;border-radius:10px;font-size:13px;font-weight:600;color:var(--sub);
  display:flex;align-items:center;gap:10px;white-space:nowrap;transition:.14s;
  border:1px solid transparent;position:relative;
}
.tab i{font-size:17px;width:18px;text-align:center;flex-shrink:0}
.tab:hover{color:var(--text);background:rgba(255,255,255,.04)}
.tab.on{color:#fff;background:linear-gradient(90deg,var(--accent),#7b3ff0);box-shadow:0 6px 18px -4px rgba(148,85,255,.55)}
.tab .bd{background:rgba(255,255,255,.16);border-radius:100px;font-size:10px;padding:1px 7px;margin-right:auto}
.tab.on .bd{background:rgba(255,255,255,.28)}
.sidebar-foot{padding:14px 16px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:10px}
.lang-mini{display:flex;background:var(--panel2);border:1px solid var(--line);border-radius:100px;padding:3px;gap:2px}
.lang-mini button{flex:1;padding:6px 10px;border:0;background:transparent;color:var(--sub);font-size:11px;font-weight:700;border-radius:100px;cursor:pointer}
.lang-mini button.on{background:linear-gradient(90deg,var(--accent-d),var(--accent));color:#fff}

/* ============ TOP BAR (slim) ============ */
.main-col{flex:1;min-width:0;display:flex;flex-direction:column;height:100vh;position:relative}
.topbar{
  height:60px;flex-shrink:0;display:flex;align-items:center;gap:16px;padding:0 22px;
  background:var(--panel);border-bottom:1px solid var(--line);position:relative;z-index:20;
}
.hamburger{display:none;width:34px;height:34px;border-radius:8px;background:var(--panel2);border:1px solid var(--line);align-items:center;justify-content:center;color:var(--sub);font-size:17px}
.page-title{font-weight:800;font-size:14.5px;color:var(--text)}
.page-title span{display:block;font-weight:400;font-size:11px;color:var(--sub);margin-top:1px}
.top-right{display:flex;align-items:center;gap:10px;flex-shrink:0;margin-right:auto}
.user-chip{display:flex;align-items:center;gap:9px;background:var(--panel2);border:1px solid var(--line);padding:6px 12px 6px 8px;border-radius:100px;font-size:12.5px;cursor:pointer}
.user-chip .av{width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,var(--accent),#3ea6ff);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:12px;color:#fff}
.icon-btn{width:36px;height:36px;border-radius:9px;background:var(--panel2);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--sub);font-size:16px}
.icon-btn:hover{color:var(--text);border-color:var(--line2)}
.sidebar-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:29;display:none}
.wide-sidebar .sidebar{width:292px}
.wide-sidebar .main-col{min-width:0}
@media(max-width:980px){
  .hamburger{display:flex}
  .sidebar{position:fixed;top:0;right:0;transform:translateX(105%)}
  #app.sb-open .sidebar{transform:translateX(0)}
  #app.sb-open .sidebar-overlay{display:block}
}

.body-wrap{flex:1;overflow:auto;padding:22px 26px 70px}
.page{display:none;max-width:1320px;margin:0 auto}
.page.on{display:block;animation:fade .18s ease}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@keyframes spin{to{transform:rotate(360deg)}}
.spin{display:inline-block;animation:spin .7s linear infinite}
.no-motion .spin{animation:none}

.pg-head{display:flex;align-items:flex-end;justify-content:space-between;gap:14px;margin-bottom:20px;flex-wrap:wrap}
.pg-head h1{font-size:19px;font-weight:800}
.pg-head p{font-size:12.5px;color:var(--sub);margin-top:3px}
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.search{position:relative}
.search input{width:230px;padding:9px 34px 9px 12px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--text);font-size:13px;outline:none}
.search input:focus{border-color:var(--accent)}
.search i{position:absolute;right:11px;top:50%;transform:translateY(-50%);color:var(--sub2);font-size:15px}
select.sel{padding:9px 12px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--text);font-size:13px;outline:none}
.btn{padding:9px 16px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--text);font-size:13px;font-weight:600;display:inline-flex;align-items:center;gap:7px}
.btn:hover{border-color:var(--line2)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn.primary:hover{background:var(--accent-d)}
.btn.danger{color:var(--bad);border-color:rgba(242,73,85,.3)}
.btn.danger:hover{background:rgba(242,73,85,.08)}
.btn.sm{padding:6px 11px;font-size:12px}
.btn:disabled{opacity:.5;cursor:not-allowed}

/* stat cards */
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;margin-bottom:22px}
.stat-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px}
.stat-card .sc-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.stat-card .sc-icon{width:34px;height:34px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px}
.stat-card .sc-val{font-size:22px;font-weight:800}
.stat-card .sc-label{font-size:11.5px;color:var(--sub);margin-top:2px}

/* table */
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{text-align:right;padding:12px 14px;background:var(--panel2);color:var(--sub);font-weight:700;font-size:11.5px;border-bottom:1px solid var(--line)}
tbody td{padding:11px 14px;border-bottom:1px solid var(--line);vertical-align:middle}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:rgba(255,255,255,.015)}
.mono{font-family:ui-monospace,Consolas,monospace;direction:ltr;text-align:left;font-size:12px;color:var(--sub)}
.badge{display:inline-flex;align-items:center;gap:5px;padding:3px 9px;border-radius:100px;font-size:11px;font-weight:700}
.badge.green{background:rgba(34,197,139,.14);color:var(--good)}
.badge.red{background:rgba(242,73,85,.14);color:var(--bad)}
.badge.gray{background:rgba(135,146,168,.14);color:var(--sub)}
.badge.orange{background:rgba(245,165,36,.14);color:var(--warn)}
.row-actions{display:flex;gap:6px;justify-content:flex-end}
.iconbtn{width:29px;height:29px;border-radius:7px;background:var(--panel2);border:1px solid var(--line);display:inline-flex;align-items:center;justify-content:center;color:var(--sub);font-size:14px}
.iconbtn:hover{color:var(--text);border-color:var(--line2)}
.empty{padding:50px 20px;text-align:center;color:var(--sub2)}
.empty i{font-size:30px;display:block;margin-bottom:10px}
.bar-mini{width:70px;height:6px;background:var(--line2);border-radius:99px;overflow:hidden;display:inline-block;vertical-align:middle;margin-left:6px}
.bar-mini i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--good))}


/* ===== Appearance Studio ===== */
.appearance-studio{display:grid;grid-template-columns:1.25fr .75fr;gap:14px;margin-bottom:18px}.appearance-card{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,rgba(124,92,255,.07),rgba(255,255,255,.018));overflow:hidden}.appearance-card h3{font-size:14px;margin-bottom:4px}.appearance-card p{font-size:10.5px;color:var(--sub);line-height:1.8}.appearance-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:14px}.appearance-field{padding:11px;border:1px solid var(--line);border-radius:12px;background:var(--panel2)}.appearance-field label{display:block;color:var(--sub);font-size:10px;margin-bottom:7px}.appearance-field select{width:100%;padding:9px 10px;border-radius:9px;border:1px solid var(--line);background:var(--panel);color:var(--text);outline:none}.theme-pills,.accent-pills{display:flex;gap:7px;flex-wrap:wrap}.theme-pill,.accent-pill{border:1px solid var(--line);background:var(--panel);color:var(--sub);border-radius:9px;padding:8px 11px;font-size:10px;cursor:pointer}.theme-pill.on,.accent-pill.on{color:#fff;border-color:var(--accent);background:rgba(124,92,255,.14)}.accent-pill{display:flex;align-items:center;gap:6px}.accent-dot{width:10px;height:10px;border-radius:50%;display:inline-block}.appearance-preview{min-height:100%;position:relative;display:flex;align-items:center;justify-content:center}.preview-window{width:100%;max-width:330px;border:1px solid var(--line);border-radius:15px;background:var(--panel);overflow:hidden;box-shadow:0 25px 60px rgba(0,0,0,.22)}.preview-top{height:36px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:6px;padding:0 10px}.preview-top i{font-size:10px;color:var(--sub)}.preview-main{display:grid;grid-template-columns:82px 1fr;min-height:140px}.preview-side{padding:10px;border-left:1px solid var(--line);background:var(--panel2)}.preview-side div{height:22px;border-radius:6px;margin-bottom:6px;background:rgba(255,255,255,.04)}.preview-side div.active{background:linear-gradient(90deg,var(--accent),var(--accent-d))}.preview-content{padding:12px}.preview-content .pv-title{font-size:12px;font-weight:800}.preview-content .pv-sub{font-size:8px;color:var(--sub);margin-top:3px}.pv-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:14px}.pv-cards span{height:45px;border-radius:9px;border:1px solid var(--line);background:rgba(255,255,255,.02)}.appearance-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:13px}.appearance-toggle{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 11px;border:1px solid var(--line);border-radius:11px;background:var(--panel2);font-size:10.5px;color:var(--sub)}.switch{width:38px;height:21px;border-radius:99px;background:var(--line2);position:relative;cursor:pointer;border:0}.switch:after{content:'';position:absolute;width:15px;height:15px;top:2px;right:2px;border-radius:50%;background:#fff;transition:.16s}.switch.on{background:var(--accent)}.switch.on:after{right:21px}.density-compact .tab{padding-top:8px;padding-bottom:8px}.density-compact .body-wrap{padding-top:16px;padding-bottom:45px}.density-compact .card{border-radius:12px}.no-motion *, .no-motion *:before, .no-motion *:after{transition:none!important;animation:none!important;scroll-behavior:auto!important}
@media(max-width:900px){.appearance-studio{grid-template-columns:1fr}}@media(max-width:600px){.appearance-grid{grid-template-columns:1fr}.preview-window{max-width:none}}

.advanced-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px}.pro-action{border:1px solid var(--line);background:linear-gradient(145deg,var(--panel2),rgba(124,92,255,.05));color:var(--text);border-radius:14px;padding:15px;text-align:right;cursor:pointer;box-shadow:var(--ui-glow);}.pro-action i{font-size:20px;color:var(--accent);display:block;margin-bottom:10px}.pro-action b{display:block;font-size:11px}.pro-action small{display:block;color:var(--sub);font-size:9px;margin-top:4px}.accent-pills{max-height:92px;overflow:auto}.radius-sharp .card,.radius-sharp .appearance-card,.radius-sharp .appearance-field,.radius-sharp .btn,.radius-sharp .tab,.radius-sharp .search input{border-radius:6px}.radius-pill .card,.radius-pill .appearance-card,.radius-pill .appearance-field{border-radius:24px}.radius-pill .btn,.radius-pill .tab,.radius-pill .search input{border-radius:999px}.font-small{font-size:92%}.font-large{font-size:108%}.appearance-card,.card,.pro-action{box-shadow:var(--ui-glow)}
@media(max-width:900px){.advanced-grid{grid-template-columns:1fr 1fr}}@media(max-width:600px){.advanced-grid{grid-template-columns:1fr}}

.ib-quickstats{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 14px}.ib-quickstats>div{position:relative;overflow:hidden;display:flex;align-items:center;gap:10px;padding:12px 15px;border:1px solid var(--line);background:linear-gradient(155deg,rgba(255,255,255,.03),rgba(255,255,255,.01));border-radius:14px;flex:1;min-width:150px;transition:transform .15s ease,border-color .15s ease}.ib-quickstats>div:hover{transform:translateY(-2px);border-color:var(--line2)}.ib-quickstats i{width:32px;height:32px;display:grid;place-items:center;border-radius:9px;background:rgba(124,92,255,.12);color:#a997ff;font-size:15px;flex-shrink:0}.ib-quickstats b{display:block;font-size:17px;line-height:1.2}.ib-quickstats small{display:block;color:var(--sub2);font-size:9.5px;margin-top:2px}
/* ===== Inbound cards (grid) ===== */
.ib-listbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 12px;flex-wrap:wrap}
.ib-selectall{display:flex;align-items:center;gap:8px;font-size:11.5px;color:var(--sub);cursor:pointer;user-select:none}
.ib-selectall input{width:15px;height:15px;accent-color:var(--accent);cursor:pointer}
.ib-count{font-size:11px;color:var(--sub2)}
.ib-bulkbar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:11px 16px;background:linear-gradient(90deg,rgba(148,85,255,.12),rgba(148,85,255,.04));border:1px solid rgba(148,85,255,.28);border-radius:13px;font-size:11.5px;color:var(--sub);flex-wrap:wrap;margin-bottom:12px}
.ib-bulkbar b{color:var(--text)}.ib-bulkactions{display:flex;gap:6px}
.ib-check{width:15px;height:15px;accent-color:var(--accent);cursor:pointer}

.ib-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(328px,1fr));gap:14px}
.ib-card{position:relative;display:flex;flex-direction:column;gap:13px;padding:16px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(165deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:var(--shadow-sm);overflow:hidden;transition:transform .15s ease,border-color .15s ease,box-shadow .15s ease}
.ib-card:before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:linear-gradient(90deg,var(--accent),#39d6ff)}
.ib-card:hover{border-color:var(--line2);box-shadow:var(--shadow-md)}
.ib-card.ib-off{opacity:.58}
.ib-card.ib-off:before{background:var(--sub2)}
.ib-card.ib-off:hover{opacity:.85}
.ib-card.ib-selected{border-color:var(--accent);box-shadow:0 0 0 3px rgba(148,85,255,.14)}

.ib-card-head{display:flex;align-items:flex-start;gap:11px}
.ib-card-check{position:absolute;top:14px;left:14px;opacity:0;pointer-events:none;transition:opacity .15s ease}
.ib-card:hover .ib-card-check,.ib-card.ib-selected .ib-card-check{opacity:1;pointer-events:auto}
.ib-avatar{width:40px;height:40px;border-radius:12px;flex-shrink:0;display:grid;place-items:center;font-size:17px;background:rgba(148,85,255,.14);color:#b79bff;border:1px solid rgba(148,85,255,.22)}
.ib-card-id{flex:1;min-width:0;padding-left:20px}
.ib-card-id .ib-name-top{display:flex;align-items:center;gap:6px}
.ib-card-id b{font-size:13px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%;display:block}
.ib-card-id .mono{font-size:9.5px;color:var(--sub2);margin-top:2px}
.ib-card-controls{display:flex;flex-direction:column;align-items:flex-end;gap:7px;flex-shrink:0}

.ib-tagrow{display:flex;flex-wrap:wrap;gap:5px}
.ib-tagrow span{padding:3px 8px;border-radius:7px;background:var(--panel2);border:1px solid var(--line);font-size:9.5px;font-weight:700;letter-spacing:.01em;color:var(--sub);white-space:nowrap;transition:border-color .12s ease}
.ib-card:hover .ib-tagrow span{border-color:var(--line2)}
.ib-live-tag{background:rgba(34,197,139,.14)!important;color:var(--good)!important;border-color:transparent!important;display:inline-flex!important;align-items:center;gap:4px}
.ib-live-tag i{width:5px;height:5px;border-radius:50%;background:var(--good);animation:ibLivePulse 1.6s ease-in-out infinite;flex-shrink:0}
@keyframes ibLivePulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.35);opacity:.6}}
.no-motion .ib-live-tag i{animation:none}
.ib-linkonly-tag{background:rgba(242,73,85,.12)!important;color:var(--bad)!important;border-color:transparent!important}

.ib-card-addr{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:8px 11px;border-radius:10px;background:var(--panel2);border:1px solid var(--line)}
.ib-card-addr span.mono{font-size:11px;color:var(--text)}
.ib-card-addr small{font-size:9px;color:var(--sub2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:110px}

.ib-card-traffic{display:flex;flex-direction:column;gap:6px}
.ib-card-traffic .ib-tf-top{display:flex;align-items:center;justify-content:space-between;font-size:9.5px;color:var(--sub2)}
.ib-card-traffic .ib-tf-top b{font-size:11.5px;color:var(--text);font-weight:800}
.ib-progress{height:6px;border-radius:99px;background:var(--line2);overflow:hidden;box-shadow:inset 0 0 0 1px var(--line)}
.ib-progress i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--accent),#39d6ff);transition:width .3s ease}
.ib-progress i.warn{background:linear-gradient(90deg,#f5a524,#f59e0b)}
.ib-progress i.crit{background:linear-gradient(90deg,#f24955,#ef4444)}

.ib-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:7px}
.ib-card-stats>div{padding:8px 9px;border-radius:10px;background:var(--panel2);border:1px solid var(--line);text-align:center}
.ib-card-stats small{display:block;color:var(--sub2);font-size:8.5px;margin-bottom:3px}
.ib-card-stats b{font-size:11px}
.ib-card-stats b.soon{color:var(--warn)}
.ib-card-stats b.expired{color:var(--bad)}

.ib-card-foot{display:flex;align-items:center;justify-content:space-between;gap:8px;padding-top:2px;border-top:1px dashed var(--line);padding-top:11px}
.ib-card-foot .ib-clientcell{display:flex;align-items:center;gap:7px;font-size:10.5px;color:var(--sub)}
.ib-card-foot .ib-clientcell .iconbtn{width:27px;height:27px;font-size:12px}
.ib-card-actions{display:flex;gap:5px}
.ib-card-actions .iconbtn{width:29px;height:29px;font-size:13px;border-radius:9px;transition:transform .12s ease,background-color .12s ease,color .12s ease}
.ib-card-actions .iconbtn:hover{transform:translateY(-1px);background:var(--panel2)}

.ib-switch{width:34px;height:19px;border-radius:99px;background:var(--line2);position:relative;cursor:pointer;border:0;flex-shrink:0;box-shadow:inset 0 0 0 1px var(--line)}
.ib-switch:after{content:'';position:absolute;width:13px;height:13px;top:3px;right:3px;border-radius:50%;background:#fff;transition:.16s}
.ib-switch.on{background:linear-gradient(90deg,var(--accent),#39d6ff);box-shadow:0 0 12px rgba(148,85,255,.35)}
.ib-switch.on:after{right:18px}
.ib-status-dot{width:8px;height:8px;border-radius:50%;background:#7688a9;flex-shrink:0}
.ib-status-dot.green{background:#22c58b;box-shadow:0 0 0 3px rgba(34,197,139,.18);animation:ibLivePulse 1.6s ease-in-out infinite}
.ib-status-dot.red{background:#f24955}
.no-motion .ib-status-dot{animation:none}
@media(max-width:560px){.ib-grid{grid-template-columns:1fr}}
.ov-quickstats>div{position:relative;overflow:hidden}
.ov-quickstats>div:nth-child(1) i{background:rgba(124,92,255,.14);color:#a997ff}
.ov-quickstats>div:nth-child(2) i{background:rgba(34,197,139,.14);color:#22c58b}
.ov-quickstats>div:nth-child(3) i{background:rgba(53,214,255,.14);color:#35d6ff}
.ov-quickstats>div:nth-child(4) i{background:rgba(245,165,36,.14);color:#f5a524}
.ov-toplinks{padding:14px 18px}
.ov-toplink-row{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px dashed var(--line)}
.ov-toplink-row:last-child{border-bottom:none}
.ov-toplink-row .otl-rank{width:20px;height:20px;border-radius:6px;background:var(--panel2);display:grid;place-items:center;font-size:10px;color:var(--sub2);flex-shrink:0}
.ov-toplink-row .otl-info{flex:1;min-width:0}
.ov-toplink-row .otl-info b{font-size:11.5px;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ov-toplink-row .otl-bar{height:4px;border-radius:99px;background:var(--line2);margin-top:5px;overflow:hidden}
.ov-toplink-row .otl-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),#39d6ff);border-radius:99px}
.ov-toplink-row .otl-val{font-size:10px;color:var(--sub2);white-space:nowrap;flex-shrink:0}
.ov-empty{padding:20px;text-align:center;color:var(--sub2);font-size:11px}
@media(max-width:900px){.ib-quickstats{flex-direction:column}}

/* drawer */
.overlay{position:fixed;inset:0;background:rgba(4,6,10,.55);backdrop-filter:blur(2px);z-index:90;display:none}
.overlay.show{display:block}
.drawer{position:fixed;top:0;left:0;bottom:0;width:680px;max-width:92vw;background:var(--panel);border-left:1px solid var(--line);z-index:91;transform:translateX(-105%);transition:transform .22s cubic-bezier(.4,0,.2,1);display:flex;flex-direction:column}
.drawer.show{transform:translateX(0)}
.dr-head{padding:18px 20px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between}
.dr-head h3{font-size:15px;font-weight:800}
.dr-body{flex:1;overflow:auto;padding:18px 20px}
.dr-foot{padding:16px 20px;border-top:1px solid var(--line);display:flex;gap:10px}
.grp{margin-bottom:16px}
.grp label{display:block;font-size:12px;font-weight:600;color:var(--sub);margin-bottom:6px}
.grp input,.grp select,.grp textarea{width:100%;padding:10px 12px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--text);font-size:13px;outline:none}
.grp input:focus,.grp select:focus,.grp textarea:focus{border-color:var(--accent)}
.grp textarea{resize:vertical;min-height:64px;font-family:ui-monospace,monospace;direction:ltr;text-align:left}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.chk{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text)}
.hint{font-size:11px;color:var(--sub2);margin-top:5px;line-height:1.7}
.divider{height:1px;background:var(--line);margin:18px 0}
.inbound-builder{display:flex;flex-direction:column;gap:16px}
.ib-hero{padding:16px;border:1px solid var(--line);border-radius:14px;background:linear-gradient(135deg,rgba(79,124,255,.10),rgba(168,85,247,.07));display:flex;align-items:center;justify-content:space-between;gap:12px}
.ib-hero .ib-title{display:flex;align-items:center;gap:12px}.ib-hero .ib-icon{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:linear-gradient(135deg,var(--accent),#6d5dfc);color:#fff;font-size:20px;box-shadow:0 10px 24px rgba(79,124,255,.22)}
.ib-hero b{display:block;font-size:14px}.ib-hero small{display:block;color:var(--sub);font-size:11px;margin-top:3px}
.ib-section{border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.018);overflow:hidden}.ib-section-head{padding:12px 14px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between}.ib-section-head b{font-size:12.5px}.ib-section-head small{font-size:10.5px;color:var(--sub2)}
.ib-section-body{padding:14px}.ib-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.ib-grid.three{grid-template-columns:1fr 1fr 1fr}.ib-full{grid-column:1/-1}
.ib-choice{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
/* Professional inbound protocol/transport matrix — renamed to .ib-opt (was
   accidentally reusing the .ib-card class name used by the main inbound
   dashboard cards above; that collision was overriding the dashboard card
   layout with these small radio-tile rules). */
.ib-matrix{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:9px}
.ib-opt{position:relative;display:flex;align-items:center;gap:10px;padding:12px;border:1px solid var(--line);border-radius:12px;background:linear-gradient(145deg,rgba(255,255,255,.025),rgba(255,255,255,.01));cursor:pointer;transition:.16s;user-select:none}
.ib-opt:hover{border-color:rgba(168,85,247,.45);transform:translateY(-1px)}
.ib-opt.on{border-color:var(--accent);background:linear-gradient(145deg,rgba(124,58,237,.18),rgba(168,85,247,.08));box-shadow:0 8px 24px rgba(124,58,237,.12),inset 0 0 0 1px rgba(168,85,247,.18)}
.ib-opt.off{opacity:.42;cursor:not-allowed;filter:saturate(.5)}
.ib-opt input{position:absolute;opacity:0;pointer-events:none}
.ib-opt .ib-opt-icon{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:rgba(255,255,255,.05);color:var(--accent);font-size:17px;flex:0 0 auto}
.ib-opt b{display:block;font-size:11.5px}.ib-opt small{display:block;color:var(--sub2);font-size:8.5px;margin-top:2px}
.ib-step{display:flex;align-items:center;gap:8px;margin-bottom:11px}.ib-step .num{width:24px;height:24px;border-radius:8px;display:grid;place-items:center;background:rgba(124,58,237,.16);color:#c9a8ff;font-size:10px;font-weight:900}.ib-step b{font-size:12px}.ib-step small{display:block;color:var(--sub2);font-size:9px;margin-top:2px}
.ib-divider{height:1px;background:var(--line);margin:15px 0}
.ib-mode-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.ib-mini{padding:9px;border:1px solid var(--line);border-radius:10px;background:var(--panel2);font-size:10px;text-align:center;color:var(--sub)}
.ib-mini b{display:block;color:var(--text);font-size:11px;margin-bottom:2px}
.ib-mini.active{border-color:rgba(34,197,139,.35);background:rgba(34,197,139,.06)}
@media(max-width:700px){.ib-matrix{grid-template-columns:repeat(2,1fr)}.ib-mode-grid{grid-template-columns:repeat(2,1fr)}}
.ib-choice label{position:relative}.ib-choice input{position:absolute;opacity:0;pointer-events:none}.ib-choice span{display:flex;align-items:center;gap:8px;padding:10px 11px;border:1px solid var(--line);border-radius:10px;background:var(--panel2);font-size:12px;cursor:pointer;transition:.15s}.ib-choice span i{font-size:15px;color:var(--sub)}.ib-choice input:checked+span{border-color:var(--accent);background:rgba(79,124,255,.12);box-shadow:inset 0 0 0 1px rgba(79,124,255,.25)}.ib-choice input:checked+span i{color:var(--accent)}
.ib-status{padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:rgba(0,0,0,.12);font-size:11px;line-height:1.8}.ib-status.ok{border-color:rgba(34,197,139,.3);background:rgba(34,197,139,.07)}.ib-status.warn{border-color:rgba(245,165,36,.3);background:rgba(245,165,36,.07)}
.ib-summary{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.ib-summary .sum{padding:9px 10px;border:1px solid var(--line);border-radius:9px;background:var(--panel2)}.ib-summary small{display:block;color:var(--sub2);font-size:9.5px}.ib-summary b{display:block;margin-top:3px;font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ib-advanced{display:none}.ib-advanced.open{display:block}.ib-advanced-toggle{width:100%;justify-content:space-between}.ib-help{font-size:10.5px;color:var(--sub2);line-height:1.8;margin-top:6px}.ib-danger{color:#ff9b9b}
@media(max-width:600px){.ib-grid,.ib-grid.three,.ib-choice,.ib-summary{grid-template-columns:1fr}.ib-full{grid-column:auto}}

.section-title{font-size:12px;font-weight:800;color:var(--sub);text-transform:uppercase;letter-spacing:.03em;margin-bottom:10px}

/* ===== Message Center ===== */
.message-center{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-bottom:14px}.message-stat{padding:15px;border:1px solid var(--line);border-radius:15px;background:linear-gradient(145deg,var(--panel),rgba(124,92,255,.04));position:relative;overflow:hidden}.message-stat:after{content:"";position:absolute;inset:auto -20px -30px auto;width:90px;height:90px;border-radius:50%;background:radial-gradient(circle,var(--accent),transparent 68%);opacity:.08}.message-stat .ms-icon{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:rgba(124,92,255,.12);color:var(--accent);margin-bottom:10px}.message-stat b{font-size:22px;display:block}.message-stat small{display:block;color:var(--sub);font-size:9px;margin-top:4px}.message-stat.danger .ms-icon{color:#fb7185;background:rgba(244,63,94,.11)}.message-stat.warn .ms-icon{color:#fbbf24;background:rgba(245,158,11,.11)}.message-stat.good .ms-icon{color:#34d399;background:rgba(16,185,129,.11)}.message-toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.message-filter{display:flex;gap:6px;flex-wrap:wrap}.message-filter button{padding:7px 10px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--sub);font-size:10px;cursor:pointer}.message-filter button.on{border-color:var(--accent);color:var(--text);background:rgba(124,92,255,.12)}.message-list{display:flex;flex-direction:column;gap:8px;padding:12px}.message-row{display:grid;grid-template-columns:38px 1fr auto;gap:10px;align-items:start;padding:12px;border:1px solid var(--line);border-radius:13px;background:rgba(255,255,255,.015)}.message-row:hover{border-color:color-mix(in srgb,var(--accent) 40%,var(--line));background:rgba(255,255,255,.025)}.message-row .mi{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:rgba(255,255,255,.04);color:var(--sub)}.message-row.err .mi{color:#fb7185;background:rgba(244,63,94,.09)}.message-row.warn .mi{color:#fbbf24;background:rgba(245,158,11,.09)}.message-row.ok .mi{color:#34d399;background:rgba(16,185,129,.09)}.message-row .mt{min-width:0}.message-row .mt b{font-size:11px;display:block;line-height:1.8}.message-row .mt p{font-size:9px;color:var(--sub);margin-top:3px;word-break:break-word;line-height:1.8}.message-row .meta{text-align:left;direction:ltr;color:var(--sub2);font-size:8px;white-space:nowrap}.message-row .meta strong{display:block;color:var(--sub);font-size:9px;margin-bottom:3px}.error-detail{margin-top:8px;padding:9px;border-radius:9px;background:rgba(0,0,0,.16);border:1px dashed var(--line);font-family:ui-monospace,Consolas,monospace;font-size:8px;line-height:1.8;direction:ltr;text-align:left;white-space:pre-wrap;word-break:break-word;color:#aeb9d2;max-height:120px;overflow:auto}.message-empty{padding:45px 20px;text-align:center;color:var(--sub);font-size:11px}.message-empty i{display:block;font-size:34px;color:var(--good);margin-bottom:10px}.message-auto{font-size:9px;color:var(--sub2);margin-right:auto}@media(max-width:900px){.message-center{grid-template-columns:repeat(2,1fr)}}@media(max-width:600px){.message-center{grid-template-columns:1fr 1fr}.message-row{grid-template-columns:34px 1fr}.message-row .meta{grid-column:2;text-align:right;direction:rtl}.message-auto{display:none}}
/* toast */
#toastWrap{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);z-index:200;display:flex;flex-direction:column;gap:8px}
.toast{background:var(--panel2);border:1px solid var(--line2);padding:11px 18px;border-radius:10px;font-size:13px;display:flex;align-items:center;gap:9px;box-shadow:0 10px 30px rgba(0,0,0,.4);animation:up .18s ease}
.toast.ok{border-color:rgba(34,197,139,.4)}.toast.ok i{color:var(--good)}
.toast.err{border-color:rgba(242,73,85,.4)}.toast.err i{color:var(--bad)}
@keyframes up{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.qr-box{background:#fff;padding:10px;border-radius:12px;width:150px;height:150px;margin:0 auto 12px}
.qr-box img{width:100%;height:100%}
.copy-row{display:flex;gap:8px}
.copy-row input{flex:1}

.two-col{display:grid;grid-template-columns:1.1fr .9fr;gap:18px}
@media(max-width:980px){.two-col{grid-template-columns:1fr}}
.status-dot{width:9px;height:9px;border-radius:50%;display:inline-block;margin-left:6px}
.status-dot.on{background:var(--good);box-shadow:0 0 0 3px rgba(34,197,139,.18)}
.status-dot.off{background:var(--sub2)}
.settings-card{padding:20px}
.link-cell{display:flex;flex-direction:column;gap:2px}
.link-cell b{font-size:13px}
.link-cell span{font-size:11px;color:var(--sub2)}
.loading{opacity:.5;pointer-events:none}

/* ALISON 17 — original premium control-center skin */
body{background:radial-gradient(900px 500px at 75% -10%,rgba(124,92,255,.10),transparent 65%),var(--bg)}
/* رفع باگ اصلیِ «پوسته روشن»: پیش‌تر پس‌زمینه‌ی سایدبار و نوار بالا همیشه
   با رنگ ثابت تیره نوشته شده بود و data-theme را نادیده می‌گرفت؛ در نتیجه
   با فعال کردن پوسته‌ی روشن، فقط بدنه‌ی صفحه سفید می‌شد ولی سایدبار/تاپ‌بار
   تیره می‌ماند (ظاهر ناقص و دو رنگ). این‌جا هر دو حالت را صریحاً تعریف می‌کنیم. */
[data-theme="dark"] .sidebar,
:root:not([data-theme]) .sidebar{background:linear-gradient(180deg,#0d111b 0%,#0b0f17 100%);box-shadow:inset -1px 0 rgba(255,255,255,.04),20px 0 60px rgba(0,0,0,.16)}
[data-theme="light"] .sidebar{background:linear-gradient(180deg,#ffffff 0%,#f7f8fb 100%);box-shadow:inset -1px 0 rgba(0,0,0,.04),20px 0 50px rgba(30,34,60,.05)}
.sidebar{width:268px}
.sidebar-brand{padding:18px 20px 17px}.sidebar-brand img{width:38px;height:38px;border-radius:12px}.sidebar-brand div{font-size:15px}.sidebar-brand small{color:var(--sub2)}
.tab{padding:11px 14px;border-radius:11px;margin:2px 0}.tab-locked{opacity:.58}.tab-locked:hover{opacity:.85}.tab.on{background:linear-gradient(135deg,var(--accent),var(--accent-d));box-shadow:0 10px 25px -10px rgba(124,92,255,.55)}
[data-theme="dark"] .topbar,
:root:not([data-theme]) .topbar{height:68px;padding:0 26px;background:rgba(13,17,27,.88);backdrop-filter:none;box-shadow:0 1px 0 rgba(255,255,255,.025)}
[data-theme="light"] .topbar{height:68px;padding:0 26px;background:rgba(255,255,255,.88);backdrop-filter:none;box-shadow:0 1px 0 rgba(30,34,60,.04)}
.body-wrap{padding:24px 28px 70px}.page{max-width:1440px}
.pg-head{margin-bottom:18px}.pg-head h1{font-size:22px;letter-spacing:-.4px}.pg-head p{font-size:12px}
.eyebrow{font-size:10px;letter-spacing:.16em;color:#8d82c9;font-weight:800;margin-bottom:7px}.live-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#22c58b;box-shadow:0 0 0 4px rgba(34,197,139,.10);vertical-align:middle;margin-left:5px}
.stat-grid{gap:12px}.stat-card{border-radius:16px;padding:16px 18px;background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.018));box-shadow:var(--shadow-sm)}
.card{border-radius:16px;background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.018));box-shadow:var(--shadow-sm)}
.inbound-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:0 0 16px}.inbound-strip>div{display:flex;align-items:center;gap:11px;padding:13px 15px;border:1px solid var(--line);background:rgba(255,255,255,.018);border-radius:13px}.inbound-strip i{width:34px;height:34px;display:grid;place-items:center;border-radius:10px;background:rgba(124,92,255,.12);color:#a997ff;font-size:17px}.inbound-strip b{display:block;font-size:12px}.inbound-strip small{display:block;color:var(--sub);font-size:10px;margin-top:2px}.btn-inbound{padding-left:20px;padding-right:20px;box-shadow:0 12px 30px -12px rgba(124,92,255,.75)}
.endpoint-input{display:flex;gap:7px;align-items:stretch}.endpoint-input input{flex:1;min-width:0}.endpoint-btn{white-space:nowrap;padding:9px 11px;font-size:11px}.endpoint-btn:disabled{opacity:.65}.ib-status.ok{border-color:rgba(34,197,139,.35)!important}.ib-status.warn{border-color:rgba(245,165,36,.35)!important}@media(max-width:800px){.inbound-strip{grid-template-columns:1fr}.body-wrap{padding:18px 14px 60px}}

.resource-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px}.resource-card{min-height:126px;padding:13px 15px;border:1px solid var(--line);border-radius:14px;background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.015));overflow:hidden}.rc-head{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--sub);font-weight:800;letter-spacing:.08em}.rc-head i{margin-left:5px;color:#7688a9}.rc-head b{font-size:21px;color:var(--text);letter-spacing:0}.rc-sub{font-size:9px;color:var(--sub2);margin-top:6px}.spark{display:block;width:100%;height:44px;margin-top:9px}.spark polyline{fill:none;stroke:#557bff;stroke-width:2;vector-effect:non-scaling-stroke}.spark path{fill:rgba(85,123,255,.08);stroke:none}.traffic-layout{display:grid;grid-template-columns:minmax(0,1.65fr) minmax(290px,.55fr);gap:14px;margin-bottom:14px}.traffic-card,.connection-card{padding:0}.panel-head{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--line)}.panel-head b{display:block;font-size:10px;letter-spacing:.09em}.panel-head small{display:block;color:var(--sub2);font-size:9px;margin-top:4px}.panel-head>i{color:var(--sub2)}.traffic-legend{display:flex;gap:14px;font-size:10px;color:var(--sub)}.traffic-legend b{color:var(--text)}.big-chart{height:250px;padding:10px 14px 0}.big-chart svg{width:100%;height:100%}.big-chart polyline{fill:none;stroke:#5b78d9;stroke-width:2;vector-effect:non-scaling-stroke}.big-chart .area{fill:rgba(91,120,217,.07);stroke:none}.traffic-foot{display:grid;grid-template-columns:1fr 1fr 1.5fr;padding:12px 16px;border-top:1px solid var(--line)}.traffic-foot small{display:block;color:var(--sub2);font-size:8px}.traffic-foot b{font-size:12px}.connection-number{font-size:28px;font-weight:900;padding:16px 18px 0}.connection-label{font-size:8px;color:var(--sub2);padding:2px 18px}.conn-chart{width:100%;height:120px;padding:0 12px}.conn-chart polyline{fill:none;stroke:#4f7cff;stroke-width:2;vector-effect:non-scaling-stroke}.conn-chart .area{fill:rgba(79,124,255,.08);stroke:none}.conn-foot{display:flex;justify-content:space-between;padding:10px 16px;border-top:1px solid var(--line);font-size:9px;color:var(--sub)}.conn-foot b{color:var(--text)}.bottom-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}.mini-panel{padding-bottom:10px}.health-row{display:flex;justify-content:space-between;padding:10px 16px;border-bottom:1px solid var(--line);font-size:11px}.health-row:last-child{border-bottom:0}.health-row span{color:var(--sub)}.health-row b{max-width:68%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.mono{direction:ltr;text-align:left}.mini-panel .panel-head .badge{font-size:8px}.inbound-head{align-items:center}@media(max-width:1050px){.resource-grid{grid-template-columns:repeat(2,1fr)}.traffic-layout{grid-template-columns:1fr}.bottom-grid{grid-template-columns:1fr}}@media(max-width:560px){.resource-grid{grid-template-columns:1fr}.traffic-foot{grid-template-columns:1fr;gap:10px}.big-chart{height:190px}}

.client-manager{display:flex;flex-direction:column;gap:12px}.client-hero{display:flex;justify-content:space-between;gap:12px;padding:14px;border:1px solid var(--line);border-radius:14px;background:linear-gradient(135deg,rgba(124,92,255,.12),rgba(57,214,255,.04))}.client-hero b{display:block;font-size:13px}.client-hero small{display:block;color:var(--sub);font-size:10px;line-height:1.8;margin-top:4px}.client-create{padding:14px;border:1px solid var(--line);border-radius:14px;background:var(--panel2)}.client-list{display:flex;flex-direction:column;gap:8px}.client-row{display:flex;align-items:center;gap:10px;padding:11px;border:1px solid var(--line);border-radius:13px;background:rgba(255,255,255,.018)}.client-avatar{width:38px;height:38px;display:grid;place-items:center;border-radius:11px;background:rgba(124,92,255,.12);color:var(--accent);font-size:17px}.client-main{flex:1;min-width:0}.client-main b{display:block;font-size:11px}.client-main small{display:block;color:var(--sub2);font-size:8px;margin-top:3px;overflow:hidden;text-overflow:ellipsis}.client-tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}.client-tags span{font-size:8px;color:var(--sub);padding:4px 6px;border:1px solid var(--line);border-radius:7px}.client-actions{display:flex;gap:5px}.empty-client{padding:24px;text-align:center;color:var(--sub2);font-size:10px}.danger-note{border-color:rgba(239,68,68,.3)!important}
.pro-diagnostics{overflow:hidden}.diag-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px}.diag-item{border:1px solid var(--line);border-radius:13px;padding:12px;background:rgba(255,255,255,.018)}.diag-item small,.diag-item span{display:block;color:var(--sub2);font-size:9px}.diag-item b{display:block;font-size:18px;margin:5px 0}.diag-empty{grid-column:1/-1;padding:22px;text-align:center;color:var(--sub2)}@media(max-width:900px){.diag-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:520px){.diag-grid{grid-template-columns:1fr}}
</style>
<style id="alison-yellow-rebuild">
/* ALISON // YELLOW SIGNAL REBUILD
   A deliberate visual reset: solar yellow canvas, carbon panels, irregular geometry.
*/
:root{
  --bg:#f4c84d!important;--panel:#171916!important;--panel2:#23251f!important;
  --line:rgba(255,255,255,.13)!important;--line2:rgba(255,255,255,.28)!important;
  --accent:#ffd84f!important;--accent-d:#ef9f1b!important;--good:#9df06e!important;
  --warn:#ffd84f!important;--bad:#ff7180!important;--text:#fff9df!important;
  --sub:#c4bfa9!important;--sub2:#8f8a75!important;
  --shadow-sm:0 8px 20px rgba(35,28,4,.12)!important;--shadow-md:0 24px 60px rgba(35,28,4,.22)!important;
}
html,body{background:#f4c84d!important;color:var(--text)!important}
body{background-image:radial-gradient(900px 620px at 6% -12%,#fff3a2 0,transparent 58%),radial-gradient(700px 500px at 98% 110%,#e89b1f 0,transparent 65%),linear-gradient(135deg,#f8d55d,#eebc35)!important}
body:before{opacity:.26!important;background-image:linear-gradient(rgba(31,29,17,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(31,29,17,.08) 1px,transparent 1px)!important;background-size:34px 34px!important;mask-image:linear-gradient(#000,transparent 86%)!important}
#app{gap:0!important}
.sidebar{width:286px!important;background:#141613!important;border:0!important;border-left:1px solid rgba(255,255,255,.10)!important;box-shadow:18px 0 60px rgba(60,42,3,.18)!important}
.sidebar-brand{height:100px!important;padding:22px 20px!important;border-bottom:1px solid rgba(255,255,255,.12)!important}
.sidebar-brand img{border-radius:15px!important;filter:grayscale(.1) sepia(.2) drop-shadow(0 8px 18px rgba(255,213,65,.25))!important}
.sidebar-brand span{color:#fff5b5!important;font-size:22px!important;letter-spacing:.17em!important}
.sidebar-brand small{color:#ffd84f!important;letter-spacing:.2em!important}
.tabnav{padding:20px 14px!important;gap:8px!important}
.tab{height:50px!important;border:1px solid transparent!important;border-radius:18px 10px 18px 10px!important;padding:0 15px!important;color:#8c9183!important}
.tab i{color:#6d7666!important;font-size:20px!important}
.tab:hover{background:#242820!important;color:#fffbdc!important;border-color:#3c4032!important;transform:translateX(-3px)}
.tab:hover i{color:#ffd84f!important}
.tab.on{background:linear-gradient(105deg,#ffd84f,#ee9f1d)!important;border-color:#ffe994!important;color:#1b1c16!important;box-shadow:8px 10px 24px rgba(44,31,0,.22),inset 0 1px rgba(255,255,255,.46)!important}
.tab.on i{color:#25251a!important}.tab.on .bd{background:rgba(24,25,17,.18)!important;color:#222!important}
.bd{background:#34382e!important;color:#e8f0bd!important}
.sidebar-foot{padding:17px!important;border-top:1px solid rgba(255,255,255,.12)!important}
.lang-mini,.user-chip{background:#20231d!important;border-color:#393e32!important}.lang-mini button.on{background:#ffd84f!important;color:#25251a!important}.user-chip{border-radius:20px!important;color:#fffbdc!important}.user-chip .av{background:linear-gradient(135deg,#ffd84f,#ef991c)!important;color:#202016!important;box-shadow:none!important}
.main-col{background:transparent!important}.topbar{height:84px!important;background:rgba(23,25,22,.90)!important;border-bottom:1px solid rgba(255,255,255,.10)!important;backdrop-filter:blur(16px)!important}.page-title{color:#fff9dc!important}.page-title span:last-child{color:#b7b59b!important}.top-right .icon-btn{background:#22251f!important;border-color:#404536!important;color:#e6dfb6!important;border-radius:14px!important}.top-right .icon-btn:hover{color:#ffd84f!important;border-color:#ffd84f!important}
.body-wrap{padding:30px 34px 80px!important;max-width:none!important}.page{max-width:1500px!important}.pg-head{margin-bottom:25px!important}.pg-head h1{font-size:38px!important;color:#171813!important;letter-spacing:-.06em!important}.pg-head p{color:#594e2e!important}.eyebrow{color:#4a3b13!important;font-weight:900!important}.live-dot{background:#1c2414!important;box-shadow:0 0 0 5px rgba(28,36,20,.11),0 0 16px #1c2414!important}
.toolbar .btn,.btn{background:#20231d!important;border-color:#3c4232!important;color:#fff6c9!important;border-radius:14px 8px 14px 8px!important;box-shadow:0 7px 18px rgba(50,38,5,.12)!important}.toolbar .btn:hover,.btn:hover{background:#2d3228!important;border-color:#ffd84f!important;color:#fffbdc!important}.btn.primary{background:#1c1d18!important;border-color:#1c1d18!important;color:#ffd84f!important;box-shadow:0 10px 22px rgba(37,27,2,.24)!important}.btn.primary:hover{background:#000!important;color:#ffe777!important}
.card,.resource-card,.stat-card,.traffic-card,.connection-card,.mini-panel,.settings-card,.admin-card,.resource-grid>div{background:linear-gradient(145deg,#1e211b,#131512)!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:28px 12px 28px 12px!important;box-shadow:0 24px 65px rgba(54,39,2,.20),inset 0 1px rgba(255,255,255,.06)!important}.card:hover,.resource-card:hover,.ib-card:hover{border-color:#ffd84f!important;box-shadow:0 28px 76px rgba(54,39,2,.26),0 0 0 1px rgba(255,216,79,.18)!important}
.stat-card{position:relative;overflow:hidden;border-radius:22px 10px 22px 10px!important}.stat-card:after{content:'';position:absolute;left:-35px;bottom:-45px;width:120px;height:100px;background:#ffd84f19;transform:rotate(-28deg)}.stat-card .sc-icon{background:#ffd84f22!important;color:#ffd84f!important}
.resource-grid{gap:16px!important}.resource-card{min-height:148px!important}.traffic-layout,.bottom-grid{gap:16px!important}.panel-head{border-bottom-color:rgba(255,255,255,.10)!important}.mono{color:#d8d3b7!important}
#pg-overview .pg-head{padding:24px 26px!important;border-radius:34px 12px 34px 12px!important;background:#ffd84f!important;box-shadow:0 18px 36px rgba(74,52,3,.18)!important}.#pg-overview .pg-head h1{color:#171813!important}.#pg-overview .pg-head p{color:#5f501d!important}
.ib-quickstats{gap:12px!important;margin-bottom:18px!important}.ib-quickstats>div{background:#1c1f1a!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:20px 8px 20px 8px!important;box-shadow:0 16px 32px rgba(54,39,2,.17)!important}.ib-quickstats i{color:#ffd84f!important}.ib-quickstats b{color:#fff7c9!important}
#pg-links .pg-head{padding:24px 26px!important;border-radius:36px 13px 36px 13px!important;background:linear-gradient(100deg,#ffd84f 0 57%,#20231d 57%)!important;box-shadow:0 18px 36px rgba(74,52,3,.20)!important}.#pg-links .pg-head h1{color:#171813!important}.#pg-links .pg-head p{color:#5f501d!important}.#pg-links .pg-head .eyebrow{color:#3f3513!important}.#pg-links .pg-head .toolbar{align-self:center}
.search input,.sel,input,select,textarea{background:#292c24!important;border-color:#4a503d!important;color:#fff8d7!important;border-radius:15px 8px 15px 8px!important}.search input::placeholder{color:#9ea28e!important}input:focus,select:focus,textarea:focus{border-color:#ffd84f!important;box-shadow:0 0 0 3px rgba(255,216,79,.16)!important}
.ib-listbar,.ib-bulkbar{background:#20231d!important;border:1px solid #3b4033!important;border-radius:18px 8px 18px 8px!important;color:#e8e0b5!important}.ib-listbar{padding:13px 18px!important;margin-bottom:14px!important}.ib-grid{grid-template-columns:repeat(auto-fit,minmax(310px,1fr))!important;gap:18px!important}
.ib-card{border-radius:32px 12px 32px 12px!important;background:linear-gradient(155deg,#24291f 0%,#151813 78%)!important;border:1px solid #4b503d!important;box-shadow:0 24px 60px rgba(54,39,2,.24)!important;min-height:310px!important}.ib-card:before{background:linear-gradient(120deg,#ffd84f20,transparent 35%,#ef9f1b14 75%,transparent)!important}.ib-card:after{content:'';position:absolute;top:-33px;left:-34px;width:110px;height:78px;background:#ffd84f;transform:rotate(-38deg);opacity:.92;pointer-events:none}.ib-card-head{padding:22px 20px 15px!important;border-bottom-color:#3b4033!important}.ib-avatar{background:linear-gradient(135deg,#ffd84f,#e98f17)!important;border-color:#ffe994!important;color:#202016!important;box-shadow:0 8px 22px rgba(255,201,62,.22)!important;transform:rotate(-5deg)}.ib-name-top b{color:#fff8d9!important;font-size:15px!important}.ib-card-id .mono{color:#aeb09a!important}.ib-card-controls{gap:10px!important}.ib-tagrow{padding:12px 20px!important}.ib-tagrow>span{background:#30352a!important;border-color:#4b513f!important;color:#dbd8b7!important;border-radius:999px!important}.ib-tagrow .ib-live-tag{background:#264125!important;color:#b9ff7e!important;border-color:#4c8b45!important}.ib-card-addr{padding:0 20px!important}.ib-card-traffic{padding:14px 20px!important}.ib-progress{height:9px!important;background:#363b2e!important;border-radius:99px!important}.ib-progress>i{background:linear-gradient(90deg,#ffd84f,#9df06e)!important}.ib-card-stats{margin:0 20px!important;background:#20241c!important;border:1px solid #3b4133!important;border-radius:18px 8px 18px 8px!important}.ib-card-stats>div{border-color:#3b4133!important}.ib-card-stats small{color:#a9aa91!important}.ib-card-stats b{color:#fff5c4!important}.ib-card-foot{padding:14px 20px 18px!important;border-top-color:#3b4033!important}.ib-clientcell{color:#ffd84f!important}.ib-card-actions .iconbtn,.ib-clientcell .iconbtn{background:#2c3026!important;border-color:#515942!important;color:#f5e9ad!important;border-radius:12px 6px 12px 6px!important}.ib-card-actions .iconbtn:hover,.ib-clientcell .iconbtn:hover{background:#ffd84f!important;color:#202016!important;border-color:#ffd84f!important}.ib-switch.on{background:#ffd84f!important}.ib-status-dot.green{color:#9df06e!important}.ib-check{accent-color:#ffd84f!important}
/* Builder: turn the long form into a visual studio instead of a plain rectangle. */
.inbound-builder{padding:4px!important}.ib-hero{background:#ffd84f!important;color:#1a1c14!important;border-radius:34px 12px 34px 12px!important;padding:24px 26px!important;box-shadow:0 18px 35px rgba(55,40,3,.20)!important}.ib-hero small{color:#66551d!important}.ib-hero .badge{background:#1c1d18!important;color:#ffd84f!important;border-color:#1c1d18!important}.ib-section{background:#1b1e19!important;border:1px solid #444a39!important;border-radius:26px 10px 26px 10px!important;box-shadow:0 18px 42px rgba(40,30,3,.15)!important}.ib-section-head{border-bottom-color:#3d4335!important}.ib-step .num{background:#ffd84f!important;color:#202016!important;box-shadow:0 7px 18px rgba(255,216,79,.20)!important}.ib-opt{background:#282c23!important;border-color:#4a503e!important;border-radius:20px 8px 20px 8px!important;min-height:78px!important}.ib-opt:hover,.ib-opt.on,.ib-opt.active{background:#3a3a25!important;border-color:#ffd84f!important;box-shadow:0 0 0 1px #ffd84f33,0 14px 28px rgba(0,0,0,.18)!important}.ib-opt-icon{background:#ffd84f1c!important;color:#ffd84f!important;border-color:#ffd84f33!important;border-radius:14px 6px 14px 6px!important}.ib-summary{background:#2b3024!important;border-color:#ffd84f55!important;border-radius:22px 8px 22px 8px!important}.ib-summary .sum{border-color:#4a503e!important}.ib-summary b{color:#ffd84f!important}.drawer{background:#161915!important;border-left-color:#454a39!important}.drawer-head{background:#ffd84f!important;color:#1a1c14!important}.drawer-head h2,.drawer-head p{color:#1a1c14!important}
.badge.green{background:#294729!important;color:#b8ff87!important;border-color:#4c8b45!important}.badge.red{background:#4b2930!important;color:#ff9aa4!important;border-color:#7c3e4a!important}.badge.gray{background:#30352b!important;color:#d5d0ae!important}.badge.orange{background:#594b23!important;color:#ffe17a!important;border-color:#866e29!important}
@media(max-width:980px){.sidebar{background:#171a16!important}.body-wrap{padding:22px 18px 60px!important}#pg-links .pg-head{background:#ffd84f!important}.pg-head h1{font-size:32px!important}}
@media(max-width:700px){.ib-grid{grid-template-columns:1fr!important}.body-wrap{padding:16px 12px 48px!important}.pg-head h1{font-size:29px!important}#pg-overview .pg-head,#pg-links .pg-head{padding:20px!important;border-radius:26px 10px 26px 10px!important}.ib-card{min-height:0!important}}
</style>
</head>
<style id="alison-original-ui">
/* ALISON // ORIGINAL COMMAND UI — visual system intentionally redesigned */
:root{--al-bg:#020706;--al-surface:#071310;--al-surface2:#0a1b17;--al-line:#14342d;--al-cyan:#38f2d0;--al-blue:#38bdf8;--al-lime:#b8ff6a;--al-red:#ff647c;--al-text:#eafff9;--al-muted:#78958e;--al-radius:22px}
*{scrollbar-width:thin;scrollbar-color:#16443a transparent}
html,body{background:var(--al-bg)!important;color:var(--al-text)!important}
body{background-image:radial-gradient(900px 500px at 75% -10%,#0d5b5140,transparent 70%),radial-gradient(700px 500px at 0 100%,#063f5430,transparent 70%),linear-gradient(180deg,#020706,#030a08 45%,#020504)!important}
body:after{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1;opacity:.16;background:linear-gradient(rgba(56,242,208,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(56,242,208,.035) 1px,transparent 1px);background-size:48px 48px;mask-image:linear-gradient(#000,transparent 90%)}
.sidebar{width:272px!important;background:linear-gradient(180deg,#06110e 0%,#030806 100%)!important;border-right:1px solid #12352e!important;box-shadow:25px 0 90px #0009!important}
.sidebar-brand{height:94px!important;padding:20px!important;border-bottom:1px solid #12352e!important}
.sidebar-brand img{width:42px!important;height:42px!important;filter:drop-shadow(0 0 16px #38f2d060)!important}
.sidebar-brand span{font-size:21px!important;letter-spacing:.12em!important;color:#eafff9!important}
.sidebar-brand small{color:#38f2d0!important;letter-spacing:.22em!important;font-size:8px!important}
.tabnav{padding:16px 12px!important;gap:7px!important}
.tab{height:48px!important;border:1px solid transparent!important;border-radius:15px!important;padding:0 13px!important;color:#69857f!important;background:transparent!important;position:relative!important;overflow:hidden!important}
.tab i{font-size:20px!important;width:27px!important;color:#50736b!important}
.tab:hover{background:#0a211b!important;color:#cffff5!important;border-color:#17483d!important;transform:translateX(-2px)}
.tab:hover i{color:#38f2d0!important}
.tab.on{background:linear-gradient(100deg,#0c2b24,#071914)!important;border-color:#1d594b!important;color:#eafff9!important;box-shadow:inset 3px 0 #38f2d0,0 10px 28px #0006!important}
.tab.on:after{content:"";position:absolute;right:12px;width:5px;height:5px;border-radius:50%;background:#38f2d0;box-shadow:0 0 12px #38f2d0}
.bd{background:#0e3028!important;border:1px solid #1b5145!important;color:#8fffe8!important}
.sidebar-foot{border-top:1px solid #12352e!important;padding:14px!important}
.user-chip{background:#071a15!important;border:1px solid #16463b!important;border-radius:16px!important;padding:10px!important}
.user-chip .av{background:linear-gradient(135deg,#38f2d0,#168fd0)!important;color:#02100c!important;box-shadow:0 0 20px #38f2d044!important}
.main-col{background:transparent!important}
.topbar{height:82px!important;background:#030b09d9!important;border-bottom:1px solid #10342c!important;backdrop-filter:blur(18px)!important}
.hamburger{border:1px solid #17453b!important;background:#071713!important;color:#8feadd!important;border-radius:12px!important}
.page-title{font-weight:900!important;letter-spacing:-.03em!important}
.top-right .icon-btn{background:#071713!important;border:1px solid #16463b!important;color:#8aa9a2!important;border-radius:12px!important}
.top-right .icon-btn:hover{color:#38f2d0!important;border-color:#2b8c78!important}
.body-wrap{padding:28px!important;max-width:1600px!important}
.pg-head{padding:4px 2px 24px!important}
.pg-head h1{font-size:34px!important;letter-spacing:-.05em!important}
.pg-head p{color:#718f88!important}
.eyebrow{color:#38f2d0!important;letter-spacing:.18em!important;font-size:9px!important}
.live-dot{background:#38f2d0!important;box-shadow:0 0 0 5px #38f2d014,0 0 18px #38f2d0!important}
.card,.resource-card,.stat-card,.traffic-card,.connection-card,.mini-panel,.ib-card,.settings-card,.admin-card,.resource-grid>div{background:linear-gradient(145deg,#091b17f2,#040b09f2)!important;border:1px solid #143c34!important;border-radius:22px!important;box-shadow:0 24px 80px #0007,inset 0 1px #ffffff08!important}
.card:hover,.resource-card:hover,.ib-card:hover{border-color:#267b68!important;box-shadow:0 28px 90px #0009,0 0 35px #38f2d00d!important;transform:translateY(-2px)}
.resource-grid{gap:14px!important}
.resource-card{min-height:145px!important;padding:20px!important;position:relative!important;overflow:hidden!important}
.resource-card:before{content:"";position:absolute;inset:auto -20% -55% 20%;height:100px;background:radial-gradient(circle,#38f2d014,transparent 65%);pointer-events:none}
.rc-head b{font-size:26px!important;color:#eafff9!important}
.rc-head i{color:#38f2d0!important}
.spark{opacity:.9!important}
.traffic-layout{gap:14px!important}
.panel-head{border-bottom:1px solid #12352d!important;padding-bottom:14px!important}
.panel-head b{letter-spacing:.08em!important;font-size:11px!important}
.traffic-legend b,.connection-number{color:#38f2d0!important}
.connection-card{background:radial-gradient(circle at 70% 25%,#0b4a3c55,transparent 35%),linear-gradient(145deg,#091b17,#040b09)!important}
.btn{border-radius:13px!important;border:1px solid #18483e!important;background:#071813!important;color:#a8c9c2!important;box-shadow:none!important}
.btn:hover{background:#0b271f!important;border-color:#2a8b74!important;color:#eafff9!important}
.btn.primary,.btn.success,.primary{background:linear-gradient(110deg,#13b89f,#087bb3)!important;border:0!important;color:#fff!important;box-shadow:0 12px 30px #0a9d8740!important}
.btn-inbound{background:linear-gradient(110deg,#0da98f,#087db7)!important}
.search input,.sel,input,select,textarea{background:#030a08!important;border:1px solid #153b33!important;color:#eafff9!important;border-radius:13px!important}
.search input:focus,input:focus,select:focus,textarea:focus{border-color:#38f2d0!important;box-shadow:0 0 0 3px #38f2d012!important}
.ib-grid{grid-template-columns:repeat(auto-fill,minmax(310px,1fr))!important;gap:16px!important}
.ib-card{min-height:250px!important;padding:0!important;overflow:hidden!important}
.ib-card:before{background:linear-gradient(120deg,#38f2d008,transparent 45%,#38bdf808)!important}
.ib-card-head{padding:18px!important;background:#071713!important;border-bottom:1px solid #12352d!important}
.ib-icon{width:48px!important;height:48px!important;border-radius:15px!important;background:linear-gradient(135deg,#0b332a,#082336)!important;border:1px solid #267565!important;color:#38f2d0!important}
.ib-live-tag,.badge.green{background:#08362c!important;color:#7dffe5!important;border-color:#1b6b58!important}
.badge{border-radius:999px!important}
.ov-quickstats{gap:14px!important}
.ov-quickstats>div{background:#071713!important;border:1px solid #143c34!important;border-radius:18px!important}
.health-row{border-bottom:1px solid #103129!important}
.mono{color:#72ffe5!important}
.modal,.drawer,.overlay{backdrop-filter:blur(18px)!important}
.drawer{background:#06110e!important;border-left:1px solid #17483d!important;box-shadow:-30px 0 90px #0009!important}
.toast{background:#071a15!important;border:1px solid #1c5c4d!important}
/* distinct page compositions */
#pg-overview .resource-grid{grid-template-columns:repeat(4,1fr)!important}
#pg-overview .traffic-layout{grid-template-columns:minmax(0,1.65fr) minmax(300px,.7fr)!important}
#pg-links .pg-head{background:linear-gradient(90deg,#071713aa,transparent)!important;padding:20px!important;border-radius:20px!important;border:1px solid #10382f!important;margin-bottom:18px!important}
#pg-links .ib-card{border-radius:24px!important}
@media(max-width:1000px){#pg-overview .resource-grid{grid-template-columns:repeat(2,1fr)!important}#pg-overview .traffic-layout{grid-template-columns:1fr!important}}
@media(max-width:700px){.sidebar{width:285px!important}.body-wrap{padding:17px!important}.pg-head h1{font-size:28px!important}.resource-grid{grid-template-columns:1fr 1fr!important}.ib-grid{grid-template-columns:1fr!important}.topbar{height:70px!important}}
</style>
<body>
<script>(function(){
  // نکته (رفع باگ): قبلاً این اسکریپت اولیه از کلید localStorage جداگانه‌ای
  // به‌نام «vw_theme» می‌خواند که هیچ‌جای برنامه هرگز در آن چیزی نمی‌نوشت
  // (تنظیمات واقعی همیشه زیر کلید «vw_appearance» ذخیره می‌شود)، پس همیشه
  // مقدار پیش‌فرض «dark» اعمال می‌شد و باعث یک فلاش کوتاهِ پوسته‌ی اشتباه
  // در بارگذاری اولیه‌ی صفحه می‌شد، تا وقتی اسکریپت اصلی اجرا شود.
  try{
    var raw = localStorage.getItem('vw_appearance');
    var pref = raw ? (JSON.parse(raw).theme || 'dark') : 'dark';
    var resolved = pref === 'system'
      ? (matchMedia('(prefers-color-scheme:light)').matches ? 'light' : 'dark')
      : pref;
    document.documentElement.setAttribute('data-theme', resolved);
  }catch(e){ document.documentElement.setAttribute('data-theme','dark'); }
})();</script>
<div id="app">
  <div class="sidebar-overlay" onclick="toggleSidebar()"></div>
  <div class="sidebar">
    <div class="sidebar-brand"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20256%20256%22%3E%0A%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20stop-color%3D%22%236fffe9%22%2F%3E%3Cstop%20offset%3D%22.48%22%20stop-color%3D%22%2325d9c3%22%2F%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%230aa4ff%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%0A%3Crect%20width%3D%22256%22%20height%3D%22256%22%20rx%3D%2262%22%20fill%3D%22%2307110f%22%2F%3E%0A%3Cpath%20d%3D%22M128%2035%20214%2078v100l-86%2043-86-43V78z%22%20fill%3D%22none%22%20stroke%3D%22url%28%23g%29%22%20stroke-width%3D%2210%22%2F%3E%0A%3Cpath%20d%3D%22m79%20169%2043-88h14l43%2088h-25l-9-20H111l-9%2020zm40-40h18l-9-22z%22%20fill%3D%22url%28%23g%29%22%2F%3E%0A%3Ccircle%20cx%3D%22193%22%20cy%3D%2264%22%20r%3D%227%22%20fill%3D%22%238ffff1%22%2F%3E%0A%3C%2Fsvg%3E"><div><span data-i18n="brand">ALISON</span><small>Control Suite</small></div></div>
    <div class="tabnav" id="tabnav">
      <div class="tab on" data-pg="overview"><i class="ti ti-radar"></i><span data-i18n="nav_overview">مرکز کنترل</span></div>
      <div class="tab" data-pg="links"><i class="ti ti-world-network"></i><span data-i18n="nav_links">نودهای اتصال</span><span class="bd" id="nb-links">0</span></div>
      <div class="tab" data-pg="clientmgr"><i class="ti ti-user-scan"></i><span data-i18n="nav_clientmgr">کلاینت ساز</span></div>
      <div class="tab" data-pg="categories"><i class="ti ti-circles"></i><span data-i18n="nav_categories">گروه‌بندی</span></div>
      <div class="tab" data-pg="subgroups"><i class="ti ti-stack-2"></i><span data-i18n="nav_subgroups">اشتراک‌ها</span><span class="bd" id="nb-subs">0</span></div>
      <div class="tab tab-locked" data-pg="plans" title="در نسخه‌های بعد فعال می‌شود"><i class="ti ti-lock"></i><span data-i18n="nav_plans">پلن‌ها</span><span class="bd">بعداً</span></div>
      <div class="tab" data-pg="reports"><i class="ti ti-activity-heartbeat"></i><span data-i18n="nav_reports">تحلیل‌گر</span></div>
      <div class="tab" data-pg="admins"><i class="ti ti-shield-user"></i><span data-i18n="nav_admins">اپراتورها</span></div>
      <div class="tab" data-pg="activity"><i class="ti ti-timeline"></i><span data-i18n="nav_activity">رویدادها</span></div>
      <div class="tab" data-pg="messages"><i class="ti ti-message-2"></i><span data-i18n="nav_messages">اعلان‌ها</span><span class="bd danger-bd" id="nb-errors">0</span></div>
      <div class="tab" data-pg="settings"><i class="ti ti-adjustments-horizontal"></i><span data-i18n="nav_settings">پیکربندی</span></div>
    </div>
    <div class="sidebar-foot">
      <div class="lang-mini">
        <button id="dashLangFa" class="on" onclick="setDashLang('fa')">فا</button>
        <button id="dashLangEn" onclick="setDashLang('en')">EN</button>
      </div>
      <div class="user-chip" id="userChip"><div class="av">A</div><span id="userName">...</span></div>
    </div>
  </div>

  <div class="main-col">
  <div class="topbar">
    <button class="hamburger" onclick="toggleSidebar()"><i class="ti ti-menu-2"></i></button>
    <div class="page-title"><span id="pageTitleMain" data-i18n="nav_overview">مرکز کنترل</span><span id="pageTitleSub" data-i18n="pt_overview">وضعیت لحظه‌ای سرویس، کانفیگ‌ها و ربات فروش</span></div>
    <div class="top-right">
      <button class="icon-btn" id="themeToggle" onclick="toggleTheme()" title="تغییر پوسته"><i class="ti ti-moon"></i></button>
      <a class="icon-btn" href="/logout" title="خروج"><i class="ti ti-logout"></i></a>
    </div>
  </div>

  <div class="body-wrap">

    <!-- OVERVIEW -->
    <div class="page on" id="pg-overview">
      <div class="pg-head"><div><div class="eyebrow"><span class="live-dot"></span> ALISON COMMAND CENTER</div><h1>ALISON Control</h1><p>نمای لحظه‌ای منابع سرور، ترافیک، اتصال‌ها و سرویس فروش.</p></div>
        <div class="toolbar"><button class="btn" onclick="refreshOverview()"><i class="ti ti-refresh"></i>بروزرسانی</button><button class="btn primary" onclick="gotoPage('links')"><i class="ti ti-world-network"></i>اینباندها</button></div></div>
      <div class="ib-quickstats ov-quickstats" id="ovBizStats"></div>
      <div class="resource-grid" id="resourceGrid">
        <div class="resource-card"><div class="rc-head"><span><i class="ti ti-cpu"></i> CPU</span><b id="cpuVal">—</b></div><div class="rc-sub" id="cpuSub">در حال دریافت...</div><svg class="spark" id="cpuSpark" viewBox="0 0 240 46" preserveAspectRatio="none"></svg></div>
        <div class="resource-card"><div class="rc-head"><span><i class="ti ti-device-ram"></i> RAM</span><b id="ramVal">—</b></div><div class="rc-sub" id="ramSub">—</div><svg class="spark" id="ramSpark" viewBox="0 0 240 46" preserveAspectRatio="none"></svg></div>
        <div class="resource-card"><div class="rc-head"><span><i class="ti ti-bolt"></i> SWAP</span><b id="swapVal">—</b></div><div class="rc-sub" id="swapSub">—</div><svg class="spark" id="swapSpark" viewBox="0 0 240 46" preserveAspectRatio="none"></svg></div>
        <div class="resource-card"><div class="rc-head"><span><i class="ti ti-database"></i> STORAGE</span><b id="storageVal">—</b></div><div class="rc-sub" id="storageSub">—</div><svg class="spark" id="storageSpark" viewBox="0 0 240 46" preserveAspectRatio="none"></svg></div>
      </div>
      <div class="traffic-layout">
        <div class="card traffic-card"><div class="panel-head"><div><b>OVERALL SPEED</b><small id="speedMeta">Network throughput</small></div><div class="traffic-legend"><span>↑ <b id="txRate">0 B/s</b></span><span>↓ <b id="rxRate">0 B/s</b></span></div></div><div class="big-chart"><svg id="trafficChart" viewBox="0 0 900 260" preserveAspectRatio="none"></svg></div><div class="traffic-foot"><div><small>SENT</small><b id="sentTotal">0 B</b></div><div><small>RECEIVED</small><b id="recvTotal">0 B</b></div><div><small>LIVE THROUGHPUT</small><b id="liveRate">↑ 0 B/s ↓ 0 B/s</b></div></div></div>
        <div class="card connection-card"><div class="panel-head"><div><b>CONNECTION STATS</b><small>Open sockets</small></div><i class="ti ti-plug-connected"></i></div><div class="connection-number" id="connVal">0</div><div class="connection-label">OPEN CONNECTIONS</div><svg class="conn-chart" id="connChart" viewBox="0 0 340 150" preserveAspectRatio="none"></svg><div class="conn-foot"><span>REQUESTS <b id="reqVal">0</b></span><span>ERRORS <b id="errVal">0</b></span></div></div>
      </div>
      <div class="bottom-grid">
        <div class="card mini-panel"><div class="panel-head"><div><b>SERVICE HEALTH</b><small>Runtime status</small></div><span class="badge green">ONLINE</span></div><div class="health-row"><span>Uptime</span><b id="uptimeVal">—</b></div><div class="health-row"><span>CPU Cores</span><b id="coresVal">—</b></div><div class="health-row"><span>Panel RAM</span><b id="procRamVal">—</b></div></div>
        <div class="card mini-panel"><div class="panel-head"><div><b>BOT SERVICES</b><small>Sales + management</small></div><span id="ovBotStatus" class="badge gray">CHECKING</span></div><div class="health-row"><span>Telegram Bot</span><b id="botStateText">—</b></div><div class="health-row"><span>Public URL</span><b class="mono" id="ovBaseUrl">—</b></div></div>
        <div class="card mini-panel"><div class="panel-head"><div><b>NETWORK</b><small>Host load</small></div><i class="ti ti-world"></i></div><div class="health-row"><span>Load</span><b id="loadVal">—</b></div><div class="health-row"><span>Traffic</span><b id="trafficTotalVal">0 B</b></div></div>
      </div>
      <div class="card mini-panel" style="margin-top:14px"><div class="panel-head"><div><b>TOP CONFIGS BY USAGE</b><small>پرمصرف‌ترین کانفیگ‌های ۷ روز اخیر</small></div><i class="ti ti-trending-up"></i></div><div id="ovTopLinks" class="ov-toplinks"></div></div>
    </div>

    <!-- LINKS -->
    <div class="page" id="pg-links">
      <div class="pg-head inbound-head"><div><div class="eyebrow"><span class="live-dot"></span> ALISON EDGE · <span id="ibLiveTag">LIVE</span></div><h1>اینباندها</h1><p>مرکز مدیریت اینباند، ساخت کلاینت و کنترل دسترسی؛ با پایش زنده هر ۵ ثانیه.</p></div>
        <div class="toolbar">
          <div class="search"><input id="linkSearch" placeholder="جستجوی اینباند / UUID..." oninput="renderLinks()"><i class="ti ti-search"></i></div>
          <select class="sel" id="linkFilterCat" onchange="renderLinks()"><option value="">همه دسته‌ها</option></select>
          <span id="ibUpdatedAt" style="font-size:9px;color:var(--sub2);align-self:center;white-space:nowrap">—</span>
          <button class="btn" id="ibRefreshBtn" onclick="refreshAllInbounds()"><i class="ti ti-refresh" id="ibRefreshIcon"></i>بروزرسانی همه</button>
          <button class="btn" onclick="openAutoLink()"><i class="ti ti-bolt"></i>ساخت سریع</button>
          <button class="btn primary btn-inbound" onclick="openLinkDrawer()"><i class="ti ti-plus"></i>اینباند جدید</button>
        </div>
      </div>
      <div class="ib-quickstats" id="ibQuickStats"></div>
      <div class="ib-listbar">
        <label class="ib-selectall"><input type="checkbox" id="ibSelAll" onchange="toggleAllLinks(this.checked)"><span>انتخاب همه</span></label>
        <span class="ib-count" id="ibCountLabel">0 اینباند</span>
      </div>
      <div class="ib-bulkbar" id="ibBulkBar" style="display:none">
        <span><b id="ibSelCount">0</b> مورد انتخاب شده</span>
        <div class="ib-bulkactions">
          <button class="btn sm" onclick="bulkToggleLinks(true)"><i class="ti ti-power"></i>فعال‌سازی</button>
          <button class="btn sm" onclick="bulkToggleLinks(false)"><i class="ti ti-power"></i>غیرفعال‌سازی</button>
          <button class="btn sm" style="color:var(--bad)" onclick="bulkDeleteLinks()"><i class="ti ti-trash"></i>حذف</button>
        </div>
      </div>
      <div class="ib-grid" id="ibGrid"></div>
      <div class="empty" id="linksEmpty" style="display:none"><i class="ti ti-inbox"></i>کانفیگی یافت نشد</div>
    </div>

    <!-- CLIENT MANAGER (بخش جدای ساخت کلاینت از روی اینباند) -->
    <div class="page" id="pg-clientmgr">
      <div class="pg-head"><div><div class="eyebrow"><span class="live-dot"></span> ALISON · CLIENT MANAGER</div><h1>ساخت کلاینت</h1><p>یک اینباند را انتخاب کن و از روی همان کلاینت‌های واقعی (زیرمجموعه) بساز؛ بدون نیاز به رفتن به صفحه اینباندها.</p></div>
        <div class="toolbar"><button class="btn" onclick="loadClientManager()"><i class="ti ti-refresh"></i>بروزرسانی</button></div>
      </div>
      <div class="card" style="padding:18px;margin-bottom:14px">
        <div class="grp"><label>انتخاب اینباند</label>
          <select class="sel" id="cmInboundSelect" style="width:100%" onchange="loadClientManagerClients(this.value)"><option value="">— انتخاب کنید —</option></select>
        </div>
        <div id="cmInboundInfo"></div>
      </div>
      <div id="cmBody"></div>
    </div>

    <!-- CATEGORIES -->
    <div class="page" id="pg-categories">
      <div class="pg-head"><div><h1>دسته‌بندی‌ها</h1><p>پیش‌فرض‌های حجم، انقضا و محدودیت برای گروه‌های کانفیگ</p></div>
        <div class="toolbar"><button class="btn primary" onclick="openCategoryDrawer()"><i class="ti ti-plus"></i>دسته جدید</button></div>
      </div>
      <div class="card"><table><thead><tr><th>نام</th><th>حجم پیش‌فرض</th><th>انقضا (روز)</th><th>محدودیت IP</th><th></th></tr></thead><tbody id="catsBody"></tbody></table></div>
    </div>

    <!-- SUBGROUPS -->
    <div class="page" id="pg-subgroups">
      <div class="pg-head"><div><h1>گروه‌های ساب</h1><p>ترکیب چند کانفیگ در یک لینک اشتراک واحد</p></div>
        <div class="toolbar"><button class="btn primary" onclick="openSubGroupDrawer()"><i class="ti ti-plus"></i>گروه جدید</button></div>
      </div>
      <div class="card"><table><thead><tr><th>نام گروه</th><th>تعداد کانفیگ</th><th>لینک عمومی</th><th></th></tr></thead><tbody id="subsBody"></tbody></table></div>
    </div>

    <!-- PLANS -->
    <div class="page" id="pg-plans">
      <div class="pg-head"><div><h1>پلن‌های فروش</h1><p>پلن‌هایی که در ربات فروش تلگرام نمایش داده می‌شوند</p></div>
        <div class="toolbar"><button class="btn primary" onclick="openPlanDrawer()"><i class="ti ti-plus"></i>پلن جدید</button></div>
      </div>
      <div class="card"><table><thead><tr><th>نام</th><th>مدت</th><th>حجم</th><th>سرعت</th><th>قیمت (⭐)</th><th>ویژه</th><th></th></tr></thead><tbody id="plansBody"></tbody></table></div>
    </div>

    <!-- REPORTS -->
    <div class="page" id="pg-reports">
      <div class="pg-head"><div><h1>گزارش‌ها</h1><p>خلاصه‌ی عملکرد فروش و کانفیگ‌ها</p></div>
        <div class="toolbar">
          <select class="sel" id="repDays" onchange="loadReports()"><option value="7">۷ روز اخیر</option><option value="14" selected>۱۴ روز اخیر</option><option value="30">۳۰ روز اخیر</option></select>
          <a class="btn" href="/api/reports/export.csv"><i class="ti ti-download"></i>خروجی CSV</a>
        </div>
      </div>
      <div class="stat-grid" id="repStats"></div>
      <div class="card">
        <div style="padding:16px 18px;border-bottom:1px solid var(--line)"><b style="font-size:13px">پرمصرف‌ترین کانفیگ‌ها</b></div>
        <table><thead><tr><th>برچسب</th><th>پروتکل</th><th>مصرف</th></tr></thead><tbody id="repTopBody"></tbody></table>
      </div>
    </div>

    <!-- ADMINS -->
    <div class="page" id="pg-admins">
      <div class="pg-head"><div><div class="eyebrow"><span class="live-dot"></span> ALISON · مدیریت حساب</div><h1>مدیریت حساب‌ها</h1><p>اینجا همه حساب‌های مدیریتی پنل را مرتب و دقیق مدیریت می‌کنیم؛ از ساخت ادمین تا تعیین دسترسی و کنترل وضعیت حساب.</p></div>
        <div class="toolbar"><button class="btn" onclick="loadAdmins()"><i class="ti ti-refresh"></i>همگام‌سازی</button><button class="btn primary" onclick="openAdminDrawer()"><i class="ti ti-user-scan"></i>ایجاد حساب مدیریتی</button></div>
      </div>
      <div class="admins-hero">
        <div class="access-command-copy"><div class="command-badge"><i class="ti ti-shield-lock"></i> مدیریت حساب‌ها</div><h2>مدیریت کامل ادمین‌ها</h2><p>حساب اصلی پنل دسترسی کامل دارد و برای هر ادمین می‌توان دسترسی‌های موردنیاز را جداگانه تعیین کرد. وضعیت هر حساب و آخرین ورود نیز از همین بخش قابل بررسی است.</p><div class="command-points"><span><i class="ti ti-check"></i> تفکیک دسترسی</span><span><i class="ti ti-check"></i> ثبت آخرین ورود</span><span><i class="ti ti-check"></i> امنیت حساب‌ها</span></div></div>
        <div class="admins-summary" id="adminsSummary"><div class="sum"><b id="adminTotal">—</b><small>حساب مدیریتی</small></div><div class="sum"><b id="adminActive">—</b><small>حساب فعال</small></div><div class="sum"><b id="adminOwner">1</b><small>مالک پنل</small></div></div>
      </div>
      <div class="card admin-directory" id="adminReqCard" style="margin-bottom:14px;display:none"><div class="panel-head"><div><b>درخواست‌های ثبت‌نام ادمینی</b><small>افرادی که از صفحه ورود درخواست دسترسی داده‌اند؛ بررسی کن و تصمیم بگیر.</small></div><span class="command-badge" id="adminReqBadge">۰ درخواست</span></div><div id="adminReqBody" style="padding:14px 18px"></div></div>
      <div class="card admin-directory"><div class="panel-head"><div><b>فهرست ادمین‌ها</b><small>وضعیت، دسترسی و فعالیت هر ادمین را از یکجا بررسی و مدیریت کن.</small></div><span class="directory-live"><i></i> کنترل فعال</span></div><div class="admin-grid" id="adminsBody"></div></div>
    </div>

    <!-- ACTIVITY -->
    <div class="page" id="pg-activity">
      <div class="pg-head"><div><h1>لاگ فعالیت‌ها</h1><p>۱۵۰ رویداد اخیر پنل</p></div>
        <div class="toolbar"><button class="btn" onclick="loadActivity()"><i class="ti ti-refresh"></i>بروزرسانی</button></div>
      </div>
      <div class="card"><table><thead><tr><th>زمان</th><th>نوع</th><th>پیام</th></tr></thead><tbody id="activityBody"></tbody></table></div>
    </div>

    <!-- MESSAGES -->
    <div class="page" id="pg-messages">
      <div class="pg-head"><div><div class="eyebrow"><span class="live-dot"></span> MESSAGE CENTER</div><h1>مرکز پیام و خطا</h1><p>تمام خطاهای سرور، خطاهای مرورگر و رویدادهای مهم اینجا جمع می‌شوند تا هیچ خطایی گم نشود.</p></div><div class="toolbar"><span class="message-auto" id="messageLastSync">همگام‌سازی خودکار</span><button class="btn" onclick="loadMessages()"><i class="ti ti-refresh"></i>بروزرسانی</button><button class="btn danger" onclick="clearErrors()"><i class="ti ti-trash"></i>پاک‌کردن خطاها</button></div></div>
      <div class="message-center" id="messageStats"></div>
      <div class="card">
        <div class="panel-head"><div><b>خطاهای ثبت‌شده</b><small>خطاهای Backend و Frontend با جزئیات مسیر و زمان</small></div><div class="message-filter"><button class="on" data-message-filter="all" onclick="setMessageFilter('all')">همه</button><button data-message-filter="err" onclick="setMessageFilter('err')">خطا</button><button data-message-filter="warn" onclick="setMessageFilter('warn')">هشدار</button><button data-message-filter="client" onclick="setMessageFilter('client')">مرورگر</button></div></div>
        <div class="message-list" id="messageList"></div>
      </div>
      <div class="card" style="margin-top:14px"><div class="panel-head"><div><b>رویدادهای مهم</b><small>آخرین فعالیت‌های پنل برای عیب‌یابی سریع</small></div></div><div class="message-list" id="messageActivityList"></div></div>
    </div>

    <!-- SETTINGS -->
    <div class="page" id="pg-settings">
      <div class="pg-head"><div><div class="eyebrow">CONTROL CENTER / PERSONALIZATION</div><h1>تنظیمات و استودیو ظاهر</h1><p>ظاهر، فونت، رنگ، تراکم، زبان و تنظیمات عملیاتی پنل را از یکجا کنترل کن.</p></div><div class="toolbar"><button class="btn" onclick="resetAppearance()"><i class="ti ti-refresh"></i>بازنشانی ظاهر</button></div></div>

      <div class="appearance-studio">
        <div class="appearance-card">
          <h3>Appearance Studio</h3><p>تنظیمات ظاهری فقط برای همین مرورگر ذخیره می‌شوند و بدون دست‌زدن به اطلاعات سرور قابل تغییرند.</p>
          <div class="appearance-grid">
            <div class="appearance-field"><label>فونت رابط کاربری</label><select id="appearanceFont" onchange="setFont(this.value)"><option value="Vazirmatn">Vazirmatn</option><option value="Estedad">Estedad</option><option value="IBM Plex Sans Arabic">IBM Plex Sans Arabic</option><option value="Shabnam">Shabnam</option><option value="Yekan Bakh">Yekan Bakh</option><option value="Inter">Inter</option></select></div>
            <div class="appearance-field"><label>اندازه متن</label><div class="theme-pills"><button class="theme-pill" data-font-size="small" onclick="setFontSize('small')">Small</button><button class="theme-pill" data-font-size="normal" onclick="setFontSize('normal')">Normal</button><button class="theme-pill" data-font-size="large" onclick="setFontSize('large')">Large</button></div></div>
            <div class="appearance-field"><label>تراکم پنل</label><div class="theme-pills"><button class="theme-pill" data-density="comfortable" onclick="setDensity('comfortable')">Comfort</button><button class="theme-pill" data-density="compact" onclick="setDensity('compact')">Compact</button></div></div>
            <div class="appearance-field"><label>گوشه‌ها</label><div class="theme-pills"><button class="theme-pill" data-radius="soft" onclick="setRadius('soft')">Soft</button><button class="theme-pill" data-radius="sharp" onclick="setRadius('sharp')">Sharp</button><button class="theme-pill" data-radius="pill" onclick="setRadius('pill')">Pill</button></div></div>
            <div class="appearance-field"><label>پوسته</label><div class="theme-pills"><button class="theme-pill" data-theme-choice="dark" onclick="setAppearanceTheme('dark')">Dark</button><button class="theme-pill" data-theme-choice="light" onclick="setAppearanceTheme('light')">Light</button><button class="theme-pill" data-theme-choice="system" onclick="setAppearanceTheme('system')">System</button></div></div>
            <div class="appearance-field"><label>رنگ اصلی</label><div class="accent-pills"><button class="accent-pill" data-accent="purple" onclick="setAccent('purple')"><span class="accent-dot" style="background:#8b5cf6"></span>Purple</button><button class="accent-pill" data-accent="blue" onclick="setAccent('blue')"><span class="accent-dot" style="background:#3b82f6"></span>Blue</button><button class="accent-pill" data-accent="cyan" onclick="setAccent('cyan')"><span class="accent-dot" style="background:#06b6d4"></span>Cyan</button><button class="accent-pill" data-accent="green" onclick="setAccent('green')"><span class="accent-dot" style="background:#10b981"></span>Green</button><button class="accent-pill" data-accent="orange" onclick="setAccent('orange')"><span class="accent-dot" style="background:#f59e0b"></span>Orange</button><button class="accent-pill" data-accent="pink" onclick="setAccent('pink')"><span class="accent-dot" style="background:#ec4899"></span>Pink</button><button class="accent-pill" data-accent="red" onclick="setAccent('red')"><span class="accent-dot" style="background:#ef4444"></span>Red</button><button class="accent-pill" data-accent="indigo" onclick="setAccent('indigo')"><span class="accent-dot" style="background:#6366f1"></span>Indigo</button><button class="accent-pill" data-accent="teal" onclick="setAccent('teal')"><span class="accent-dot" style="background:#14b8a6"></span>Teal</button><button class="accent-pill" data-accent="gold" onclick="setAccent('gold')"><span class="accent-dot" style="background:#eab308"></span>Gold</button></div></div>
          </div>
          <div class="appearance-actions">
            <div class="appearance-toggle"><span>انیمیشن‌های پنل</span><button id="motionSwitch" class="switch" onclick="toggleMotion()"></button></div>
            <div class="appearance-toggle"><span>سایدبار باز در دسکتاپ</span><button id="wideSwitch" class="switch" onclick="toggleWideSidebar()"></button></div>
            <div class="appearance-toggle"><span>Glow / نورپردازی</span><button id="glowSwitch" class="switch" onclick="toggleGlow()"></button></div>
          </div>
        </div>
        <div class="appearance-card appearance-preview"><div class="preview-window"><div class="preview-top"><i class="ti ti-circle-filled"></i><i class="ti ti-circle-filled"></i><i class="ti ti-circle-filled"></i></div><div class="preview-main"><div class="preview-side"><div class="active"></div><div></div><div></div><div></div></div><div class="preview-content"><div class="pv-title">ALISON Control Suite</div><div class="pv-sub">Live network overview</div><div class="pv-cards"><span></span><span></span><span></span></div></div></div></div></div>
      </div>

      <div class="card pro-diagnostics" style="margin-top:14px">
        <div class="panel-head"><div><b>SYSTEM HEALTH / LIVE DIAGNOSTICS</b><small>Live server, resource, object and security telemetry</small></div><div class="toolbar"><span id="diagStatus" class="badge green">READY</span><button class="btn" onclick="loadDiagnostics()"><i class="ti ti-activity"></i>Refresh</button></div></div>
        <div class="diag-grid" id="diagGrid"><div class="diag-empty">Press Refresh to inspect the live system.</div></div>
      </div>

      <div class="two-col">
        <div class="card settings-card">
          <div class="section-title">آدرس عمومی پنل</div>
          <p class="hint" style="margin-bottom:12px">برای لینک‌های Subscription، دامنه واقعی پنل را ثابت کن. روی Railway بهتر است دامنه عمومی سرویس را اینجا قرار بدهی.</p>
          <div class="grp"><input id="setBaseUrl" placeholder="https://panel.example.com"></div>
          <button class="btn primary" onclick="saveBaseUrl()"><i class="ti ti-device-floppy"></i>ذخیره آدرس</button>
          <div class="divider"></div><div class="section-title">امنیت حساب</div>
          <div class="grp"><label>نام کاربری پنل</label><div class="row2"><input type="text" id="adminUsername" autocomplete="username" maxlength="40" placeholder="admin"><button class="btn primary" onclick="changeUsername()"><i class="ti ti-user-edit"></i>تغییر نام کاربری</button></div><div class="hint">نام کاربری جدید بدون فاصله و بین ۳ تا ۴۰ کاراکتر.</div></div>
          <div class="divider"></div>
          <div class="grp"><label>رمز فعلی</label><div style="position:relative"><input type="password" id="curPass" autocomplete="current-password"><button type="button" class="iconbtn" style="position:absolute;left:7px;top:6px" onclick="toggleSettingsPass('curPass',this)"><i class="ti ti-eye"></i></button></div></div><div class="row2"><div class="grp"><label>رمز جدید</label><div style="position:relative"><input type="password" id="newPass" autocomplete="new-password" oninput="passwordMeter()"><button type="button" class="iconbtn" style="position:absolute;left:7px;top:6px" onclick="toggleSettingsPass('newPass',this)"><i class="ti ti-eye"></i></button></div><div id="passMeter" style="height:4px;background:var(--line);border-radius:99px;margin-top:7px;overflow:hidden"><i id="passMeterBar" style="display:block;height:100%;width:0;background:var(--bad);transition:.2s"></i></div><div id="passHint" class="hint">حداقل ۸ کاراکتر، ترجیحاً ترکیب حروف، عدد و نماد.</div></div><div class="grp"><label>تکرار رمز جدید</label><div style="position:relative"><input type="password" id="repPass" autocomplete="new-password"><button type="button" class="iconbtn" style="position:absolute;left:7px;top:6px" onclick="toggleSettingsPass('repPass',this)"><i class="ti ti-eye"></i></button></div></div></div>
          <button class="btn primary" onclick="changePassword()"><i class="ti ti-key"></i>تغییر امن رمز</button><button class="btn" style="margin-right:7px" onclick="revokeOtherSessions()"><i class="ti ti-shield-lock"></i>لغو نشست‌های قبلی</button>
        </div>
        <div class="card settings-card">
          <div class="section-title">Railway Network Center</div>
          <p class="hint" style="margin-bottom:12px">دامنه و پورت TCP عمومی Railway را اینجا مدیریت کن. Railway دامنه و پورت TCP Proxy را خودش تولید می‌کند و باید همان مقدار استفاده شود.</p>
          <div class="row2"><div class="grp"><label>TCP Host</label><input id="setTcpHost" placeholder="roundhouse.proxy.rlwy.net" class="mono" style="direction:ltr;text-align:left"></div><div class="grp"><label>TCP Port</label><input id="setTcpPort" placeholder="11105" class="mono" style="direction:ltr;text-align:left"></div></div>
          <p class="hint" id="tcpListenHint">—</p><button class="btn primary" onclick="saveTcpSettings()"><i class="ti ti-device-floppy"></i>ذخیره شبکه</button>
          <div class="divider"></div><div class="section-title">Sales & Management Bot</div>
          <div class="grp"><label>Bot Token</label><input id="setBotToken" placeholder="123456:ABC-DEF..." class="mono" style="direction:ltr;text-align:left"></div><div class="grp"><label>Admin IDs</label><input id="setBotAdmins" placeholder="123456789,987654321"></div>
          <div style="display:flex;gap:10px;align-items:center;margin-top:8px"><span class="status-dot off" id="botDot"></span><span id="botStatusText" style="font-size:13px">وضعیت نامشخص</span></div><div style="display:flex;gap:10px;margin-top:14px"><button class="btn primary" onclick="saveBotSettings()"><i class="ti ti-device-floppy"></i>ذخیره</button><button class="btn" id="botStartBtn" onclick="botStart()"><i class="ti ti-player-play"></i>شروع</button><button class="btn danger" id="botStopBtn" onclick="botStop()"><i class="ti ti-player-stop"></i>توقف</button></div>
        </div>
      </div>
      <div class="card settings-card tpl-studio" style="margin-top:14px">
        <div class="tpl-studio-head"><div><div class="section-title">Subscription Template</div><p class="hint">همان یک لینک ساب که به کاربر می‌دهی؛ فقط تعیین کن نام کانفیگ داخل اپ او دقیقاً چه چیزهایی را نشان دهد.</p></div><div class="tpl-badge"><i class="ti ti-wand"></i>Template Studio</div></div>
        <div class="tpl-grid">
          <div class="tpl-fields">
            <label class="tpl-row"><div class="tpl-row-main"><i class="ti ti-tag"></i><div><b>نام کانفیگ</b><small>نام دلخواه یا برند شما</small></div></div><input type="checkbox" class="tpl-switch" id="subTplName"></label>
            <label class="tpl-row"><div class="tpl-row-main"><i class="ti ti-database"></i><div><b>حجم اختصاص‌یافته</b><small>مثلاً ۵۰ گیگابایت</small></div></div><input type="checkbox" class="tpl-switch" id="subTplVolume"></label>
            <label class="tpl-row"><div class="tpl-row-main"><i class="ti ti-fingerprint"></i><div><b>شناسه کانفیگ (ID)</b><small>شناسه کوتاه یکتا</small></div></div><input type="checkbox" class="tpl-switch" id="subTplId"></label>
            <label class="tpl-row"><div class="tpl-row-main"><i class="ti ti-router"></i><div><b>نام اینباند</b><small>نام اینباند مادر این کانفیگ</small></div></div><input type="checkbox" class="tpl-switch" id="subTplInbound"></label>
          </div>
          <div class="tpl-preview">
            <div class="tpl-preview-label"><i class="ti ti-device-mobile"></i>پیش‌نمایش داخل اپ کاربر</div>
            <div class="tpl-preview-row"><span class="tpl-preview-dot"></span><div class="tpl-preview-text" id="subTplPreview">MyConfig</div><span class="tpl-preview-proto">VLESS</span></div>
            <p class="hint" style="margin-top:10px">ترتیب نمایش دقیقاً همین ترتیب بالاست؛ بین هر بخش یک خط جداکننده (|) قرار می‌گیرد.</p>
          </div>
        </div>
        <button class="btn primary" style="margin-top:14px" onclick="saveSubTemplate()"><i class="ti ti-device-floppy"></i>ذخیره الگوی ساب</button>
      </div>

      <div class="card settings-card" style="margin-top:14px"><div class="section-title">Bot Text Studio</div><p class="hint">تمام پیام‌های کلیدی ربات را از همین پنل ویرایش کن؛ تغییرات روی ربات در اجرای بعدی/ری‌استارت اعمال می‌شوند.</p><div class="bot-text-grid"><div class="grp"><label>پیام خوش‌آمد</label><textarea id="botTxtWelcome" rows="4"></textarea></div><div class="grp"><label>منوی مدیریت</label><textarea id="botTxtAdmin" rows="4"></textarea></div><div class="grp"><label>پیام ساخت کانفیگ</label><textarea id="botTxtCreated" rows="3"></textarea></div><div class="grp"><label>پیام فروشگاه</label><textarea id="botTxtStore" rows="3"></textarea></div><div class="grp"><label>پیام پرداخت موفق</label><textarea id="botTxtPayment" rows="3"></textarea></div></div><button class="btn primary" onclick="saveBotTexts()"><i class="ti ti-device-floppy"></i>ذخیره متن‌های ربات</button></div>

      <div class="card advanced-settings" style="margin-top:14px"><div class="panel-head"><div><b>CONTROL CENTER PRO</b><small>ابزارهای حرفه‌ای برای شخصی‌سازی و نگهداری پنل</small></div><span class="badge green">PRO</span></div><div class="advanced-grid"><button class="pro-action" onclick="refreshOverview();toast('داده‌های زنده بروزرسانی شد ✓')"><i class="ti ti-activity-heartbeat"></i><b>Live Refresh</b><small>مانیتورینگ فوری منابع</small></button><button class="pro-action" onclick="loadSettings();toast('تنظیمات دوباره بارگذاری شد ✓')"><i class="ti ti-refresh"></i><b>Reload Settings</b><small>دریافت تنظیمات واقعی سرور</small></button><button class="pro-action" onclick="location.reload()"><i class="ti ti-reload"></i><b>Hard Reload</b><small>بارگذاری کامل رابط</small></button><button class="pro-action" onclick="navigator.clipboard?.writeText(location.origin);toast('دامنه پنل کپی شد ✓')"><i class="ti ti-world-copy"></i><b>Copy Panel URL</b><small>دامنه فعلی پنل</small></button></div></div>
    </div>

  </div>
  </div>
</div>

<div class="overlay" id="overlay" onclick="closeDrawer()"></div>
<div class="drawer" id="drawer">
  <div class="dr-head"><h3 id="drTitle">—</h3><button class="iconbtn" onclick="closeDrawer()"><i class="ti ti-x"></i></button></div>
  <div class="dr-body" id="drBody"></div>
  <div class="dr-foot" id="drFoot"></div>
</div>

<div id="toastWrap"></div>

<script>
// ============================================================
// Core helpers
// ============================================================
const $ = (id) => document.getElementById(id);
function toast(msg, ok=true){
  const t = document.createElement('div');
  t.className = 'toast ' + (ok?'ok':'err');
  const safeMsg = dashTranslateValue(String(msg ?? ''), typeof getDashLang === 'function' ? getDashLang() : 'fa');
  t.innerHTML = `<i class="ti ti-${ok?'circle-check':'alert-circle'}"></i><span>${escapeHtml(safeMsg)}</span>`;
  $('toastWrap').appendChild(t);
  setTimeout(()=>t.remove(), 3800);
}
async function api(path, opts={}){
  const res = await fetch(path, {credentials:'same-origin', headers:{'Content-Type':'application/json'}, ...opts});
  let data = {};
  try{ data = await res.json(); }catch(e){}
  if(!res.ok){
    const message = data.detail || data.error || data.message || ('خطا ' + res.status);
    throw new Error(message);
  }
  return data;
}

let MESSAGE_FILTER='all';
let messageTimer=null;
let reportingClientError=false;
async function reportClientError(message, source='browser', extra={}){
  if(reportingClientError) return;
  reportingClientError=true;
  try{
    await fetch('/api/errors/client',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},keepalive:true,body:JSON.stringify({message:String(message||'Unknown client error').slice(0,1200),source:String(source||'browser').slice(0,40),path:location.pathname,stack:String(extra.stack||'').slice(0,4000),details:String(extra.details||'').slice(0,1500)})});
  }catch(e){} finally{reportingClientError=false;}
}
window.addEventListener('error',e=>{ if(e?.message) reportClientError(e.message,'browser',{stack:e.error?.stack,details:`${e.filename||''}:${e.lineno||''}:${e.colno||''}`}); });
window.addEventListener('unhandledrejection',e=>{ const r=e?.reason; reportClientError(r?.message||String(r||'Unhandled promise rejection'),'promise',{stack:r?.stack}); });
function fmtBytes(n){
  n = Number(n||0);
  if(n<=0) return '0';
  const u=['B','KB','MB','GB','TB']; let i=0;
  while(n>=1024 && i<u.length-1){n/=1024;i++;}
  return n.toFixed(n<10&&i>0?1:0)+' '+u[i];
}
function escapeHtml(s){ return String(s??'').replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

// ============================================================
// Nav
// ============================================================
document.querySelectorAll('.tab').forEach(t=>{
  t.addEventListener('click', ()=> gotoPage(t.dataset.pg));
});
function gotoPage(pg){
  if(pg==='plans'){ openDrawer('پلن‌های فروش', `<div class=\"feature-lock\"><div class=\"feature-lock-icon\"><i class=\"ti ti-lock-star\"></i></div><h3>این بخش در حال توسعه است</h3><p>ماژول فروش اشتراک در نسخه‌های بعدی ALISON فعال خواهد شد. فعلاً مدیریت سرویس، اینباند، کلاینت و سابسکریپشن بدون وابستگی به فروش در دسترس است.</p><div class=\"feature-lock-note\"><i class=\"ti ti-sparkles\"></i> Coming in a future release</div></div>`, `<button class=\"btn\" style=\"flex:1\" onclick=\"closeDrawer()\"><i class=\"ti ti-check\"></i>متوجه شدم</button>`); return; }
  document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('on', t.dataset.pg===pg));
  document.querySelectorAll('.page').forEach(p=>p.classList.toggle('on', p.id==='pg-'+pg));
  CURRENT_PAGE = pg;
  updatePageTitle(pg);
  document.getElementById('app').classList.remove('sb-open');
  const loaders = {overview:refreshOverview, links:loadLinks, clientmgr:loadClientManager, categories:loadCategories, subgroups:loadSubGroups,
    reports:loadReports, admins:()=>{loadAdmins();loadAdminRequests();}, activity:loadActivity, messages:loadMessages, settings:()=>{loadSettings();loadDiagnostics();}};
  if(loaders[pg]) loaders[pg]();
}

// ============================================================
// Drawer
// ============================================================
function openDrawer(title, bodyHtml, footHtml){
  $('drTitle').textContent = title;
  $('drBody').innerHTML = bodyHtml;
  $('drFoot').innerHTML = footHtml;
  $('overlay').classList.add('show');
  $('drawer').classList.add('show');
}
function closeDrawer(){
  $('overlay').classList.remove('show');
  $('drawer').classList.remove('show');
}

// ============================================================
// Appearance Studio
// ============================================================
const APPEARANCE_DEFAULTS={font:'Vazirmatn',theme:'dark',accent:'purple',density:'comfortable',motion:true,wide:false,radius:'soft',glow:true,fontSize:'normal'};
const ACCENTS={purple:['#8b5cf6','#6d28d9'],blue:['#3b82f6','#1d4ed8'],cyan:['#06b6d4','#0e7490'],green:['#10b981','#047857'],orange:['#f59e0b','#b45309'],pink:['#ec4899','#be185d'],red:['#ef4444','#b91c1c'],indigo:['#6366f1','#4338ca'],teal:['#14b8a6','#0f766e'],gold:['#eab308','#a16207']};
function getAppearance(){try{return {...APPEARANCE_DEFAULTS,...JSON.parse(localStorage.getItem('vw_appearance')||'{}')}}catch(e){return {...APPEARANCE_DEFAULTS}}}
function saveAppearance(a){try{localStorage.setItem('vw_appearance',JSON.stringify(a))}catch(e){} applyAppearance()}
function applyAppearance(){const a=getAppearance();const root=document.documentElement;root.style.setProperty('--font-ui',`'${a.font}',sans-serif`);const theme=a.theme==='system'?(matchMedia('(prefers-color-scheme:light)').matches?'light':'dark'):a.theme;root.setAttribute('data-theme',theme);const c=ACCENTS[a.accent]||ACCENTS.purple;root.style.setProperty('--accent',c[0]);root.style.setProperty('--accent-d',c[1]);root.style.setProperty('--ui-glow',a.glow?`0 14px 40px -18px ${c[0]}88`:'none');document.body.classList.toggle('density-compact',a.density==='compact');document.body.classList.toggle('no-motion',!a.motion);document.body.classList.toggle('wide-sidebar',!!a.wide);document.body.classList.toggle('radius-sharp',a.radius==='sharp');document.body.classList.toggle('radius-pill',a.radius==='pill');document.body.classList.toggle('font-small',a.fontSize==='small');document.body.classList.toggle('font-large',a.fontSize==='large');if($('appearanceFont'))$('appearanceFont').value=a.font;document.querySelectorAll('[data-theme-choice]').forEach(x=>x.classList.toggle('on',x.dataset.themeChoice===a.theme));document.querySelectorAll('[data-accent]').forEach(x=>x.classList.toggle('on',x.dataset.accent===a.accent));document.querySelectorAll('[data-density]').forEach(x=>x.classList.toggle('on',x.dataset.density===a.density));document.querySelectorAll('[data-radius]').forEach(x=>x.classList.toggle('on',x.dataset.radius===a.radius));document.querySelectorAll('[data-font-size]').forEach(x=>x.classList.toggle('on',x.dataset.fontSize===a.fontSize));if($('motionSwitch'))$('motionSwitch').classList.toggle('on',a.motion);if($('wideSwitch'))$('wideSwitch').classList.toggle('on',a.wide);if($('glowSwitch'))$('glowSwitch').classList.toggle('on',a.glow);updateThemeIcon()}
function setFont(v){const a=getAppearance();a.font=v;saveAppearance(a);toast('فونت پنل تغییر کرد ✓')}
function setAppearanceTheme(v){const a=getAppearance();a.theme=v;saveAppearance(a)}
function setAccent(v){const a=getAppearance();a.accent=v;saveAppearance(a)}
function setDensity(v){const a=getAppearance();a.density=v;saveAppearance(a)}
function setRadius(v){const a=getAppearance();a.radius=v;saveAppearance(a)}
function setFontSize(v){const a=getAppearance();a.fontSize=v;saveAppearance(a)}
function toggleMotion(){const a=getAppearance();a.motion=!a.motion;saveAppearance(a)}
function toggleWideSidebar(){const a=getAppearance();a.wide=!a.wide;saveAppearance(a)}
function toggleGlow(){const a=getAppearance();a.glow=!a.glow;saveAppearance(a)}
try{matchMedia('(prefers-color-scheme:light)').addEventListener('change',()=>{if(getAppearance().theme==='system')applyAppearance()})}catch(e){}
function resetAppearance(){try{localStorage.removeItem('vw_appearance');localStorage.removeItem('vw_theme')}catch(e){};applyAppearance();toast('ظاهر پنل به حالت پیش‌فرض برگشت ✓')}
applyAppearance();

// ============================================================
// Bootstrapping / current user
// ============================================================
let CATEGORIES = [];
let LINKS = [];
let PROTOCOLS = [];
let MANUAL_META = {};
let ADMIN_CACHE = [];

function toggleTheme(){
  const a=getAppearance(); a.theme=(a.theme==='light'?'dark':'light'); saveAppearance(a); toast(a.theme==='light'?'پوسته روشن و کاملاً سفید فعال شد ✓':'پوسته تیره فعال شد ✓');
}
function updateThemeIcon(){
  const btn = document.getElementById('themeToggle');
  if(!btn) return;
  const cur = document.documentElement.getAttribute('data-theme') || 'dark';
  btn.innerHTML = cur === 'light' ? '<i class="ti ti-sun"></i>' : '<i class="ti ti-moon"></i>';
}
updateThemeIcon();

function toggleSidebar(){
  document.getElementById('app').classList.toggle('sb-open');
}

var DASH_I18N = {
  fa: {
    dir:'rtl', brand:'ALISON',
    nav_overview:'داشبورد', nav_links:'اینباندها', nav_clientmgr:'ساخت کلاینت', nav_categories:'دسته‌بندی‌ها', nav_subgroups:'گروه‌های ساب',
    nav_plans:'پلن‌های فروش', nav_reports:'گزارش‌ها', nav_admins:'ادمین‌ها', nav_activity:'فعالیت‌ها', nav_messages:'پیام‌ها', nav_settings:'تنظیمات',
    pt_overview:'وضعیت لحظه‌ای سرویس، کانفیگ‌ها و ربات فروش',
    pt_links:'مدیریت حرفه‌ای اینباندها، کلاینت‌ها و لینک‌های اشتراک',
    pt_clientmgr:'ساخت کلاینت واقعی از روی اینباند دلخواه، جدا از صفحه اینباندها',
    pt_categories:'پیش‌فرض‌های حجم، انقضا و محدودیت برای گروه‌های کانفیگ',
    pt_subgroups:'ترکیب چند کانفیگ در یک لینک اشتراک واحد',
    pt_plans:'پلن‌هایی که در ربات فروش تلگرام نمایش داده می‌شوند',
    pt_reports:'خلاصه‌ی عملکرد فروش و کانفیگ‌ها',
    pt_admins:'حساب‌های دسترسی جانبی به پنل (فقط مالک)',
    pt_activity:'۱۵۰ رویداد اخیر پنل',
    pt_messages:'مرکز خطاها، هشدارها و پیام‌های سیستم',
    pt_settings:'آدرس عمومی پنل، ربات فروش تلگرام و رمز عبور'
  },
  en: {
    dir:'ltr', brand:'ALISON',
    nav_overview:'Overview', nav_links:'Inbounds', nav_clientmgr:'Create Client', nav_categories:'Categories', nav_subgroups:'Sub Groups',
    nav_plans:'Sale Plans', nav_reports:'Reports', nav_admins:'Admins', nav_activity:'Activity', nav_messages:'Messages', nav_settings:'Settings',
    pt_overview:'Live status of the service, configs and sales bot',
    pt_links:'Manage inbounds, clients and subscription links',
    pt_clientmgr:'Create a real client from any inbound, separate from the inbounds page',
    pt_categories:'Default traffic, expiry and IP-limit presets for config groups',
    pt_subgroups:'Combine several configs into one subscription link',
    pt_plans:'Plans shown in the Telegram sales bot',
    pt_reports:'Summary of sales and config performance',
    pt_admins:'Secondary panel access accounts (owner only)',
    pt_activity:'Last 150 panel events',
    pt_messages:'Errors, warnings and system messages',
    pt_settings:'Panel public URL, Telegram sales bot and password'
  }
};
var CURRENT_PAGE = 'overview';
const DASH_EN_TERMS = {
  // Navigation / pages
  'داشبورد':'Dashboard','اینباندها':'Inbounds','اینباند':'Inbound','دسته‌بندی‌ها':'Categories','دسته‌بندی':'Category',
  'گروه‌های ساب':'Subscription Groups','گروه ساب':'Subscription Group','گروه جدید':'New Group','پلن‌های فروش':'Sales Plans','پلن فروش':'Sales Plan','پلن جدید':'New Plan',
  'گزارش‌ها':'Reports','ادمین‌ها':'Admins','ادمین':'Admin','ادمین جدید':'New Admin','مالک':'Owner','فعالیت‌ها':'Activity','فعالیت':'Activity','پیام‌ها':'Messages','تنظیمات':'Settings',
  'مرکز کنترل':'Control Suite','مرکز پیام و خطا':'Message & Error Center','مدیریت حساب‌ها':'Admin Management','مدیریت حساب':'Admin Management',
  'تنظیمات و استودیو ظاهر':'Settings & Appearance Studio','استودیو ظاهر':'Appearance Studio',

  // Common actions / states
  'فعال':'Active','غیرفعال':'Inactive','فعال/غیرفعال':'Enable/Disable','خاموش':'Stopped','در حال اجرا':'Running','روشن':'Online','آنلاین':'Online','آفلاین':'Offline',
  'در دسترس نیست':'Unavailable','وضعیت نامشخص':'Unknown status','در حال دریافت...':'Loading...','بروزرسانی':'Refresh','بروزرسانی زنده':'Live Refresh',
  'ذخیره':'Save','ذخیره تغییرات':'Save Changes','ذخیره آدرس':'Save URL','ذخیره شبکه':'Save Network','ذخیره متن‌های ربات':'Save Bot Texts','حذف':'Delete','ویرایش':'Edit','ساخت':'Create','ساخت سریع':'Quick Create','لغو':'Cancel','تأیید':'Confirm','انصراف':'Cancel','بازگشت':'Back','نمایش':'View','کپی':'Copy','کپی لینک':'Copy Link','کپی لینک ساب':'Copy Subscription Link','دریافت فایل':'Download','خروجی CSV':'CSV Export','جستجو':'Search','فیلتر':'Filter','همه':'All','پاک‌کردن خطاها':'Clear Errors','لغو نشست‌های قبلی':'Revoke Previous Sessions',
  'شروع':'Start','توقف':'Stop','فعال‌سازی':'Enable','غیرفعال‌سازی':'Disable','عملیات':'Actions','کنترل':'Control','جزئیات':'Details','بستن':'Close','بارگذاری کامل رابط':'Hard Reload','بازنشانی ظاهر':'Reset Appearance','بارگذاری دوباره':'Reload',

  // Titles / descriptions
  'وضعیت لحظه‌ای سرویس، کانفیگ‌ها و ربات فروش':'Live service, configuration and sales-bot status',
  'مدیریت حرفه‌ای اینباندها، کلاینت‌ها و لینک‌های اشتراک':'Professional inbound, client and subscription management',
  'پیش‌فرض‌های حجم، انقضا و محدودیت برای گروه‌های کانفیگ':'Traffic, expiry and limit presets for config groups',
  'ترکیب چند کانفیگ در یک لینک اشتراک واحد':'Combine multiple configs into one subscription link',
  'پلن‌هایی که در ربات فروش تلگرام نمایش داده می‌شوند':'Plans shown in the Telegram sales bot',
  'خلاصه‌ی عملکرد فروش و کانفیگ‌ها':'Sales and configuration performance',
  'حساب‌های دسترسی جانبی به پنل (فقط مالک)':'Secondary panel access accounts (owner only)',
  '۱۵۰ رویداد اخیر پنل':'Latest 150 panel events',
  'مرکز خطاها، هشدارها و پیام‌های سیستم':'Errors, warnings and system messages',
  'آدرس عمومی پنل، ربات فروش تلگرام و رمز عبور':'Panel public URL, Telegram sales bot and account security',
  'نمای لحظه‌ای منابع سرور، ترافیک، اتصال‌ها و سرویس فروش.':'Live server resources, traffic, connections and sales service.',
  'مرکز مدیریت اینباند، ساخت کلاینت و کنترل دسترسی؛ با پایش زنده هر ۵ ثانیه.':'Inbound management, client creation and access control with live monitoring every 5 seconds.',
  'تمام خطاهای سرور، خطاهای مرورگر و رویدادهای مهم اینجا جمع می‌شوند تا هیچ خطایی گم نشود.':'All server errors, browser errors and important events are collected here.',
  'ظاهر، فونت، رنگ، تراکم، زبان و تنظیمات عملیاتی پنل را از یکجا کنترل کن.':'Control appearance, font, colors, density, language and operational settings from one place.',
  'برای لینک‌های Subscription، دامنه واقعی پنل را ثابت کن. روی Railway بهتر است دامنه عمومی سرویس را اینجا قرار بدهی.':'Set the real panel domain for subscription links. On Railway, use the service public domain here.',
  'دامنه و پورت TCP عمومی Railway را اینجا مدیریت کن. Railway دامنه و پورت TCP Proxy را خودش تولید می‌کند و باید همان مقدار استفاده شود.':'Manage the public Railway TCP domain and port here. Railway generates the TCP Proxy values.',
  'تمام پیام‌های کلیدی ربات را از همین پنل ویرایش کن؛ تغییرات روی ربات در اجرای بعدی/ری‌استارت اعمال می‌شوند.':'Edit the bot messages here; changes apply on the next bot start/restart.',
  'حداقل ۸ کاراکتر، ترجیحاً ترکیب حروف، عدد و نماد.':'At least 8 characters; a mix of letters, numbers and symbols is recommended.',
  'نام کاربری جدید بدون فاصله و بین ۳ تا ۴۰ کاراکتر.':'New username without spaces, between 3 and 40 characters.',
  'ابزارهای حرفه‌ای برای شخصی‌سازی و نگهداری پنل':'Professional tools for panel personalization and maintenance',

  // Dashboard metrics
  'کل اینباندها':'Total Inbounds','مشتریان فروشگاه':'Store Customers','فروش (Stars)':'Sales (Stars)','پرمصرف‌ترین کانفیگ‌های ۷ روز اخیر':'Top configs from the last 7 days',
  'پرمصرف‌ترین کانفیگ‌ها':'Top Configs by Usage','خطاهای ثبت‌شده':'Recorded Errors','خطاهای Backend و Frontend با جزئیات مسیر و زمان':'Backend and frontend errors with route and time details',
  'رویدادهای مهم':'Important Events','آخرین فعالیت‌های پنل برای عیب‌یابی سریع':'Recent panel activity for quick troubleshooting',
  'وضعیت سیستم':'System Status','سیستم سالم است.':'System is healthy.','خطای ثبت‌شده‌ای وجود ندارد. سیستم سالم است.':'No recorded errors. System is healthy.','رویدادی وجود ندارد.':'No events found.','لاگی وجود ندارد':'No activity logs.','داده‌ای موجود نیست':'No data available.','هنوز داده‌ی مصرفی ثبت نشده':'No usage data recorded yet.','کانفیگی یافت نشد':'No configs found.','گروهی وجود ندارد':'No groups found.','پلنی وجود ندارد':'No plans found.',
  'همگام‌سازی خودکار':'Auto Sync','آخرین بروزرسانی':'Last Updated','۳۰ روز اخیر':'Last 30 days','۱۴ روز اخیر':'Last 14 days','۷ روز اخیر':'Last 7 days',
  'در حال ذخیره...':'Saving...','تغییر امن رمز':'Change Password','تغییر نام کاربری':'Change Username','نام کاربری پنل':'Panel Username','نام کاربری جدید':'New Username','رمز عبور':'Password','رمز فعلی':'Current Password','رمز جدید':'New Password','تکرار رمز جدید':'Repeat New Password','تکرار رمز عبور':'Repeat Password','امنیت حساب':'Account Security',
  'پیام خوش‌آمد':'Welcome Message','منوی مدیریت':'Admin Menu','پیام ساخت کانفیگ':'Config Created Message','پیام فروشگاه':'Store Message','پیام پرداخت موفق':'Payment Success Message',
  'آدرس عمومی پنل':'Panel Public URL','دامنه فعلی پنل':'Current panel domain','ذخیره شد':'Saved','ذخیره شد ✓':'Saved ✓','ساخته شد':'Created','حذف شد':'Deleted','بروزرسانی شد':'Updated','کپی شد':'Copied','کپی شد ✓':'Copied ✓','تنظیمات دوباره بارگذاری شد ✓':'Settings reloaded ✓','داده‌های زنده بروزرسانی شد ✓':'Live data refreshed ✓','دامنه پنل کپی شد ✓':'Panel URL copied ✓','نام کاربری با موفقیت تغییر کرد ✓':'Username changed successfully ✓','رمز عبور با موفقیت تغییر کرد ✓':'Password changed successfully ✓',

  // Tables / forms
  'نام کاربری':'Username','نام':'Name','نام گروه':'Group Name','برچسب':'Label','نقش':'Role','وضعیت':'Status','زمان':'Time','نوع':'Type','پیام':'Message','تعداد':'Count','تعداد کانفیگ':'Config Count','لینک عمومی':'Public Link',
  'پروتکل':'Protocol','آدرس':'Address','آدرس / Domain':'Address / Domain','پورت':'Port','سرعت':'Speed','حجم':'Traffic','حجم مصرفی':'Usage','حجم پیش‌فرض (GB)':'Default Traffic (GB)','انقضا':'Expiry','انقضا (روز)':'Expiry (Days)','اعتبار (روز)':'Validity (Days)','زمان دقیق انقضا':'Exact Expiry','محدودیت IP':'IP Limit','Connection Limit':'Connection Limit','تعداد کاربر':'Client Limit','تعداد خروجی':'Output Count','توضیحات':'Description','یادداشت داخلی':'Internal Note',
  'مدت':'Duration','قیمت (⭐)':'Price (⭐)','ویژه':'Featured','آخرین ورود':'Last Login','کل':'Total','روز':'Days','ساعت':'Hours','دقیقه':'Minutes','نامحدود':'Unlimited','پیش‌فرض':'Default','اختیاری':'Optional','اجباری':'Required','مصرف':'Usage','اتصال':'Connection','اتصالات':'Connections','کلاینت‌ها':'Clients','کلاینت':'Client','مشتریان':'Customers','مشتری‌ها':'Customers',
  'کپی VLESS':'Copy VLESS','اشتراک':'Subscription','مدیریت کلاینت‌های واقعی':'Real Client Manager','ساخت کلاینت واقعی':'Create Client','کنترل پنل':'Panel Control','مدیریت ربات':'Bot Management','ربات':'Bot',

  // Inbound builder
  'ساخت اینباند':'Create Inbound','ویرایش اینباند':'Edit Inbound','ساخت کلاینت':'Create Client','ویرایش کلاینت':'Edit Client','انتخاب پروتکل':'Select Protocol','پروتکل پایه':'Base Protocol','انتقال':'Transport','لایه انتقال':'Transport Layer','امنیت':'Security','تنظیمات اتصال':'Connection Settings','تنظیمات پیشرفته':'Advanced Settings','خلاصه':'Summary','قبل از ذخیره ترکیب نهایی را بررسی کن':'Review the final combination before saving',
  'ترکیب نهایی':'Final Combination','شبکه':'Network','روش رمزنگاری':'Encryption Method','رمز / Secret':'Password / Secret','کلید عمومی':'Public Key','شناسه کوتاه':'Short ID','مسیر Spider':'Spider X','تولید کلید Reality':'Generate Reality Keypair','تست پینگ':'Ping Test','در حال تست':'Testing...','ابتدا آدرس یا دامنه را وارد کنید':'Enter an address or domain first','پورت نامعتبر است':'Invalid port','اتصال برقرار نشد':'Connection failed',
  'این ترکیب آماده استفاده است.':'This combination is ready to use.','این ترکیب برای ساخت لینک و مدیریت سرویس آماده شده است.':'This combination is prepared for link and service management.','Shadowsocks به‌صورت TCP-only در این Builder ارائه می‌شود.':'Shadowsocks is provided as TCP-only in this builder.','Transport فقط مسیر انتقال است و جدا از پروتکل پایه انتخاب می‌شود.':'Transport is only the transfer layer and is selected separately from the base protocol.',
  'VLESS':'VLESS','VMess':'VMess','Trojan':'Trojan','Shadowsocks':'Shadowsocks','TCP':'TCP','WebSocket':'WebSocket','WS':'WebSocket','gRPC':'gRPC','XHTTP':'XHTTP','TLS':'TLS','Reality':'Reality','None':'None','امنیت بدون رمزنگاری':'No encryption','بدون رمزنگاری':'No encryption',

  // Settings / appearance
  'فونت رابط کاربری':'Interface Font','اندازه متن':'Text Size','تراکم پنل':'Panel Density','گوشه‌ها':'Corners','پوسته':'Theme','رنگ اصلی':'Accent Color','انیمیشن‌های پنل':'Panel Animations','سایدبار باز در دسکتاپ':'Open sidebar on desktop','نورپردازی':'Glow','Appearance Studio':'Appearance Studio','ظاهر پنل به حالت پیش‌فرض برگشت ✓':'Appearance reset ✓','فونت پنل تغییر کرد ✓':'Panel font updated ✓',
  'پوسته تاریک':'Dark Theme','پوسته روشن':'Light Theme','سیستم':'System','فونت پیش‌فرض':'Default Font','کوچک':'Small','متوسط':'Medium','بزرگ':'Large','فشرده':'Compact','راحت':'Comfortable','گرد':'Rounded','تیز':'Sharp',

  // Messages / diagnostics
  'خطا':'Error','هشدار':'Warning','اطلاعات':'Info','مرورگر':'Browser','پاک‌کردن':'Clear','مرکز خطاها':'Error Center','مرکز پیام و خطا':'Message & Error Center','خطا در پردازش اطلاعات ورود.':'Login data could not be processed.',
  'آدرس TCP ذخیره شد':'TCP address saved','آدرس ذخیره شد':'Address saved','ربات روشن شد':'Bot started','ربات خاموش شد':'Bot stopped','ربات در حال اجراست':'Bot is running','ربات خاموش است':'Bot is stopped',
  'Caps Lock فعال است':'Caps Lock is on','قدرت رمز':'Password strength','حداقل ۸ کاراکتر، ترکیب حروف بزرگ/کوچک، عدد و نماد پیشنهاد می‌شود.':'At least 8 characters; uppercase/lowercase letters, numbers and symbols are recommended.',

  // Railway / service
  'دامنه عمومی Railway وارد شد؛ برای TCP خام باید TCP Proxy فعال باشد':'Railway public domain loaded; raw TCP requires TCP Proxy.','اطلاعات TCP Proxy ریل‌وی در این سرویس پیدا نشد':'Railway TCP Proxy information was not found for this service.',
  'همه دسته‌ها':'All categories','مورد انتخاب شده':'selected','اینباند جدید':'New Inbound','دسته جدید':'New Category','وضعیت':'Status','آدرس':'Address','ترافیک':'Traffic','کلاینت / اتصال':'Client / Connection','عملیات':'Actions','نام گروه':'Group Name','تعداد کانفیگ':'Config Count','لینک عمومی':'Public Link','حجم پیش‌فرض':'Default Traffic','قیمت (⭐)':'Price (⭐)','خروجی CSV':'CSV Export','برچسب':'Label','مدیریت حساب‌ها':'Admin Management','ادمین جدید':'New Admin','نقش':'Role','آخرین ورود':'Last Login','مرکز پیام و خطا':'Message & Error Center','پاک‌کردن خطاها':'Clear Errors','خطاهای ثبت‌شده':'Recorded Errors','خطاهای Backend و Frontend با جزئیات مسیر و زمان':'Backend and frontend errors with route and time details','همه':'All','هشدار':'Warning','مرورگر':'Browser','بازنشانی ظاهر':'Reset Appearance','اندازه متن':'Text Size','تراکم پنل':'Panel Density','گوشه‌ها':'Corners','پوسته':'Theme','رنگ اصلی':'Accent Color','انیمیشن‌های پنل':'Panel Animations','سایدبار باز در دسکتاپ':'Open sidebar on desktop','Glow / نورپردازی':'Glow / Lighting','امنیت حساب':'Account Security','رمز فعلی':'Current Password','رمز جدید':'New Password','تکرار رمز جدید':'Repeat New Password','تغییر امن رمز':'Change Password','لغو نشست‌های قبلی':'Revoke Previous Sessions','توقف':'Stop','منوی مدیریت':'Admin Menu','پیام ساخت کانفیگ':'Config Created Message','پیام فروشگاه':'Store Message','پیام پرداخت موفق':'Payment Success Message','مانیتورینگ فوری منابع':'Instant resource monitoring','دریافت تنظیمات واقعی سرور':'Load real server settings','بارگذاری کامل رابط':'Hard Reload','دامنه فعلی پنل':'Current panel domain','در حال دریافت...':'Loading...','بروزرسانی':'Refresh','ساخت سریع':'Quick Create','کانفیگی یافت نشد':'No configs found','دسته‌بندی‌ها':'Categories','پلن‌های فروش':'Sales Plans','گروه‌های ساب':'Subscription Groups','ادمین‌ها':'Admins','پیام‌ها':'Messages','تنظیمات':'Settings',

  // --- Added: fill remaining gaps found across dashboard toasts, confirm()
  // dialogs, inbound builder, client manager and admin permission matrix ---
  'اینباند حذف شود؟':'inbound(s) be deleted?','این کلاینت حذف شود؟':'Delete this client?','این کانفیگ حذف شود؟':'Delete this config?','این دسته حذف شود؟':'Delete this category?','این گروه حذف شود؟':'Delete this group?','این پلن حذف شود؟':'Delete this plan?','این ادمین حذف شود؟':'Delete this admin?','همه خطاهای ثبت‌شده پاک شوند؟':'Clear all recorded errors?','همه نشست‌های قبلی این حساب لغو شوند؟':'Revoke all previous sessions for this account?','دسته‌بندی‌ای وجود ندارد':'No categories found','بروزرسانی گروهی انجام شد':'Bulk update completed','حذف گروهی انجام شد':'Bulk delete completed','کانفیگ خودکار ساخته شد':'Auto config created','اینباند بروزرسانی شد':'Inbound updated','اینباند با موفقیت ساخته شد':'Inbound created successfully','خطا در ذخیره اینباند':'Error saving inbound','خطا در دریافت اطلاعات Railway':'Error fetching Railway information','کلاینت واقعی ساخته شد ✓':'Client created ✓','متن‌های ربات ذخیره شد ✓':'Bot texts saved ✓','خطاها پاک شدند ✓':'Errors cleared ✓','ذخیره شد و ربات با تنظیمات جدید ری‌استارت شد':'Saved — the bot restarted with the new settings','ذخیره شد — برای اعمال، ربات را روشن کنید':'Saved — turn the bot on to apply the changes','کلید Reality ساخته شد. Private Key را روی نود خودتان نگه دارید.':'Reality keypair generated. Keep the private key on your own node.','پورت باید بین 1 تا 65535 باشد':'Port must be between 1 and 65535','Shadowsocks فقط با TCP ساخته می‌شود':'Shadowsocks can only be created over TCP','رمز جدید باید حداقل ۸ کاراکتر باشد':'New password must be at least 8 characters','رمز جدید باید با رمز فعلی متفاوت باشد':'New password must be different from the current password','تکرار رمز یکسان نیست':'Password confirmation does not match','همه‌ی فیلدهای رمز عبور را پر کنید':'Please fill in all password fields','نام کاربری باید ۳ تا ۴۰ کاراکتر و بدون فاصله باشد':'Username must be 3–40 characters with no spaces','نام کاربری را وارد کنید':'Please enter a username','هر کلاینت UUID مستقل دارد و برای پروتکل‌های Live مستقیماً توسط Relay قابل احراز است.':'Each client has its own UUID and, for Live protocols, is authenticated directly by the relay.','این اینباند فعلاً فقط لینک تولید می‌کند. برای Client واقعی، ابتدا یک ترکیب Live مثل VLESS + WS/TCP/XHTTP انتخاب کنید.':'This inbound currently only generates links. For a real client, first choose a Live combination such as VLESS + WS/TCP/XHTTP.','مدیریت کلاینت‌ها':'Manage Clients','حجم (GB، خالی = والد)':'Traffic (GB, empty = parent)','انقضا (روز، 0 = والد)':'Expiry (days, 0 = parent)','بدون تغییر خالی بگذار':'Leave empty for no change','والد':'parent','ساخت اینباند حرفه‌ای':'Create Professional Inbound','پروتکل پایه، ترنسپورت و امنیت کاملاً تفکیک‌شده':'Base protocol, transport and security are fully separated','اول مشخص کن با چه پروتکلی کانفیگ ساخته شود':'First decide which protocol the config will use','حالا مسیر انتقال را جداگانه انتخاب کن':'Now choose the transport layer separately','TLS / Reality / None را مستقل از ترنسپورت انتخاب کن':'Choose TLS / Reality / None independently of the transport','فقط فیلدهای مرتبط با انتخاب بالا نمایش داده می‌شوند':'Only fields relevant to the selection above are shown','لینک اشتراک':'Subscription Link','اگر این لینک برای مشتری باز نمی‌شود، ابتدا از تب «تنظیمات» آدرس عمومی پنل را درست تنظیم کنید.':'If this link doesn\'t open for the customer, first set the panel\'s public URL correctly under the “Settings” tab.','دسته':'Category','گروه ساب جدید':'New Subscription Group','پلن':'Plan','پیشنهاد ویژه':'Featured offer','در حال اتصال':'Connecting','غیرفعال/منقضی':'Disabled/Expired','فعال - بدون اتصال':'Active – No connection','منقضی شده':'Expired','روز مانده':'days left','بدون انقضا':'No expiry','اتصال زنده':'Live connections','کل کانفیگ‌ها':'Total Configs','تعداد سفارش':'Order Count','ساخت و مدیریت اینباند':'Create & manage inbounds','سابسکریپشن':'Subscription','پیام‌ها و خطاها':'Messages & Errors','اینباند و کلاینت':'Inbounds & Clients','هشدارهای اخیر':'Recent Warnings','خطاهای مرورگر':'Browser Errors','خطای نامشخص':'Unknown error','سرور TCP روی پورت داخلی':'TCP server on internal port','گوش می‌دهد — این را در Railway به همین پورت داخلی متصل کن، نه به':'is listening — in Railway, point this at the same internal port, not at the main HTTP','مثلاً':'e.g.','اصلی':'main','همه‌ی اینباندها بروزرسانی شدند ✓':'All inbounds refreshed ✓','بروزرسانی همه':'Refresh All','الگوی نام کانفیگ‌های ساب ذخیره شد ✓':'Subscription remark template saved ✓','نام کانفیگ':'Config Name','حجم اختصاص‌یافته':'Assigned Traffic','شناسه کانفیگ (ID)':'Config ID','نام اینباند':'Inbound Name','پیش‌نمایش: ':'Preview: ','همان یک لینک ساب که به کاربر می‌دهی؛ فقط تعیین کن نام کانفیگ داخل اپ او دقیقاً چه چیزهایی را نشان دهد.':'It\'s still the same single subscription link you hand out — just choose exactly what shows in the config name inside their app.','ذخیره الگوی ساب':'Save Template','Subscription Template':'Subscription Template'
};

// ============================================================
// Stable dashboard language engine
// ============================================================
// The dashboard contains both static DOM and HTML that is created later by
// drawers, tables, API responses and toast messages.  Translation therefore
// uses one stateful engine for the whole dashboard document (not only #app).
// Each text node/attribute remembers its Persian source and its last rendered
// value.  This prevents EN -> FA loss and also lets dynamically updated nodes
// refresh correctly while English mode is active.
const DASH_NODE_STATE = new WeakMap();
const DASH_ATTR_STATE = new WeakMap();
const DASH_TERM_LIST = Object.keys(DASH_EN_TERMS).sort((a,b)=>b.length-a.length);
const DASH_TRANSLATABLE_ATTRS = ['placeholder','title','aria-label'];
let DASH_TRANSLATING = false;

// Word-safe substring replace: a term is only replaced when the character
// right before/after it is NOT another Persian letter. Without this guard a
// short dictionary entry like 'کل' ("total") would also match *inside* an
// unrelated word such as 'کلید' ("key") -> 'Totalید', silently corrupting
// text that has nothing to do with the term. Persian suffixes attached with
// a ZWNJ (e.g. 'کلاینت‌ها') still match correctly because \u200c is not a
// Persian letter and is left outside this guard.
const DASH_FA_LETTER_RE = /[\u0600-\u06FF]/;
function dashReplaceTermSafely(out, term, replacement){
  if(!out.includes(term)) return out;
  let result = '';
  let i = 0;
  const len = term.length;
  while(i < out.length){
    if(out.startsWith(term, i)){
      const before = i > 0 ? out[i - 1] : '';
      const after = out[i + len] || '';
      if(!DASH_FA_LETTER_RE.test(before) && !DASH_FA_LETTER_RE.test(after)){
        result += replacement;
        i += len;
        continue;
      }
    }
    result += out[i];
    i++;
  }
  return result;
}

function dashTranslateValue(value, lang){
  if(lang !== 'en' || !value) return value || '';
  let out = String(value);
  for(const term of DASH_TERM_LIST){
    out = dashReplaceTermSafely(out, term, DASH_EN_TERMS[term]);
  }
  return out;
}

// Shorthand for one-off strings that never live in the DOM long enough for
// the tree-walker/observer to reach them — native confirm()/prompt() dialogs
// in particular. Translates against the current dashboard language.
function t(fa){
  return dashTranslateValue(fa, typeof getDashLang === 'function' ? getDashLang() : 'fa');
}

function dashShouldTranslateElement(el){
  if(!el) return false;
  if(/^(SCRIPT|STYLE|NOSCRIPT)$/i.test(el.tagName)) return false;
  if(el.closest('[data-no-translate],.mono,[data-i18n]')) return false;
  return true;
}

function dashRenderTextNode(textNode, lang){
  if(!textNode || !textNode.parentElement || !dashShouldTranslateElement(textNode.parentElement)) return;
  const current = textNode.nodeValue || '';
  let state = DASH_NODE_STATE.get(textNode);
  if(!state){
    state = {fa: current, last: current};
    DASH_NODE_STATE.set(textNode, state);
  }else if(current !== state.last){
    // The node was changed by application code. Treat the new value as the
    // canonical Persian source rather than translating an old snapshot.
    state.fa = current;
  }
  const next = lang === 'en' ? dashTranslateValue(state.fa,'en') : state.fa;
  state.last = next;
  if(current !== next) textNode.nodeValue = next;
}

function dashRenderAttr(el, attr, lang){
  if(!el || el.matches('[data-no-translate],.mono,[data-i18n]')) return;
  if(!el.hasAttribute(attr)) return;
  const current = el.getAttribute(attr) || '';
  let attrs = DASH_ATTR_STATE.get(el);
  if(!attrs){ attrs = {}; DASH_ATTR_STATE.set(el, attrs); }
  let state = attrs[attr];
  if(!state){
    state = {fa: current, last: current};
    attrs[attr] = state;
  }else if(current !== state.last){
    state.fa = current;
  }
  const next = lang === 'en' ? dashTranslateValue(state.fa,'en') : state.fa;
  state.last = next;
  if(current !== next) el.setAttribute(attr,next);
}

function translateDashTree(lang){
  const root=document.body;
  if(!root || DASH_TRANSLATING) return;
  DASH_TRANSLATING = true;
  try{
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    const nodes=[];
    let node;
    while((node=walker.nextNode())) nodes.push(node);
    for(const textNode of nodes) dashRenderTextNode(textNode,lang);

    root.querySelectorAll('input,textarea,button,[aria-label],select').forEach(el=>{
      for(const attr of DASH_TRANSLATABLE_ATTRS) dashRenderAttr(el,attr,lang);
    });

    root.querySelectorAll('option').forEach(option=>dashRenderTextNode(option.firstChild || option,lang));
  }finally{
    DASH_TRANSLATING = false;
  }
}

function setDashI18nElement(el, key, lang){
  if(!el || !key) return;
  const fa = DASH_I18N.fa?.[key];
  const en = DASH_I18N.en?.[key];
  if(fa === undefined && en === undefined) return;
  if(fa !== undefined) el.dataset.vwFa = String(fa);
  if(en !== undefined) el.dataset.vwEn = String(en);
  const next = lang === 'en' ? (en ?? fa ?? '') : (fa ?? '');
  el.textContent = String(next);
}

function updatePageTitle(pg){
  const mainEl = document.getElementById('pageTitleMain');
  const subEl = document.getElementById('pageTitleSub');
  const lang = getDashLang();
  if(mainEl) setDashI18nElement(mainEl, 'nav_'+pg, lang);
  if(subEl) setDashI18nElement(subEl, 'pt_'+pg, lang);
}

function applyDashLang(lang){
  lang = lang === 'en' ? 'en' : 'fa';
  const dictionary = DASH_I18N[lang] || DASH_I18N.fa;
  document.documentElement.setAttribute('dir', dictionary.dir || (lang==='fa'?'rtl':'ltr'));
  document.documentElement.setAttribute('lang', lang);
  document.body.classList.toggle('dash-en', lang==='en');
  document.getElementById('dashLangFa')?.classList.toggle('on', lang==='fa');
  document.getElementById('dashLangEn')?.classList.toggle('on', lang==='en');

  document.querySelectorAll('#app [data-i18n]').forEach(el=>{
    setDashI18nElement(el, el.getAttribute('data-i18n'), lang);
  });
  updatePageTitle(CURRENT_PAGE);
  translateDashTree(lang);
  try{ localStorage.setItem('vw_dash_lang',lang); }catch(e){}
}

function getDashLang(){
  try{ return localStorage.getItem('vw_dash_lang') === 'en' ? 'en' : 'fa'; }
  catch(e){ return 'fa'; }
}

function setDashLang(lang){
  applyDashLang(lang);
}

let dashTranslateObserver=null;
let dashTranslateQueued=false;
function enableDashTranslation(){
  if(dashTranslateObserver) dashTranslateObserver.disconnect();
  const root=document.getElementById('app') || document.body;
  if(!root) return;
  dashTranslateObserver=new MutationObserver(mutations=>{
    if(getDashLang()!=='en' || DASH_TRANSLATING || dashTranslateQueued) return;
    let hasAdded=false;
    for(const m of mutations){
      if(m.type==='childList' && m.addedNodes && m.addedNodes.length){ hasAdded=true; break; }
    }
    if(!hasAdded) return;
    dashTranslateQueued=true;
    const run=()=>{ dashTranslateQueued=false; if(getDashLang()==='en' && !DASH_TRANSLATING) translateDashTree('en'); };
    if(window.requestIdleCallback) requestIdleCallback(run,{timeout:120});
    else requestAnimationFrame(run);
  });
  dashTranslateObserver.observe(root,{subtree:true,childList:true});
}

// Apply the saved language only after the dashboard DOM exists.
applyDashLang(getDashLang());
enableDashTranslation();

async function boot(){
  try{
    const me = await api('/api/me');
    if(!me.authenticated){ location.href='/login'; return; }
    $('userName').textContent = me.admin.username;
    $('userChip').querySelector('.av').textContent = (me.admin.username||'?').slice(0,1).toUpperCase();
    if(me.admin.role !== 'owner'){
      document.querySelector('.tab[data-pg="admins"]').style.display='none';
      document.querySelector('.tab[data-pg="settings"]').style.display='none';
      if(!(me.admin.permissions||[]).includes('clients')){
        document.querySelector('.tab[data-pg="clientmgr"]').style.display='none';
      }
    } else {
      loadAdminRequests();
    }
  }catch(e){ location.href='/login'; return; }
  try{ const p = await api('/api/protocols'); PROTOCOLS = p.protocols||[]; MANUAL_META = p.manual||{}; }catch(e){}
  refreshOverview();
}
boot();

// ============================================================
// OVERVIEW
// ============================================================
async function refreshOverview(){
  try{
    const [stats, linksRes] = await Promise.all([api('/stats'), api('/api/links')]);
    LINKS = linksRes.links || [];
    $('nb-links').textContent = LINKS.filter(x=>!x.is_client).length;
    $('trafficTotalVal').textContent = fmtBytes(stats.total_traffic_bytes || 0);
  }catch(e){ toast(e.message, false); }
  try{
    const s = await api('/api/settings');
    $('ovBaseUrl').textContent = s.public_base_url || s.effective_host || '—';
    const running = !!s.bot_running;
    $('ovBotStatus').className = 'badge ' + (running?'green':'red');
    $('ovBotStatus').textContent = running?'ONLINE':'OFFLINE';
    $('botStateText').textContent = running?'در حال اجرا':'خاموش';
  }catch(e){}
  try{
    const rep = await api('/api/reports/summary?days=7');
    const t = rep.totals || {};
    $('ovBizStats').innerHTML = `
      <div><i class="ti ti-world-network"></i><span><b>${t.links||0}</b><small>کل اینباندها</small></span></div>
      <div><i class="ti ti-circle-check"></i><span><b>${t.active_links||0}</b><small>فعال</small></span></div>
      <div><i class="ti ti-users"></i><span><b>${t.customers||0}</b><small>مشتریان فروشگاه</small></span></div>`;
    const top = (rep.top_links||[]).slice(0,6);
    if(!top.length){
      $('ovTopLinks').innerHTML = '<div class="ov-empty">هنوز داده‌ی مصرفی ثبت نشده</div>';
    }else{
      const maxUsed = Math.max(1, ...top.map(l=>l.used_bytes||0));
      $('ovTopLinks').innerHTML = top.map((l,i)=>{
        const pct = Math.round((l.used_bytes||0)/maxUsed*100);
        return `<div class="ov-toplink-row"><div class="otl-rank">${i+1}</div><div class="otl-info"><b>${escapeHtml(l.label||'—')}</b><div class="otl-bar"><i style="width:${pct}%"></i></div></div><div class="otl-val">${fmtBytes(l.used_bytes||0)}</div></div>`;
      }).join('');
    }
  }catch(e){}
  await refreshTelemetry();
}
let TEL={cpu:[],ram:[],swap:[],storage:[],traffic:[],conn:[]};
function pushSeries(arr,v,max=36){arr.push(Number(v)||0);while(arr.length>max)arr.shift();}
function drawSpark(id,arr){const el=$(id);if(!el||!arr.length)return;const max=Math.max(100, ...arr), min=Math.min(0,...arr);const pts=arr.map((v,i)=>{const x=(i/Math.max(1,arr.length-1))*240;const y=44-((v-min)/(max-min||1))*38;return `${x.toFixed(1)},${y.toFixed(1)}`}).join(' ');el.innerHTML=`<polyline points="${pts}"/>`; }
function drawChart(id,arr,maxY){const el=$(id);if(!el||!arr.length)return;const w=id==='trafficChart'?900:340,h=id==='trafficChart'?260:150;const max=maxY||Math.max(1,...arr);const pts=arr.map((v,i)=>{const x=(i/Math.max(1,arr.length-1))*w;const y=h-8-(Math.min(max,v)/max)*(h-20);return `${x.toFixed(1)},${y.toFixed(1)}`}).join(' ');const area=`0,${h} ${pts} ${w},${h}`;el.innerHTML=`<polygon class="area" points="${area}"/><polyline points="${pts}"/>`; }
async function refreshTelemetry(){
  try{const t=await api('/api/telemetry');
    $('cpuVal').textContent=t.cpu+'%'; $('cpuSub').textContent=(t.cpu_cores||1)+' logical cores';
    $('ramVal').textContent=t.ram.percent+'%'; $('ramSub').textContent=fmtBytes(t.ram.used)+' / '+fmtBytes(t.ram.total);
    $('swapVal').textContent=t.swap.percent+'%'; $('swapSub').textContent=fmtBytes(t.swap.used)+' / '+fmtBytes(t.swap.total);
    $('storageVal').textContent=t.storage.percent+'%'; $('storageSub').textContent=fmtBytes(t.storage.used)+' / '+fmtBytes(t.storage.total);
    $('txRate').textContent=fmtBytes(t.network.tx_bps)+'/s'; $('rxRate').textContent=fmtBytes(t.network.rx_bps)+'/s'; $('liveRate').textContent='↑ '+fmtBytes(t.network.tx_bps)+'/s ↓ '+fmtBytes(t.network.rx_bps)+'/s';
    $('connVal').textContent=t.connections; $('reqVal').textContent=t.requests; $('errVal').textContent=t.errors; $('uptimeVal').textContent=t.uptime; $('coresVal').textContent=t.cpu_cores; $('procRamVal').textContent=fmtBytes(t.process.rss); $('loadVal').textContent=(t.load||[]).join('  '); $('sentTotal').textContent=fmtBytes(t.network.bytes_sent); $('recvTotal').textContent=fmtBytes(t.network.bytes_recv);
    const hist=Array.isArray(t.history)?t.history:[];
    if(hist.length){
      TEL.cpu=hist.map(x=>Number(x.cpu)||0); TEL.ram=hist.map(x=>Number(x.ram)||0); TEL.swap=hist.map(x=>Number(x.swap)||0); TEL.storage=hist.map(x=>Number(x.storage)||0);
      TEL.traffic=hist.map(x=>(Number(x.tx_bps)||0)+(Number(x.rx_bps)||0)); TEL.conn=hist.map(x=>Number(x.connections)||0);
    }else{
      pushSeries(TEL.cpu,t.cpu);pushSeries(TEL.ram,t.ram.percent);pushSeries(TEL.swap,t.swap.percent);pushSeries(TEL.storage,t.storage.percent);pushSeries(TEL.traffic,(t.network.tx_bps+t.network.rx_bps));pushSeries(TEL.conn,t.connections);
    }
    drawSpark('cpuSpark',TEL.cpu);drawSpark('ramSpark',TEL.ram);drawSpark('swapSpark',TEL.swap);drawSpark('storageSpark',TEL.storage);drawChart('trafficChart',TEL.traffic);drawChart('connChart',TEL.conn);
  }catch(e){}
}
let telemetryTimer=null;
function startTelemetryLoop(){ if(telemetryTimer) clearInterval(telemetryTimer); telemetryTimer=setInterval(()=>{ if(!document.hidden) refreshTelemetry(); },8000); }
startTelemetryLoop();

function statCard(icon,color,val,label){
  return `<div class="stat-card"><div class="sc-top"><div class="sc-icon" style="background:${color}22;color:${color}"><i class="ti ${icon}"></i></div></div>
    <div class="sc-val">${val ?? 0}</div><div class="sc-label">${label}</div></div>`;
}
function protoLabel(l){
  if(l && typeof l === 'object'){
    if(l.protocol_display) return l.protocol_display;
    const found = PROTOCOLS.find(x=>x.id===l.protocol);
    return found ? found.label : (l.protocol||'—');
  }
  const found = PROTOCOLS.find(x=>x.id===l);
  return found ? found.label : (l||'—');
}
function statusBadge(l){
  if(l.expired || !l.active) return `<span class="badge red">غیرفعال/منقضی</span>`;
  if(l.status_color==='green') return `<span class="badge green">متصل</span>`;
  return `<span class="badge gray">فعال</span>`;
}

// ============================================================
// LINKS
// ============================================================
async function loadLinks(silent){
  try{
    const [linksRes, catsRes] = await Promise.all([api('/api/links'), api('/api/categories')]);
    const selectedBefore = silent ? selectedLinkUuids() : [];
    LINKS = linksRes.links || [];
    CATEGORIES = catsRes.categories || [];
    const sel = $('linkFilterCat');
    const prevCatVal = sel.value;
    sel.innerHTML = '<option value="">همه دسته‌ها</option>' + CATEGORIES.map(c=>`<option value="${c.id}">${escapeHtml(c.name)}</option>`).join('');
    sel.value = prevCatVal;
    $('nb-links').textContent = LINKS.filter(x=>!x.is_client).length;
    renderLinks();
    if(silent && selectedBefore.length){
      selectedBefore.forEach(uid=>{const c=document.querySelector(`.ib-row-check[data-uid="${uid}"]`); if(c) c.checked=true;});
      updateLinksBulkBar();
    }
    if($('ibUpdatedAt')) $('ibUpdatedAt').textContent = 'بروزرسانی ' + new Date().toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
  }catch(e){ if(!silent) toast(e.message, false); }
}
let linksTimer=setInterval(()=>{if(!document.hidden && CURRENT_PAGE==='links') loadLinks(true)},12000);
async function refreshAllInbounds(){
  const btn=$('ibRefreshBtn'), icon=$('ibRefreshIcon');
  if(btn) btn.disabled=true;
  if(icon) icon.classList.add('spin');
  try{
    await loadLinks();
    await refreshOverview();
    toast('همه‌ی اینباندها بروزرسانی شدند ✓');
  }catch(e){ toast(e.message, false); }
  finally{ if(btn) btn.disabled=false; if(icon) icon.classList.remove('spin'); }
}
function renderQuickStats(list){
  const total=list.length, active=list.filter(l=>l.active && !l.expired).length, live=list.filter(l=>l.live_status==='live').length, clients=list.reduce((s,l)=>s+Number(l.client_count||0),0);
  $('ibQuickStats').innerHTML = `
    <div><i class="ti ti-world-network"></i><span><b>${total}</b><small>کل اینباندها</small></span></div>
    <div><i class="ti ti-circle-check"></i><span><b>${active}</b><small>فعال</small></span></div>
    <div><i class="ti ti-bolt"></i><span><b>${live}</b><small>LIVE</small></span></div>
    <div><i class="ti ti-users"></i><span><b>${clients}</b><small>کل کلاینت‌ها</small></span></div>`;
}
function ibCardHtml(l){
  const pct=l.limit_bytes>0?Math.min(100,Math.round((l.used_bytes/l.limit_bytes)*100)):0; const port=l.port||443;
  const pctClass = pct>=90?'crit':(pct>=70?'warn':'');
  const isLive = l.live_status==='live';
  const daysLeft = l.expires_at ? Math.ceil((new Date(l.expires_at).getTime()-Date.now())/86400000) : null;
  const expClass = l.expired ? 'expired' : (daysLeft!==null && daysLeft<=3 ? 'soon' : '');
  const expSub = l.expires_at ? (l.expired ? 'منقضی شده' : (daysLeft!==null ? daysLeft+' روز مانده' : '')) : 'بدون انقضا';
  return `<article class="ib-card ${l.active?'':'ib-off'}" data-uid="${l.uuid}">
    <label class="ib-card-check"><input type="checkbox" class="ib-check ib-row-check" data-uid="${l.uuid}" onchange="updateLinksBulkBar()"></label>
    <div class="ib-card-head">
      <div class="ib-avatar"><i class="ti ti-router"></i></div>
      <div class="ib-card-id">
        <div class="ib-name-top"><b title="${escapeHtml(l.label||'Unnamed Inbound')}">${escapeHtml(l.label||'Unnamed Inbound')}</b>${l.expired?'<span class="badge red">منقضی</span>':''}</div>
        <div class="mono">${escapeHtml((l.uuid||'').slice(0,18))}…</div>
      </div>
      <div class="ib-card-controls">
        <button class="ib-switch ${l.active?'on':''}" title="فعال/غیرفعال" onclick="toggleLink('${l.uuid}', ${!l.active})"></button>
        <span class="ib-status-dot ${l.status_color||'gray'}" title="${l.status_color==='green'?'در حال اتصال':(l.status_color==='red'?'غیرفعال/منقضی':'فعال - بدون اتصال')}"></span>
      </div>
    </div>
    <div class="ib-tagrow"><span>${protoLabel(l)}</span><span>${l.network||'tcp'}/${l.security||'none'}</span>${isLive?'<span class="ib-live-tag"><i></i>LIVE</span>':'<span class="ib-linkonly-tag">LINK-ONLY</span>'}<span>${escapeHtml(l.category_name||'بدون دسته')}</span></div>
    <div class="ib-card-addr"><span class="mono">${escapeHtml(l.address||'0.0.0.0')}:${port}</span><small>${expSub}</small></div>
    <div class="ib-card-traffic">
      <div class="ib-tf-top"><span>مصرف</span><b>${fmtBytes(l.used_bytes||0)}${l.limit_bytes>0?' / '+fmtBytes(l.limit_bytes):' / ∞'}</b></div>
      <div class="ib-progress"><i class="${pctClass}" style="width:${pct}%"></i></div>
    </div>
    <div class="ib-card-stats">
      <div><small>کلاینت</small><b>${Number(l.client_count||0)}</b></div>
      <div><small>اتصال</small><b>${Number(l.connected_ips||0)}/${Number(l.connection_limit||0)||'∞'}</b></div>
      <div><small>انقضا</small><b class="${expClass}">${l.expires_at?escapeHtml(l.expires_at.slice(0,10)):'∞'}</b></div>
    </div>
    <div class="ib-card-foot">
      <div class="ib-clientcell"><button class="iconbtn" title="مدیریت کلاینت‌ها" onclick="openClients('${l.uuid}')"><i class="ti ti-users"></i></button><span>مدیریت کلاینت</span></div>
      <div class="ib-card-actions">
        <button class="iconbtn" title="اشتراک" onclick="showSubLink('${l.uuid}')"><i class="ti ti-qrcode"></i></button>
        <button class="iconbtn" title="ویرایش" onclick="openLinkDrawer('${l.uuid}')"><i class="ti ti-pencil"></i></button>
        <button class="iconbtn" title="تعویض لینک (UUID جدید)" onclick="regenerateLink('${l.uuid}')"><i class="ti ti-replace"></i></button>
        <button class="iconbtn" title="ریست حجم مصرفی" onclick="resetLinkUsage('${l.uuid}')"><i class="ti ti-refresh"></i></button>
        <button class="iconbtn" title="حذف" onclick="deleteLink('${l.uuid}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button>
      </div>
    </div>
  </article>`;
}
function renderLinks(){
  const q = ($('linkSearch').value||'').toLowerCase(); const cat = $('linkFilterCat').value;
  const all = LINKS.filter(l=>!l.is_client);
  renderQuickStats(all);
  const filtered = all.filter(l=>{ if(cat && String(l.category_id)!==String(cat)) return false; if(q && !(`${l.label||''} ${l.uuid||''} ${l.protocol||''}`).toLowerCase().includes(q)) return false; return true; });
  $('linksEmpty').style.display = filtered.length ? 'none' : 'block';
  $('ibGrid').innerHTML = filtered.map(ibCardHtml).join('');
  if($('ibCountLabel')) $('ibCountLabel').textContent = `${filtered.length} اینباند`;
  updateLinksBulkBar();
}
function toggleAllLinks(checked){
  document.querySelectorAll('.ib-row-check').forEach(c=>c.checked=checked);
  updateLinksBulkBar();
}
function selectedLinkUuids(){
  return Array.from(document.querySelectorAll('.ib-row-check:checked')).map(c=>c.dataset.uid);
}
function updateLinksBulkBar(){
  const sel = selectedLinkUuids();
  $('ibBulkBar').style.display = sel.length ? 'flex' : 'none';
  if($('ibSelCount')) $('ibSelCount').textContent = sel.length;
  const all = document.querySelectorAll('.ib-row-check');
  if($('ibSelAll')) $('ibSelAll').checked = all.length>0 && sel.length===all.length;
  document.querySelectorAll('.ib-card').forEach(card=>{
    const cb = card.querySelector('.ib-row-check');
    card.classList.toggle('ib-selected', !!(cb && cb.checked));
  });
}
async function bulkToggleLinks(active){
  const sel = selectedLinkUuids(); if(!sel.length) return;
  try{ await Promise.all(sel.map(uid=>api(`/api/links/${uid}`, {method:'PATCH', body: JSON.stringify({active})}))); toast('بروزرسانی گروهی انجام شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
async function bulkDeleteLinks(){
  const sel = selectedLinkUuids(); if(!sel.length) return;
  if(!confirm(`${sel.length} ${t('اینباند حذف شود؟')}`)) return;
  try{ await Promise.all(sel.map(uid=>api(`/api/links/${uid}`, {method:'DELETE'}))); toast('حذف گروهی انجام شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
async function openClients(uid){
  const inbound=LINKS.find(x=>x.uuid===uid); if(!inbound) return;
  try{
    const d=await api(`/api/links/${uid}/clients`);
    const clients=d.clients||[];
    openDrawer(`Client Manager · ${escapeHtml(inbound.label||'Inbound')}`, `
      <div class="client-manager">
        <div class="client-hero"><div><b>مدیریت کلاینت‌های واقعی</b><small>هر کلاینت UUID مستقل دارد و برای پروتکل‌های Live مستقیماً توسط Relay قابل احراز است.</small></div><span class="badge ${inbound.live_status==='live'?'green':'red'}">${inbound.live_status==='live'?'LIVE':'LINK-ONLY'}</span></div>
        ${inbound.live_status!=='live'?`<div class="notice danger-note">این اینباند فعلاً فقط لینک تولید می‌کند. برای Client واقعی، ابتدا یک ترکیب Live مثل VLESS + WS/TCP/XHTTP انتخاب کنید.</div>`:''}
        <div class="client-create"><div class="grp"><label>نام کلاینت</label><input id="clientName" placeholder="مثلاً iPhone · User 01"></div><div class="row2"><div class="grp"><label>حجم (GB، خالی = والد)</label><input id="clientLimit" type="number" min="0" placeholder="0"></div><div class="grp"><label>انقضا (روز، 0 = والد)</label><input id="clientDays" type="number" min="0" placeholder="0"></div></div><button class="btn primary" style="width:100%" onclick="createClient('${uid}')"><i class="ti ti-user-scan"></i>ساخت کلاینت واقعی</button></div>
        <div class="client-list">${clients.length?clients.map(c=>`<article class="client-row"><div class="client-avatar"><i class="ti ti-device-laptop"></i></div><div class="client-main"><b>${escapeHtml(c.label||'Client')}</b><small class="mono">${escapeHtml(c.uuid)}</small><div class="client-tags"><span>${c.active?'فعال':'خاموش'}</span><span>${fmtBytes(c.used_bytes||0)}${c.limit_bytes?' / '+fmtBytes(c.limit_bytes):''}</span><span>${c.expires_at?escapeHtml(c.expires_at.slice(0,10)):'∞'}</span></div></div><div class="client-actions"><button class="iconbtn" title="لینک اشتراک" onclick="showClientSubLink(${escapeHtml(JSON.stringify(c.sub||''))})"><i class="ti ti-qrcode"></i></button><button class="iconbtn" title="کپی VLESS" onclick="copyText(${escapeHtml(JSON.stringify(c.vless_full||''))})"><i class="ti ti-copy"></i></button><button class="iconbtn" title="تعویض لینک (UUID جدید)" onclick="regenerateClient('${uid}','${c.uuid}')"><i class="ti ti-replace"></i></button><button class="iconbtn" title="ریست حجم مصرفی" onclick="resetClientUsage('${uid}','${c.uuid}')"><i class="ti ti-refresh"></i></button><button class="iconbtn" title="حذف" onclick="deleteClient('${uid}','${c.uuid}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button></div></article>`).join(''):'<div class="empty-client">هنوز کلاینتی برای این اینباند ساخته نشده.</div>'}</div>
      </div>
  `, `<button class="btn" style="width:100%" onclick="loadLinks();openClients('${uid}')"><i class="ti ti-refresh"></i>بروزرسانی</button>`);
  }catch(e){toast(e.message,false)}
}
async function createClient(uid){
  const label=$('clientName')?.value||''; const limit=Number($('clientLimit')?.value||0); const days=Number($('clientDays')?.value||0);
  try{await api(`/api/links/${uid}/clients`,{method:'POST',body:JSON.stringify({label,limit_bytes:limit?limit*1024*1024*1024:0,expires_days:days})});toast('کلاینت واقعی ساخته شد ✓');openClients(uid);loadLinks();}catch(e){toast(e.message,false)}
}
async function deleteClient(uid,cid){
  if(!confirm(t('این کلاینت حذف شود؟'))) return;
  try{await api(`/api/links/${uid}/clients/${cid}`,{method:'DELETE'});toast('کلاینت حذف شد');openClients(uid);loadLinks();}catch(e){toast(e.message,false)}
}
async function regenerateClient(uid,cid){
  if(!confirm(t('یک لینک/UUID جدید برای این کلاینت صادر شود؟ لینک قبلی بلافاصله از کار می‌افتد و باید لینک جدید را دوباره برای کاربر بفرستید.'))) return;
  try{await api(`/api/links/${cid}/regenerate`,{method:'POST'});toast('لینک کلاینت تعویض شد ✓');openClients(uid);loadLinks();}catch(e){toast(e.message,false)}
}
async function resetClientUsage(uid,cid){
  if(!confirm(t('حجم مصرفی این کلاینت از صفر شروع شود؟'))) return;
  try{await api(`/api/links/${cid}/reset-usage`,{method:'POST'});toast('حجم مصرف ریست شد ✓');openClients(uid);loadLinks();}catch(e){toast(e.message,false)}
}

// ============================================================
// Standalone Client Manager page (بخش جدای ساخت کلاینت)
// ============================================================
let CM_INBOUNDS = [];
let CM_SELECTED_UID = '';
async function loadClientManager(){
  try{
    const res = await api('/api/links');
    CM_INBOUNDS = res.links || [];
    const sel = $('cmInboundSelect');
    const keep = CM_SELECTED_UID;
    sel.innerHTML = '<option value="">— انتخاب کنید —</option>' + CM_INBOUNDS.map(l=>
      `<option value="${l.uuid}">${escapeHtml(l.label||'Inbound')} · ${escapeHtml(protoLabel(l))} ${l.live_status==='live'?'(LIVE)':'(LINK-ONLY)'}</option>`
    ).join('');
    if(keep && CM_INBOUNDS.some(l=>l.uuid===keep)){
      sel.value = keep;
      loadClientManagerClients(keep);
    } else {
      $('cmInboundInfo').innerHTML = '';
      $('cmBody').innerHTML = `<div class="empty"><i class="ti ti-router"></i>ابتدا یک اینباند را از بالا انتخاب کن</div>`;
    }
  }catch(e){ toast(e.message, false); }
}
async function loadClientManagerClients(uid){
  CM_SELECTED_UID = uid || '';
  if(!uid){
    $('cmInboundInfo').innerHTML = '';
    $('cmBody').innerHTML = `<div class="empty"><i class="ti ti-router"></i>ابتدا یک اینباند را از بالا انتخاب کن</div>`;
    return;
  }
  const inbound = CM_INBOUNDS.find(x=>x.uuid===uid);
  try{
    const d = await api(`/api/links/${uid}/clients`);
    const clients = d.clients || [];
    $('cmInboundInfo').innerHTML = inbound ? `
      <div class="client-hero" style="margin-top:12px"><div><b>${escapeHtml(inbound.label||'Inbound')}</b><small>${escapeHtml(protoLabel(inbound))} · ${escapeHtml(inbound.address||'')}:${inbound.port||443}</small></div><span class="badge ${inbound.live_status==='live'?'green':'red'}">${inbound.live_status==='live'?'LIVE':'LINK-ONLY'}</span></div>
      ${inbound.live_status!=='live'?`<div class="notice danger-note" style="margin-top:10px">این اینباند فعلاً فقط لینک تولید می‌کند. برای Client واقعی، ابتدا یک ترکیب Live مثل VLESS + WS/TCP/XHTTP انتخاب کنید.</div>`:''}
    ` : '';
    $('cmBody').innerHTML = `
      <div class="card" style="padding:16px;margin-bottom:14px">
        <div class="client-create">
          <div class="grp"><label>نام کلاینت</label><input id="cmClientName" placeholder="مثلاً iPhone · User 01"></div>
          <div class="row2">
            <div class="grp"><label>حجم (GB، خالی = والد)</label><input id="cmClientLimit" type="number" min="0" placeholder="0"></div>
            <div class="grp"><label>انقضا (روز، 0 = والد)</label><input id="cmClientDays" type="number" min="0" placeholder="0"></div>
          </div>
          <button class="btn primary" style="width:100%" onclick="createClientMgr('${uid}')"><i class="ti ti-user-scan"></i>ساخت کلاینت واقعی</button>
        </div>
      </div>
      <div class="card" style="padding:16px">
        <div class="panel-head" style="padding:0 0 12px;border:0"><div><b>کلاینت‌های این اینباند</b><small>${clients.length} کلاینت</small></div></div>
        <div class="client-list">${clients.length ? clients.map(c=>`<article class="client-row"><div class="client-avatar"><i class="ti ti-device-laptop"></i></div><div class="client-main"><b>${escapeHtml(c.label||'Client')}</b><small class="mono">${escapeHtml(c.uuid)}</small><div class="client-tags"><span>${c.active?'فعال':'خاموش'}</span><span>${fmtBytes(c.used_bytes||0)}${c.limit_bytes?' / '+fmtBytes(c.limit_bytes):''}</span><span>${c.expires_at?escapeHtml(c.expires_at.slice(0,10)):'∞'}</span></div></div><div class="client-actions"><button class="iconbtn" title="لینک اشتراک" onclick="showClientSubLink(${escapeHtml(JSON.stringify(c.sub||''))})"><i class="ti ti-qrcode"></i></button><button class="iconbtn" title="کپی VLESS" onclick="copyText(${escapeHtml(JSON.stringify(c.vless_full||''))})"><i class="ti ti-copy"></i></button><button class="iconbtn" title="تعویض لینک (UUID جدید)" onclick="regenerateClientMgr('${uid}','${c.uuid}')"><i class="ti ti-replace"></i></button><button class="iconbtn" title="ریست حجم مصرفی" onclick="resetClientMgrUsage('${uid}','${c.uuid}')"><i class="ti ti-refresh"></i></button><button class="iconbtn" title="حذف" onclick="deleteClientMgr('${uid}','${c.uuid}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button></div></article>`).join('') : '<div class="empty-client">هنوز کلاینتی برای این اینباند ساخته نشده.</div>'}</div>
      </div>
    `;
  }catch(e){ toast(e.message, false); }
}
async function createClientMgr(uid){
  const label = $('cmClientName').value.trim();
  const limit = Number($('cmClientLimit').value) || 0;
  const days = Number($('cmClientDays').value) || 0;
  try{
    await api(`/api/links/${uid}/clients`, {method:'POST', body: JSON.stringify({label, limit_bytes: limit ? limit*1024*1024*1024 : 0, expires_days: days})});
    toast('کلاینت واقعی ساخته شد ✓');
    loadClientManagerClients(uid);
  }catch(e){ toast(e.message, false); }
}
async function deleteClientMgr(uid, cid){
  if(!confirm(t('این کلاینت حذف شود؟'))) return;
  try{ await api(`/api/links/${uid}/clients/${cid}`, {method:'DELETE'}); toast('کلاینت حذف شد'); loadClientManagerClients(uid); }
  catch(e){ toast(e.message, false); }
}
async function regenerateClientMgr(uid, cid){
  if(!confirm(t('یک لینک/UUID جدید برای این کلاینت صادر شود؟ لینک قبلی بلافاصله از کار می‌افتد و باید لینک جدید را دوباره برای کاربر بفرستید.'))) return;
  try{ await api(`/api/links/${cid}/regenerate`, {method:'POST'}); toast('لینک کلاینت تعویض شد ✓'); loadClientManagerClients(uid); }
  catch(e){ toast(e.message, false); }
}
async function resetClientMgrUsage(uid, cid){
  if(!confirm(t('حجم مصرفی این کلاینت از صفر شروع شود؟'))) return;
  try{ await api(`/api/links/${cid}/reset-usage`, {method:'POST'}); toast('حجم مصرف ریست شد ✓'); loadClientManagerClients(uid); }
  catch(e){ toast(e.message, false); }
}
async function copyText(v){
  v = v || '';
  if(window.isSecureContext && navigator.clipboard && navigator.clipboard.writeText){
    try{ await navigator.clipboard.writeText(v); toast('کپی شد ✓'); return; }catch(e){ /* برو سراغ روش قدیمی */ }
  }
  if(legacyCopy(v)){ toast('کپی شد ✓'); } else { prompt('کپی کنید:', v); }
}
function showClientSubLink(subUrl){
  if(!subUrl){ toast('لینک ساب برای این کلاینت در دسترس نیست', false); return; }
  const qr = 'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=' + encodeURIComponent(subUrl);
  openDrawer('لینک اشتراک کلاینت', `
    <div class="qr-box"><img src="${qr}"></div>
    <div class="grp"><label>لینک ساب</label><div class="copy-row"><input readonly value="${escapeHtml(subUrl)}" id="clientSubLinkInp"></div></div>
    <p class="hint">اگر این لینک برای مشتری باز نمی‌شود، ابتدا از تب «تنظیمات» آدرس عمومی پنل را درست تنظیم کنید.</p>
  `, `<button class="btn primary" style="width:100%" onclick="copyInput('clientSubLinkInp')"><i class="ti ti-copy"></i>کپی لینک ساب</button>`);
}

function showSubLink(uid){
  const l = LINKS.find(x=>x.uuid===uid);
  if(!l) return;
  const qr = 'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=' + encodeURIComponent(l.sub_url || l.sub);
  openDrawer('لینک اشتراک', `
    <div class="qr-box"><img src="${qr}"></div>
    <div class="grp"><label>لینک ساب</label><div class="copy-row"><input readonly value="${escapeHtml(l.sub_url||l.sub)}" id="subLinkInp"></div></div>
    <div class="grp"><label>صفحه‌ی نمایش اشتراک (برای مشتری)</label><div class="copy-row"><input readonly value="${escapeHtml((l.sub_url||l.sub||'').replace('/sub/','/subscription/'))}" id="subPortalInp"></div></div>
    <p class="hint">اگر این لینک برای مشتری باز نمی‌شود، ابتدا از تب «تنظیمات» آدرس عمومی پنل را درست تنظیم کنید.</p>
  `, `<button class="btn primary" style="width:100%" onclick="copyInput('subLinkInp')"><i class="ti ti-copy"></i>کپی لینک ساب</button>`);
}
function legacyCopy(text){
  // execCommand روی همه‌ی مرورگرها حتی بدون HTTPS (secure context) کار می‌کند.
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.top = '-9999px';
  ta.style.left = '-9999px';
  document.body.appendChild(ta);
  ta.focus();
  ta.select();
  let ok = false;
  try{ ok = document.execCommand('copy'); }catch(e){ ok = false; }
  document.body.removeChild(ta);
  return ok;
}
async function copyInput(id){
  const el = $(id);
  if(!el) return;
  const value = el.value || '';
  el.focus();
  el.select();
  // navigator.clipboard فقط در HTTPS (secure context) در دسترسه؛ اگر پنل با HTTP
  // (بدون دامنه/SSL) باز شده باشه این آبجکت اصلاً وجود نداره و باید مستقیم به
  // روش قدیمی (execCommand) یا در آخرین حالت به prompt دستی سوییچ کنیم.
  if(window.isSecureContext && navigator.clipboard && navigator.clipboard.writeText){
    try{
      await navigator.clipboard.writeText(value);
      toast('کپی شد ✓');
      return;
    }catch(e){ /* برو سراغ روش قدیمی */ }
  }
  if(legacyCopy(value)){
    toast('کپی شد ✓');
  } else {
    prompt('کپی کنید:', value);
  }
}
async function toggleLink(uid, active){
  try{ await api(`/api/links/${uid}`, {method:'PATCH', body: JSON.stringify({active})}); toast('بروزرسانی شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
async function deleteLink(uid){
  if(!confirm(t('این کانفیگ حذف شود؟'))) return;
  try{ await api(`/api/links/${uid}`, {method:'DELETE'}); toast('حذف شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
async function resetLinkUsage(uid){
  if(!confirm(t('حجم مصرفی این کانفیگ از صفر شروع شود؟'))) return;
  try{ await api(`/api/links/${uid}/reset-usage`, {method:'POST'}); toast('حجم مصرف ریست شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
async function regenerateLink(uid){
  if(!confirm(t('یک لینک/UUID جدید صادر شود؟ لینک قبلی بلافاصله از کار می‌افتد و باید لینک جدید را دوباره برای کاربر بفرستید.'))) return;
  try{ const r = await api(`/api/links/${uid}/regenerate`, {method:'POST'}); toast('لینک جدید صادر شد'); loadLinks(); showSubLink(r.uuid); }
  catch(e){ toast(e.message, false); }
}
async function openAutoLink(){
  try{ await api('/api/links/auto', {method:'POST', body: JSON.stringify({profile:'balanced'})}); toast('کانفیگ خودکار ساخته شد'); loadLinks(); }
  catch(e){ toast(e.message, false); }
}
// Single source of truth for turning a link's stored fields into
// {base_protocol, network, security}. Both the builder's initial render and
// the edit-drawer's hidden-field sync must agree, or the visible transport
// card and the value that actually gets submitted can diverge (this used to
// happen for links whose `protocol` was a legacy shortcut like "vless-ws":
// the card correctly showed WebSocket, but the hidden #mNetwork field fell
// back to a stale/defaulted "tcp" a moment later).
function deriveManualParts(l){
  l = l || {};
  const proto = l.protocol || 'manual';
  if(proto === 'manual'){
    // Created by the advanced builder: base_protocol/network/security were
    // explicitly written by the backend and are always reliable.
    return {bp: l.base_protocol || 'vless', net: l.network || 'ws', sec: l.security || 'tls'};
  }
  if(proto==='vless-ws') return {bp:'vless',net:'ws',sec:'tls'};
  if(proto==='vless-tcp') return {bp:'vless',net:'tcp',sec:'none'};
  if(proto.startsWith('xhttp-')) return {bp:'vless',net:'xhttp',sec:'tls'};
  if(proto==='vmess-ws') return {bp:'vmess',net:'ws',sec:'tls'};
  if(proto==='trojan-ws') return {bp:'trojan',net:'ws',sec:'tls'};
  return {bp: l.base_protocol || 'vless', net: l.network || 'ws', sec: l.security || 'tls'};
}
function manualBuilderHtml(l){
  l = l || {};
  const parts = deriveManualParts(l);
  let bp = parts.bp, net = parts.net, sec = parts.sec;
  const methods = MANUAL_META.shadowsocks_methods || ['chacha20-ietf-poly1305','aes-128-gcm','aes-256-gcm'];
  const icons = {vless:'ti-bolt',vmess:'ti-brand-vscode',trojan:'ti-shield-lock',shadowsocks:'ti-brand-shield'};
  const bpLabels = {vless:'VLESS',vmess:'VMess',trojan:'Trojan',shadowsocks:'Shadowsocks'};
  const nets = [
    ['tcp','TCP','Raw / direct','ti-arrows-right-left'],
    ['ws','WebSocket','WS over HTTP','ti-world'],
    ['grpc','gRPC','HTTP/2 transport','ti-transfer'],
    ['xhttp','XHTTP','Modern HTTP transport','ti-brand-xamarin']
  ];
  const secs = (MANUAL_META.securities||[]);
  const fpOpts=(MANUAL_META.fingerprints||['chrome','firefox','safari','ios','android','edge','random']).map(x=>`<option value="${x}" ${(l.fingerprint||'chrome')===x?'selected':''}>${x}</option>`).join('');
  const methodOpts=methods.map(x=>`<option value="${x}" ${(l.ss_method||methods[0])===x?'selected':''}>${x}</option>`).join('');
  const conn=Number(l.connection_limit||0), speed=Number(l.speed_limit_bytes||0), speedMbit=speed?Math.max(1,Math.round(speed*8/1000000)):'';
  return `
    <div class="inbound-builder">
      <div class="ib-hero">
        <div class="ib-title"><div class="ib-icon"><i class="ti ti-adjustments-horizontal"></i></div><div><b>${l.uuid?'ویرایش اینباند':'ساخت اینباند حرفه‌ای'}</b><small>پروتکل پایه، ترنسپورت و امنیت کاملاً تفکیک‌شده</small></div></div>
        <span class="badge gray">INBOUND BUILDER</span>
      </div>

      <div class="ib-section">
        <div class="ib-section-body">
          <div class="ib-step"><span class="num">1</span><div><b>پروتکل پایه</b><small>اول مشخص کن با چه پروتکلی کانفیگ ساخته شود</small></div></div>
          <div id="ibProtocolCards" class="ib-matrix">
            ${Object.entries(bpLabels).map(([id,label])=>`<label class="ib-opt ${bp===id?'on':''}" data-proto-card="${id}"><input type="radio" name="ibBaseProtocol" value="${id}" ${bp===id?'checked':''} onchange="selectBaseProtocol('${id}')"><span class="ib-opt-icon"><i class="ti ${icons[id]||'ti-network'}"></i></span><span><b>${label}</b><small>${id==='vless'?'UUID / XTLS ecosystem':id==='vmess'?'Legacy-compatible':id==='trojan'?'Password-style auth':'AEAD proxy'}</small></span></label>`).join('')}
          </div>
        </div>
      </div>

      <div class="ib-section">
        <div class="ib-section-body">
          <div class="ib-step"><span class="num">2</span><div><b>Transport / Network</b><small>حالا مسیر انتقال را جداگانه انتخاب کن</small></div></div>
          <div id="ibTransportCards" class="ib-matrix">
            ${nets.map(([id,label,sub,icon])=>`<label class="ib-opt ${net===id?'on':''}" data-net-card="${id}"><input type="radio" name="ibNetwork" value="${id}" ${net===id?'checked':''} onchange="selectTransport('${id}')"><span class="ib-opt-icon"><i class="ti ${icon}"></i></span><span><b>${label}</b><small>${sub}</small></span></label>`).join('')}
          </div>
          <div id="ibTransportNote" class="ib-status" style="margin-top:10px"></div>
        </div>
      </div>

      <div class="ib-section">
        <div class="ib-section-body">
          <div class="ib-step"><span class="num">3</span><div><b>Security</b><small>TLS / Reality / None را مستقل از ترنسپورت انتخاب کن</small></div></div>
          <div id="ibSecurityCards" class="ib-matrix">
            ${secs.map(x=>`<label class="ib-opt ${sec===x.id?'on':''}" data-sec-card="${x.id}"><input type="radio" name="ibSecurity" value="${x.id}" ${sec===x.id?'checked':''} onchange="selectSecurity('${x.id}')"><span class="ib-opt-icon"><i class="ti ${x.id==='reality'?'ti-key':x.id==='tls'?'ti-lock':'ti-lock-open'}"></i></span><span><b>${x.label}</b><small>${x.id==='reality'?'Reality public-key mode':x.id==='tls'?'Standard TLS':'No TLS wrapper'}</small></span></label>`).join('')}
          </div>
          <div id="mLiveHint" class="ib-status" style="margin-top:10px"></div>
        </div>
      </div>

      <div class="ib-section">
        <div class="ib-section-head"><div><b>4. Endpoint & Advanced Parameters</b><small>فقط فیلدهای مرتبط با انتخاب بالا نمایش داده می‌شوند</small></div><i class="ti ti-server-2"></i></div>
        <div class="ib-section-body">
          <div class="ib-grid">
            <div class="grp"><label>نام / Remark</label><input id="fLabel" value="${escapeHtml(l.label||'')}" placeholder="مثلاً: VIP-01"></div>
            <div class="grp"><label>دسته‌بندی</label><select id="fCategory"><option value="0">بدون دسته</option>${CATEGORIES.map(c=>`<option value="${c.id}" ${String(l.category_id)===String(c.id)?'selected':''}>${escapeHtml(c.name)}</option>`).join('')}</select></div>
            <div class="grp"><label>آدرس / Domain</label><div class="endpoint-input"><input id="mAddress" placeholder="example.com" value="${escapeHtml(l.address||'')}" oninput="updateBuilderSummary()"><button type="button" class="btn endpoint-btn" onclick="loadRailwayEndpoint()"><i class="ti ti-cloud"></i>Railway</button></div></div>
            <div class="grp"><label>Port</label><div class="endpoint-input"><input id="mPort" type="number" min="1" max="65535" value="${l.port||443}" oninput="updateBuilderSummary()"><button type="button" class="btn endpoint-btn" onclick="testCurrentTcp()"><i class="ti ti-activity"></i>Ping</button></div></div>
            <div class="grp"><label>Fingerprint</label><select id="mFingerprint">${fpOpts}</select></div>
            <div class="grp"><label>ALPN</label><input id="mAlpn" value="${escapeHtml(l.alpn||'')}" placeholder="h2,http/1.1"></div>
            <div id="mWsXhttpWrap" class="ib-grid ib-full">
              <div class="grp"><label>Path</label><input id="mPath" placeholder="/ws" value="${escapeHtml(l.path||'')}"></div>
              <div class="grp"><label>Host Header</label><input id="mHost" placeholder="domain.com" value="${escapeHtml(l.host_header||'')}"></div>
            </div>
            <div id="mXhttpModeWrap" class="grp ib-full"><label>XHTTP Mode</label><select id="mXhttpMode">${(MANUAL_META.xhttp_modes||['auto','packet-up','stream-up','stream-one']).map(x=>`<option value="${x}" ${(l.xhttp_mode||'packet-up')===x?'selected':''}>${x}</option>`).join('')}</select><small style="opacity:.7">packet-up و stream-up توسط این پنل واقعاً سرو می‌شن؛ auto به‌صورت خودکار روی packet-up قفل می‌شه، stream-one فقط لینک می‌سازه (Live نیست).</small></div>
            <div id="mGrpcWrap" class="ib-grid ib-full"><div class="grp"><label>Service Name</label><input id="mGrpcService" placeholder="service" value="${escapeHtml(l.grpc_service_name||'')}"></div><div class="grp"><label>gRPC Mode</label><select id="mGrpcMode"><option value="gun" ${(l.grpc_mode||'gun')==='gun'?'selected':''}>gun</option><option value="multi" ${l.grpc_mode==='multi'?'selected':''}>multi</option></select></div></div>
            <div id="mTcpWrap" class="ib-grid ib-full"><div class="grp"><label>Header Type</label><select id="mHeaderType"><option value="" ${!l.header_type?'selected':''}>none</option><option value="http" ${l.header_type==='http'?'selected':''}>http</option></select></div><div class="grp"><label>Flow</label><select id="mFlow"><option value="" ${!l.flow?'selected':''}>—</option><option value="xtls-rprx-vision" ${l.flow==='xtls-rprx-vision'?'selected':''}>xtls-rprx-vision</option></select></div></div>
            <div id="mTlsWrap" class="ib-grid ib-full"><div class="grp"><label>SNI</label><input id="mSni" value="${escapeHtml(l.sni||'')}" placeholder="example.com"></div><label class="chk" style="align-self:end;margin-bottom:16px"><input id="mAllowInsecure" type="checkbox" ${l.allow_insecure?'checked':''}> Allow Insecure</label></div>
            <div id="mRealityWrap" class="ib-grid ib-full"><div class="grp"><label>Reality SNI</label><input id="mRealitySni" value="${escapeHtml(l.sni||'')}" placeholder="www.example.com"></div><div class="grp"><label>Public Key</label><input id="mRealityPbk" value="${escapeHtml(l.reality_public_key||'')}" placeholder="public key"></div><div class="grp"><label>Short ID</label><input id="mRealitySid" value="${escapeHtml(l.reality_short_id||'')}" placeholder="short id"></div><div class="grp"><label>Spider X</label><input id="mRealitySpx" value="${escapeHtml(l.reality_spider_x||'/')}" placeholder="/"></div><div class="grp ib-full"><label>Private Key (فقط برای نود Xray-core خودتان — این پنل ذخیره‌اش نمی‌کند)</label><div class="endpoint-input"><input id="mRealityPrivRaw" readonly placeholder="بعد از «Generate Reality Keypair» اینجا نمایش داده می‌شود" value=""><button type="button" class="btn endpoint-btn" onclick="copyText($('mRealityPrivRaw').value)"><i class="ti ti-copy"></i>Copy</button></div></div><div class="ib-full"><button type="button" class="btn" onclick="generateRealityKeys()"><i class="ti ti-key"></i>Generate Reality Keypair</button></div></div>
            <div id="mShadowWrap" class="ib-grid ib-full"><div class="grp"><label>Encryption Method</label><select id="mSsMethod">${methodOpts}</select></div><div class="grp"><label>Password</label><input id="mSsPassword" type="password" value="${escapeHtml(l.ss_password||'')}" placeholder="Password / secret"></div></div>
            <div class="grp"><label>حجم (GB)</label><input id="fLimitVal" type="number" min="0" value="${l.limit_bytes?Math.round(l.limit_bytes/1073741824):''}"></div>
            <div class="grp"><label>اعتبار (روز)</label><input id="fDays" type="number" min="0" value="${l.expires_at?Math.max(0,Math.ceil((new Date(l.expires_at).getTime()-Date.now())/86400000)):''}"></div>
            <div class="grp"><label>زمان دقیق انقضا</label><input id="fExpiresAt" type="datetime-local" value="${l.expires_at?new Date(l.expires_at).toISOString().slice(0,16):''}"></div>
            <div class="grp"><label>IP Limit</label><input id="fIpLimit" type="number" min="0" value="${l.ip_limit||0}"></div>
            <div class="grp"><label>Connection Limit</label><input id="fConnLimit" type="number" min="0" value="${conn}"></div>
            <div class="grp"><label>تعداد کاربر</label><input id="fClientLimit" type="number" min="0" max="1000" value="${l.client_limit||0}" placeholder="0 = نامحدود"></div>
            <div class="grp"><label>تعداد خروجی</label><input id="fConfigCount" type="number" min="1" max="40" value="${l.config_count||1}"></div>
            <div class="grp ib-full"><label>آی‌پی‌های تمیز (Clean IP) — هر خط یک آی‌پی/دامنه</label><textarea id="fCleanIps" rows="3" placeholder="1.2.3.4&#10;5.6.7.8&#10;clean.example.com" style="width:100%;resize:vertical;font-family:monospace">${escapeHtml((l.clean_ips||[]).join('\n'))}</textarea><small style="opacity:.7">اگه اینجا چند آی‌پی/دامنه بذاری، «تعداد خروجی» به همون تعداد کانفیگ می‌سازه که هرکدوم روی یکی از این آی‌پی‌ها می‌ره (همه توی یک سابسکریپشن)؛ اگه خالی باشه، فقط همون تعداد کپیِ یک کانفیگ با نام‌های متفاوت ساخته می‌شه.</small></div>
            <div class="grp"><label>Speed (Mbit/s)</label><input id="fSpeed" type="number" min="0" value="${speedMbit}" placeholder="0 = نامحدود"></div>
            <div class="grp ib-full"><label>یادداشت داخلی</label><input id="fNote" value="${escapeHtml(l.note||'')}" placeholder="توضیحات اختیاری"></div>
          </div>
        </div>
      </div>

      <div class="ib-section">
        <div class="ib-section-body"><div class="ib-step"><span class="num">5</span><div><b>Summary</b><small>قبل از ذخیره ترکیب نهایی را بررسی کن</small></div></div>
          <div class="ib-summary"><div class="sum"><small>PROTOCOL</small><b id="sumProtocol">${bp.toUpperCase()}</b></div><div class="sum"><small>NETWORK</small><b id="sumNetwork">${net.toUpperCase()}</b></div><div class="sum"><small>SECURITY</small><b id="sumSecurity">${sec.toUpperCase()}</b></div><div class="sum"><small>PORT</small><b id="sumPort">${l.port||443}</b></div><div class="sum"><small>TRAFFIC</small><b id="sumTraffic">—</b></div><div class="sum"><small>LIMITS</small><b id="sumLimits">—</b></div></div>
        </div>
      </div>
    </div>`;
}

function refreshInboundCards(){
  const bp=$('mBase')?.value || document.querySelector('input[name="ibBaseProtocol"]:checked')?.value || 'vless';
  const net=$('mNetwork')?.value || document.querySelector('input[name="ibNetwork"]:checked')?.value || 'ws';
  const sec=$('mSecurity')?.value || document.querySelector('input[name="ibSecurity"]:checked')?.value || 'tls';
  document.querySelectorAll('[data-proto-card]').forEach(e=>e.classList.toggle('on',e.dataset.protoCard===bp));
  document.querySelectorAll('[data-net-card]').forEach(e=>e.classList.toggle('on',e.dataset.netCard===net));
  document.querySelectorAll('[data-sec-card]').forEach(e=>e.classList.toggle('on',e.dataset.secCard===sec));
}
function selectBaseProtocol(id){
  let hidden=document.getElementById('mBase'); if(!hidden){hidden=document.createElement('input');hidden.type='hidden';hidden.id='mBase';document.body.appendChild(hidden)} hidden.value=id;
  const ss=id==='shadowsocks';
  const secWrap=document.getElementById('ibSecurityCards');
  if(secWrap){document.querySelectorAll('[data-sec-card]').forEach(e=>{const sid=e.dataset.secCard; e.classList.toggle('off',ss && sid!=='none'); const inp=e.querySelector('input'); if(inp) inp.disabled=ss&&sid!=='none';}); if(ss){selectSecurity('none');}}
  if(ss && document.querySelector('input[name="ibNetwork"]:checked')?.value!=='tcp') selectTransport('tcp');
  document.getElementById('mShadowWrap')?.style.setProperty('display',ss?'':'none');
  refreshInboundCards(); onManualChange(); updateBuilderSummary();
}
function selectTransport(id){
  let hidden=document.getElementById('mNetwork'); if(!hidden){hidden=document.createElement('input');hidden.type='hidden';hidden.id='mNetwork';document.body.appendChild(hidden)} hidden.value=id;
  const ss=document.getElementById('mBase')?.value==='shadowsocks';
  if(ss && id!=='tcp'){toast('Shadowsocks در این سازنده فقط با TCP پشتیبانی می‌شود',false);hidden.value='tcp';return selectTransport('tcp');}
  refreshInboundCards(); onManualChange(); updateBuilderSummary();
}
function selectSecurity(id){
  let hidden=document.getElementById('mSecurity'); if(!hidden){hidden=document.createElement('input');hidden.type='hidden';hidden.id='mSecurity';document.body.appendChild(hidden)} hidden.value=id;
  refreshInboundCards(); onManualChange(); updateBuilderSummary();
}

function updateBuilderSummary(){
  const val=id=>$(id)?.value || '—'; const set=(id,v)=>{const e=$(id);if(e)e.textContent=v};
  set('sumProtocol',(val('mBase')||'vless').toUpperCase()); set('sumNetwork',(val('mNetwork')||'tcp').toUpperCase()); set('sumSecurity',(val('mSecurity')||'none').toUpperCase()); set('sumPort',val('mPort'));
  const traffic=Number(val('fLimitVal'))||0; set('sumTraffic',traffic?`${traffic} GB`:'نامحدود');
  const ip=Number(val('fIpLimit'))||0, conn=Number(val('fConnLimit'))||0; set('sumLimits',`IP ${ip||'∞'} / CONN ${conn||'∞'}`);
}
function onManualChange(){
  const base=$('mBase')?.value || 'vless', net=$('mNetwork')?.value || 'ws', sec=$('mSecurity')?.value || 'tls';
  const show=(id,yes)=>{const e=$(id);if(e)e.style.display=yes?'':'none'};
  show('mWsXhttpWrap',net==='ws'||net==='xhttp'); show('mXhttpModeWrap',net==='xhttp'); show('mGrpcWrap',net==='grpc'); show('mTcpWrap',net==='tcp'); show('mTlsWrap',sec==='tls'); show('mRealityWrap',sec==='reality'); show('mShadowWrap',base==='shadowsocks');
  if(base==='shadowsocks'){ if($('mNetwork') && $('mNetwork').value!=='tcp') $('mNetwork').value='tcp'; if($('mSecurity')) $('mSecurity').value='none'; }
  const hint=$('mLiveHint');
  if(hint){
    const live=base!=='shadowsocks' && (MANUAL_META.live_combos||[]).some(c=>c[0]===net&&c[1]===sec) && !(net==='xhttp'&&($('mXhttpMode')?.value||'packet-up')==='stream-one');
    hint.className='ib-status '+(live?'ok':'warn'); hint.innerHTML=live?'<i class="ti ti-circle-check"></i> این ترکیب آماده استفاده است.':'<i class="ti ti-alert-triangle"></i> این ترکیب برای ساخت لینک و مدیریت سرویس آماده شده است.';
  }
  const tn=$('ibTransportNote');
  if(tn){tn.innerHTML=base==='shadowsocks'?'<i class="ti ti-info-circle"></i> Shadowsocks به‌صورت TCP-only در این Builder ارائه می‌شود.':'<i class="ti ti-adjustments-horizontal"></i> Transport فقط مسیر انتقال است و جدا از پروتکل پایه انتخاب می‌شود.';}
  refreshInboundCards(); updateBuilderSummary();
}

async function testCurrentTcp(){
  const host=($('mAddress')?.value||'').trim();
  const port=Number($('mPort')?.value||0);
  if(!host){toast('ابتدا آدرس یا دامنه را وارد کنید',false);return}
  if(!Number.isInteger(port)||port<1||port>65535){toast('پورت نامعتبر است',false);return}
  const btn=document.querySelector('.endpoint-btn[onclick="testCurrentTcp()"]');
  if(btn){btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2 spin"></i> در حال تست'}
  try{
    const r=await api('/api/network/tcp-ping',{method:'POST',body:JSON.stringify({host,port,timeout:4})});
    if(r.ok) toast(`TCP OK • ${r.latency_ms}ms • ${host}:${port}`);
    else toast(r.message||'اتصال برقرار نشد',false);
  }catch(e){toast(e.message||'خطا در تست TCP',false)}
  finally{if(btn){btn.disabled=false;btn.innerHTML='<i class="ti ti-activity"></i> تست پینگ'}}
}

async function loadRailwayEndpoint(){
  try{
    const r=await api('/api/network/railway');
    if(!r.is_railway && !r.tcp_proxy_domain){toast('اطلاعات TCP Proxy ریل‌وی در این سرویس پیدا نشد',false);return}
    if(r.tcp_proxy_domain){$('mAddress').value=r.tcp_proxy_domain; if(r.tcp_proxy_port) $('mPort').value=r.tcp_proxy_port; updateBuilderSummary(); toast(`Railway TCP Proxy: ${r.tcp_proxy_domain}:${r.tcp_proxy_port||'?'}`)}
    else if(r.public_domain){$('mAddress').value=r.public_domain; updateBuilderSummary(); toast('دامنه عمومی Railway وارد شد؛ برای TCP خام باید TCP Proxy فعال باشد')}
  }catch(e){toast(e.message||'خطا در دریافت اطلاعات Railway',false)}
}

async function generateRealityKeys(){
  try{
    const r=await api('/api/reality-keypair');
    $('mRealityPbk').value=r.public_key;
    $('mRealitySid').value=r.short_id;
    if($('mRealityPrivRaw')) $('mRealityPrivRaw').value=r.private_key||'';
    toast('کلید Reality ساخته شد — Private Key را همین‌جا کپی کنید و روی نود Xray-core خودتان قرار دهید (این پنل آن را ذخیره نمی‌کند).');
  }
  catch(e){ toast(e.message, false); }
}

function onProtocolModeChange(){
  // Kept for compatibility with older inline handlers; the new builder is always advanced.
  const wrap=$('manualBuilderWrap'); if(wrap) wrap.style.display='block'; const quick=$('quickFieldsWrap'); if(quick) quick.style.display='none';
}
function openLinkDrawer(uid){
  const editing=!!uid, l=editing?(LINKS.find(x=>x.uuid===uid)||{}):{};
  openDrawer(editing?'ویرایش اینباند':'ساخت اینباند', `${manualBuilderHtml(l)}`,
    `${editing?`<button class="btn danger" onclick="deleteLink('${uid}');closeDrawer()"><i class="ti ti-trash"></i>حذف</button>`:''}<button class="btn primary" style="flex:1" onclick="submitLink('${uid||''}')"><i class="ti ti-device-floppy"></i>${editing?'ذخیره تغییرات':'ساخت اینباند'}</button>`);
  setTimeout(()=>{
    let bp=document.getElementById('mBase'); if(!bp){bp=document.createElement('input');bp.type='hidden';bp.id='mBase';document.querySelector('.drawer .dr-body')?.appendChild(bp)}
    let net=document.getElementById('mNetwork'); if(!net){net=document.createElement('input');net.type='hidden';net.id='mNetwork';document.querySelector('.drawer .dr-body')?.appendChild(net)}
    let sec=document.getElementById('mSecurity'); if(!sec){sec=document.createElement('input');sec.type='hidden';sec.id='mSecurity';document.querySelector('.drawer .dr-body')?.appendChild(sec)}
    let proto=l.protocol||'manual'; const parts=deriveManualParts(l);
    bp.value=parts.bp;
    net.value=parts.net;
    sec.value=parts.sec;
    if(bp.value==='shadowsocks'){net.value='tcp';sec.value='none'}
    refreshInboundCards(); onManualChange(); updateBuilderSummary();
  },0);
}

async function submitLink(uid){
  const base=$('mBase')?.value || 'vless', net=$('mNetwork')?.value || 'ws', sec=$('mSecurity')?.value || 'tls';
  const port=Number($('mPort')?.value||443);
  if(!Number.isInteger(port)||port<1||port>65535){toast('پورت باید بین 1 تا 65535 باشد',false);return}
  if(base==='shadowsocks' && net!=='tcp'){toast('Shadowsocks فقط با TCP ساخته می‌شود',false);return}
  const num=id=>Math.max(0,Number($(id)?.value||0));
  const body={label:($('fLabel')?.value||'').trim(),protocol:'manual',category_id:$('fCategory')?.value||'0',limit_value:num('fLimitVal'),limit_unit:'GB',expires_days:num('fDays'),expires_at:$('fExpiresAt')?.value||'',ip_limit:num('fIpLimit'),connection_limit:num('fConnLimit'),client_limit:num('fClientLimit'),config_count:Math.max(1,Math.min(40,num('fConfigCount')||1)),clean_ips:($('fCleanIps')?.value||'').trim(),speed_limit_value:num('fSpeed'),speed_limit_unit:'MBIT',note:($('fNote')?.value||'').trim(),port,fingerprint:$('mFingerprint')?.value||'chrome',alpn:$('mAlpn')?.value||''};
  body.manual={base_protocol:base,network:net,security:base==='shadowsocks'?'none':sec,address:$('mAddress')?.value||'',path:$('mPath')?.value||'',host_header:$('mHost')?.value||'',sni:sec==='reality'?($('mRealitySni')?.value||''):($('mSni')?.value||''),alpn:$('mAlpn')?.value||'',flow:$('mFlow')?.value||'',grpc_service_name:$('mGrpcService')?.value||'',grpc_mode:$('mGrpcMode')?.value||'gun',xhttp_mode:$('mXhttpMode')?.value||'packet-up',header_type:$('mHeaderType')?.value||'',allow_insecure:!!$('mAllowInsecure')?.checked,reality_public_key:$('mRealityPbk')?.value||'',reality_short_id:$('mRealitySid')?.value||'',reality_spider_x:$('mRealitySpx')?.value||'/',ss_method:$('mSsMethod')?.value||'chacha20-ietf-poly1305',ss_password:$('mSsPassword')?.value||''};
  try{if(uid) await api(`/api/links/${uid}`,{method:'PATCH',body:JSON.stringify(body)});else await api('/api/links',{method:'POST',body:JSON.stringify(body)});toast(uid?'اینباند بروزرسانی شد':'اینباند با موفقیت ساخته شد');closeDrawer();loadLinks();}
  catch(e){toast(e.message||'خطا در ذخیره اینباند',false)}
}

// ============================================================
// CATEGORIES
// ============================================================
async function loadCategories(){
  try{
    const res = await api('/api/categories');
    CATEGORIES = res.categories||[];
    $('catsBody').innerHTML = CATEGORIES.map(c=>`
      <tr><td>${escapeHtml(c.name)}</td><td>${c.limit_bytes?fmtBytes(c.limit_bytes):'نامحدود'}</td>
      <td>${c.expires_days||'—'}</td><td>${c.ip_limit||'—'}</td>
      <td><div class="row-actions">
        <button class="iconbtn" onclick="openCategoryDrawer('${c.id}')"><i class="ti ti-pencil"></i></button>
        ${['0','1'].includes(String(c.id))?'':`<button class="iconbtn" onclick="deleteCategory('${c.id}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button>`}
      </div></td></tr>
    `).join('') || `<tr><td colspan="5" class="empty">دسته‌بندی‌ای وجود ندارد</td></tr>`;
  }catch(e){ toast(e.message, false); }
}
function openCategoryDrawer(cid){
  const editing = !!cid;
  const c = editing ? CATEGORIES.find(x=>String(x.id)===String(cid)) : {};
  openDrawer(editing?'ویرایش دسته':'دسته جدید', `
    <div class="grp"><label>نام</label><input id="cName" value="${escapeHtml(c.name||'')}"></div>
    <div class="row2">
      <div class="grp"><label>حجم پیش‌فرض (GB)</label><input id="cLimit" type="number" min="0" value="${c.limit_bytes?Math.round(c.limit_bytes/1073741824):''}"></div>
      <div class="grp"><label>انقضا (روز)</label><input id="cDays" type="number" min="0" value="${c.expires_days||''}"></div>
    </div>
    <div class="grp"><label>محدودیت IP</label><input id="cIp" type="number" min="0" value="${c.ip_limit||''}"></div>
  `, `<button class="btn primary" style="flex:1" onclick="submitCategory('${cid||''}')"><i class="ti ti-device-floppy"></i>ذخیره</button>`);
}
async function submitCategory(cid){
  const body = {name:$('cName').value, limit_value:$('cLimit').value||0, limit_unit:'GB', expires_days:$('cDays').value||0, ip_limit:$('cIp').value||0};
  try{
    if(cid){ await api(`/api/categories/${cid}`, {method:'PATCH', body:JSON.stringify(body)}); }
    else{ await api('/api/categories', {method:'POST', body:JSON.stringify(body)}); }
    toast('ذخیره شد'); closeDrawer(); loadCategories();
  }catch(e){ toast(e.message, false); }
}
async function deleteCategory(cid){
  if(!confirm(t('این دسته حذف شود؟'))) return;
  try{ await api(`/api/categories/${cid}`, {method:'DELETE'}); toast('حذف شد'); loadCategories(); }
  catch(e){ toast(e.message, false); }
}

// ============================================================
// SUB GROUPS
// ============================================================
async function loadSubGroups(){
  try{
    const res = await api('/api/subs');
    const subs = res.subs || [];
    $('nb-subs').textContent = subs.length;
    $('subsBody').innerHTML = subs.map(s=>`
      <tr><td>${escapeHtml(s.name||'—')}</td><td>${s.links_count||0}</td>
      <td class="mono">${escapeHtml(s.sub_url||'')}</td>
      <td><div class="row-actions"><button class="iconbtn" onclick="deleteSubGroup('${s.sub_id}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button></div></td></tr>
    `).join('') || `<tr><td colspan="4" class="empty">گروهی وجود ندارد</td></tr>`;
  }catch(e){ $('subsBody').innerHTML = `<tr><td colspan="4" class="empty">در دسترس نیست</td></tr>`; }
}
function openSubGroupDrawer(){
  openDrawer('گروه ساب جدید', `<div class="grp"><label>نام گروه</label><input id="sgName" placeholder="مثلاً: بسته-VIP"></div>
  <p class="hint">بعد از ساخت گروه، از صفحه‌ی کانفیگ‌ها می‌توانید کانفیگ‌ها را به این گروه اضافه کنید.</p>`,
  `<button class="btn primary" style="flex:1" onclick="submitSubGroup()"><i class="ti ti-device-floppy"></i>ساخت</button>`);
}
async function submitSubGroup(){
  try{ await api('/api/subs', {method:'POST', body: JSON.stringify({name: $('sgName').value})}); toast('ساخته شد'); closeDrawer(); loadSubGroups(); }
  catch(e){ toast(e.message, false); }
}
async function deleteSubGroup(id){
  if(!confirm(t('این گروه حذف شود؟'))) return;
  try{ await api(`/api/subs/${id}`, {method:'DELETE'}); toast('حذف شد'); loadSubGroups(); }
  catch(e){ toast(e.message, false); }
}

// ============================================================
// PLANS
// ============================================================
async function loadPlans(){
  try{
    const res = await api('/api/plans');
    const plans = res.plans||[];
    $('plansBody').innerHTML = plans.map(p=>`
      <tr><td>${escapeHtml(p.name)}</td><td>${p.days} روز</td><td>${p.volume_gb} GB</td><td>${p.speed_mbps||0} Mbps</td>
      <td>⭐ ${p.stars}</td><td>${p.featured?'<span class="badge green">بله</span>':'—'}</td>
      <td><div class="row-actions">
        <button class="iconbtn" onclick="openPlanDrawer('${p.id}')"><i class="ti ti-pencil"></i></button>
        <button class="iconbtn" onclick="deletePlan('${p.id}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button>
      </div></td></tr>
    `).join('') || `<tr><td colspan="7" class="empty">پلنی وجود ندارد</td></tr>`;
  }catch(e){ toast(e.message, false); }
}
function openPlanDrawer(pid){
  openDrawer(pid?'ویرایش پلن':'پلن جدید', `
    <div class="grp"><label>نام</label><input id="pName"></div>
    <div class="row2"><div class="grp"><label>مدت (روز)</label><input id="pDays" type="number" value="30"></div>
    <div class="grp"><label>حجم (GB)</label><input id="pVolume" type="number" value="50"></div></div>
    <div class="row2"><div class="grp"><label>سرعت (Mbps، 0=نامحدود)</label><input id="pSpeed" type="number" value="0"></div>
    <div class="grp"><label>قیمت (Stars)</label><input id="pStars" type="number" value="99"></div></div>
    <label class="chk"><input type="checkbox" id="pFeatured"> پیشنهاد ویژه</label>
  `, `<button class="btn primary" style="flex:1" onclick="submitPlan('${pid||''}')"><i class="ti ti-device-floppy"></i>ذخیره</button>`);
}
async function submitPlan(pid){
  const body = {name:$('pName').value, days:$('pDays').value, volume_gb:$('pVolume').value, speed_mbps:$('pSpeed').value, stars:$('pStars').value, featured:$('pFeatured').checked};
  try{
    if(pid){ await api(`/api/plans/${pid}`, {method:'PATCH', body:JSON.stringify(body)}); }
    else{ await api('/api/plans', {method:'POST', body:JSON.stringify(body)}); }
    toast('ذخیره شد'); closeDrawer(); loadPlans();
  }catch(e){ toast(e.message, false); }
}
async function deletePlan(pid){
  if(!confirm(t('این پلن حذف شود؟'))) return;
  try{ await api(`/api/plans/${pid}`, {method:'DELETE'}); toast('حذف شد'); loadPlans(); }
  catch(e){ toast(e.message, false); }
}

// ============================================================
// REPORTS
// ============================================================
async function loadReports(){
  try{
    const days = $('repDays').value;
    const res = await api(`/api/reports/summary?days=${days}`);
    const t = res.totals||{};
    $('repStats').innerHTML = `
      ${statCard('ti-link','#4f7cff', t.links, 'کل کانفیگ‌ها')}
      ${statCard('ti-shopping-cart','#22c58b', t.orders, 'تعداد سفارش')}
      ${statCard('ti-star','#f5a524', t.stars, 'مجموع ⭐ فروش')}
      ${statCard('ti-users','#4f7cff', t.customers, 'مشتری‌ها')}
    `;
    $('repTopBody').innerHTML = (res.top_links||[]).map(l=>`
      <tr><td>${escapeHtml(l.label)}</td><td><span class="badge gray">${protoLabel(l)}</span></td><td class="mono">${fmtBytes(l.used_bytes)}</td></tr>
    `).join('') || `<tr><td colspan="3" class="empty">داده‌ای موجود نیست</td></tr>`;
  }catch(e){ toast(e.message, false); }
}

// ============================================================
// ADMINS
// ============================================================
const ADMIN_PERM_LABELS = {dashboard:'داشبورد',inbounds:'اینباند و کلاینت',clients:'ساخت کلاینت (بخش جدا)',subscriptions:'سابسکریپشن',categories:'دسته‌بندی',plans:'پلن فروش',reports:'گزارش‌ها',messages:'پیام‌ها و خطاها',bot:'ربات',admins:'مدیریت حساب',settings:'تنظیمات'};
async function loadAdmins(){
  try{
    const res = await api('/api/admins');
    ADMIN_CACHE = res.admins || [];
    const adminRows = res.admins || [];
    const activeAdmins = adminRows.filter(a=>a.active).length;
    if($('adminTotal')) $('adminTotal').textContent = adminRows.length;
    if($('adminActive')) $('adminActive').textContent = activeAdmins;
    $('adminsBody').innerHTML = adminRows.map(a=>{
      const isOwner = a.role==='owner';
      const initials = (a.username||'?').replace(/[^A-Za-z0-9آ-ی]/g,'').slice(0,2).toUpperCase() || '?';
      const lastLogin = a.last_login_at ? a.last_login_at.slice(0,16).replace('T',' ') : 'بدون ورود';
      const chips = isOwner
        ? '<span class="admin-perm-chip all"><i class="ti ti-shield-star"></i> دسترسی کامل</span>'
        : ((a.permissions||[]).length
            ? (a.permissions||[]).map(p=>`<span class="admin-perm-chip">${ADMIN_PERM_LABELS[p]||p}</span>`).join('')
            : '<span class="admin-perm-chip">بدون دسترسی</span>');
      const actions = isOwner ? '' : `
        <button class="iconbtn edit" title="ویرایش دسترسی" aria-label="ویرایش دسترسی" onclick="editAdmin('${a.id}')"><i class="ti ti-edit"></i></button>
        <button class="iconbtn power" title="${a.active?'غیرفعال‌سازی':'فعال‌سازی'}" onclick="toggleAdmin('${a.id}', ${!a.active})"><i class="ti ti-power"></i></button>
        <button class="iconbtn danger" title="حذف ادمین" aria-label="حذف ادمین" onclick="deleteAdmin('${a.id}')"><i class="ti ti-trash" style="color:var(--bad)"></i></button>`;
      return `
      <div class="admin-card ${isOwner?'is-owner':''} ${a.active?'':'is-inactive'}">
        <div class="admin-card-top">
          <div class="admin-id">
            <div class="admin-avatar">${escapeHtml(initials)}</div>
            <div class="admin-meta">
              <div class="admin-name">${escapeHtml(a.username)}</div>
              <div class="admin-sub"><span class="admin-status-dot"></span>${a.active?'فعال':'غیرفعال'}</div>
            </div>
          </div>
          <span class="admin-role-badge ${isOwner?'owner':'admin'}"><i class="ti ti-${isOwner?'crown':'shield-check'}"></i>${isOwner?'مالک':'ادمین'}</span>
        </div>
        <div class="admin-perm-row">${chips}</div>
        <div class="admin-card-foot">
          <div class="admin-login-block"><span class="admin-login-label">آخرین فعالیت</span><span class="admin-login mono"><i class="ti ti-clock"></i> ${escapeHtml(lastLogin)}</span></div>
          <div class="row-actions"><span class="admin-actions-label">کنترل حساب</span>${actions}</div>
        </div>
      </div>`;
    }).join('');
  }catch(e){ toast(e.message, false); }
}
function openAdminDrawer(){
  openDrawer('ادمین جدید', `
    <div class="grp"><label>نام کاربری</label><input id="aUser"></div>
    <div class="grp"><label>رمز عبور</label><input type="password" id="aPass"></div>
    <div class="perm-grid">${Object.entries({dashboard:'داشبورد',inbounds:'ساخت و مدیریت اینباند',clients:'ساخت کلاینت (بخش جدا)',subscriptions:'سابسکریپشن',categories:'دسته‌بندی',plans:'پلن فروش',reports:'گزارش‌ها',messages:'پیام‌ها و خطاها',bot:'ربات',admins:'مدیریت حساب',settings:'تنظیمات'}).map(([k,v])=>`<label class="perm-item"><input type="checkbox" data-perm="${k}" ${['dashboard','inbounds','subscriptions'].includes(k)?'checked':''}>${v}</label>`).join('')}</div>
  `, `<button class="btn primary" style="flex:1" onclick="submitAdmin()"><i class="ti ti-device-floppy"></i>ساخت</button>`);
}
function editAdmin(id){
  const a = ADMIN_CACHE.find(x=>x.id===id); if(!a || a.role==='owner') return;
  const perms=['dashboard','inbounds','clients','subscriptions','categories','plans','reports','messages','bot','admins','settings'];
  const labels={dashboard:'داشبورد',inbounds:'اینباند و کلاینت',clients:'ساخت کلاینت (بخش جدا)',subscriptions:'سابسکریپشن',categories:'دسته‌بندی',plans:'پلن فروش',reports:'گزارش‌ها',messages:'پیام‌ها و خطاها',bot:'ربات',admins:'مدیریت حساب',settings:'تنظیمات'};
  openDrawer('ویرایش ادمین', `
    <div class="grp"><label>نام کاربری</label><input id="eUser" value="${escapeHtml(a.username||'')}"></div>
    <div class="grp"><label>رمز جدید <small>(اختیاری)</small></label><input type="password" id="ePass" placeholder="بدون تغییر خالی بگذار"></div>
    <div class="perm-grid">${perms.map(k=>`<label class="perm-item"><input type="checkbox" data-eperm="${k}" ${((a.permissions||[]).includes(k)?'checked':'')}>${labels[k]}</label>`).join('')}</div>
  `, `<button class="btn primary" style="flex:1" onclick="saveAdminEdit('${a.id}')"><i class="ti ti-device-floppy"></i>ذخیره تغییرات</button>`);
}
async function saveAdminEdit(id){
  try{ const permissions=[...document.querySelectorAll('[data-eperm]:checked')].map(x=>x.dataset.eperm); const body={username:$('eUser').value.trim(),permissions}; if($('ePass').value) body.password=$('ePass').value; await api(`/api/admins/${id}`,{method:'PATCH',body:JSON.stringify(body)}); toast('اطلاعات ادمین بروزرسانی شد ✓'); closeDrawer(); loadAdmins(); }catch(e){toast(e.message,false)}
}

async function submitAdmin(){
  try{ await api('/api/admins', {method:'POST', body: JSON.stringify({username:$('aUser').value, password:$('aPass').value, permissions:[...document.querySelectorAll('[data-perm]:checked')].map(x=>x.dataset.perm)})}); toast('ساخته شد'); closeDrawer(); loadAdmins(); }
  catch(e){ toast(e.message, false); }
}
async function toggleAdmin(id, active){
  try{ await api(`/api/admins/${id}`, {method:'PATCH', body:JSON.stringify({active})}); loadAdmins(); }
  catch(e){ toast(e.message, false); }
}
async function deleteAdmin(id){
  if(!confirm(t('این ادمین حذف شود؟'))) return;
  try{ await api(`/api/admins/${id}`, {method:'DELETE'}); toast('حذف شد'); loadAdmins(); }
  catch(e){ toast(e.message, false); }
}

// ============================================================
// Admin registration requests
// ============================================================
let ADMIN_REQ_CACHE = [];
async function loadAdminRequests(){
  try{
    const res = await api('/api/admin-requests');
    ADMIN_REQ_CACHE = res.requests || [];
    const card = $('adminReqCard');
    const pending = ADMIN_REQ_CACHE.filter(r=>r.status==='pending');
    $('adminReqBadge').textContent = pending.length + ' درخواست';
    if(!ADMIN_REQ_CACHE.length){ card.style.display='none'; return; }
    card.style.display = '';
    const rows = [...pending, ...ADMIN_REQ_CACHE.filter(r=>r.status!=='pending')].slice(0, 30);
    $('adminReqBody').innerHTML = rows.length ? rows.map(r=>{
      const date = r.created_at ? r.created_at.slice(0,16).replace('T',' ') : '';
      let statusHtml = '';
      let actions = '';
      if(r.status==='pending'){
        actions = `<button class="btn primary" style="padding:8px 12px;font-size:11px" onclick="approveAdminReq('${r.id}')"><i class="ti ti-check"></i>تایید و ساخت ادمین</button>
                   <button class="btn" style="padding:8px 12px;font-size:11px" onclick="rejectAdminReq('${r.id}')"><i class="ti ti-x"></i>رد</button>`;
      } else {
        statusHtml = `<span class="areq-status ${r.status}">${r.status==='approved'?'تایید شده':'رد شده'}</span>`;
      }
      return `<div class="areq-row">
        <div class="areq-info">
          <div class="areq-name">${escapeHtml(r.full_name||'-')}</div>
          <div class="areq-meta"><span><i class="ti ti-brand-telegram"></i>@${escapeHtml(r.telegram_id||'-')}</span><span><i class="ti ti-clock"></i>${escapeHtml(date)}</span></div>
          ${r.note ? `<div class="areq-note">${escapeHtml(r.note)}</div>` : ''}
        </div>
        <div class="areq-actions">${actions}${statusHtml}</div>
      </div>`;
    }).join('') : `<div class="areq-empty">درخواستی ثبت نشده است</div>`;
  }catch(e){ /* silent: پنل قدیمی‌تر ممکنه این endpoint رو نداشته باشه */ }
}
function approveAdminReq(id){
  const r = ADMIN_REQ_CACHE.find(x=>x.id===id); if(!r) return;
  const suggestedUser = (r.telegram_id||'admin').replace(/[^A-Za-z0-9_]/g,'').toLowerCase() || 'admin';
  openDrawer('تایید ادمین: ' + r.full_name, `
    <div class="grp"><label>درخواست‌کننده</label><input value="${escapeHtml(r.full_name)} (@${escapeHtml(r.telegram_id)})" disabled></div>
    <div class="grp"><label>نام کاربری</label><input id="arUser" value="${escapeHtml(suggestedUser)}"></div>
    <div class="grp"><label>رمز عبور</label><input id="arPass" value="${Math.random().toString(36).slice(-8)}"></div>
    <div class="grp"><label>شارژ اولیه (استارز)</label><input id="arCredit" type="number" min="0" value="0"></div>
    <div class="perm-grid">${Object.entries({dashboard:'داشبورد',inbounds:'ساخت و مدیریت اینباند',clients:'ساخت کلاینت (بخش جدا)',subscriptions:'سابسکریپشن',categories:'دسته‌بندی',plans:'پلن فروش',reports:'گزارش‌ها',messages:'پیام‌ها و خطاها',bot:'ربات',admins:'مدیریت حساب',settings:'تنظیمات'}).map(([k,v])=>`<label class="perm-item"><input type="checkbox" data-arperm="${k}" ${['dashboard','inbounds','subscriptions'].includes(k)?'checked':''}>${v}</label>`).join('')}</div>
  `, `<button class="btn primary" style="flex:1" onclick="confirmApproveAdminReq('${r.id}')"><i class="ti ti-check"></i>تایید و ساخت حساب</button>`);
}
async function confirmApproveAdminReq(id){
  try{
    const permissions=[...document.querySelectorAll('[data-arperm]:checked')].map(x=>x.dataset.arperm);
    const body={
      username: $('arUser').value.trim(),
      password: $('arPass').value,
      permissions,
      credit_stars: Number($('arCredit').value)||0,
    };
    const res = await api(`/api/admin-requests/${id}/approve`, {method:'POST', body: JSON.stringify(body)});
    closeDrawer();
    const msg = res.delivery_message || '';
    openDrawer('اطلاعات ورود ادمین', `
      <p style="font-size:11.5px;color:var(--sub);line-height:1.9">این متن را برای <b>@${escapeHtml(res.telegram_id||'')}</b> در تلگرام ارسال کن:</p>
      <textarea id="arDeliveryMsg" readonly style="width:100%;min-height:150px;background:var(--panel2);border:1px solid var(--line);color:var(--text);border-radius:12px;padding:12px;font:inherit;line-height:1.9">${escapeHtml(msg)}</textarea>
    `, `<button class="btn primary" style="flex:1" onclick="copyDeliveryMsg()"><i class="ti ti-copy"></i>کپی متن</button><button class="btn" style="flex:1" onclick="closeDrawer()">بستن</button>`);
    loadAdmins(); loadAdminRequests();
  }catch(e){ toast(e.message, false); }
}
function copyDeliveryMsg(){
  const el = document.getElementById('arDeliveryMsg');
  if(!el) return;
  el.select();
  try{ navigator.clipboard.writeText(el.value); toast('کپی شد ✓'); }catch(e){ document.execCommand('copy'); toast('کپی شد ✓'); }
}
async function rejectAdminReq(id){
  if(!confirm('این درخواست رد شود؟')) return;
  try{ await api(`/api/admin-requests/${id}/reject`, {method:'POST', body: JSON.stringify({})}); toast('درخواست رد شد'); loadAdminRequests(); }
  catch(e){ toast(e.message, false); }
}

// ============================================================
// ACTIVITY
// ============================================================
async function loadActivity(){
  try{
    const res = await api('/api/activity');
    $('activityBody').innerHTML = (res.logs||[]).slice().reverse().map(l=>`
      <tr><td class="mono">${(l.time||l.ts||'').toString().slice(0,16).replace('T',' ')}</td>
      <td><span class="badge ${l.level==='err'?'red':l.level==='warn'?'orange':'green'}">${l.type||l.kind||'—'}</span></td>
      <td>${escapeHtml(l.message||l.text||'')}</td></tr>
    `).join('') || `<tr><td colspan="3" class="empty">لاگی وجود ندارد</td></tr>`;
  }catch(e){ toast(e.message, false); }
}

// ============================================================
// MESSAGE CENTER
// ============================================================
function setMessageFilter(filter){
  MESSAGE_FILTER=filter;
  document.querySelectorAll('[data-message-filter]').forEach(b=>b.classList.toggle('on',b.dataset.messageFilter===filter));
  loadMessages();
}
function messageIcon(level, source){
  if(source==='client') return 'browser';
  if(level==='warn') return 'alert-triangle';
  if(level==='err') return 'alert-circle';
  return 'info-circle';
}
async function clearErrors(){
  if(!confirm(t('همه خطاهای ثبت‌شده پاک شوند؟'))) return;
  try{await api('/api/errors/clear',{method:'POST'});toast('خطاها پاک شدند ✓');loadMessages();}
  catch(e){toast(e.message,false);}
}
async function loadMessages(){
  try{
    const [er,act]=await Promise.all([api('/api/errors'),api('/api/activity')]);
    const errors=(er.errors||[]).slice().reverse();
    const filtered=errors.filter(x=>MESSAGE_FILTER==='all' || x.level===MESSAGE_FILTER || x.source===MESSAGE_FILTER);
    $('messageStats').innerHTML=`
      <div class="message-stat ${er.total_errors?'danger':'good'}"><div class="ms-icon"><i class="ti ti-alert-circle"></i></div><b>${Number(er.total_errors||0)}</b><small>کل خطاهای ثبت‌شده</small></div>
      <div class="message-stat warn"><div class="ms-icon"><i class="ti ti-alert-triangle"></i></div><b>${Number(er.warnings||0)}</b><small>هشدارهای اخیر</small></div>
      <div class="message-stat"><div class="ms-icon"><i class="ti ti-browser"></i></div><b>${Number(er.client_errors||0)}</b><small>خطاهای مرورگر</small></div>
      <div class="message-stat good"><div class="ms-icon"><i class="ti ti-heartbeat"></i></div><b>${er.healthy?'OK':'CHECK'}</b><small>وضعیت سیستم</small></div>`;
    $('nb-errors').textContent=String(Math.min(99,Number(er.total_errors||0)));
    $('nb-errors').style.display=Number(er.total_errors||0)?'inline-flex':'none';
    $('messageLastSync').textContent='آخرین بروزرسانی '+new Date().toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
    $('messageList').innerHTML=filtered.length?filtered.map(x=>{
      const lvl=x.level||'err'; const src=x.source||'server';
      return `<article class="message-row ${lvl}"><div class="mi"><i class="ti ti-${messageIcon(lvl,src)}"></i></div><div class="mt"><b>${escapeHtml(x.error||x.message||'خطای نامشخص')}</b><p>${escapeHtml(src==='client'?'Frontend / Browser':(x.method||'SERVER')+' · '+(x.path||''))}</p>${x.stack||x.details?`<div class="error-detail">${escapeHtml(x.stack||x.details||'')}</div>`:''}</div><div class="meta"><strong>${escapeHtml(x.time||'—')}</strong><span>${escapeHtml(src)}</span></div></article>`;
    }).join(''):`<div class="message-empty"><i class="ti ti-shield-check"></i>خطای ثبت‌شده‌ای وجود ندارد. سیستم سالم است.</div>`;
    const logs=(act.logs||[]).slice().reverse().slice(0,25);
    $('messageActivityList').innerHTML=logs.length?logs.map(l=>`<article class="message-row ${l.level==='err'?'err':l.level==='warn'?'warn':'ok'}"><div class="mi"><i class="ti ti-${l.level==='err'?'alert-circle':l.level==='warn'?'alert-triangle':'circle-check'}"></i></div><div class="mt"><b>${escapeHtml(l.message||l.text||'')}</b><p>${escapeHtml(l.kind||l.type||'system')}</p></div><div class="meta"><strong>${escapeHtml((l.time||l.ts||'').toString().replace('T',' ').slice(0,19))}</strong></div></article>`).join(''):'<div class="message-empty">رویدادی وجود ندارد.</div>';
  }catch(e){toast(e.message,false);reportClientError(e.message,'messages',{stack:e.stack});}
}
if(messageTimer) clearInterval(messageTimer);
let messagesTimer=setInterval(()=>{if(!document.hidden && CURRENT_PAGE==='messages') loadMessages()},15000);

// ============================================================
// SETTINGS
// ============================================================
function setBotDot(running){
  $('botDot').className = 'status-dot ' + (running?'on':'off');
  $('botStatusText').textContent = running ? 'ربات در حال اجراست' : 'ربات خاموش است';
  $('botStartBtn').disabled = !!running;
  $('botStopBtn').disabled = !running;
}
async function loadSettings(){
  try{
    const s = await api('/api/settings');
    $('setBaseUrl').value = s.public_base_url || '';
    if($('adminUsername')) $('adminUsername').value = s.admin_username || '';
    $('setTcpHost').value = s.tcp_public_host || '';
    $('setTcpPort').value = s.tcp_public_port || '';
    $('tcpListenHint').textContent = `سرور TCP روی پورت داخلی ${s.tcp_listen_port} گوش می‌دهد — این را در Railway به همین پورت داخلی متصل کن، نه به PORT اصلی HTTP.`;
    $('setBotToken').value = s.bot_token || '';
    $('setBotAdmins').value = s.bot_admin_ids || '';
    setBotDot(s.bot_running);
    if($('subTplName')) $('subTplName').checked = s.sub_remark_show_name !== false;
    if($('subTplVolume')) $('subTplVolume').checked = !!s.sub_remark_show_volume;
    if($('subTplId')) $('subTplId').checked = !!s.sub_remark_show_id;
    if($('subTplInbound')) $('subTplInbound').checked = !!s.sub_remark_show_inbound;
    updateSubTemplatePreview();
    try{ const bt=await api('/api/bot/texts'); const x=bt.texts||{}; if($('botTxtWelcome'))$('botTxtWelcome').value=x.welcome||''; if($('botTxtAdmin'))$('botTxtAdmin').value=x.admin_menu||''; if($('botTxtCreated'))$('botTxtCreated').value=x.config_created||''; if($('botTxtStore'))$('botTxtStore').value=x.store_intro||''; if($('botTxtPayment'))$('botTxtPayment').value=x.payment_success||''; }catch(_){}
  }catch(e){ toast(e.message, false); }
}
function updateSubTemplatePreview(){
  const parts=[];
  if($('subTplName')?.checked) parts.push('MyConfig');
  if($('subTplVolume')?.checked) parts.push('50 GB');
  if($('subTplId')?.checked) parts.push('a1b2c3d4');
  if($('subTplInbound')?.checked) parts.push('Inbound-1');
  const el=$('subTplPreview'); if(el) el.textContent = parts.join(' | ') || 'MyConfig';
}
document.addEventListener('change', e=>{ if(['subTplName','subTplVolume','subTplId','subTplInbound'].includes(e.target?.id)) updateSubTemplatePreview(); });
async function saveSubTemplate(){
  try{
    await api('/api/settings', {method:'POST', body: JSON.stringify({
      sub_remark_show_name: !!$('subTplName')?.checked,
      sub_remark_show_volume: !!$('subTplVolume')?.checked,
      sub_remark_show_id: !!$('subTplId')?.checked,
      sub_remark_show_inbound: !!$('subTplInbound')?.checked,
    })});
    toast('الگوی نام کانفیگ‌های ساب ذخیره شد ✓');
  }catch(e){ toast(e.message, false); }
}
async function saveTcpSettings(){
  try{
    await api('/api/settings', {method:'POST', body: JSON.stringify({tcp_public_host: $('setTcpHost').value, tcp_public_port: $('setTcpPort').value})});
    toast('آدرس TCP ذخیره شد');
  }catch(e){ toast(e.message, false); }
}
async function saveBaseUrl(){
  try{ await api('/api/settings', {method:'POST', body: JSON.stringify({public_base_url: $('setBaseUrl').value})}); toast('آدرس ذخیره شد'); refreshOverview(); }
  catch(e){ toast(e.message, false); }
}
async function saveBotSettings(){
  try{
    const r = await api('/api/settings', {method:'POST', body: JSON.stringify({bot_token: $('setBotToken').value, bot_admin_ids: $('setBotAdmins').value})});
    toast(r.bot_restarted ? 'ذخیره شد و ربات با تنظیمات جدید ری‌استارت شد' : 'ذخیره شد — برای اعمال، ربات را روشن کنید');
    setBotDot(r.running);
  }catch(e){ toast(e.message, false); }
}
async function botStart(){
  try{ const r = await api('/api/settings/bot/start', {method:'POST'}); toast('ربات روشن شد'); setBotDot(r.running); }
  catch(e){ toast(e.message, false); }
}
async function botStop(){
  try{ const r = await api('/api/settings/bot/stop', {method:'POST'}); toast('ربات خاموش شد'); setBotDot(r.running); }
  catch(e){ toast(e.message, false); }
}
async function saveBotTexts(){
  try{ await api('/api/bot/texts',{method:'POST',body:JSON.stringify({texts:{welcome:$('botTxtWelcome').value,admin_menu:$('botTxtAdmin').value,config_created:$('botTxtCreated').value,store_intro:$('botTxtStore').value,payment_success:$('botTxtPayment').value}})}); toast('متن‌های ربات ذخیره شد ✓'); }catch(e){toast(e.message,false)}
}
function toggleSettingsPass(id, btn){
  const inp = $(id);
  if(!inp) return;
  const icon = btn ? btn.querySelector('i') : null;
  if(inp.type === 'password'){ inp.type = 'text'; if(icon) icon.className = 'ti ti-eye-off'; }
  else { inp.type = 'password'; if(icon) icon.className = 'ti ti-eye'; }
}
function passwordMeter(){
  const val = $('newPass') ? $('newPass').value : '';
  const bar = $('passMeterBar'), hint = $('passHint');
  if(!bar) return;
  let score = 0;
  if(val.length >= 8) score++;
  if(val.length >= 12) score++;
  if(/[a-z]/.test(val) && /[A-Z]/.test(val)) score++;
  if(/[0-9]/.test(val)) score++;
  if(/[^A-Za-z0-9]/.test(val)) score++;
  const levels = [
    {pct:4,  color:'var(--bad)',  label:'خیلی ضعیف'},
    {pct:25, color:'var(--bad)',  label:'ضعیف'},
    {pct:50, color:'var(--warn)', label:'متوسط'},
    {pct:75, color:'var(--warn)', label:'خوب'},
    {pct:100,color:'var(--good)', label:'قوی'},
    {pct:100,color:'var(--good)', label:'خیلی قوی'},
  ];
  const lv = levels[Math.min(score, levels.length-1)];
  bar.style.width = (val ? lv.pct : 0) + '%';
  bar.style.background = lv.color;
  if(hint) hint.textContent = val ? `قدرت رمز: ${lv.label} — حداقل ۸ کاراکتر، ترکیب حروف بزرگ/کوچک، عدد و نماد پیشنهاد می‌شود.` : 'حداقل ۸ کاراکتر، ترجیحاً ترکیب حروف، عدد و نماد.';
}
async function revokeOtherSessions(){
  if(!confirm(t('همه نشست‌های قبلی این حساب لغو شوند؟'))) return;
  try{const r=await api('/api/security/revoke-other-sessions',{method:'POST'});toast(`${r.revoked||0} نشست قبلی لغو شد ✓`)}catch(e){toast(e.message,false)}
}
function fmtDiagBytes(n){return fmtBytes(Number(n||0))}
async function loadDiagnostics(){
  const box=$('diagGrid'), st=$('diagStatus'); if(!box) return;
  st.textContent='CHECKING'; st.className='badge orange';
  try{
    const d=await api('/api/system/diagnostics'); const r=d.resources||{}, o=d.objects||{}, b=d.bot||{}, sec=d.security||{};
    box.innerHTML=`<div class="diag-item"><small>Service</small><b>${escapeHtml(d.service?.status||'—')}</b><span>${escapeHtml(d.uptime||'—')}</span></div><div class="diag-item"><small>CPU</small><b>${Number(r.cpu_percent||0).toFixed(1)}%</b><span>Process load</span></div><div class="diag-item"><small>Memory</small><b>${Number(r.memory_percent||0).toFixed(1)}%</b><span>${fmtDiagBytes(r.memory_rss)}</span></div><div class="diag-item"><small>Disk</small><b>${Number(r.disk_percent||0).toFixed(1)}%</b><span>Root filesystem</span></div><div class="diag-item"><small>Inbounds</small><b>${o.inbounds||0}</b><span>${o.active_links||0} active</span></div><div class="diag-item"><small>Clients</small><b>${o.clients||0}</b><span>${o.subscriptions||0} subscriptions</span></div><div class="diag-item"><small>Bot</small><b>${b.running?'ONLINE':'OFFLINE'}</b><span>${b.admin_count||0} bot admins</span></div><div class="diag-item"><small>Sessions</small><b>${sec.session_count||0}</b><span>${escapeHtml(sec.username||'—')}</span></div>`;
    st.textContent='HEALTHY'; st.className='badge green';
  }catch(e){box.innerHTML=`<div class="diag-empty">${escapeHtml(e.message||'Diagnostics unavailable')}</div>`;st.textContent='ERROR';st.className='badge red';}
}

async function changeUsername(){
  const username = ($('adminUsername')?.value || '').trim();
  if(!username){ toast('نام کاربری را وارد کنید', false); return; }
  if(username.length < 3 || username.length > 40 || /\s/.test(username)){ toast('نام کاربری باید ۳ تا ۴۰ کاراکتر و بدون فاصله باشد', false); return; }
  const btn = document.activeElement && document.activeElement.tagName === 'BUTTON' ? document.activeElement : null; const originalHtml = btn ? btn.innerHTML : '';
  if(btn){ btn.disabled=true; btn.innerHTML='<i class="ti ti-loader-2 spin"></i>در حال ذخیره...'; }
  try{
    const r = await api('/api/change-username',{method:'POST',body:JSON.stringify({username})});
    if($('userName')) $('userName').textContent=r.username;
    if($('userChip')?.querySelector('.av')) $('userChip').querySelector('.av').textContent=(r.username||'?').slice(0,1).toUpperCase();
    toast('نام کاربری با موفقیت تغییر کرد ✓');
  }catch(e){ toast(e.message,false); }
  finally{ if(btn){btn.disabled=false;btn.innerHTML=originalHtml;} }
}
async function changePassword(){
  const current_password = $('curPass').value, new_password = $('newPass').value, repeat_password = $('repPass').value;
  if(!current_password || !new_password || !repeat_password){ toast('همه‌ی فیلدهای رمز عبور را پر کنید', false); return; }
  if(new_password.length < 8){ toast('رمز جدید باید حداقل ۸ کاراکتر باشد', false); return; }
  if(new_password !== repeat_password){ toast('تکرار رمز یکسان نیست', false); return; }
  if(new_password === current_password){ toast('رمز جدید باید با رمز فعلی متفاوت باشد', false); return; }
  const btn = document.activeElement && document.activeElement.tagName === 'BUTTON' ? document.activeElement : null;
  const originalHtml = btn ? btn.innerHTML : '';
  if(btn){ btn.disabled = true; btn.innerHTML = '<i class="ti ti-loader-2 spin"></i>در حال ذخیره...'; }
  try{
    await api('/api/change-password', {method:'POST', body: JSON.stringify({current_password, new_password, repeat_password})});
    toast('رمز عبور با موفقیت تغییر کرد ✓');
    $('curPass').value=$('newPass').value=$('repPass').value='';
    passwordMeter();
  }catch(e){ toast(e.message, false); }
  finally{ if(btn){ btn.disabled = false; btn.innerHTML = originalHtml; } }
}
</script>
</body>
</html>
"""
