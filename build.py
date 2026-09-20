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
    lede="Every document you or your family needs, scanned into one encrypted app. Upgrade to Unlimited for advance expiry reminders.",
    ctanote="Free to start. No subscriptions, ever. <strong>$12.99 / 12,99&nbsp;€ once — yours forever.</strong>",
    figcap="Thirty-five seconds: three photos become one PDF, watermarked, shared.",
    f1h="Private by design", f1p="No account needed. Your documents stay on your device and, with Unlimited sync enabled, in your own iCloud, behind Face&nbsp;ID if you want it.",
    f2h="It reads the expiry date for you", f2p="Save a passport, permit or policy and Amano finds the renewal date on the document itself — no typing — then reminds you in time to renew. No more silent lapses.",
    f3h="Sign it on your phone", f3p="Draw or type your signature, place it on the page, and send a signed copy. The original stays untouched.",
    f4h="Watermark every copy", f4p="With Unlimited, mark a copy with its recipient and purpose: “For the gym”, “Rental only”. Your original stays unchanged.",
    f5h="Many files, one PDF", f5p="Photos and PDFs become one ordered document — contracts, receipts, school forms — ready to share.",
    f6h="Share safely, from your phone", f6p="Review every page and file before it leaves your iPhone. Family folders keep shared paperwork in one place.",
    ph2="Your documents stay yours.",
    pp="Your document contents stay on your device or in your own iCloud. RevenueCat processes purchase information to unlock Unlimited, restore purchases and measure sales. Apple Ads attribution helps measure ad performance.",
    price="Free to start &middot; everything forever for one payment of $12.99 / 12,99 €",
    made="made by M&amp;D in Madrid", privacy="Privacy", terms="Terms", support="Support", review="Write a review", heroalt="The Amano vault on an iPhone", tagfree="Free for everyone", tagunl="Included with Unlimited", alsoh="Also in Amano", freeh="Start free", freep="Scan or import five documents and organize them in two folders for free. Advance reminders are included with Unlimited.", store="App&nbsp;Store",
    videolabel="Amano turning three photos into one watermarked PDF and sharing it",
    shotsh2="A look inside",
    shotsalt=["Renewals screen reminding about an expiring passport", "Placing a signature on a document page", "A shared family folder with travel documents"],
    shotcaps=["Confirm the expiry date Amano finds. Set a reminder to renew.", "Draw or type your signature, place it on the page, and share a clean copy.", "Share a folder with your family. Keep your private files separate."],
    faqh2="Questions, answered",
    faq=[
        ("What do I get for free?", "Five documents, two folders, scanning and import, merging files into PDFs, signatures, expiry dates, a contact card with QR code, Face ID protection and widgets. Advance reminders require Unlimited. Vaults containing documents when first opened in version 1.3.2 keep their ten-document allowance; empty vaults start with five. Folders remain two."),
        ("Where are my documents stored?", "On your iPhone, encrypted — and, if you turn on sync, in your own iCloud."),
        ("What happens if I lose my phone?", "With iCloud sync on (part of Unlimited), your vault is waiting on your next iPhone. Without it, documents live only on the device — that is the trade-off of fully local storage."),
        ("What exactly does the one payment include?", "Everything, forever: unlimited documents, folders and subfolders, iCloud sync and backup, shared family folders, expiry reminders, personal watermarks, document packs and Event mode. No subscription, ever."),
        ("Do I need to create an account?", "No. Amano works the moment you open it. There is nothing to sign up for."),
    ],
    painh2="Sound familiar?",
    pains=[
        ("&ldquo;Where&rsquo;s the passport?&rdquo;",
         "At a counter, scrolling months of camera roll for a document you know you photographed. In Amano it&rsquo;s one search away — behind Face&nbsp;ID, in folders that make sense."),
        ("&ldquo;It expired last month.&rdquo;",
         "Amano reads the expiry date when you save. Unlimited adds advance reminders for IDs, policies and permits."),
        ("&ldquo;I emailed my ID&hellip; who has it now?&rdquo;",
         "With Unlimited, add a visible purpose to the copy you share, such as &ldquo;rental application only&rdquo;. Your original stays unchanged."),
    ],
    priceh2="One price. Once.",
    freecolh="Free", unlcolh="Unlimited",
    pricefree=["3 documents &amp; 2 folders", "Scanning, import &amp; PDF merging", "Signatures &amp; expiry dates", "Contact card &amp; QR code", "Face ID &amp; widgets"],
    pricenum="$12.99", priceonce="one payment — yours forever",
    priceunl=["Unlimited documents &amp; folders", "Advance expiry reminders", "iCloud sync &amp; backup", "Shared family folders", "Personal watermarks", "Document packs &amp; Event mode"],
    pricenote="No subscription. No ads. No accounts. Pricing varies slightly by region (12,99&nbsp;€ in Europe).",
    scanh="Scan it once. Find it forever.",
    scanp="Point the camera at any paper — or import from Photos, Files and other apps. Several photos become one tidy PDF, filed where you&rsquo;ll actually find it, behind Face&nbsp;ID.",
    wmh="Share a copy with a clear purpose.",
    wmp="Add the recipient and intended use as a visible watermark: &ldquo;rental application only&rdquo;, &ldquo;for the gym&rdquo;. Your original stays unchanged.",
    wmalt="A shared ID copy with a personal watermark across it",

),
"es": dict(
    title="Amano — Documentos privados",
    desc="Amano es un espacio privado para los documentos que importan: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    getapp="Descargar la app",
    h1="Lo importante, <em>a mano.</em>",
    lede="Amano es un espacio privado para los documentos que importan: escaneados, organizados, renovados a tiempo y compartidos solo en tus términos. En tu iPhone y en tu iCloud. En ningún otro sitio.",
    ctanote="Empieza gratis, sin suscripciones — nunca. <strong>Un solo pago de 12,99 € y es tuya para siempre.</strong>",
    figcap="Treinta y cinco segundos: tres fotos se convierten en un PDF, con marca de agua, compartido.",
    f1h="Privacidad desde el principio", f1p="Tus documentos permanecen en tu dispositivo y, con la sincronización de Unlimited, en tu iCloud. Face&nbsp;ID protege el acceso.",
    f2h="Renovado a tiempo", f2p="Amano lee la fecha de caducidad al guardar un documento y te avisa antes de que caduquen pasaportes, permisos y pólizas.",
    f3h="Fírmalo desde el móvil", f3p="Dibuja o escribe tu firma, colócala en la página y envía una copia firmada. El original no cambia.",
    f4h="Marca de agua en cada copia", f4p="Con Unlimited, marca una copia con su destinatario y propósito. El original no cambia.",
    f5h="Varios archivos, un solo PDF", f5p="Fotos y PDF se convierten en un único documento ordenado: contratos, recibos, papeles del cole, listos para compartir.",
    f6h="Comparte seguro desde el móvil", f6p="Revisa cada página y cada archivo antes de que salga de tu iPhone. Las carpetas familiares reúnen el papeleo compartido.",
    ph2="Tus documentos siguen siendo tuyos.",
    pp="RevenueCat procesa información de compras para activar Unlimited, restaurar compras y medir ventas. La atribución de Apple Ads mide el rendimiento de los anuncios. El contenido de tus documentos permanece en tu dispositivo o iCloud.",
    price="Empieza gratis &middot; todo, para siempre, por un solo pago de 12,99 €",
    made="hecho por M&amp;D en Madrid", privacy="Privacidad", terms="Condiciones", support="Ayuda", review="Escribe una reseña", heroalt="El espacio de Amano en un iPhone", tagfree="Gratis para todos", tagunl="Incluido en Unlimited", alsoh="Y además, en Amano", freeh="Empieza gratis", freep="Escanea o importa cinco documentos y organízalos en dos carpetas gratis. Los recordatorios anticipados requieren Unlimited.", store="App&nbsp;Store",
    videolabel="Amano convirtiendo tres fotos en un PDF con marca de agua y compartiéndolo",
    shotsh2="Un vistazo por dentro",
    shotsalt=["Pantalla de renovaciones avisando de un pasaporte a punto de caducar", "Colocando una firma en la página de un documento", "Una carpeta familiar compartida con documentos de viaje"],
    shotcaps=["Confirma la fecha que detecta Amano. Activa un recordatorio para renovar.", "Dibuja o escribe tu firma, colócala en la página y comparte una copia limpia.", "Comparte una carpeta con tu familia. Tus archivos privados, por separado."],
    faqh2="Preguntas, respondidas",
    faq=[
        ("¿Qué incluye la versión gratuita?", "Cinco documentos, dos carpetas, escaneo e importación, unión en PDF, firmas, fechas de caducidad, tarjeta de contacto con QR, Face ID y widgets. Los recordatorios anticipados requieren Unlimited. Los espacios con documentos al abrirse por primera vez en 1.3.2 conservan diez; los vacíos empiezan con cinco. Siempre dos carpetas."),
        ("¿Dónde se guardan mis documentos?", "En tu iPhone, cifrados; y si activas la sincronización, en tu propio iCloud."),
        ("¿Qué pasa si pierdo el móvil?", "Con la sincronización de iCloud activada (parte de Unlimited), tu espacio te espera en tu siguiente iPhone. Sin ella, los documentos viven solo en el dispositivo: es la contrapartida del almacenamiento totalmente local."),
        ("¿Qué incluye exactamente el pago único?", "Todo, para siempre: documentos ilimitados, carpetas y subcarpetas, sincronización y copia en iCloud, carpetas familiares compartidas, recordatorios de caducidad, marcas de agua personales, dosieres y el modo evento. Sin suscripción, nunca."),
        ("¿Necesito crear una cuenta?", "No. Amano funciona desde el momento en que lo abres. No hay nada que registrar."),
    ],
),
"fr": dict(
    title="Amano — Documents privés",
    desc="Amano est un espace privé pour les documents qui comptent : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    getapp="Obtenir l’app",
    h1="L’essentiel, <em>à portée de main.</em>",
    lede="Amano est un espace privé pour les documents qui comptent : scannés, organisés, renouvelés à temps et partagés uniquement selon tes conditions. Sur ton iPhone et dans ton iCloud. Nulle part ailleurs.",
    ctanote="Commence gratuitement, jamais d’abonnement. <strong>Un seul paiement de 12,99 € — à toi pour toujours.</strong>",
    figcap="Trente-cinq secondes : trois photos deviennent un PDF, filigrané, partagé.",
    f1h="Privé dès la conception", f1p="Tes documents restent sur ton appareil et, avec la synchronisation Unlimited, dans ton iCloud. Face&nbsp;ID protège l’accès.",
    f2h="Renouvelé à temps", f2p="Amano lit la date d’échéance quand tu enregistres un document et te prévient avant que passeports, permis et contrats n’expirent.",
    f3h="Signe depuis ton iPhone", f3p="Dessine ou tape ta signature, place-la sur la page et envoie une copie signée. L’original ne change pas.",
    f4h="Un filigrane sur chaque copie", f4p="Avec Unlimited, indique le destinataire et l’usage sur la copie. L’original ne change pas.",
    f5h="Plusieurs fichiers, un seul PDF", f5p="Photos et PDF deviennent un document unique et ordonné : contrats, reçus, papiers d’école, prêts à partager.",
    f6h="Partage en sécurité, depuis le téléphone", f6p="Vérifie chaque page et chaque fichier avant qu’il quitte ton iPhone. Les dossiers familiaux réunissent les papiers partagés.",
    ph2="Tes documents restent les tiens.",
    pp="RevenueCat traite les informations d’achat pour activer Unlimited, restaurer les achats et mesurer les ventes. L’attribution Apple Ads mesure les performances publicitaires. Le contenu de tes documents reste sur ton appareil ou dans iCloud.",
    price="Gratuit pour commencer &middot; tout, pour toujours, pour un seul paiement de 12,99 €",
    made="fait par M&amp;D à Madrid", privacy="Confidentialité", terms="Conditions", support="Assistance", review="Laisser un avis", heroalt="Le coffre Amano sur un iPhone", tagfree="Gratuit pour tous", tagunl="Inclus dans Unlimited", alsoh="Et aussi, dans Amano", freeh="Commence gratuitement", freep="Scanne ou importe cinq documents et organise-les dans deux dossiers gratuitement. Les rappels anticipés nécessitent Unlimited.", store="App&nbsp;Store",
    videolabel="Amano transforme trois photos en un PDF filigrané et le partage",
    shotsh2="Un aperçu de l’intérieur",
    shotsalt=["Écran des renouvellements signalant un passeport bientôt expiré", "Pose d’une signature sur la page d’un document", "Un dossier familial partagé avec des documents de voyage"],
    shotcaps=["Confirmez la date repérée par Amano. Activez un rappel de renouvellement.", "Dessine ou tape ta signature, place-la sur la page et partage une copie propre.", "Partagez un dossier avec votre famille. Gardez vos fichiers privés à part."],
    faqh2="Vos questions, nos réponses",
    faq=[
        ("Que comprend la version gratuite ?", "Cinq documents, deux dossiers, numérisation et importation, fusion en PDF, signatures, dates d’échéance, carte de contact avec QR, Face ID et widgets. Les rappels anticipés nécessitent Unlimited. Les espaces contenant des documents à leur première ouverture avec la version 1.3.2 conservent leur limite de dix ; les espaces vides commencent avec cinq. Toujours deux dossiers."),
        ("Où mes documents sont-ils stockés ?", "Sur ton iPhone, chiffrés — et, si tu actives la synchronisation, dans ton propre iCloud."),
        ("Que se passe-t-il si je perds mon téléphone ?", "Avec la synchronisation iCloud activée (incluse dans Unlimited), ton espace t’attend sur ton prochain iPhone. Sans elle, les documents ne vivent que sur l’appareil — c’est la contrepartie d’un stockage entièrement local."),
        ("Que comprend exactement le paiement unique ?", "Tout, pour toujours : documents illimités, dossiers et sous-dossiers, synchronisation et sauvegarde iCloud, dossiers familiaux partagés, rappels d’échéance, filigranes personnels, sélections de documents et mode événement. Jamais d’abonnement."),
        ("Dois-je créer un compte ?", "Non. Amano fonctionne dès l’ouverture. Il n’y a rien à créer."),
    ],
),
"de": dict(
    title="Amano — Private Dokumente",
    desc="Amano ist ein privater Ort für die Dokumente, die zählen: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    getapp="App laden",
    h1="Alles Wichtige, <em>griffbereit.</em>",
    lede="Amano ist ein privater Ort für die Dokumente, die zählen: gescannt, geordnet, rechtzeitig verlängert und nur zu deinen Bedingungen geteilt. Auf deinem iPhone und in deiner iCloud. Nirgendwo sonst.",
    ctanote="Kostenlos starten, nie ein Abo. <strong>Einmal 12,99 € zahlen – für immer deins.</strong>",
    figcap="Fünfunddreißig Sekunden: Drei Fotos werden ein PDF, mit Wasserzeichen, geteilt.",
    f1h="Privat von Grund auf", f1p="Deine Dokumente bleiben auf deinem Gerät und mit Unlimited-Synchronisierung in deiner iCloud. Face&nbsp;ID schützt den Zugriff.",
    f2h="Rechtzeitig verlängert", f2p="Amano liest das Ablaufdatum beim Speichern und erinnert dich, bevor Reisepässe, Ausweise und Policen ablaufen.",
    f3h="Unterschreibe am iPhone", f3p="Zeichne oder tippe deine Unterschrift, platziere sie auf der Seite und sende eine signierte Kopie. Das Original bleibt unverändert.",
    f4h="Wasserzeichen auf jeder Kopie", f4p="Mit Unlimited kennzeichnest du eine Kopie mit Empfänger und Zweck. Das Original bleibt unverändert.",
    f5h="Viele Dateien, ein PDF", f5p="Fotos und PDFs werden ein geordnetes Dokument – Verträge, Belege, Schulunterlagen – bereit zum Teilen.",
    f6h="Sicher teilen, direkt vom Handy", f6p="Prüfe jede Seite und jede Datei, bevor sie dein iPhone verlässt. Familienordner halten gemeinsame Unterlagen an einem Ort.",
    ph2="Deine Dokumente bleiben deine.",
    pp="RevenueCat verarbeitet Kaufdaten, um Unlimited freizuschalten, Käufe wiederherzustellen und Verkäufe auszuwerten. Apple Ads Attribution misst die Anzeigenleistung. Deine Dokumentinhalte bleiben auf deinem Gerät oder in iCloud.",
    price="Kostenlos starten &middot; alles, für immer, für einmalig 12,99 €",
    made="von M&amp;D in Madrid gemacht", privacy="Datenschutz", terms="Bedingungen", support="Support", review="Bewertung schreiben", heroalt="Der Amano-Bereich auf einem iPhone", tagfree="Für alle kostenlos", tagunl="In Unlimited enthalten", alsoh="Außerdem in Amano", freeh="Kostenlos starten", freep="Scanne oder importiere fünf Dokumente und ordne sie kostenlos in zwei Ordnern. Voraberinnerungen erfordern Unlimited.", store="App&nbsp;Store",
    videolabel="Amano macht aus drei Fotos ein PDF mit Wasserzeichen und teilt es",
    shotsh2="Ein Blick hinein",
    shotsalt=["Verlängerungs-Ansicht warnt vor einem ablaufenden Reisepass", "Eine Unterschrift wird auf einer Dokumentseite platziert", "Ein geteilter Familienordner mit Reisedokumenten"],
    shotcaps=["Bestätige das erkannte Ablaufdatum. Lass dich ans Verlängern erinnern.", "Zeichne oder tippe deine Unterschrift, platziere sie auf der Seite und teile eine saubere Kopie.", "Teile einen Ordner mit deiner Familie. Deine privaten Dateien bleiben privat."],
    faqh2="Fragen, beantwortet",
    faq=[
        ("Was ist kostenlos enthalten?", "Fünf Dokumente, zwei Ordner, Scannen und Importieren, Zusammenführen zu PDFs, Unterschriften, Ablaufdaten, Kontaktkarte mit QR-Code, Face ID und Widgets. Voraberinnerungen erfordern Unlimited. Tresore mit Dokumenten beim ersten Öffnen in Version 1.3.2 behalten ihr Limit von zehn; leere Tresore starten mit fünf. Das Ordnerlimit bleibt bei zwei."),
        ("Wo werden meine Dokumente gespeichert?", "Auf deinem iPhone, verschlüsselt — und wenn du die Synchronisierung einschaltest, in deiner eigenen iCloud."),
        ("Was passiert, wenn ich mein iPhone verliere?", "Mit iCloud-Synchronisierung (Teil von Unlimited) wartet dein Bereich auf deinem nächsten iPhone. Ohne sie leben die Dokumente nur auf dem Gerät — das ist der Preis rein lokaler Speicherung."),
        ("Was genau enthält der Einmalkauf?", "Alles, für immer: unbegrenzte Dokumente, Ordner und Unterordner, iCloud-Synchronisierung und Sicherung, gemeinsame Familienordner, Ablauferinnerungen, eigene Wasserzeichen, Dokumentmappen und den Event-Modus. Nie ein Abo."),
        ("Brauche ich ein Konto?", "Nein. Amano funktioniert ab dem ersten Öffnen. Es gibt nichts zu registrieren."),
    ],
),
"it": dict(
    title="Amano — Documenti privati",
    desc="Amano è uno spazio privato per i documenti che contano: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    getapp="Scarica l’app",
    h1="Ciò che conta, <em>a portata di mano.</em>",
    lede="Amano è uno spazio privato per i documenti che contano: scansionati, organizzati, rinnovati in tempo e condivisi solo alle tue condizioni. Sul tuo iPhone e nel tuo iCloud. Da nessun’altra parte.",
    ctanote="Inizia gratis, mai abbonamenti. <strong>Un solo pagamento di 12,99 € — tua per sempre.</strong>",
    figcap="Trentacinque secondi: tre foto diventano un PDF, con filigrana, condiviso.",
    f1h="Privato fin dall’inizio", f1p="I documenti restano sul dispositivo e, con la sincronizzazione Unlimited, nel tuo iCloud. Face&nbsp;ID protegge l’accesso.",
    f2h="Rinnovato in tempo", f2p="Amano legge la scadenza quando salvi un documento e ti avvisa prima che passaporti, patenti e polizze scadano.",
    f3h="Firma dal telefono", f3p="Disegna o digita la firma, posizionala sulla pagina e invia una copia firmata. L’originale non cambia.",
    f4h="Filigrana su ogni copia", f4p="Con Unlimited, indica destinatario e scopo sulla copia. L’originale non cambia.",
    f5h="Tanti file, un solo PDF", f5p="Foto e PDF diventano un unico documento ordinato: contratti, ricevute, moduli della scuola, pronti da condividere.",
    f6h="Condividi in sicurezza dal telefono", f6p="Controlla ogni pagina e ogni file prima che lasci il tuo iPhone. Le cartelle famiglia tengono insieme le pratiche condivise.",
    ph2="I tuoi documenti restano tuoi.",
    pp="RevenueCat elabora i dati degli acquisti per attivare Unlimited, ripristinare gli acquisti e misurare le vendite. L’attribuzione Apple Ads misura il rendimento degli annunci. Il contenuto dei documenti resta sul dispositivo o in iCloud.",
    price="Inizia gratis &middot; tutto, per sempre, con un solo pagamento di 12,99 €",
    made="fatto da M&amp;D a Madrid", privacy="Privacy", terms="Termini", support="Assistenza", review="Scrivi una recensione", heroalt="L’archivio Amano su un iPhone", tagfree="Gratis per tutti", tagunl="Incluso in Unlimited", alsoh="E inoltre, in Amano", freeh="Inizia gratis", freep="Scansiona o importa cinque documenti e organizzali in due cartelle gratis. I promemoria anticipati richiedono Unlimited.", store="App&nbsp;Store",
    videolabel="Amano trasforma tre foto in un PDF con filigrana e lo condivide",
    shotsh2="Uno sguardo dentro",
    shotsalt=["Schermata dei rinnovi che segnala un passaporto in scadenza", "Una firma viene posizionata sulla pagina di un documento", "Una cartella famiglia condivisa con documenti di viaggio"],
    shotcaps=["Conferma la scadenza trovata da Amano. Imposta un promemoria per rinnovare.", "Disegna o digita la tua firma, posizionala sulla pagina e condividi una copia pulita.", "Condividi una cartella con la tua famiglia. I file privati restano a parte."],
    faqh2="Domande, risposte",
    faq=[
        ("Cosa include la versione gratuita?", "Cinque documenti, due cartelle, scansione e importazione, unione in PDF, firme, date di scadenza, scheda contatto con QR, Face ID e widget. I promemoria anticipati richiedono Unlimited. Gli archivi con documenti alla prima apertura nella versione 1.3.2 mantengono il limite di dieci; quelli vuoti iniziano con cinque. Sempre due cartelle."),
        ("Dove sono conservati i miei documenti?", "Sul tuo iPhone, cifrati — e, se attivi la sincronizzazione, nel tuo iCloud."),
        ("Cosa succede se perdo il telefono?", "Con la sincronizzazione iCloud attiva (parte di Unlimited), il tuo archivio ti aspetta sul prossimo iPhone. Senza, i documenti vivono solo sul dispositivo: è il compromesso dell’archiviazione interamente locale."),
        ("Cosa include esattamente il pagamento unico?", "Tutto, per sempre: documenti illimitati, cartelle e sottocartelle, sincronizzazione e backup iCloud, cartelle famiglia condivise, promemoria di scadenza, filigrane personali, raccolte di documenti e la modalità evento. Mai un abbonamento."),
        ("Devo creare un account?", "No. Amano funziona appena lo apri. Non c’è nulla da registrare."),
    ],
),
"pt": dict(
    title="Amano — Documentos privados",
    desc="O Amano é um espaço privado para os documentos que importam: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    getapp="Obter a app",
    h1="O que importa, <em>à mão.</em>",
    lede="O Amano é um espaço privado para os documentos que importam: digitalizados, organizados, renovados a tempo e partilhados apenas nos seus termos. No seu iPhone e no seu iCloud. Em mais lado nenhum.",
    ctanote="Comece grátis, sem subscrições. <strong>Um único pagamento de 12,99 € — sua para sempre.</strong>",
    figcap="Trinta e cinco segundos: três fotos tornam-se um PDF, com marca de água, partilhado.",
    f1h="Privado por conceção", f1p="Os documentos ficam no dispositivo e, com a sincronização Unlimited, no seu iCloud. O Face&nbsp;ID protege o acesso.",
    f2h="Renovado a tempo", f2p="O Amano lê a validade quando guarda um documento e avisa antes que passaportes, cartas e apólices caduquem.",
    f3h="Assine no telemóvel", f3p="Desenhe ou escreva a assinatura, coloque-a na página e envie uma cópia assinada. O original não muda.",
    f4h="Marca de água em cada cópia", f4p="Com Unlimited, marque a cópia com o destinatário e a finalidade. O original não muda.",
    f5h="Vários ficheiros, um só PDF", f5p="Fotos e PDF tornam-se um único documento ordenado: contratos, recibos, papéis da escola, prontos a partilhar.",
    f6h="Partilhe em segurança, do telemóvel", f6p="Reveja cada página e cada ficheiro antes de sair do seu iPhone. As pastas de família juntam a papelada partilhada.",
    ph2="Os seus documentos continuam seus.",
    pp="A RevenueCat processa informações de compras para ativar o Unlimited, restaurar compras e medir vendas. A atribuição Apple Ads mede o desempenho dos anúncios. O conteúdo dos documentos fica no dispositivo ou no iCloud.",
    price="Comece grátis &middot; tudo, para sempre, por um único pagamento de 12,99 €",
    made="feito por M&amp;D em Madrid", privacy="Privacidade", terms="Termos", support="Suporte", review="Escrever uma avaliação", heroalt="O espaço do Amano num iPhone", tagfree="Grátis para todos", tagunl="Incluído no Unlimited", alsoh="E ainda, no Amano", freeh="Comece grátis", freep="Digitalize ou importe cinco documentos e organize-os em duas pastas gratuitamente. Os lembretes antecipados exigem Unlimited.", store="App&nbsp;Store",
    videolabel="O Amano transforma três fotos num PDF com marca de água e partilha-o",
    shotsh2="Um olhar por dentro",
    shotsalt=["Ecrã de renovações a avisar de um passaporte prestes a caducar", "Uma assinatura a ser colocada na página de um documento", "Uma pasta de família partilhada com documentos de viagem"],
    shotcaps=["Confirme a data de validade que o Amano encontra. Defina um lembrete para renovar.", "Desenhe ou escreva a sua assinatura, coloque-a na página e partilhe uma cópia limpa.", "Partilhe uma pasta com a família. Mantenha os ficheiros privados à parte."],
    faqh2="Perguntas, respondidas",
    faq=[
        ("O que inclui a versão gratuita?", "Cinco documentos, duas pastas, digitalização e importação, união em PDF, assinaturas, datas de validade, cartão de contacto com QR, Face ID e widgets. Os lembretes antecipados exigem Unlimited. Os espaços com documentos na primeira abertura na versão 1.3.2 mantêm o limite de dez; os vazios começam com cinco. Sempre duas pastas."),
        ("Onde ficam guardados os meus documentos?", "No seu iPhone, cifrados — e, se ativar a sincronização, no seu próprio iCloud."),
        ("O que acontece se perder o telemóvel?", "Com a sincronização iCloud ativa (parte do Unlimited), o seu espaço espera por si no próximo iPhone. Sem ela, os documentos vivem apenas no dispositivo — é a contrapartida do armazenamento totalmente local."),
        ("O que inclui exatamente o pagamento único?", "Tudo, para sempre: documentos ilimitados, pastas e subpastas, sincronização e cópia iCloud, pastas de família partilhadas, lembretes de validade, marcas de água pessoais, dossiês de documentos e o modo evento. Nunca uma subscrição."),
        ("Preciso de criar uma conta?", "Não. O Amano funciona assim que o abre. Não há nada para registar."),
    ],
),
"tr": dict(
    title="Amano — Özel Belge Kasası",
    desc="Amano, önemli belgeleriniz için özel bir kasa: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    getapp="Uygulamayı edin",
    h1="Önemli olan her şey, <em>elinizin altında.</em>",
    lede="Amano, önemli belgeleriniz için özel bir kasa: taranır, düzenlenir, zamanında yenilenir ve yalnızca sizin koşullarınızla paylaşılır. iPhone’unuzda ve iCloud’unuzda. Başka hiçbir yerde.",
    ctanote="Ücretsiz başlayın, asla abonelik yok. <strong>Tek seferlik ödeme — sonsuza kadar sizin.</strong>",
    figcap="Otuz beş saniye: üç fotoğraf tek bir PDF olur, filigran eklenir, paylaşılır.",
    f1h="Tasarımdan özel", f1p="Belgeleriniz cihazınızda ve Unlimited eşitlemesi ile kendi iCloud’unuzda kalır. Face&nbsp;ID erişimi korur.",
    f2h="Zamanında yenilenir", f2p="Amano bir belgeyi kaydederken son geçerlilik tarihini okur; pasaportlar, ehliyetler ve poliçeler dolmadan önce hatırlatır.",
    f3h="Telefonunuzdan imzalayın", f3p="İmzanızı çizin veya yazın, sayfaya yerleştirin ve imzalı bir kopya gönderin. Orijinal değişmez.",
    f4h="Her kopyaya filigran", f4p="Unlimited ile kopyaya alıcısını ve amacını ekleyin. Orijinal değişmez.",
    f5h="Birçok dosya, tek PDF", f5p="Fotoğraflar ve PDF’ler tek ve düzenli bir belgeye dönüşür: sözleşmeler, makbuzlar, okul evrakı — paylaşıma hazır.",
    f6h="Telefondan güvenle paylaşın", f6p="Her sayfayı ve dosyayı iPhone’unuzdan çıkmadan önce gözden geçirin. Aile klasörleri ortak evrakı bir arada tutar.",
    ph2="Belgeleriniz sizin kalır.",
    pp="RevenueCat, Unlimited’ı açmak, satın alımları geri yüklemek ve satışları ölçmek için satın alma bilgilerini işler. Apple Ads ilişkilendirmesi reklam performansını ölçer. Belge içerikleriniz cihazınızda veya iCloud’da kalır.",
    price="Ücretsiz başlayın &middot; tek seferlik satın almayla her şey, sonsuza kadar",
    made="Madrid'de M&amp;D tarafından yapıldı", privacy="Gizlilik", terms="Koşullar", support="Destek", review="Değerlendirme yaz", heroalt="iPhone’da Amano kasası", tagfree="Herkese ücretsiz", tagunl="Unlimited’a dahil", alsoh="Ayrıca Amano’da", freeh="Ücretsiz başlayın", freep="Beş belgeyi ücretsiz tarayın veya içe aktarın ve iki klasörde düzenleyin. Önceden hatırlatmalar Unlimited gerektirir.", store="App&nbsp;Store",
    videolabel="Amano üç fotoğrafı filigranlı tek bir PDF’e dönüştürüp paylaşıyor",
    shotsh2="İçeriden bir bakış",
    shotsalt=["Yenilemeler ekranı süresi dolmak üzere olan bir pasaportu bildiriyor", "Bir belge sayfasına imza yerleştiriliyor", "Seyahat belgeleriyle paylaşılan bir aile klasörü"],
    shotcaps=["Amano'nun bulduğu tarihi onaylayın. Yenilemek için hatırlatıcı ayarlayın.", "İmzanızı çizin veya yazın, sayfaya yerleştirin ve temiz bir kopya paylaşın.", "Bir klasörü ailenizle paylaşın. Özel dosyalarınız ayrı kalsın."],
    faqh2="Sorular ve yanıtları",
    faq=[
        ("Ücretsiz sürüme neler dahil?", "Beş belge, iki klasör, tarama ve içe aktarma, PDF birleştirme, imzalar, son geçerlilik tarihleri, QR kodlu kişi kartı, Face ID ve araç takımları. Önceden hatırlatmalar Unlimited gerektirir. 1.3.2 sürümünde ilk açılışta belge içeren kasalar on belge sınırını korur; boş kasalar beşle başlar. Klasör sınırı iki olarak kalır."),
        ("Belgelerim nerede saklanıyor?", "iPhone’unuzda, şifrelenmiş olarak — ve eşitlemeyi açarsanız kendi iCloud’unuzda."),
        ("Telefonumu kaybedersem ne olur?", "iCloud eşitleme açıksa (Unlimited’ın parçası), kasanız bir sonraki iPhone’unuzda sizi bekler. Kapalıysa belgeler yalnızca cihazda yaşar — tamamen yerel saklamanın bedeli budur."),
        ("Tek ödeme tam olarak neleri içeriyor?", "Her şeyi, sonsuza dek: sınırsız belge, klasör ve alt klasörler, iCloud eşitleme ve yedekleme, paylaşılan aile klasörleri, süre hatırlatıcıları, kişisel filigranlar, belge dosyaları ve etkinlik modu. Asla abonelik yok."),
        ("Hesap açmam gerekiyor mu?", "Hayır. Amano açtığınız anda çalışır. Kaydolacak bir şey yok."),
    ],
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
  .cta-note { font-size: 22px; color: var(--muted); width: 100%; margin-top: 4px; }
  .cta-note strong { display: block; margin-top: 6px; font-weight: 650; color: #101722; }
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
  .pricing .buy { display: inline-block; margin-top: 16px; background: var(--navy); color: #fff; text-decoration: none; border-radius: 12px; padding: 12px 22px; font-weight: 600; }
  .pricing .pricenote { color: var(--muted); font-size: 14px; margin-top: 14px; }

  .chapter .art video { display: block; width: 100%; height: auto; border-radius: 22px; }
"""

GLYPH1 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>'
GLYPH2 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4M12 13v4M10 15h4"/></svg>'
GLYPH3 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 20l4-1L19 8l-3-3L5 16l-1 4z"/><path d="M13.5 7.5l3 3"/></svg>'
GLYPH4 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 4c3 3.8 5 6.3 5 8.8a5 5 0 0 1-10 0C7 10.3 9 7.8 12 4z"/></svg>'
GLYPH5 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="4" y="3" width="9" height="12" rx="2"/><rect x="11" y="9" width="9" height="12" rx="2"/></svg>'
GLYPH6 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>'

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

def scan_chapter(s, key, root):
    if not s.get("scanh"): return ""
    return (f'<div class="chapter"><div class="art">'
            f'<video src="{root}assets/demo.mp4" poster="{root}assets/poster.jpg" '
            f'muted loop playsinline autoplay preload="metadata" aria-label="{s["videolabel"]}"></video></div>'
            f'<div><span class="chip free">{s["tagfree"]}</span><h2>{s["scanh"]}</h2><p>{s["scanp"]}</p></div></div>')

def wm_chapter(s, key, root):
    if not s.get("wmh"): return ""
    return (f'<div class="chapter"><div class="art">'
            f'<img src="{root}assets/features/{key}/share.webp" alt="{s["wmalt"]}" loading="lazy" width="560" height="918"></div>'
            f'<div><span class="chip unl">{s["tagunl"]}</span><h2>{s["wmh"]}</h2><p>{s["wmp"]}</p></div></div>')

def demo_html(s, root):
    if s.get("scanh"): return ""  # the video already stars in the scan chapter
    return (f'<section class="demo"><figure>'
            f'<video src="{root}assets/demo.mp4" poster="{root}assets/poster.jpg" '
            f'muted loop playsinline autoplay preload="metadata" aria-label="{s["videolabel"]}"></video>'
            f'<figcaption>{s["figcap"]}</figcaption></figure></section>')

def pains_html(s):
    if not s.get("pains"): return ""
    cards = "".join(f'<article class="pain"><h3>{q}</h3><p>{a}</p></article>' for q, a in s["pains"])
    return f'<section class="pains"><h2>{s["painh2"]}</h2><div class="grid">{cards}</div></section>'

def pricing_html(s, store, badge):
    if not s.get("priceh2"): return ""
    free = "".join(f"<li>{x}</li>" for x in s["pricefree"])
    unl = "".join(f"<li>{x}</li>" for x in s["priceunl"])
    return (f'<section class="pricing"><h2>{s["priceh2"]}</h2><div class="cols">'
            f'<div class="col"><h3>{s["freecolh"]}</h3><ul>{free}</ul></div>'
            f'<div class="col main"><h3>{s["unlcolh"]}</h3><div class="num">{s["pricenum"]}</div>'
            f'<div class="once">{s["priceonce"]}</div><ul>{unl}</ul>'
            f'<a class="buy" href="{store}" aria-label="{badge}">{s["getapp"]}</a></div>'
            f'</div><p class="pricenote">{s["pricenote"]}</p></section>')

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
    shots = "".join(
        f'<figure><img src="{root}assets/features/{key}/{name}.webp" alt="{alt}" loading="lazy" width="560" height="918">'
        f'<figcaption>{cap}</figcaption></figure>'
        for name, alt, cap in zip(["renew", "sign"], s["shotsalt"], s["shotcaps"]))
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faq"])
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
      <h1>{s['h1']}</h1>
      <p class="lede">{s['lede']}</p>
      <div class="cta-row">
        <a href="{store}" aria-label="{badge}"><img class="badge badge-hero" src="{root}assets/badges/{key}.svg" alt="{badge}" width="174" height="58"></a>
        <span class="cta-note">{s['ctanote']}</span>
      </div>
    </div>
    <div class="hero-visual">
      <img src="{root}assets/features/{key}/family.webp" alt="{s['heroalt']}" width="560" height="918" fetchpriority="high">
    </div>
  </section>
  {pains_html(s)}
  <section class="chapters">
    {scan_chapter(s, key, root)}
    {wm_chapter(s, key, root)}
    <div class="chapter">
      <div class="art"><img src="{root}assets/features/{key}/renew.webp" alt="{s['shotsalt'][0]}" loading="lazy" width="560" height="918"></div>
      <div>
        <span class="chip unl">{s['tagunl']}</span>
        <h2>{s['f2h']}</h2>
        <p>{s['f2p']}</p>
      </div>
    </div>
    <div class="chapter">
      <div class="art"><img src="{root}assets/features/{key}/sign.webp" alt="{s['shotsalt'][1]}" loading="lazy" width="560" height="918"></div>
      <div>
        <span class="chip free">{s['tagfree']}</span>
        <h2>{s['f3h']}</h2>
        <p>{s['f3p']}</p>
      </div>
    </div>
    <div class="chapter">
      <div class="art"><img src="{root}assets/features/{key}/family.webp" alt="{s['shotsalt'][2]}" loading="lazy" width="560" height="918"></div>
      <div>
        <span class="chip unl">{s['tagunl']}</span>
        <h2>{s['f6h']}</h2>
        <p>{s['f6p']}</p>
      </div>
    </div>
  </section>
  <section class="also">
    <h2>{s['alsoh']}</h2>
    <div class="grid">
      <article class="feature"><div class="glyph">{GLYPH1}</div><h3>{s['f1h']}</h3><p>{s['f1p']}</p></article>
      <article class="feature"><div class="glyph">{GLYPH5}</div><h3>{s['f5h']}</h3><p>{s['f5p']}</p></article>
      <article class="feature"><div class="glyph">{GLYPH2}</div><h3>{s['freeh']}</h3><p>{s['freep']}</p></article>
    </div>
  </section>
  {demo_html(s, root)}
</div>
<section class="promise">
  <div class="inner">
    <h2>{s['ph2']}</h2>
    <p>{s['pp']}</p>
    <span class="price">{s['price']}</span>
  </div>
</section>
<div class="wrap">
  {pricing_html(s, store, badge)}
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
