# E-commerce Customer Segmentation

An explainable RFM and clustering pipeline for the public Olist e-commerce dataset. The project turns exploratory customer analysis into reusable, testable code suitable for a Data Science portfolio.

## Business question

How can an e-commerce team group customers by recency, frequency and monetary value to adapt retention campaigns without exposing personal data?

## Workflow

```text
public Olist tables → order-level joins → RFM features → scaling → K-means → segment profile
```

## Quick start

```bash
python -m venv .venv
pip install -e .[dev]
pytest
jupyter lab notebooks/customer_segmentation.ipynb
```

Raw Olist CSVs belong in `data/raw/` and are never committed. The repository contains no database credentials and does not require MariaDB.

## Engineering choices

- deterministic feature dates and random seeds;
- explicit validation of required columns;
- separate RFM feature engineering and clustering;
- synthetic tests that exercise customer histories safely;
- MIT-licensed code, with source datasets governed separately.

## License

Released under the [MIT License](LICENSE).
