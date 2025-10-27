
# Crop Recommendation (Smart Crop Recommendation)

This repository contains a small machine-learning demo for recommending crops based on soil and environmental features. It includes two Streamlit apps:

- `app.py` — a simple single-input Streamlit app that loads a pickled model (`crop_model.pkl`) and predicts the best crop for given inputs.
- `app_with_chat.py` — a more advanced Streamlit app with batch prediction, a simple rule-based chat assistant, model upload support, and utilities to generate a sample dataset (`dataset.csv`).

## Files

- `app.py` — minimal Streamlit UI for single predictions.
- `app_with_chat.py` — full demo with batch predictions, chat assistant, model/data management, and quick dataset generator.
- `Crop_recommendation.csv`, `dataset.csv` — example datasets (if present).
- `crop_model.pkl` — the trained model file (not included). The apps expect a model saved with `pickle`. `app_with_chat.py` supports both a dict containing `{'model': model, 'label_encoder': le}` and a plain model object for backward compatibility.

## Quick setup (Windows / PowerShell)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app (choose one):

```powershell
# Run the simple single-input app
streamlit run app.py

# Or run the full demo with chat and batch prediction
streamlit run app_with_chat.py
```

Notes:
- The apps expect a trained model file named `crop_model.pkl` in the project root. `app_with_chat.py` allows uploading a model via the sidebar (it will save as `crop_model_uploaded.pkl`).
- If you don't have a model, `app_with_chat.py` can generate a sample dataset (`dataset.csv`) from the sidebar which you can use to train a model externally.

## Input columns

Both apps expect the following features in this order when performing batch predictions or when parsing values:

- `N` — Nitrogen
- `P` — Phosphorus
- `K` — Potassium
- `temperature` — temperature (°C)
- `humidity` — humidity (%)
- `ph` — soil pH
- `rainfall` — rainfall (mm)

When uploading a CSV for batch predictions, ensure those columns are present with these exact names.

## About the Chat Assistant (in `app_with_chat.py`)

The chat assistant is rule-based and can:

- Provide simple agricultural tips (irrigation, harvesting, crop characteristics).
- Attempt to extract numeric feature values from a user message (N,P,K,temperature,humidity,pH,rainfall) and call the loaded model to return a recommendation if enough numbers are present and a model is loaded.

It is not connected to external LLMs — responses are generated using simple pattern matching and local rules.

## Creating a model

This repository does not include a training script by default. You can train a scikit-learn model using `dataset.csv` or your own labelled data and then save it with `pickle`:

```python
import pickle
# model = <your trained sklearn model>
# optionally, save {'model': model, 'label_encoder': le}
with open('crop_model.pkl', 'wb') as f:
	pickle.dump(model, f)
```

If your model's predictions need to be converted from encoded labels to strings, save a label encoder as `{'model': model, 'label_encoder': le}` so `app_with_chat.py` can invert predictions.

## Requirements

See `requirements.txt` for the package list used by the apps.

## Troubleshooting

- If Streamlit fails to start, ensure your virtual environment is activated and dependencies are installed.
- If the app reports "No model found", create or upload `crop_model.pkl` (or upload via the sidebar in `app_with_chat.py`).
- For CSV upload issues, make sure the file is a valid CSV and contains the required columns.

## License

This repository is provided as-is for educational/demo purposes. Feel free to adapt and extend it.

## Next steps / suggestions

- Add a `train_model.py` script to train a model from `dataset.csv` and save `crop_model.pkl` automatically.
- Add tests or a CI pipeline to validate model loading and predictions.
- Consider adding instructions for exporting a model from popular frameworks if the app will support them.

---
Generated README — updated to describe the project, usage, and quick setup.
