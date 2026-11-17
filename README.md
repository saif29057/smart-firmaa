# Smart Firma — Smart agriculture platform

A web platform that helps farmers decide **what to plant** and **keep their crops healthy**: crop recommendation from soil and weather data, plant-disease detection from leaf photos, real-time weather, agricultural news and an AI chatbot.

## Features

- **Crop recommendation** — a Random Forest model recommends the best crop from soil nutrients and weather conditions.
- **Plant disease detection** — a CNN classifies leaf images uploaded by the user.
- **Real-time weather** — OpenWeather API.
- **AI chatbot** — GPT-3.5 assistant for agronomy questions.
- **News & messaging** — agricultural news feed and messaging between users.
- **Authentication** — accounts and protected routes.

## Architecture

```
React / TypeScript (pages, components, Axios services, AuthContext)
                │  REST
Django REST Framework apps: authentication · weather · news · analysis · crops · chatbot · messaging
                │
SQLite · uploaded images · crop_model.pkl (Random Forest) · plant_disease_cnn.h5 (CNN)
```

More detail in [ARCHITECTURE.md](ARCHITECTURE.md), [API_DOCUMENTATION.md](API_DOCUMENTATION.md), [UML_DESIGN.md](UML_DESIGN.md) and [SPRINTS.md](SPRINTS.md).

## Project structure

| Folder / file | Content |
| --- | --- |
| `backend/` | Django REST Framework API and ML models |
| `frontend/` | React + TypeScript interface |
| `docs/` | documentation and diagrams |
| `rapport_pfe_smartfirma.tex` | project report (LaTeX) |

## Tech stack

Python · Django REST Framework · scikit-learn (Random Forest) · TensorFlow/Keras (CNN) · OpenAI API · OpenWeather API · React · TypeScript · SQLite

## Author

**Saif Sbaiti** — final-year engineering student, Data Science & AI, TEK-UP University (Tunisia) · [LinkedIn](https://www.linkedin.com/in/saif-sbaiti-3b9a32360)
