# appV2H – Application Streamlit

Ce dépôt contient l’**application Streamlit** du simulateur énergétique V2H (*Vehicle-to-Home*), développée dans le cadre d’un stage au laboratoire LUCAMI – Université de Ljubljana.

lien vers 1er version de l'app : https://appv2h-juezzmflsjsuvucgecthpd.streamlit.app/
lien vers version optimisée : https://appv2h-bwyfw87l7f2hkcui2o9ru4.streamlit.app/
lien version comparaison : https://appv2h-7jqrlvgtjyd6h7wkjzka6x.streamlit.app/

## 🎯 Objectif

Proposer une interface simple et interactive pour simuler les échanges d’énergie entre :
- un véhicule électrique (VE),
- une maison (consommation horaire),
- une production solaire (PV),
- et le réseau électrique.

L’utilisateur peut choisir :
- son profil de consommation,
- la période de simulation (mois),
- les caractéristiques du VE,
- et visualiser les résultats sous forme de graphiques et tableaux.

## 🗂️ Organisation du projet
appV2H/
├── app/ # Fichiers Streamlit (.py)
├── data/ # Données : profils utilisateurs, PV, tarifs
├── assets/ # Images, logos pour l’interface
├── .streamlit/ # Fichiers de configuration Streamlit (layout, thème)
├── requirements.txt # Librairies Python nécessaires
├── CHANGELOG.md # Suivi des versions de l'app
└── README.md


