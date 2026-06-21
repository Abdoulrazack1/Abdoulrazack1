<h1 align="center">Abdoulrazack Abdillahi Mahamoud</h1>

<p align="center">
  <b>Développeur Full-Stack</b> — JavaScript · Node.js · PHP · MySQL
</p>

<p align="center">
  🌱 <b>En recherche d'alternance (18 mois)</b> — Concepteur Développeur d'Applications, spécialisation <b>éco-conception</b>
</p>

<p align="center">
  <i>Également ouvert à toute opportunité — stage, CDD, CDI junior, freelance</i>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/abdoulrazack-abdillahi-mahamoud/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Abdoulrazack%20Abdillahi-0A66C2?style=flat-square&logo=linkedin&logoColor=white">
  </a>
  <a href="mailto:abdoul.abdillahi@gmail.com">
    <img alt="Email" src="https://img.shields.io/badge/Email-abdoul.abdillahi%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white">
  </a>
  <img alt="Location" src="https://img.shields.io/badge/Lille%2C%20France-remote%20nationwide-2E7D32?style=flat-square&logo=googlemaps&logoColor=white">
  <img alt="Status" src="https://img.shields.io/badge/Recherche-Alternance%20CDA%20%C3%89co--conception-1B6E45?style=flat-square">
  <img alt="Open to work" src="https://img.shields.io/badge/Ouvert%20%C3%A0-toutes%20opportunit%C3%A9s-1976D2?style=flat-square">
  <img alt="DWWM" src="https://img.shields.io/badge/Certifi%C3%A9-DWWM-2E7D32?style=flat-square&logo=javascript&logoColor=white">
</p>

<p align="center">
  <img alt="Profile views" src="https://komarev.com/ghpvc/?username=Abdoulrazack1&style=flat-square&color=1B6E45&label=Profile+views" />
  <img alt="Followers" src="https://img.shields.io/github/followers/Abdoulrazack1?style=flat-square&color=1B6E45&logo=github&label=Followers" />
  <img alt="Stars" src="https://img.shields.io/github/stars/Abdoulrazack1?style=flat-square&color=1B6E45&logo=github&label=Total%20stars" />
</p>

---

## À propos · About

> **FR** — Développeur full-stack diplômé du **titre professionnel DWWM** (Lille), avec un Master en **Économie et Management Publics**. Je conçois et livre des applications web complètes — APIs REST, e-commerce, sport, outils pour développeurs, intégrations IA — en privilégiant un **code léger en JavaScript natif**, une **architecture en couches** et des **applications qui tournent vraiment en production**.
>
> Je me spécialise aujourd'hui en **éco-conception / sobriété numérique** : pages légères, performances optimisées et empreinte environnementale réduite dès la conception.

> **EN** — Full-stack developer (DWWM certified, Lille) with a Master's in Public Economics. I design and ship complete web apps — REST APIs, e-commerce, sports tech, developer tooling, AI integrations — favouring lightweight vanilla JavaScript, layered architecture and apps that actually run in production.
>
> Currently specialising in **eco-design / digital sobriety**: lean pages, optimised performance and a lower environmental footprint by design.

---

## Projets phares · Featured projects

### Tsundoku — Blog & chroniques manga · *en production* 🚀
> Application full-stack **déployée en production** : chroniques et critiques manga, intégrations **Anilist** & **Inko**, génération audio par **voix neuronale (Edge-TTS)** pour écouter les articles, et espace d'administration.
>
> **Stack** · Node.js · Express · MySQL · JavaScript natif · APIs REST · Edge-TTS
> **Highlights** · architecture en couches (front / API / BDD) · front léger en JS natif · hébergement Render + base MySQL Aiven
>
> → **Live** : [tsundoku-s6lz.onrender.com](https://tsundoku-s6lz.onrender.com) · **Code** : [github.com/Abdoulrazack1/tsundoku](https://github.com/Abdoulrazack1/tsundoku)

### Cycling — Club de Cyclisme de Salouël
> Plateforme web complète pour un club cycliste : gestion des sorties, parsing GPX, intégration **Strava OAuth**, profils altimétriques, météo & élévation via Open-Meteo, itinéraires depuis OpenStreetMap, espace membre et back-office admin.
>
> **Stack** · Node.js · Express · MySQL · JWT · Bcrypt · Multer · Nodemailer · Helmet · Rate-limit · Migrations versionnées · Pino · Vanilla JS / Leaflet
> **Highlights** · 14 tables relationnelles · API REST sécurisée · backups MySQL planifiés · scraper OSM avec mirrors de fallback · tests unitaires & d'intégration
>
> → [github.com/Abdoulrazack1/Cycling](https://github.com/Abdoulrazack1/Cycling)

### Inko — Lecteur de mangas PWA
> Plateforme de lecture manga complète : catalogue **MangaDex** (83 000+ séries) en proxy backend, lecteur intégré (page/scroll/double), bibliothèque personnelle synchronisée (favoris, progression, listes), authentification **JWT** + **bcrypt**, **PWA installable** avec service worker (mode hors-ligne), prêt **Capacitor** pour Android/iOS.
>
> **Stack** · Node.js · Express · MySQL (9 tables) · JWT · Bcrypt · Axios · Vanilla JS · Service Worker · Capacitor
> **Highlights** · 28 endpoints REST · proxy MangaDex avec cache TTL · progression auto-sauvée par chapitre · mode hors-ligne via SW (sobriété réseau)
>
> → [github.com/Abdoulrazack1/Inko](https://github.com/Abdoulrazack1/Inko)

### Js-Ranker — ML-powered JavaScript code quality scorer
> Moteur de notation **Machine Learning** pour évaluer la qualité de fonctions JavaScript : 10 features extraites par analyse **AST** (acorn), modèle entraîné avec **TensorFlow.js**, API REST, CLI et **Quality Gate** pour CI/CD.
>
> **Stack** · Node.js · TensorFlow.js · Acorn (AST) · Express · CLI (commander) · CI/CD
> **Highlights** · entraînement local (~15 s) · analyse depuis URL GitHub ou snippet · pipeline reproductible · dataset versionné
>
> → [github.com/Abdoulrazack1/Js-Ranker](https://github.com/Abdoulrazack1/Js-Ranker)

### Galactic Brain MCP — AI tooling for Claude Desktop
> Serveur **Model Context Protocol** open-source qui expose un ensemble complet d'outils de **mémoire et de raisonnement** à Claude Desktop / Claude Code : indexation de notes, recherche **BM25**, scoring adaptatif, audit de duplicats, raisonnement séquentiel, auto-sync via hooks.
>
> **Stack** · Node.js · TypeScript · @modelcontextprotocol/sdk · Zod · BM25
> **Highlights** · architecture modulaire (core / render / tools) · `brain_brief` / `brain_advise` / `brain_chain` / `brain_critic` · vault Obsidian git-versionné
>
> → [github.com/Abdoulrazack1/galactic-brain-mcp](https://github.com/Abdoulrazack1/galactic-brain-mcp)

### Kinka — E-commerce manga
> Boutique e-commerce de mangas (projet DWWM) : maquette **Figma**, intégration responsive, filtres dynamiques multi-critères, recherche instantanée, **panier hybride** (localStorage invité / MySQL utilisateur connecté), tunnel d'achat complet.
>
> **Stack** · HTML5 · CSS3 · JavaScript ES6+ (no framework) · Node.js · Express · MySQL · JWT · Bcrypt
>
> → [github.com/Abdoulrazack1/Kinka](https://github.com/Abdoulrazack1/Kinka)

<details>
<summary><b>Autres projets · More projects</b></summary>

### Logic-Lens — AI that decodes JavaScript logic
> Transformer Encoder **TensorFlow.js** qui extrait la formule mathématique ou l'invariant logique sous-jacent à n'importe quelle fonction JS. Pipeline : mutations AST (`acorn`) → dataset ~3000 paires → modèle.
> **Stack** · Node.js · TensorFlow.js · Acorn (AST) · Express
> → [github.com/Abdoulrazack1/Logic-Lens](https://github.com/Abdoulrazack1/Logic-Lens)

### PearTech — E-commerce high-tech
> Boutique téléphonie & high-tech : filtres à facettes combinables (marque, prix, OS, stockage), tri sans rechargement, architecture JS orientée composants.
> **Stack** · HTML5 · CSS3 · JavaScript ES6+
> → [github.com/Abdoulrazack1/Peartech](https://github.com/Abdoulrazack1/Peartech)

### Portfolio Pro — Site personnel
> Portfolio one-page 100 % vanilla : **Three.js** (icosaèdre wireframe + exploded view), curseur magnétique, scroll-aware nav, 3D tilt — zéro framework, zéro dépendance, zéro build.
> **Stack** · HTML5 · CSS3 · JavaScript vanilla · Three.js
> → [github.com/Abdoulrazack1/portfolio_pro](https://github.com/Abdoulrazack1/portfolio_pro)

### Safari Frenzy — Mini browser game
> Jeu navigateur pixel-art type Game Boy avec API de scores, niveaux, modes et power-ups. Frontend zéro dépendance, backend Express + SQLite avec fallback JSON.
> **Stack** · HTML5 Canvas · JavaScript vanilla · Node.js · Express · SQLite
> → [github.com/Abdoulrazack1/safari-frenzy](https://github.com/Abdoulrazack1/safari-frenzy)

</details>

---

## Tech stack

**Languages**
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**Frontend**
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Tailwind](https://img.shields.io/badge/Tailwind%20CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=three.js&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)

**Backend**
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![REST API](https://img.shields.io/badge/REST%20API-005571?style=flat-square)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)

**Databases**
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**Éco-conception · AI / ML · Tooling**
![Green IT](https://img.shields.io/badge/Green%20IT%20%2F%20Sobri%C3%A9t%C3%A9-1B6E45?style=flat-square&logo=leaflet&logoColor=white)
![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-7C5CFF?style=flat-square)

**DevOps & Tools**
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)

---

## GitHub stats

<p align="center">
  <img alt="Activity" src="https://github-readme-activity-graph.vercel.app/graph?username=Abdoulrazack1&theme=github-compact&hide_border=true&area=true&radius=8&color=1B6E45&line=1B6E45&point=ffffff" />
</p>

<p align="center">
  <img alt="Streak" src="https://streak-stats.demolab.com?user=Abdoulrazack1&hide_border=true&theme=github-dark-blue" />
</p>

<!-- Cartes générées par lowlighter/metrics et committées dans le repo -->
<p align="center">
  <img alt="Metrics" src="./github-metrics.svg" />
</p>

<p align="center">
  <img alt="Languages" src="./github-metrics-langs.svg" />
  <img alt="Achievements" src="./github-metrics-achievements.svg" />
</p>

<p align="center">
  <img alt="Habits" src="./github-metrics-habits.svg" />
</p>

---

## Ce que je cherche · What I'm looking for

**FR** — Je recherche une **alternance de 18 mois** pour préparer le titre **Concepteur Développeur d'Applications (spécialisation éco-conception)** avec Simplon, comme développeur **full-stack** ou **back-end**. Basé à Lille, ouvert au télétravail partout en France. À l'aise pour prendre en charge des features de bout en bout, livrer en intégration continue et m'intégrer dans une équipe et une codebase existantes. Je reste également **ouvert à toute opportunité** — stage, CDD, CDI junior ou mission freelance.

**EN** — Looking for an **18-month apprenticeship (alternance)** to earn the **Application Designer-Developer** title (eco-design specialisation) with Simplon, as a **full-stack** or **back-end** developer. Based in Lille, open to remote across France. Also **open to any opportunity** — internship, fixed-term or junior permanent role, freelance.

---

## Contact

- **LinkedIn** — [linkedin.com/in/abdoulrazack-abdillahi-mahamoud](https://www.linkedin.com/in/abdoulrazack-abdillahi-mahamoud/)
- **Email** — abdoul.abdillahi@gmail.com
- **Localisation** — Lille, France · télétravail toute la France
