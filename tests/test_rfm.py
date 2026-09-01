import pandas as pd
import pytest

from customer_segments import build_rfm, cluster_rfm


def sample_orders():
    return pd.DataFrame({
        "customer_id": ["a", "a", "b", "c"],
        "order_id": ["1", "2", "3", "4"],
        "order_date": ["2024-01-01", "2024-01-10", "2024-01-05", "2024-01-09"],
        "payment_value": [10.0, 20.0, 5.0, 50.0],
    })


def test_builds_deterministic_rfm_features():
    rfm = build_rfm(sample_orders(), "2024-01-11")
    assert rfm.loc["a"].to_dict() == {"recency": 1.0, "frequency": 2.0, "monetary": 30.0}


def test_validates_cluster_count():
    with pytest.raises(ValueError, match="clusters"):
        cluster_rfm(build_rfm(sample_orders(), "2024-01-11"), clusters=5)
