import pandas as pd


REQUIRED = {"customer_id", "order_id", "order_date", "payment_value"}


def build_rfm(orders: pd.DataFrame, reference_date: str | pd.Timestamp) -> pd.DataFrame:
    missing = REQUIRED - set(orders.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    data = orders.copy()
    data["order_date"] = pd.to_datetime(data["order_date"], errors="raise")
    reference = pd.Timestamp(reference_date)
    grouped = data.groupby("customer_id")
    rfm = grouped.agg(
        recency=("order_date", lambda values: (reference - values.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("payment_value", "sum"),
    )
    return rfm.sort_index()


def cluster_rfm(rfm: pd.DataFrame, clusters: int = 4, random_state: int = 42) -> pd.DataFrame:
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    if clusters < 2 or clusters > len(rfm):
        raise ValueError("clusters must be between 2 and the number of customers")
    features = rfm[["recency", "frequency", "monetary"]]
    labels = KMeans(n_clusters=clusters, random_state=random_state, n_init="auto").fit_predict(
        StandardScaler().fit_transform(features)
    )
    result = rfm.copy()
    result["cluster"] = labels
    return result
