#!/usr/bin/env python3
"""Generate the Amano landing pages: English root + six localized folders.

One template, one strings table. Copy follows the approved App Store
metadata voice (docs/localization/app-store-metadata.json in the app repo).
Run `python3 build.py` after editing, then commit the generated files.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
BASE = "https://getamano.app/"
APP_ID = "6809212902"
PROVIDER_TOKEN = "128749840"

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
    lede="Your documents, ready when you need them. Scan once, find them quickly, and keep expiry dates, copies and family paperwork in one place.",
    ctanote="Try every feature free for 7 days. Then pay <strong>€7.99</strong> once (price may vary by country) to unlock it for life. Check your price in the app. No subscription or automatic charge.",
    figcap="Thirty-five seconds: three photos become one PDF, watermarked, shared.",
    f1h="Private by design", f1p="No Amano account needed. Keep your documents on your iPhone, protect access with Face&nbsp;ID, and enable personal iCloud backup if you want it.",
    f2h="Keep track of renewal dates", f2p="Amano looks for expiry dates when you save a document. Check the suggested date and set a reminder for your passport, permit or policy.",
    f3h="Sign it on your phone", f3p="Draw or type your signature, place it on the page, and send a signed copy. The original stays untouched.",
    f4h="Watermark every copy", f4p="Mark a copy with its recipient and purpose: “For the gym”, “Rental only”. Your original stays unchanged.",
    f5h="Many files, one PDF", f5p="Photos and PDFs become one ordered document — contracts, receipts, school forms — ready to share.",
    f6h="Review before you share", f6p="Choose the pages and files to include, check your watermark or signature, then share the copy. Your original stays unchanged.",
    ph2="Your documents stay yours.",
    pp="Your document contents stay on your device or in your own iCloud. RevenueCat processes purchase information to unlock Unlimited, restore purchases and measure sales. Apple Ads attribution helps measure ad performance.",
    price="7 days free &middot; €7.99 once (price may vary by country) &middot; no subscription",
    made="made by M&amp;D in Madrid", privacy="Privacy", terms="Terms", support="Support", review="Write a review", heroalt="Amano document vault with private folders and search on iPhone", tagfree="Included in your 7-day trial", tagunl="Included in your 7-day trial", alsoh="Also in Amano", freeh="Copy key details without retyping", freep="Extract useful details from a document, then copy one item or everything at once. Check the results against the original before using them. Requires a supported iPhone with Apple Intelligence enabled and its on-device model downloaded and ready.", store="App&nbsp;Store",
    videolabel="Amano turning three photos into one watermarked PDF and sharing it",
    shotsh2="A look inside",
    shotsalt=["Renewals screen reminding about an expiring passport", "Placing a signature on a document page", "Reviewing a watermarked copy before sharing"],
    shotcaps=["Confirm the expiry date Amano finds. Set a reminder to renew.", "Draw or type your signature, place it on the page, and share a signed copy.", "Review the copy before sharing. Your original stays unchanged."],
    faqh2="Questions, answered",
    faq=[
        ("How does the free trial work?", "New customers can try every feature for seven days, with no document or folder limits. Smart extraction requires a supported device with Apple Intelligence enabled and its on-device model ready. After the trial, choose a one-time purchase to keep full access. No subscription and no automatic charge."),
        ("What happens when my trial ends?", "You can still view your saved documents and export plain copies, without signatures or watermarks added by Amano. You can also copy details already extracted from your documents. A one-time purchase unlocks adding documents and using the full set of features again."),
        ("Can I buy before the trial ends?", "Yes. You can unlock Amano at any time during your trial. Pay once for permanent full access, with no subscription."),
        ("What if I already had Amano?", "Customers who first downloaded Amano before the seven-day-trial release keep full access forever, at no extra cost. This includes existing free customers. Existing purchases remain valid."),
        ("Where are my documents stored?", "On your iPhone, encrypted — and, if you turn on sync, in your own iCloud."),
        ("What happens if I lose my phone?", "With iCloud sync on (part of Unlimited), your vault is waiting on your next iPhone. Without it, documents live only on the device — that is the trade-off of fully local storage."),
        ("What does the one-time purchase unlock?", "Permanent full access: unlimited documents and private folders, watermarked or signed copies, renewal reminders, personal iCloud backup, document kits and Home Screen widgets. Smart extraction is included on supported devices with Apple Intelligence enabled and its on-device model ready. The app shows your local price before you buy."),
        ("Do I need to create an account?", "No. Amano works the moment you open it. There is nothing to sign up for."),
    ],
    painh2="Sound familiar?",
    pains=[
        ("&ldquo;Where&rsquo;s the passport?&rdquo;",
         "At a counter, scrolling months of camera roll for a document you know you photographed. In Amano it&rsquo;s one search away — behind Face&nbsp;ID, in folders that make sense."),
        ("&ldquo;It expired last month.&rdquo;",
         "Check the expiry date Amano suggests when you save, then set an advance reminder for your ID, policy or permit."),
        ("&ldquo;I emailed my ID&hellip; who has it now?&rdquo;",
         "Add a visible purpose to the copy you share, such as &ldquo;rental application only&rdquo;. Your original stays unchanged."),
    ],
    priceh2="Try it for a week. Keep it with one payment.",
    freecolh="7-day free trial", unlcolh="Amano forever",
    pricefree=["Every feature for seven days", "Unlimited documents and private folders", "Watermarked and signed copies", "No automatic charge"],
    pricenum="€7.99", priceonce="One payment. Permanent full access.",
    priceunl=["Unlimited scanning and document storage", "Watermarked and signed copies", "Renewal reminders", "Personal iCloud backup", "Kits and Home Screen widgets", "Smart extraction on supported devices"],
    pricenote="Buy at any time, during or after your trial. Your local price is shown in the app before purchase. No subscription. After the trial, saved documents remain viewable and exportable as plain copies, without signatures or watermarks added by Amano.",
    scanh="Scan it once. Find it forever.",
    scanp="Point the camera at any paper — or import from Photos, Files and other apps. Several photos become one tidy PDF, filed where you&rsquo;ll actually find it, behind Face&nbsp;ID.",
    wmh="Share a copy with a clear purpose.",
    wmp="Add the recipient and intended use as a visible watermark: &ldquo;rental application only&rdquo;, &ldquo;for the gym&rdquo;. Your original stays unchanged.",
    wmalt="A shared ID copy with a personal watermark across it",

),
"es": dict(
    title="Amano — DNI y documentos",
    desc="Tu DNI, pasaporte, carnet y los papeles de casa: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    getapp="Descargar la app",
    h1="Lo importante, <em>a mano.</em>",
    lede="Tu DNI, pasaporte, carnet y los papeles de casa: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    ctanote="Prueba todas las funciones gratis durante 7 días. Después, desbloquea Amano para siempre con un pago de <strong>7,99 €</strong> (el precio puede variar según el país). Consulta tu precio en la app. Sin suscripción ni cobro automático.",
    figcap="Treinta y cinco segundos: tres fotos se convierten en un PDF, con marca de agua, compartido.",
    f1h="Privacidad desde el principio", f1p="Tus documentos permanecen en tu dispositivo y, con la sincronización de Unlimited, en tu iCloud. Face&nbsp;ID protege el acceso.",
    f2h="Renovado a tiempo", f2p="Amano lee la fecha de caducidad al guardar un documento y te avisa antes de que caduquen pasaportes, permisos y pólizas.",
    f3h="Fírmalo desde el móvil", f3p="Dibuja o escribe tu firma, colócala en la página y envía una copia firmada. El original no cambia.",
    f4h="Marca de agua en cada copia", f4p="Añade el destinatario y el propósito a una copia. El original no cambia.",
    f5h="Varios archivos, un solo PDF", f5p="Fotos y PDF se convierten en un único documento ordenado: contratos, recibos, papeles del cole, listos para compartir.",
    f6h="Comparte seguro desde el móvil", f6p="Revisa cada página y cada archivo antes de que salga de tu iPhone. Las carpetas familiares reúnen el papeleo compartido.",
    ph2="Tus documentos siguen siendo tuyos.",
    pp="RevenueCat procesa la información de compra para activar el acceso, restaurarlo y medir las ventas. La atribución de Apple Ads mide el rendimiento de los anuncios. El contenido de tus documentos permanece en tu dispositivo o iCloud.",
    price="7 días gratis &middot; un pago para desbloquearla para siempre &middot; sin suscripción",
    made="hecho por M&amp;D en Madrid", privacy="Privacidad", terms="Condiciones", support="Ayuda", review="Escribe una reseña", heroalt="El espacio de Amano en un iPhone", tagfree="Incluido en tu prueba de 7 días", tagunl="Incluido en tu prueba de 7 días", alsoh="Y además, en Amano", freeh="Prueba todas las funciones", freep="Durante 7 días puedes escanear, importar, organizar y compartir tus documentos sin límites. Después puedes comprar el acceso completo para siempre con un solo pago. Sin suscripción ni cobro automático.", store="App&nbsp;Store",
    videolabel="Amano convirtiendo tres fotos en un PDF con marca de agua y compartiéndolo",
    shotsh2="Un vistazo por dentro",
    shotsalt=["Pantalla de renovaciones avisando de un pasaporte a punto de caducar", "Colocando una firma en la página de un documento", "Una carpeta familiar compartida con documentos de viaje"],
    shotcaps=["Confirma la fecha que detecta Amano. Activa un recordatorio para renovar.", "Dibuja o escribe tu firma, colócala en la página y comparte una copia limpia.", "Comparte una carpeta con tu familia. Tus archivos privados, por separado."],
    faqh2="Preguntas, respondidas",
    faq=[
        ("¿Cómo funciona la prueba gratuita?", "Las personas nuevas pueden probar todas las funciones durante siete días, sin límites de documentos ni carpetas. Después pueden desbloquear el acceso completo para siempre con un solo pago. No hay suscripción ni cobro automático."),
        ("¿Qué pasa cuando termina la prueba?", "Puedes seguir viendo tus documentos guardados y exportarlos como copias simples. Los detalles ya extraídos siguen disponibles para copiar. Para añadir documentos y usar todas las funciones necesitas desbloquear Amano con un solo pago."),
        ("¿Puedo comprar antes de que termine la prueba?", "Sí. Puedes desbloquear Amano en cualquier momento durante la prueba. El acceso completo empieza inmediatamente y el pago es único."),
        ("¿Dónde se guardan mis documentos?", "En tu iPhone, cifrados; y si activas la sincronización, en tu propio iCloud."),
        ("¿Qué pasa si pierdo el móvil?", "Con la sincronización de iCloud activada (parte de Unlimited), tu espacio te espera en tu siguiente iPhone. Sin ella, los documentos viven solo en el dispositivo: es la contrapartida del almacenamiento totalmente local."),
        ("¿Qué incluye exactamente el pago único?", "Acceso completo para siempre: documentos y carpetas privadas ilimitados, copias con firma o marca de agua, recordatorios de caducidad, copia personal en iCloud, kits y widgets. La extracción inteligente requiere un iPhone compatible. Sin suscripción."),
        ("¿Necesito crear una cuenta?", "No. Amano funciona desde el momento en que lo abres. No hay nada que registrar."),
    ],
),
"fr": dict(
    title="Amano — Permis et documents",
    desc="Ton permis, ta CNI, ton passeport et les papiers de la maison : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    getapp="Obtenir l’app",
    h1="L’essentiel, <em>à portée de main.</em>",
    lede="Ton permis, ta CNI, ton passeport et les papiers de la maison : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    ctanote="Essaie toutes les fonctions gratuitement pendant 7 jours. Ensuite, débloque tout à vie avec un seul paiement de <strong>7,99 €</strong> (le prix peut varier selon le pays). Vérifie ton prix dans l’app. Aucun abonnement ni prélèvement automatique.",
    figcap="Trente-cinq secondes : trois photos deviennent un PDF, filigrané, partagé.",
    f1h="Privé dès la conception", f1p="Tes documents restent sur ton appareil et, avec la synchronisation Unlimited, dans ton iCloud. Face&nbsp;ID protège l’accès.",
    f2h="Renouvelé à temps", f2p="Amano lit la date d’échéance quand tu enregistres un document et te prévient avant que passeports, permis et contrats n’expirent.",
    f3h="Signe depuis ton iPhone", f3p="Dessine ou tape ta signature, place-la sur la page et envoie une copie signée. L’original ne change pas.",
    f4h="Un filigrane sur chaque copie", f4p="Avec Unlimited, indique le destinataire et l’usage sur la copie. L’original ne change pas.",
    f5h="Plusieurs fichiers, un seul PDF", f5p="Photos et PDF deviennent un document unique et ordonné : contrats, reçus, papiers d’école, prêts à partager.",
    f6h="Partage en sécurité, depuis le téléphone", f6p="Vérifie chaque page et chaque fichier avant qu’il quitte ton iPhone. Les dossiers familiaux réunissent les papiers partagés.",
    ph2="Tes documents restent les tiens.",
    pp="RevenueCat traite les informations d’achat pour activer l’accès, restaurer les achats et mesurer les ventes. L’attribution Apple Ads mesure les performances publicitaires. Le contenu de tes documents reste sur ton appareil ou dans iCloud.",
    price="7 jours gratuits &middot; un paiement pour tout débloquer à vie &middot; aucun abonnement",
    made="fait par M&amp;D à Madrid", privacy="Confidentialité", terms="Conditions", support="Assistance", review="Laisser un avis", heroalt="Le coffre Amano sur un iPhone", tagfree="Inclus dans ton essai de 7 jours", tagunl="Inclus dans ton essai de 7 jours", alsoh="Et aussi, dans Amano", freeh="Essaie toutes les fonctions", freep="Pendant 7 jours, scanne, importe, organise et partage tes documents sans limites. Ensuite, débloque l’accès complet à vie avec un seul paiement. Aucun abonnement ni prélèvement automatique.", store="App&nbsp;Store",
    videolabel="Amano transforme trois photos en un PDF filigrané et le partage",
    shotsh2="Un aperçu de l’intérieur",
    shotsalt=["Écran des renouvellements signalant un passeport bientôt expiré", "Pose d’une signature sur la page d’un document", "Un dossier familial partagé avec des documents de voyage"],
    shotcaps=["Confirmez la date repérée par Amano. Activez un rappel de renouvellement.", "Dessine ou tape ta signature, place-la sur la page et partage une copie propre.", "Partagez un dossier avec votre famille. Gardez vos fichiers privés à part."],
    faqh2="Vos questions, nos réponses",
    faq=[
        ("Comment fonctionne l’essai gratuit ?", "Les nouveaux utilisateurs peuvent essayer toutes les fonctions pendant sept jours, sans limite de documents ni de dossiers. Ensuite, un seul paiement débloque l’accès complet à vie. Aucun abonnement ni prélèvement automatique."),
        ("Que se passe-t-il à la fin de l’essai ?", "Tu peux continuer à consulter tes documents enregistrés et les exporter en copies simples. Les informations déjà extraites restent copiables. Pour ajouter des documents et utiliser toutes les fonctions, il faut débloquer Amano avec un seul paiement."),
        ("Où mes documents sont-ils stockés ?", "Sur ton iPhone, chiffrés — et, si tu actives la synchronisation, dans ton propre iCloud."),
        ("Que se passe-t-il si je perds mon téléphone ?", "Avec la synchronisation iCloud activée (incluse dans Unlimited), ton espace t’attend sur ton prochain iPhone. Sans elle, les documents ne vivent que sur l’appareil — c’est la contrepartie d’un stockage entièrement local."),
        ("Que comprend exactement le paiement unique ?", "Accès complet à vie : documents et dossiers privés illimités, copies signées ou filigranées, rappels d’échéance, sauvegarde personnelle iCloud, kits et widgets. L’extraction intelligente nécessite un iPhone compatible. Aucun abonnement."),
        ("Dois-je créer un compte ?", "Non. Amano fonctionne dès l’ouverture. Il n’y a rien à créer."),
    ],
),
"de": dict(
    title="Amano — Ausweis &amp; Dokumente",
    desc="Dein Ausweis, Pass, Führerschein und die Unterlagen von zu Hause: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    getapp="App laden",
    h1="Alles Wichtige, <em>griffbereit.</em>",
    lede="Dein Ausweis, Pass, Führerschein und die Unterlagen von zu Hause: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    ctanote="Teste alle Funktionen 7 Tage kostenlos. Danach schaltest du alles für einmalig <strong>7,99 €</strong> dauerhaft frei (der Preis kann je nach Land variieren). Prüfe deinen Preis in der App. Kein Abo und keine automatische Abbuchung.",
    figcap="Fünfunddreißig Sekunden: Drei Fotos werden ein PDF, mit Wasserzeichen, geteilt.",
    f1h="Privat von Grund auf", f1p="Deine Dokumente bleiben auf deinem Gerät und mit Unlimited-Synchronisierung in deiner iCloud. Face&nbsp;ID schützt den Zugriff.",
    f2h="Rechtzeitig verlängert", f2p="Amano liest das Ablaufdatum beim Speichern und erinnert dich, bevor Reisepässe, Ausweise und Policen ablaufen.",
    f3h="Unterschreibe am iPhone", f3p="Zeichne oder tippe deine Unterschrift, platziere sie auf der Seite und sende eine signierte Kopie. Das Original bleibt unverändert.",
    f4h="Wasserzeichen auf jeder Kopie", f4p="Mit Unlimited kennzeichnest du eine Kopie mit Empfänger und Zweck. Das Original bleibt unverändert.",
    f5h="Viele Dateien, ein PDF", f5p="Fotos und PDFs werden ein geordnetes Dokument – Verträge, Belege, Schulunterlagen – bereit zum Teilen.",
    f6h="Sicher teilen, direkt vom Handy", f6p="Prüfe jede Seite und jede Datei, bevor sie dein iPhone verlässt. Familienordner halten gemeinsame Unterlagen an einem Ort.",
    ph2="Deine Dokumente bleiben deine.",
    pp="RevenueCat verarbeitet Kaufdaten, um den Zugang freizuschalten, Käufe wiederherzustellen und Verkäufe auszuwerten. Apple Ads Attribution misst die Anzeigenleistung. Deine Dokumentinhalte bleiben auf deinem Gerät oder in iCloud.",
    price="7 Tage kostenlos &middot; einmalig dauerhaft freischalten &middot; kein Abo",
    made="von M&amp;D in Madrid gemacht", privacy="Datenschutz", terms="Bedingungen", support="Support", review="Bewertung schreiben", heroalt="Der Amano-Bereich auf einem iPhone", tagfree="In deiner 7-Tage-Testphase enthalten", tagunl="In deiner 7-Tage-Testphase enthalten", alsoh="Außerdem in Amano", freeh="Alle Funktionen testen", freep="Teste 7 Tage lang Scannen, Importieren, Ordnen und Teilen ohne Limits. Danach schaltest du den vollständigen Zugang mit einer einmaligen Zahlung dauerhaft frei. Kein Abo und keine automatische Abbuchung.", store="App&nbsp;Store",
    videolabel="Amano macht aus drei Fotos ein PDF mit Wasserzeichen und teilt es",
    shotsh2="Ein Blick hinein",
    shotsalt=["Verlängerungs-Ansicht warnt vor einem ablaufenden Reisepass", "Eine Unterschrift wird auf einer Dokumentseite platziert", "Ein geteilter Familienordner mit Reisedokumenten"],
    shotcaps=["Bestätige das erkannte Ablaufdatum. Lass dich ans Verlängern erinnern.", "Zeichne oder tippe deine Unterschrift, platziere sie auf der Seite und teile eine saubere Kopie.", "Teile einen Ordner mit deiner Familie. Deine privaten Dateien bleiben privat."],
    faqh2="Fragen, beantwortet",
    faq=[
        ("Wie funktioniert die kostenlose Testphase?", "Neue Nutzer können sieben Tage lang alle Funktionen ohne Dokument- oder Ordnerlimit testen. Danach schaltet eine einmalige Zahlung den vollständigen Zugang dauerhaft frei. Kein Abo und keine automatische Abbuchung."),
        ("Was passiert nach der Testphase?", "Du kannst deine gespeicherten Dokumente weiterhin ansehen und als einfache Kopien exportieren. Bereits extrahierte Details bleiben kopierbar. Für neue Dokumente und alle Funktionen brauchst du die dauerhafte Freischaltung mit einer einmaligen Zahlung."),
        ("Wo werden meine Dokumente gespeichert?", "Auf deinem iPhone, verschlüsselt — und wenn du die Synchronisierung einschaltest, in deiner eigenen iCloud."),
        ("Was passiert, wenn ich mein iPhone verliere?", "Mit iCloud-Synchronisierung (Teil von Unlimited) wartet dein Bereich auf deinem nächsten iPhone. Ohne sie leben die Dokumente nur auf dem Gerät — das ist der Preis rein lokaler Speicherung."),
        ("Was genau enthält der Einmalkauf?", "Dauerhafter Vollzugriff: unbegrenzte Dokumente und private Ordner, Kopien mit Unterschrift oder Wasserzeichen, Ablauferinnerungen, persönliches iCloud-Backup, Kits und Widgets. Intelligente Texterkennung erfordert ein unterstütztes iPhone. Kein Abo."),
        ("Brauche ich ein Konto?", "Nein. Amano funktioniert ab dem ersten Öffnen. Es gibt nichts zu registrieren."),
    ],
),
"it": dict(
    title="Amano — CIE e documenti",
    desc="La tua CIE, la patente, il passaporto e le carte di casa: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    getapp="Scarica l’app",
    h1="Ciò che conta, <em>a portata di mano.</em>",
    lede="La tua CIE, la patente, il passaporto e le carte di casa: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    ctanote="Prova tutte le funzioni gratis per 7 giorni. Poi sblocca tutto per sempre con un unico pagamento di <strong>7,99 €</strong> (il prezzo può variare in base al Paese). Controlla il tuo prezzo nell’app. Nessun abbonamento né addebito automatico.",
    figcap="Trentacinque secondi: tre foto diventano un PDF, con filigrana, condiviso.",
    f1h="Privato fin dall’inizio", f1p="I documenti restano sul dispositivo e, con la sincronizzazione Unlimited, nel tuo iCloud. Face&nbsp;ID protegge l’accesso.",
    f2h="Rinnovato in tempo", f2p="Amano legge la scadenza quando salvi un documento e ti avvisa prima che passaporti, patenti e polizze scadano.",
    f3h="Firma dal telefono", f3p="Disegna o digita la firma, posizionala sulla pagina e invia una copia firmata. L’originale non cambia.",
    f4h="Filigrana su ogni copia", f4p="Con Unlimited, indica destinatario e scopo sulla copia. L’originale non cambia.",
    f5h="Tanti file, un solo PDF", f5p="Foto e PDF diventano un unico documento ordinato: contratti, ricevute, moduli della scuola, pronti da condividere.",
    f6h="Condividi in sicurezza dal telefono", f6p="Controlla ogni pagina e ogni file prima che lasci il tuo iPhone. Le cartelle famiglia tengono insieme le pratiche condivise.",
    ph2="I tuoi documenti restano tuoi.",
    pp="RevenueCat elabora i dati degli acquisti per attivare l’accesso, ripristinare gli acquisti e misurare le vendite. L’attribuzione Apple Ads misura il rendimento degli annunci. Il contenuto dei documenti resta sul dispositivo o in iCloud.",
    price="7 giorni gratis &middot; un pagamento per sbloccare tutto per sempre &middot; nessun abbonamento",
    made="fatto da M&amp;D a Madrid", privacy="Privacy", terms="Termini", support="Assistenza", review="Scrivi una recensione", heroalt="L’archivio Amano su un iPhone", tagfree="Incluso nella prova di 7 giorni", tagunl="Incluso nella prova di 7 giorni", alsoh="E inoltre, in Amano", freeh="Prova tutte le funzioni", freep="Per 7 giorni puoi scansionare, importare, organizzare e condividere i tuoi documenti senza limiti. Poi sblocca l’accesso completo per sempre con un unico pagamento. Nessun abbonamento né addebito automatico.", store="App&nbsp;Store",
    videolabel="Amano trasforma tre foto in un PDF con filigrana e lo condivide",
    shotsh2="Uno sguardo dentro",
    shotsalt=["Schermata dei rinnovi che segnala un passaporto in scadenza", "Una firma viene posizionata sulla pagina di un documento", "Una cartella famiglia condivisa con documenti di viaggio"],
    shotcaps=["Conferma la scadenza trovata da Amano. Imposta un promemoria per rinnovare.", "Disegna o digita la tua firma, posizionala sulla pagina e condividi una copia pulita.", "Condividi una cartella con la tua famiglia. I file privati restano a parte."],
    faqh2="Domande, risposte",
    faq=[
        ("Come funziona la prova gratuita?", "I nuovi utenti possono provare tutte le funzioni per sette giorni, senza limiti di documenti o cartelle. Poi un unico pagamento sblocca l’accesso completo per sempre. Nessun abbonamento né addebito automatico."),
        ("Cosa succede quando finisce la prova?", "Puoi continuare a vedere i documenti salvati ed esportarli come copie semplici. I dettagli già estratti restano copiabili. Per aggiungere documenti e usare tutte le funzioni devi sbloccare Amano con un unico pagamento."),
        ("Dove sono conservati i miei documenti?", "Sul tuo iPhone, cifrati — e, se attivi la sincronizzazione, nel tuo iCloud."),
        ("Cosa succede se perdo il telefono?", "Con la sincronizzazione iCloud attiva (parte di Unlimited), il tuo archivio ti aspetta sul prossimo iPhone. Senza, i documenti vivono solo sul dispositivo: è il compromesso dell’archiviazione interamente locale."),
        ("Cosa include esattamente il pagamento unico?", "Accesso completo per sempre: documenti e cartelle private illimitati, copie firmate o con filigrana, promemoria, backup personale iCloud, kit e widget. L’estrazione intelligente richiede un iPhone compatibile. Nessun abbonamento."),
        ("Devo creare un account?", "No. Amano funziona appena lo apri. Non c’è nulla da registrare."),
    ],
),
"pt": dict(
    title="Amano — CC e documentos",
    desc="O seu CC, a carta de condução, o passaporte e os papéis de casa: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    getapp="Obter a app",
    h1="O que importa, <em>à mão.</em>",
    lede="O seu CC, a carta de condução, o passaporte e os papéis de casa: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    ctanote="Experimente todas as funcionalidades gratuitamente durante 7 dias. Depois, desbloqueie tudo para sempre com um único pagamento de <strong>7,99 €</strong> (o preço pode variar consoante o país). Consulte o seu preço na app. Sem subscrição nem cobrança automática.",
    figcap="Trinta e cinco segundos: três fotos tornam-se um PDF, com marca de água, partilhado.",
    f1h="Privado por conceção", f1p="Os documentos ficam no dispositivo e, com a sincronização Unlimited, no seu iCloud. O Face&nbsp;ID protege o acesso.",
    f2h="Renovado a tempo", f2p="O Amano lê a validade quando guarda um documento e avisa antes que passaportes, cartas e apólices caduquem.",
    f3h="Assine no telemóvel", f3p="Desenhe ou escreva a assinatura, coloque-a na página e envie uma cópia assinada. O original não muda.",
    f4h="Marca de água em cada cópia", f4p="Com Unlimited, marque a cópia com o destinatário e a finalidade. O original não muda.",
    f5h="Vários ficheiros, um só PDF", f5p="Fotos e PDF tornam-se um único documento ordenado: contratos, recibos, papéis da escola, prontos a partilhar.",
    f6h="Partilhe em segurança, do telemóvel", f6p="Reveja cada página e cada ficheiro antes de sair do seu iPhone. As pastas de família juntam a papelada partilhada.",
    ph2="Os seus documentos continuam seus.",
    pp="A RevenueCat processa informações de compras para ativar o acesso, restaurar compras e medir vendas. A atribuição Apple Ads mede o desempenho dos anúncios. O conteúdo dos documentos fica no dispositivo ou no iCloud.",
    price="7 dias grátis &middot; um pagamento para desbloquear tudo para sempre &middot; sem subscrição",
    made="feito por M&amp;D em Madrid", privacy="Privacidade", terms="Termos", support="Suporte", review="Escrever uma avaliação", heroalt="O espaço do Amano num iPhone", tagfree="Incluído no seu teste de 7 dias", tagunl="Incluído no seu teste de 7 dias", alsoh="E ainda, no Amano", freeh="Experimente tudo", freep="Durante 7 dias, digitalize, importe, organize e partilhe os seus documentos sem limites. Depois, desbloqueie o acesso completo para sempre com um único pagamento. Sem subscrição nem cobrança automática.", store="App&nbsp;Store",
    videolabel="O Amano transforma três fotos num PDF com marca de água e partilha-o",
    shotsh2="Um olhar por dentro",
    shotsalt=["Ecrã de renovações a avisar de um passaporte prestes a caducar", "Uma assinatura a ser colocada na página de um documento", "Uma pasta de família partilhada com documentos de viagem"],
    shotcaps=["Confirme a data de validade que o Amano encontra. Defina um lembrete para renovar.", "Desenhe ou escreva a sua assinatura, coloque-a na página e partilhe uma cópia limpa.", "Partilhe uma pasta com a família. Mantenha os ficheiros privados à parte."],
    faqh2="Perguntas, respondidas",
    faq=[
        ("Como funciona o teste gratuito?", "Os novos utilizadores podem experimentar todas as funcionalidades durante sete dias, sem limites de documentos ou pastas. Depois, um único pagamento desbloqueia o acesso completo para sempre. Sem subscrição nem cobrança automática."),
        ("O que acontece quando termina o teste?", "Pode continuar a ver os documentos guardados e exportá-los como cópias simples. Os detalhes já extraídos continuam disponíveis para copiar. Para adicionar documentos e usar todas as funcionalidades, precisa de desbloquear o Amano com um único pagamento."),
        ("Onde ficam guardados os meus documentos?", "No seu iPhone, cifrados — e, se ativar a sincronização, no seu próprio iCloud."),
        ("O que acontece se perder o telemóvel?", "Com a sincronização iCloud ativa (parte do Unlimited), o seu espaço espera por si no próximo iPhone. Sem ela, os documentos vivem apenas no dispositivo — é a contrapartida do armazenamento totalmente local."),
        ("O que inclui exatamente o pagamento único?", "Acesso completo para sempre: documentos e pastas privadas ilimitados, cópias assinadas ou com marca de água, lembretes, cópia pessoal no iCloud, kits e widgets. A extração inteligente requer um iPhone compatível. Sem subscrição."),
        ("Preciso de criar uma conta?", "Não. O Amano funciona assim que o abre. Não há nada para registar."),
    ],
),
"tr": dict(
    title="Amano — Ehliyet ve Belgeler",
    desc="Ehliyetiniz, pasaportunuz, kimliğiniz ve evin evrakları: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    getapp="Uygulamayı edin",
    h1="Önemli olan her şey, <em>elinizin altında.</em>",
    lede="Ehliyetiniz, pasaportunuz, kimliğiniz ve evin evrakları: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    ctanote="Tüm özellikleri 7 gün ücretsiz deneyin. Ardından tek seferlik <strong>7,99 €</strong> ödeyerek ömür boyu erişimin kilidini açın (fiyat ülkeye göre değişebilir). Size özel fiyatı uygulamada görün. Abonelik veya otomatik ücret yok.",
    figcap="Otuz beş saniye: üç fotoğraf tek bir PDF olur, filigran eklenir, paylaşılır.",
    f1h="Tasarımdan özel", f1p="Belgeleriniz cihazınızda ve Unlimited eşitlemesi ile kendi iCloud’unuzda kalır. Face&nbsp;ID erişimi korur.",
    f2h="Zamanında yenilenir", f2p="Amano bir belgeyi kaydederken son geçerlilik tarihini okur; pasaportlar, ehliyetler ve poliçeler dolmadan önce hatırlatır.",
    f3h="Telefonunuzdan imzalayın", f3p="İmzanızı çizin veya yazın, sayfaya yerleştirin ve imzalı bir kopya gönderin. Orijinal değişmez.",
    f4h="Her kopyaya filigran", f4p="Unlimited ile kopyaya alıcısını ve amacını ekleyin. Orijinal değişmez.",
    f5h="Birçok dosya, tek PDF", f5p="Fotoğraflar ve PDF’ler tek ve düzenli bir belgeye dönüşür: sözleşmeler, makbuzlar, okul evrakı — paylaşıma hazır.",
    f6h="Telefondan güvenle paylaşın", f6p="Her sayfayı ve dosyayı iPhone’unuzdan çıkmadan önce gözden geçirin. Aile klasörleri ortak evrakı bir arada tutar.",
    ph2="Belgeleriniz sizin kalır.",
    pp="RevenueCat, erişimi açmak, satın alımları geri yüklemek ve satışları ölçmek için satın alma bilgilerini işler. Apple Ads ilişkilendirmesi reklam performansını ölçer. Belge içerikleriniz cihazınızda veya iCloud’da kalır.",
    price="7 gün ücretsiz &middot; her şeyi sonsuza kadar açmak için tek ödeme &middot; abonelik yok",
    made="Madrid'de M&amp;D tarafından yapıldı", privacy="Gizlilik", terms="Koşullar", support="Destek", review="Değerlendirme yaz", heroalt="iPhone’da Amano kasası", tagfree="7 günlük denemeye dahil", tagunl="7 günlük denemeye dahil", alsoh="Ayrıca Amano’da", freeh="Tüm özellikleri deneyin", freep="7 gün boyunca belgelerinizi sınırsız tarayın, içe aktarın, düzenleyin ve paylaşın. Sonra tek seferlik ödeme ile tam erişimi sonsuza kadar açın. Abonelik ve otomatik ücret yok.", store="App&nbsp;Store",
    videolabel="Amano üç fotoğrafı filigranlı tek bir PDF’e dönüştürüp paylaşıyor",
    shotsh2="İçeriden bir bakış",
    shotsalt=["Yenilemeler ekranı süresi dolmak üzere olan bir pasaportu bildiriyor", "Bir belge sayfasına imza yerleştiriliyor", "Seyahat belgeleriyle paylaşılan bir aile klasörü"],
    shotcaps=["Amano'nun bulduğu tarihi onaylayın. Yenilemek için hatırlatıcı ayarlayın.", "İmzanızı çizin veya yazın, sayfaya yerleştirin ve temiz bir kopya paylaşın.", "Bir klasörü ailenizle paylaşın. Özel dosyalarınız ayrı kalsın."],
    faqh2="Sorular ve yanıtları",
    faq=[
        ("Ücretsiz deneme nasıl çalışır?", "Yeni kullanıcılar yedi gün boyunca tüm özellikleri belge veya klasör sınırı olmadan deneyebilir. Sonrasında tek seferlik ödeme tam erişimi sonsuza kadar açar. Abonelik ve otomatik ücret yok."),
        ("Deneme süresi bitince ne olur?", "Kaydettiğiniz belgeleri görmeye ve basit kopyalar olarak dışa aktarmaya devam edebilirsiniz. Daha önce çıkarılmış bilgiler kopyalanabilir. Yeni belge eklemek ve tüm özellikleri kullanmak için Amano’yu tek seferlik ödeme ile açmanız gerekir."),
        ("Belgelerim nerede saklanıyor?", "iPhone’unuzda, şifrelenmiş olarak — ve eşitlemeyi açarsanız kendi iCloud’unuzda."),
        ("Telefonumu kaybedersem ne olur?", "iCloud eşitleme açıksa (Unlimited’ın parçası), kasanız bir sonraki iPhone’unuzda sizi bekler. Kapalıysa belgeler yalnızca cihazda yaşar — tamamen yerel saklamanın bedeli budur."),
        ("Tek ödeme tam olarak neleri içeriyor?", "Ömür boyu tam erişim: sınırsız belge ve özel klasör, imzalı veya filigranlı kopyalar, son geçerlilik hatırlatmaları, kişisel iCloud yedeklemesi, kitler ve araç takımları. Akıllı bilgi çıkarma uyumlu iPhone gerektirir. Abonelik yok."),
        ("Hesap açmam gerekiyor mu?", "Hayır. Amano açtığınız anda çalışır. Kaydolacak bir şey yok."),
    ],
),
}

APPLE_SVG = '<svg width="20" height="24" viewBox="0 0 20 24" fill="currentColor" aria-hidden="true"><path d="M16.6 12.8c0-3 2.4-4.4 2.5-4.5-1.4-2-3.5-2.3-4.3-2.3-1.8-.2-3.5 1.1-4.4 1.1-.9 0-2.3-1-3.8-1-2 0-3.8 1.1-4.8 2.9-2 3.5-.5 8.8 1.5 11.6 1 1.4 2.1 3 3.6 2.9 1.5-.1 2-.9 3.8-.9s2.3.9 3.8.9c1.6 0 2.6-1.4 3.5-2.8 1.1-1.6 1.6-3.2 1.6-3.3-.1-.1-3-1.2-3-4.6zM13.7 3.9c.8-1 1.4-2.4 1.2-3.9-1.2.1-2.7.8-3.5 1.9-.8.9-1.5 2.3-1.3 3.7 1.4.1 2.8-.7 3.6-1.7z"/></svg>'

STORY = {
    "en": [
        ("scan-review", "Save the paper. Skip the typing.", "Scan or import a document. Amano suggests a name and expiry date; you check them before saving."),
        ("renewals", "Know when to renew.", "Get a reminder before a passport, permit or policy expires — while there is still time to act."),
        ("signature", "Send the copy, keep the original.", "Sign a page or add a visible watermark for its recipient and purpose. Review the copy before sharing."),
        ("extraction", "Find the detail without digging.", "Copy the information you need without retyping it. Check against the original. Available on supported iPhones with Apple Intelligence ready."),
        ("settings-icloud", "Your documents. Your iCloud.", "Your vault stays on your iPhone. Turn on personal iCloud backup if you want it on your next device."),
    ],
    "es": [
        ("scan-review", "Guarda el papel. No lo transcribas.", "Escanea o importa un documento. Amano sugiere un nombre y la fecha de caducidad; tú los confirmas antes de guardar."),
        ("renewals", "Renueva antes de que caduque.", "Recibe un recordatorio para el DNI, el pasaporte o la póliza cuando todavía estás a tiempo."),
        ("signature", "Envía la copia. Conserva el original.", "Firma una página o añade una marca de agua con el destinatario y el motivo. Revisa la copia antes de compartirla."),
        ("extraction", "Encuentra el dato sin buscar entre papeles.", "Copia la información sin volver a escribirla. Compruébala con el original. Requiere un iPhone compatible con Apple Intelligence listo para usar."),
        ("settings-icloud", "Tus documentos. Tu iCloud.", "Tu espacio permanece en el iPhone. Activa la copia personal en iCloud si quieres tenerlo en tu próximo dispositivo."),
    ],
    "fr": [
        ("scan-review", "Garde le document. Évite la saisie.", "Scanne ou importe un document. Amano suggère un nom et une date d’expiration ; tu les vérifies avant d’enregistrer."),
        ("renewals", "Renouvelle avant l’échéance.", "Reçois un rappel pour ton passeport, ton permis ou ton contrat pendant qu’il est encore temps d’agir."),
        ("signature", "Envoie la copie. Garde l’original.", "Signe une page ou ajoute un filigrane indiquant le destinataire et l’usage. Vérifie la copie avant de l’envoyer."),
        ("extraction", "Trouve l’information sans fouiller.", "Copie les détails sans les retaper. Vérifie-les sur l’original. Nécessite un iPhone compatible avec Apple Intelligence prêt à l’emploi."),
        ("settings-icloud", "Tes documents. Ton iCloud.", "Ton coffre reste sur ton iPhone. Active la sauvegarde personnelle iCloud pour le retrouver sur ton prochain appareil."),
    ],
    "de": [
        ("scan-review", "Papier sichern. Tippen sparen.", "Scanne oder importiere ein Dokument. Amano schlägt Name und Ablaufdatum vor; du bestätigst beides vor dem Speichern."),
        ("renewals", "Vor dem Ablauf Bescheid wissen.", "Erhalte eine Erinnerung für Pass, Ausweis oder Police, solange noch Zeit zum Handeln ist."),
        ("signature", "Kopie senden. Original behalten.", "Unterschreibe eine Seite oder kennzeichne die Kopie mit Empfänger und Zweck. Prüfe sie vor dem Teilen."),
        ("extraction", "Details finden, ohne zu suchen.", "Kopiere wichtige Angaben statt sie abzutippen. Vergleiche sie mit dem Original. Erfordert ein unterstütztes iPhone mit einsatzbereiter Apple Intelligence."),
        ("settings-icloud", "Deine Dokumente. Deine iCloud.", "Dein Archiv bleibt auf deinem iPhone. Aktiviere das persönliche iCloud-Backup für dein nächstes Gerät."),
    ],
    "it": [
        ("scan-review", "Conserva il documento. Evita di trascriverlo.", "Scansiona o importa un documento. Amano suggerisce nome e scadenza; controllali prima di salvare."),
        ("renewals", "Rinnova prima della scadenza.", "Ricevi un promemoria per passaporto, patente o polizza quando sei ancora in tempo."),
        ("signature", "Invia la copia. Tieni l’originale.", "Firma una pagina o aggiungi una filigrana con destinatario e scopo. Controlla la copia prima di condividerla."),
        ("extraction", "Trova il dato senza cercare.", "Copia le informazioni senza riscriverle. Verificale sull’originale. Richiede un iPhone compatibile con Apple Intelligence pronto all’uso."),
        ("settings-icloud", "I tuoi documenti. Il tuo iCloud.", "L’archivio resta sul tuo iPhone. Attiva il backup personale iCloud per ritrovarlo sul prossimo dispositivo."),
    ],
    "pt": [
        ("scan-review", "Guarde o documento. Evite transcrevê-lo.", "Digitalize ou importe um documento. O Amano sugere nome e validade; confirme-os antes de guardar."),
        ("renewals", "Renove antes do prazo.", "Receba um lembrete para o passaporte, carta ou apólice enquanto ainda há tempo."),
        ("signature", "Envie a cópia. Guarde o original.", "Assine uma página ou acrescente uma marca de água com destinatário e finalidade. Reveja a cópia antes de partilhar."),
        ("extraction", "Encontre o dado sem procurar.", "Copie as informações sem voltar a escrevê-las. Confirme-as no original. Requer um iPhone compatível com Apple Intelligence pronto a usar."),
        ("settings-icloud", "Os seus documentos. O seu iCloud.", "O arquivo fica no seu iPhone. Ative a cópia pessoal no iCloud para o ter no próximo dispositivo."),
    ],
    "tr": [
        ("scan-review", "Belgeyi saklayın. Yeniden yazmayın.", "Bir belgeyi tarayın veya içe aktarın. Amano ad ve son geçerlilik tarihi önerir; kaydetmeden önce siz onaylarsınız."),
        ("renewals", "Süresi dolmadan yenileyin.", "Pasaport, ehliyet veya poliçeniz için hâlâ zaman varken hatırlatma alın."),
        ("signature", "Kopyayı gönderin. Orijinali koruyun.", "Bir sayfayı imzalayın veya alıcı ve amacı gösteren filigran ekleyin. Paylaşmadan önce kopyayı inceleyin."),
        ("extraction", "Bilgiyi yeniden yazmadan bulun.", "Bilgileri yeniden yazmadan kopyalayın. Orijinaliyle karşılaştırın. Kullanıma hazır Apple Intelligence bulunan uyumlu bir iPhone gerekir."),
        ("settings-icloud", "Belgeleriniz. iCloud’unuz.", "Arşiviniz iPhone’unuzda kalır. Sonraki cihazınızda kullanmak için kişisel iCloud yedeklemesini açın."),
    ],
}

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
  header.top { display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 50; background: var(--paper);
    padding: 14px 0; border-bottom: 1px solid rgba(16, 23, 34, 0.06); }
  .badge { display: block; height: 40px; width: auto; }
  .badge-hero { height: 58px; }
  .shots figure { margin: 0; }
  .shots figcaption { font-size: 14px; color: var(--muted); padding: 10px 4px 0; text-wrap: pretty; }
  .wordmark { font-family: var(--display); font-weight: 600; font-size: 30px; color: var(--navy);
    font-variation-settings: "opsz" 72, "SOFT" 100; letter-spacing: 0.01em; text-decoration: none; }
  .top a.store-mini { font-weight: 600; font-size: 15px; color: var(--link);
    text-decoration: none; padding: 10px 16px; border-radius: 999px; }
  .top a.store-mini:hover { background: var(--card); }
  .hero { padding: 48px 0 24px; text-align: center; }
  .hero-visual { max-width: 320px; margin: 24px auto 0; }
  .hero-visual, .chapter .art { background: #F4F6F9; }
  .hero-visual img { width: 100%; height: auto; display: block; }
  @media (min-width: 900px) {
    .hero { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 56px;
      align-items: center; text-align: left; padding: 48px 0 32px; }
    .hero .cta-row { justify-content: flex-start; }
    .hero .cta-note { text-align: left; }
    .hero h1, .hero p.lede { margin-left: 0; }
    .hero-visual { max-width: 460px; margin: 0 0 0 auto; }
  }
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
  .cta-note { width: 100%; max-width: 34em; text-align: center;
    font-size: clamp(17px, 2.2vw, 20px); line-height: 1.6; color: var(--ink); text-wrap: pretty; }
  .cta-note strong { font-weight: 650; color: var(--deep); }
  .demo { padding: 44px 0 20px; }
  .demo figure { max-width: 560px; margin: 0 auto; border-radius: 24px; overflow: hidden; }
  .demo video { display: block; width: 100%; height: auto; }
  .demo figcaption { text-align: center; font-size: 14px; color: var(--muted);
    padding: 14px 16px 16px; background: var(--card); }
  section.chapters { padding: 56px 0 8px; }
  .chapter { display: grid; gap: 40px; align-items: center; margin: 0 0 64px; }
  .chapter .art { max-width: 300px; margin: 0 auto; }
  .chapter .art img { width: 100%; height: auto; display: block; }
  .chapter h2 { font-family: var(--display); font-variation-settings: "opsz" 72, "SOFT" 100;
    font-weight: 560; font-size: clamp(28px, 4.4vw, 40px); line-height: 1.12;
    text-wrap: balance; margin: 12px 0 14px; }
  .chapter p { color: var(--muted); font-size: 17px; max-width: 30em; text-wrap: pretty; }
  .chip { display: inline-block; font-size: 13px; font-weight: 600; letter-spacing: 0.02em;
    padding: 5px 12px; border-radius: 999px; }
  .chip.free { background: rgba(25, 59, 112, 0.10); color: var(--navy); }
  .chip.unl { background: var(--deep); color: #F4F6F9; }
  @media (min-width: 860px) {
    .chapter { grid-template-columns: 1fr 1fr; gap: 64px; margin: 0 0 40px; }
    .chapter .art { max-width: 380px; }
    .chapter:nth-child(even) .art { order: 2; margin-left: auto; }
    .chapter:nth-child(odd) .art { margin-right: auto; }
  }
  section.also { padding: 40px 0 10px; }
  .also h2 { font-family: var(--display); font-variation-settings: "opsz" 40, "SOFT" 100;
    font-weight: 600; font-size: 22px; text-align: center; margin-bottom: 26px; color: var(--muted); }
  .also .grid { display: grid; gap: 18px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
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
  footer a.mail { margin-left: 0; color: #ABB7C8; }
  footer a:hover { text-decoration: underline; }
  footer .langs { width: 100%; margin-top: 14px; }
  footer .langs a { margin: 0 12px 0 0; color: #8FA0B8; font-size: 13px; }
  footer .langs span { color: #F4F6F9; font-size: 13px; margin-right: 12px; }
  section.shots { padding: 40px 0 30px; }
  .shots h2, .faq h2 { font-family: var(--display); font-variation-settings: "opsz" 72, "SOFT" 100;
    font-weight: 560; font-size: clamp(28px, 4vw, 38px); text-align: center; margin-bottom: 30px;
    color: var(--ink); text-wrap: balance; }
  .shots .strip { display: grid; grid-template-columns: repeat(2, 1fr); gap: 28px; max-width: 760px; margin: 0 auto; }
  .shots img { width: 100%; height: auto; display: block; }
  @media (max-width: 640px) { .shots .strip { grid-template-columns: 1fr; max-width: 320px; } }
  section.faq { padding: 70px 0 84px; }
  .faq .qa { max-width: 680px; margin: 0 auto; }
  .faq details { background: var(--card); border-radius: var(--radius); padding: 4px 24px; margin-bottom: 12px; }
  .faq summary { cursor: pointer; font-weight: 600; font-size: 17px; padding: 16px 0; list-style-position: outside; }
  .faq details p { color: var(--muted); padding: 0 0 18px; text-wrap: pretty; }
  @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } .store-button { transition: none; } }

  /* Pain cards + explicit pricing (PoC: rendered only when a locale defines them) */
  .pains { padding: 26px 0 8px; }
  .pains h2, .pricing h2 { font-family: Fraunces, Georgia, serif; font-weight: 550; font-size: 30px; margin: 0 0 18px; }
  .pains .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }
  .pain { background: var(--card); border-radius: 16px; padding: 20px 22px; box-shadow: 0 1px 2px rgba(16,23,34,.06); }
  .pain h3 { font-family: Fraunces, Georgia, serif; font-weight: 550; font-size: 20px; margin: 0 0 8px; color: var(--deep); }
  .pain p { margin: 0; color: var(--muted); font-size: 15.5px; }
  .pricing { padding: 34px 0 10px; }
  .pricing .cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; align-items: stretch; }
  .pricing .col { background: var(--card); border-radius: 16px; padding: 22px 24px; }
  .pricing .col.main { border: 2px solid var(--navy); }
  .pricing h3 { margin: 0 0 6px; font-size: 15px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }
  .pricing .num { font-family: Fraunces, Georgia, serif; font-weight: 650; font-size: 52px; color: var(--deep); line-height: 1; }
  .pricing .once { color: var(--navy); font-weight: 600; margin: 4px 0 12px; }
  .pricing ul { margin: 10px 0 0; padding-left: 20px; color: var(--muted); }
  .pricing li { margin: 6px 0; }
  .pricing .badge-hero { margin-top: 16px; }
  .pricing .pricenote { color: var(--muted); font-size: 14px; margin-top: 14px; }

  .chapter .art video { display: block; width: 100%; height: auto; border-radius: 22px; }
  .hero-visual img, .chapter .art img { border-radius: 18px; }
  .eyebrow { display: inline-block; color: var(--navy); font-size: 13px; font-weight: 600;
    letter-spacing: .12em; text-transform: uppercase; margin-bottom: 16px; }
  .pricing { padding: 76px 0 14px; }
  .pricing h2 { font-family: var(--display); font-size: clamp(30px, 4.5vw, 46px); }
  .pricing .col { padding: 30px; }
  .pricing .col p { color: var(--muted); max-width: 30em; }
  .pricing .num { margin: 16px 0 8px; }
  @media (max-width: 640px) { .hero { padding-top: 36px; } .chapter { gap: 8px; margin-bottom: 70px; } }
"""

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

def faq_jsonld(s):
    import json as _json
    return _json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]],
    }, ensure_ascii=False)

def page(key):
    folder, lang, _, storefront, badge = LOCALES[key]
    s = S[key]
    root = "../" if folder else "./"
    canon = BASE + folder
    # Apple Search Ads campaign attribution. pt is the provider token; ct is
    # reported per value in App Store Connect, so each locale is countable
    # on its own. The write-review link below stays untagged: it is for
    # people who already installed and would pollute install attribution.
    store = (f"https://apps.apple.com/{storefront}app/id{APP_ID}"
             f"?pt={PROVIDER_TOKEN}&amp;ct=web-{key}&amp;mt=8")
    chapters = "".join(
        f'<div class="chapter"><div class="art"><img src="{root}assets/phones/{key}/{scene}.webp?v=a3cd617" '
        f'alt="{heading}" loading="lazy" width="900" height="1200"></div>'
        f'<div><span class="eyebrow">0{number}</span><h2>{heading}</h2><p>{body}</p></div></div>'
        for number, (scene, heading, body) in enumerate(STORY[key], 1))
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faq"])
    trial = {
        "en": ("Seven days, every feature.", "Try Amano with no document or folder limit. Your saved documents remain viewable after the trial. Nothing is charged automatically.", "€7.99", "One payment for lifetime access. Price may vary by country; check the app before purchase."),
        "es": ("Siete días, todas las funciones.", "Prueba Amano sin límite de documentos ni carpetas. Al terminar, puedes seguir viendo los documentos guardados. No hay cobro automático.", "7,99 €", "Un solo pago para usar Amano para siempre. El precio puede variar según el país; consúltalo en la app antes de comprar."),
        "fr": ("Sept jours, toutes les fonctions.", "Essaie Amano sans limite de documents ni de dossiers. Tes documents restent consultables après l’essai. Aucun prélèvement automatique.", "7,99 €", "Un seul paiement pour un accès à vie. Le prix peut varier selon le pays ; vérifie-le dans l’app avant l’achat."),
        "de": ("Sieben Tage, alle Funktionen.", "Teste Amano ohne Dokument- oder Ordnerlimit. Gespeicherte Dokumente bleiben nach der Testphase sichtbar. Keine automatische Abbuchung.", "7,99 €", "Einmalzahlung für dauerhaften Zugang. Der Preis kann je nach Land variieren; prüfe ihn vor dem Kauf in der App."),
        "it": ("Sette giorni, tutte le funzioni.", "Prova Amano senza limiti di documenti o cartelle. I documenti salvati restano consultabili dopo la prova. Nessun addebito automatico.", "7,99 €", "Un solo pagamento per l’accesso a vita. Il prezzo può variare in base al Paese; controllalo nell’app prima dell’acquisto."),
        "pt": ("Sete dias, todas as funcionalidades.", "Experimente o Amano sem limites de documentos ou pastas. Os documentos guardados continuam acessíveis após o teste. Sem cobrança automática.", "7,99 €", "Um único pagamento para acesso vitalício. O preço pode variar consoante o país; consulte-o na app antes da compra."),
        "tr": ("Yedi gün, tüm özellikler.", "Amano’yu belge veya klasör sınırı olmadan deneyin. Kayıtlı belgelerinizi deneme sonrasında da görebilirsiniz. Otomatik ücret yok.", "€7.99", "Ömür boyu erişim için tek ödeme. Fiyat ülkeye göre değişebilir; satın almadan önce uygulamada kontrol edin."),
    }[key]
    steps = {
        "en": ("7-day trial", "Amano forever"), "es": ("Prueba de 7 días", "Amano para siempre"),
        "fr": ("Essai de 7 jours", "Amano à vie"), "de": ("7 Tage testen", "Amano für immer"),
        "it": ("Prova di 7 giorni", "Amano per sempre"), "pt": ("Teste de 7 dias", "Amano para sempre"),
        "tr": ("7 günlük deneme", "Ömür boyu Amano"),
    }[key]
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
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..650,100&family=Instrument+Sans:wght@400;500;600&display=swap">
<script type="application/ld+json">{faq_jsonld(s)}</script>
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="wordmark" href="{canon}">amano</a>
    <a href="{store}" aria-label="{s['getapp']}"><img class="badge" src="{root}assets/badges/{key}.svg" alt="{badge}" width="120" height="40"></a>
  </header>
  <section class="hero">
    <div>
      <span class="eyebrow">Amano · iPhone</span>
      <h1>{s['h1']}</h1>
      <p class="lede">{s['lede']}</p>
      <div class="cta-row">
        <a href="{store}" aria-label="{badge}"><img class="badge badge-hero" src="{root}assets/badges/{key}.svg" alt="{badge}" width="174" height="58"></a>
        <p class="cta-note">{s['ctanote']}</p>
      </div>
    </div>
    <div class="hero-visual">
      <img src="{root}assets/phones/{key}/folders.webp?v=a3cd617" alt="{s['heroalt']}" width="900" height="1200" fetchpriority="high">
    </div>
  </section>
  <section class="chapters">
    {chapters}
  </section>
</div>
<section class="promise">
  <div class="inner">
    <h2>{s['ph2']}</h2>
    <p>{s['f1p']}</p>
    <span class="price">{s['price']}</span>
  </div>
</section>
<div class="wrap">
  <section class="pricing" id="pricing">
    <h2>{trial[0]}</h2>
    <div class="cols">
      <div class="col"><h3>01 / {steps[0]}</h3><p>{trial[1]}</p></div>
      <div class="col main"><h3>02 / {steps[1]}</h3><div class="num">{trial[2]}</div><p>{trial[3]}</p>
        <a href="{store}" aria-label="{badge}"><img class="badge badge-hero" src="{root}assets/badges/{key}.svg" alt="{badge}" width="174" height="58"></a></div>
    </div>
  </section>
  <section class="faq">
    <h2>{s['faqh2']}</h2>
    <div class="qa">{faqs}</div>
  </section>
</div>
<footer>
  <div class="wrap">
    <span>&copy; 2026 Amano &middot; {s['made']} &middot; <a class="mail" href="mailto:dani@getamano.app">dani@getamano.app</a></span>
    <span>
      <a href="{BASE}privacy/">{s['privacy']}</a>
      <a href="{BASE}terms/">{s['terms']}</a>
      <a href="{BASE}support/">{s['support']}</a>
      <a href="https://apps.apple.com/app/apple-store/id6809212902?action=write-review">{s['review']}</a>
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

for extra in ["privacy/", "terms/", "support/", "support/sync-two-devices/"]:
    urls.append(BASE + extra)
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
sitemap += "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
print("wrote sitemap.xml, robots.txt")
