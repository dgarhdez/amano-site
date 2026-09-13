#!/usr/bin/env python3
"""Generate the Amano landing pages: English root + six localized folders.

One template, one strings table. Copy follows the approved App Store
metadata voice (docs/localization/app-store-metadata.json in the app repo).
Run `python3 build.py` after editing, then commit the generated files.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
BASE = "https://dgarhdez.github.io/amano-site/"
APP_ID = "6809212902"

# locale key -> (folder, html lang, hreflang, storefront path, App Store link label)
LOCALES = {
    "en": ("", "en", "en", "", "Download on the App Store"),
    "es": ("es/", "es", "es", "es/", "Descárgala en el App Store"),
    "fr": ("fr/", "fr", "fr", "fr/", "Télécharger dans l’App Store"),
    "de": ("de/", "de", "de", "de/", "Laden im App Store"),
    "it": ("it/", "it", "it", "it/", "Scarica su App Store"),
    "pt": ("pt/", "pt-PT", "pt-PT", "pt/", "Descarregar na App Store"),
    "tr": ("tr/", "tr", "tr", "tr/", "App Store’dan indir"),
}

S = {
"en": dict(
    title="Amano — Private Document Vault",
    desc="Amano is a private vault for the documents that matter — scanned, organized, renewed on time, and shared only on your terms. On your iPhone and in your iCloud. Nowhere else.",
    getapp="Get the app",
    h1="What matters, <em>close at hand.</em>",
    lede="Amano is a private vault for the documents that matter — scanned, organized, renewed on time, and shared only on your terms. On your iPhone and in your iCloud. Nowhere else.",
    ctanote="Free to start. One single payment for everything — no subscriptions, ever.",
    figcap="Thirty-five seconds: three photos become one PDF, watermarked, shared.",
    f1h="Private by design", f1p="No accounts, no servers, no tracking. Your documents stay on your device and in your own iCloud, behind Face&nbsp;ID if you want it.",
    f2h="Renewed on time", f2p="Amano reads expiry dates when you save a document and reminds you before passports, permits and policies lapse.",
    f3h="Shared on your terms", f3p="Send watermarked copies that say exactly what they are for — worthless anywhere else. Originals never change. Family folders keep shared paperwork in one place.",
    ph2="No accounts. No ads. No&nbsp;tracking.",
    pp="Amano has no servers to breach and no interest in your data. Everything lives on your iPhone and in your iCloud — private by architecture, not by promise.",
    price="Free to start &middot; one payment unlocks everything, forever",
    made="made by one person, with care", privacy="Privacy", store="App&nbsp;Store",
    videolabel="Amano turning three photos into one watermarked PDF and sharing it",
),
"es": dict(
    title="Amano — Documentos privados",
    desc="Amano es un espacio privado para los documentos que importan: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    getapp="Descargar la app",
    h1="Lo importante, <em>a mano.</em>",
    lede="Amano es un espacio privado para los documentos que importan: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    ctanote="Empieza gratis. Un solo pago para todo: sin suscripciones, nunca.",
    figcap="Treinta y cinco segundos: tres fotos se convierten en un PDF, con marca de agua, compartido.",
    f1h="Privacidad desde el principio", f1p="Sin cuentas, sin servidores, sin rastreo. Tus documentos se quedan en tu dispositivo y en tu propio iCloud, protegidos con Face&nbsp;ID si quieres.",
    f2h="Renovado a tiempo", f2p="Amano lee la fecha de caducidad al guardar un documento y te avisa antes de que caduquen pasaportes, permisos y pólizas.",
    f3h="Compartes tú, en tus términos", f3p="Envía copias con marca de agua que dicen exactamente para qué son: inútiles en cualquier otro sitio. Los originales no cambian. Las carpetas familiares reúnen el papeleo compartido en un solo lugar.",
    ph2="Sin cuentas. Sin anuncios. Sin&nbsp;rastreo.",
    pp="Amano no tiene servidores que hackear ni interés en tus datos. Todo vive en tu iPhone y en tu iCloud: privado por arquitectura, no por promesa.",
    price="Empieza gratis &middot; un solo pago lo desbloquea todo, para siempre",
    made="hecho por una persona, con cariño", privacy="Privacidad", store="App&nbsp;Store",
    videolabel="Amano convirtiendo tres fotos en un PDF con marca de agua y compartiéndolo",
),
"fr": dict(
    title="Amano — Documents privés",
    desc="Amano est un espace privé pour les documents qui comptent : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    getapp="Obtenir l’app",
    h1="L’essentiel, <em>à portée de main.</em>",
    lede="Amano est un espace privé pour les documents qui comptent : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    ctanote="Commence gratuitement. Un seul paiement pour tout — jamais d’abonnement.",
    figcap="Trente-cinq secondes : trois photos deviennent un PDF, filigrané, partagé.",
    f1h="Privé dès la conception", f1p="Pas de compte, pas de serveur, pas de pistage. Tes documents restent sur ton appareil et dans ton propre iCloud, derrière Face&nbsp;ID si tu le souhaites.",
    f2h="Renouvelé à temps", f2p="Amano lit la date d’échéance quand tu enregistres un document et te prévient avant que passeports, permis et contrats n’expirent.",
    f3h="Partagé selon tes conditions", f3p="Envoie des copies filigranées qui disent exactement à quoi elles servent — inutilisables ailleurs. Les originaux ne changent jamais. Les dossiers familiaux réunissent les papiers partagés au même endroit.",
    ph2="Pas de compte. Pas de pub. Pas de&nbsp;pistage.",
    pp="Amano n’a aucun serveur à pirater et aucun intérêt pour tes données. Tout vit sur ton iPhone et dans ton iCloud — privé par architecture, pas par promesse.",
    price="Gratuit pour commencer &middot; un seul paiement débloque tout, pour toujours",
    made="fait par une seule personne, avec soin", privacy="Confidentialité", store="App&nbsp;Store",
    videolabel="Amano transforme trois photos en un PDF filigrané et le partage",
),
"de": dict(
    title="Amano — Private Dokumente",
    desc="Amano ist ein privater Ort für die Dokumente, die zählen: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    getapp="App laden",
    h1="Alles Wichtige, <em>griffbereit.</em>",
    lede="Amano ist ein privater Ort für die Dokumente, die zählen: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    ctanote="Kostenlos starten. Einmal zahlen für alles – nie ein Abo.",
    figcap="Fünfunddreißig Sekunden: Drei Fotos werden ein PDF, mit Wasserzeichen, geteilt.",
    f1h="Privat von Grund auf", f1p="Keine Konten, keine Server, kein Tracking. Deine Dokumente bleiben auf deinem Gerät und in deiner eigenen iCloud – auf Wunsch hinter Face&nbsp;ID.",
    f2h="Rechtzeitig verlängert", f2p="Amano liest das Ablaufdatum beim Speichern und erinnert dich, bevor Reisepässe, Ausweise und Policen ablaufen.",
    f3h="Geteilt zu deinen Bedingungen", f3p="Verschicke Kopien mit Wasserzeichen, die genau sagen, wofür sie sind – überall sonst wertlos. Originale bleiben unverändert. Familienordner halten gemeinsame Unterlagen an einem Ort.",
    ph2="Keine Konten. Keine Werbung. Kein&nbsp;Tracking.",
    pp="Amano hat keine Server, die man hacken könnte, und kein Interesse an deinen Daten. Alles lebt auf deinem iPhone und in deiner iCloud – privat durch Architektur, nicht durch Versprechen.",
    price="Kostenlos starten &middot; ein Kauf schaltet alles frei, für immer",
    made="von einer Person gemacht, mit Sorgfalt", privacy="Datenschutz", store="App&nbsp;Store",
    videolabel="Amano macht aus drei Fotos ein PDF mit Wasserzeichen und teilt es",
),
"it": dict(
    title="Amano — Documenti privati",
    desc="Amano è uno spazio privato per i documenti che contano: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    getapp="Scarica l’app",
    h1="Ciò che conta, <em>a portata di mano.</em>",
    lede="Amano è uno spazio privato per i documenti che contano: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    ctanote="Inizia gratis. Un solo pagamento per tutto: mai abbonamenti.",
    figcap="Trentacinque secondi: tre foto diventano un PDF, con filigrana, condiviso.",
    f1h="Privato fin dall’inizio", f1p="Niente account, niente server, niente tracciamento. I tuoi documenti restano sul tuo dispositivo e nel tuo iCloud, dietro Face&nbsp;ID se vuoi.",
    f2h="Rinnovato in tempo", f2p="Amano legge la scadenza quando salvi un documento e ti avvisa prima che passaporti, patenti e polizze scadano.",
    f3h="Condiviso alle tue condizioni", f3p="Invia copie con filigrana che dicono esattamente a cosa servono: inutili altrove. Gli originali non cambiano. Le cartelle famiglia tengono le pratiche condivise in un unico posto.",
    ph2="Niente account. Niente pubblicità. Niente&nbsp;tracciamento.",
    pp="Amano non ha server da violare e nessun interesse per i tuoi dati. Tutto vive sul tuo iPhone e nel tuo iCloud: privato per architettura, non per promessa.",
    price="Inizia gratis &middot; un solo pagamento sblocca tutto, per sempre",
    made="fatto da una persona sola, con cura", privacy="Privacy", store="App&nbsp;Store",
    videolabel="Amano trasforma tre foto in un PDF con filigrana e lo condivide",
),
"pt": dict(
    title="Amano — Documentos privados",
    desc="O Amano é um espaço privado para os documentos que importam: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    getapp="Obter a app",
    h1="O que importa, <em>à mão.</em>",
    lede="O Amano é um espaço privado para os documentos que importam: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    ctanote="Comece grátis. Um único pagamento para tudo — sem subscrições, nunca.",
    figcap="Trinta e cinco segundos: três fotos tornam-se um PDF, com marca de água, partilhado.",
    f1h="Privado por conceção", f1p="Sem contas, sem servidores, sem rastreio. Os seus documentos ficam no seu dispositivo e no seu próprio iCloud, protegidos com Face&nbsp;ID se quiser.",
    f2h="Renovado a tempo", f2p="O Amano lê a validade quando guarda um documento e avisa antes que passaportes, cartas e apólices caduquem.",
    f3h="Partilhado nos seus termos", f3p="Envie cópias com marca de água que dizem exatamente para que servem — inúteis em qualquer outro lado. Os originais nunca mudam. As pastas de família juntam a papelada partilhada num só lugar.",
    ph2="Sem contas. Sem anúncios. Sem&nbsp;rastreio.",
    pp="O Amano não tem servidores para atacar nem interesse nos seus dados. Tudo vive no seu iPhone e no seu iCloud — privado por arquitetura, não por promessa.",
    price="Comece grátis &middot; um único pagamento desbloqueia tudo, para sempre",
    made="feito por uma pessoa, com cuidado", privacy="Privacidade", store="App&nbsp;Store",
    videolabel="O Amano transforma três fotos num PDF com marca de água e partilha-o",
),
"tr": dict(
    title="Amano — Özel Belge Kasası",
    desc="Amano, önemli belgeleriniz için özel bir kasa: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    getapp="Uygulamayı edin",
    h1="Önemli olan her şey, <em>elinizin altında.</em>",
    lede="Amano, önemli belgeleriniz için özel bir kasa: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    ctanote="Ücretsiz başlayın. Her şey için tek ödeme — asla abonelik yok.",
    figcap="Otuz beş saniye: üç fotoğraf tek bir PDF olur, filigran eklenir, paylaşılır.",
    f1h="Tasarımdan özel", f1p="Hesap yok, sunucu yok, takip yok. Belgeleriniz cihazınızda ve kendi iCloud’unuzda kalır; isterseniz Face&nbsp;ID arkasında.",
    f2h="Zamanında yenilenir", f2p="Amano bir belgeyi kaydederken son geçerlilik tarihini okur; pasaportlar, ehliyetler ve poliçeler dolmadan önce hatırlatır.",
    f3h="Sizin koşullarınızla paylaşılır", f3p="Ne için olduğunu tam olarak söyleyen filigranlı kopyalar gönderin — başka her yerde işe yaramaz. Orijinaller asla değişmez. Aile klasörleri ortak evrakı tek yerde tutar.",
    ph2="Hesap yok. Reklam yok. Takip&nbsp;yok.",
    pp="Amano’nun ele geçirilecek sunucusu ve verilerinizde gözü yok. Her şey iPhone’unuzda ve iCloud’unuzda yaşar — vaatle değil, mimariyle özel.",
    price="Ücretsiz başlayın &middot; tek ödeme her şeyi sonsuza dek açar",
    made="tek kişi tarafından, özenle yapıldı", privacy="Gizlilik", store="App&nbsp;Store",
    videolabel="Amano üç fotoğrafı filigranlı tek bir PDF’e dönüştürüp paylaşıyor",
),
}

APPLE_SVG = '<svg width="20" height="24" viewBox="0 0 20 24" fill="currentColor" aria-hidden="true"><path d="M16.6 12.8c0-3 2.4-4.4 2.5-4.5-1.4-2-3.5-2.3-4.3-2.3-1.8-.2-3.5 1.1-4.4 1.1-.9 0-2.3-1-3.8-1-2 0-3.8 1.1-4.8 2.9-2 3.5-.5 8.8 1.5 11.6 1 1.4 2.1 3 3.6 2.9 1.5-.1 2-.9 3.8-.9s2.3.9 3.8.9c1.6 0 2.6-1.4 3.5-2.8 1.1-1.6 1.6-3.2 1.6-3.3-.1-.1-3-1.2-3-4.6zM13.7 3.9c.8-1 1.4-2.4 1.2-3.9-1.2.1-2.7.8-3.5 1.9-.8.9-1.5 2.3-1.3 3.7 1.4.1 2.8-.7 3.6-1.7z"/></svg>'

STYLE = """
  :root {
    --paper: #F4F6F9; --card: #FFFFFF; --navy: #193B70; --deep: #101722;
    --ink: #1D2939; --muted: #637084; --link: #275CA5; --radius: 16px;
    --display: "Fraunces", "Iowan Old Style", Georgia, serif;
    --body: "Instrument Sans", -apple-system, "Helvetica Neue", sans-serif;
  }
  * { margin: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { background: var(--paper); color: var(--ink); font-family: var(--body);
    font-size: 17px; line-height: 1.6; -webkit-font-smoothing: antialiased; }
  .wrap { max-width: 1020px; margin: 0 auto; padding: 0 24px; }
  header.top { display: flex; align-items: center; justify-content: space-between; padding: 28px 0 0; }
  .wordmark { font-family: var(--display); font-weight: 600; font-size: 30px; color: var(--navy);
    font-variation-settings: "opsz" 72, "SOFT" 100; letter-spacing: 0.01em; text-decoration: none; }
  .top a.store-mini { font-weight: 600; font-size: 15px; color: var(--link);
    text-decoration: none; padding: 10px 16px; border-radius: 999px; }
  .top a.store-mini:hover { background: var(--card); }
  .hero { padding: 88px 0 40px; text-align: center; }
  .hero h1 { font-family: var(--display); font-variation-settings: "opsz" 72, "SOFT" 100;
    font-weight: 560; font-size: clamp(42px, 7vw, 74px); line-height: 1.06;
    color: var(--ink); text-wrap: balance; letter-spacing: -0.01em; }
  .hero h1 em { font-style: normal; color: var(--navy); }
  .hero p.lede { max-width: 34em; margin: 26px auto 0;
    font-size: clamp(17px, 2.2vw, 20px); color: var(--muted); text-wrap: pretty; }
  .cta-row { margin-top: 38px; display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; align-items: center; }
  .store-button { display: inline-flex; align-items: center; gap: 10px;
    background: var(--navy); color: #fff; text-decoration: none; font-weight: 600; font-size: 17px;
    padding: 15px 26px; border-radius: 14px; transition: transform 120ms ease, box-shadow 120ms ease;
    box-shadow: 0 10px 28px rgba(25, 59, 112, 0.28); }
  .store-button:hover { transform: translateY(-1px); box-shadow: 0 14px 34px rgba(25, 59, 112, 0.34); }
  .store-button:focus-visible, a:focus-visible { outline: 3px solid var(--link); outline-offset: 3px; }
  .store-button svg { flex: none; }
  .cta-note { font-size: 14px; color: var(--muted); width: 100%; margin-top: 4px; }
  .demo { padding: 44px 0 20px; }
  .demo figure { max-width: 560px; margin: 0 auto; border-radius: 24px; overflow: hidden;
    box-shadow: 0 30px 70px rgba(16, 23, 34, 0.16); background: var(--paper); }
  .demo video { display: block; width: 100%; height: auto; }
  .demo figcaption { text-align: center; font-size: 14px; color: var(--muted);
    padding: 14px 16px 16px; background: var(--card); }
  section.features { padding: 84px 0 30px; }
  .features .grid { display: grid; gap: 18px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
  .feature { background: var(--card); border-radius: var(--radius); padding: 30px 28px 32px; }
  .feature .glyph { width: 44px; height: 44px; border-radius: 12px; background: rgba(25, 59, 112, 0.08);
    display: grid; place-items: center; margin-bottom: 18px; color: var(--navy); }
  .feature h3 { font-family: var(--display); font-variation-settings: "opsz" 40, "SOFT" 100;
    font-weight: 600; font-size: 23px; color: var(--ink); margin-bottom: 8px; }
  .feature p { color: var(--muted); font-size: 16px; text-wrap: pretty; }
  section.promise { margin: 84px 0 0; background: var(--deep); color: #EEF2F8; }
  .promise .inner { padding: 88px 24px; text-align: center; max-width: 760px; margin: 0 auto; }
  .promise h2 { font-family: var(--display); font-variation-settings: "opsz" 72, "SOFT" 100;
    font-weight: 560; font-size: clamp(30px, 4.6vw, 46px); line-height: 1.15; text-wrap: balance; color: #F4F6F9; }
  .promise p { margin-top: 20px; color: #ABB7C8; font-size: 18px; max-width: 36em; margin-left: auto; margin-right: auto; }
  .promise .price { margin-top: 34px; display: inline-block; border: 1px solid rgba(244, 246, 249, 0.25);
    border-radius: 999px; padding: 10px 22px; font-size: 15px; font-weight: 500; color: #F4F6F9; }
  footer { background: var(--deep); color: #ABB7C8; padding: 26px 0 46px; font-size: 14px; }
  footer .wrap { display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap;
    align-items: baseline; border-top: 1px solid rgba(244,246,249,0.12); padding-top: 26px; }
  footer a { color: #EEF2F8; text-decoration: none; margin-left: 18px; }
  footer a:hover { text-decoration: underline; }
  footer .langs { width: 100%; margin-top: 14px; }
  footer .langs a { margin: 0 12px 0 0; color: #8FA0B8; font-size: 13px; }
  footer .langs span { color: #F4F6F9; font-size: 13px; margin-right: 12px; }
  @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } .store-button { transition: none; } }
"""

GLYPH1 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>'
GLYPH2 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4M12 13v4M10 15h4"/></svg>'
GLYPH3 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 15V4M8 7l4-3.5L16 7"/><rect x="5" y="11" width="14" height="9" rx="2"/></svg>'

LANG_NAMES = {"en": "English", "es": "Español", "fr": "Français", "de": "Deutsch",
              "it": "Italiano", "pt": "Português", "tr": "Türkçe"}

def hreflang_links():
    lines = []
    for key, (folder, _, hreflang, _, _) in LOCALES.items():
        lines.append(f'<link rel="alternate" hreflang="{hreflang}" href="{BASE}{folder}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}">')
    return "\n".join(lines)

def lang_switcher(current):
    parts = []
    for key, (folder, _, _, _, _) in LOCALES.items():
        name = LANG_NAMES[key]
        if key == current:
            parts.append(f"<span>{name}</span>")
        else:
            parts.append(f'<a href="{BASE}{folder}" lang="{LOCALES[key][1]}">{name}</a>')
    return '<span class="langs">' + "".join(parts) + "</span>"

def page(key):
    folder, lang, _, storefront, badge = LOCALES[key]
    s = S[key]
    root = "../" if folder else "./"
    canon = BASE + folder
    store = f"https://apps.apple.com/{storefront}app/id{APP_ID}"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['desc']}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="canonical" href="{canon}">
{hreflang_links()}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Amano">
<meta property="og:title" content="{s['title']}">
<meta property="og:description" content="{s['desc']}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..650,100&family=Instrument+Sans:wght@400;500;600&display=swap">
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="wordmark" href="{canon}">amano</a>
    <a class="store-mini" href="{store}">{s['getapp']}</a>
  </header>
  <section class="hero">
    <h1>{s['h1']}</h1>
    <p class="lede">{s['lede']}</p>
    <div class="cta-row">
      <a class="store-button" href="{store}">{APPLE_SVG}{badge}</a>
      <span class="cta-note">{s['ctanote']}</span>
    </div>
  </section>
  <section class="demo">
    <figure>
      <video src="{root}assets/demo.mp4" poster="{root}assets/poster.jpg" muted loop playsinline controls preload="metadata" aria-label="{s['videolabel']}"></video>
      <figcaption>{s['figcap']}</figcaption>
    </figure>
  </section>
  <section class="features">
    <div class="grid">
      <article class="feature"><div class="glyph">{GLYPH1}</div><h3>{s['f1h']}</h3><p>{s['f1p']}</p></article>
      <article class="feature"><div class="glyph">{GLYPH2}</div><h3>{s['f2h']}</h3><p>{s['f2p']}</p></article>
      <article class="feature"><div class="glyph">{GLYPH3}</div><h3>{s['f3h']}</h3><p>{s['f3p']}</p></article>
    </div>
  </section>
</div>
<section class="promise">
  <div class="inner">
    <h2>{s['ph2']}</h2>
    <p>{s['pp']}</p>
    <span class="price">{s['price']}</span>
  </div>
</section>
<footer>
  <div class="wrap">
    <span>&copy; 2026 Amano &middot; {s['made']}</span>
    <span>
      <a href="{BASE}privacy/">{s['privacy']}</a>
      <a href="{store}">{s['store']}</a>
    </span>
    {lang_switcher(key)}
  </div>
</footer>
</body>
</html>
"""

urls = []
for key, (folder, _, _, _, _) in LOCALES.items():
    dest = ROOT / folder / "index.html" if folder else ROOT / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page(key))
    urls.append(BASE + folder)
    print("wrote", dest.relative_to(ROOT))

for extra in ["privacy/", "terms/", "support/"]:
    urls.append(BASE + extra)
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
sitemap += "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
print("wrote sitemap.xml, robots.txt")
