# 📌 Comment pin Inko sur ton profil (action manuelle)

> ⚠️ **Pourquoi pas automatique** : GitHub a retiré l'API GraphQL `updateUserPinnedItems` en 2021. Aucune action `gh` CLI ne le permet. La seule voie automatisable serait l'extension Chrome, mais elle n'était pas connectée au moment de l'action.

## Étapes (30 secondes)

1. **Va sur ton profil** : https://github.com/Abdoulrazack1
2. Clique **"Customize your pins"** (bouton en haut à droite de la section "Pinned")
3. **Décoche** `Portfolio` (l'ancien, déprécié — il a une banner redirect vers `portfolio_pro`)
4. **Coche** `Inko`
5. (optionnel) **Réorganise** par drag-drop dans cet ordre conseillé :
   1. **Cycling** — flagship full-stack
   2. **Inko** — nouveau, multi-plateforme
   3. **Logic-Lens** — wow-effect ML
   4. **Js-Ranker** — outil dev ML
   5. **Kinka** — gros DWWM e-commerce
   6. **safari-frenzy** — créatif/ludique
6. Clique **Save pins**

## État cible

```
┌─────────────┬─────────────┬─────────────┐
│  Cycling    │    Inko     │ Logic-Lens  │
├─────────────┼─────────────┼─────────────┤
│  Js-Ranker  │   Kinka     │safari-frenzy│
└─────────────┴─────────────┴─────────────┘
```

## Alternatives à considérer

Si tu veux mettre en valeur ton outil le plus stratégique (`galactic-brain-mcp` — 114 outils MCP) ou ton portfolio actuel (`portfolio_pro` — Three.js), tu peux aussi swapper :
- `Kinka` (DWWM, démontre full-stack mais moins original) → `galactic-brain-mcp`
- `safari-frenzy` (sympa mais petit) → `portfolio_pro`

Mais c'est à toi de juger selon ta cible (recruteurs full-stack vs devs IA/MCP).

---

Une fois fait tu peux supprimer ce fichier : `git rm PIN_INKO.md && git commit -m "chore: remove pin guide (done)" && git push`
