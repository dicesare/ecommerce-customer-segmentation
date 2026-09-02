# Historical experiment inventory

## Repository evolution

`master` contained the original end-to-end segmentation notebook. The `dev` branch expanded it into six analytical notebooks plus a MariaDB connectivity experiment. The public repository separates those concerns into reusable code, case studies and a secure data contract.

| Historical notebook | Competency demonstrated |
|---|---|
| main segmentation notebook | complete business-to-model workflow |
| `..._RFM.ipynb` | joining Olist tables, quality analysis, RFM engineering and business segment labels |
| `..._exploration_RFM.ipynb` | distributions, outliers and feature interpretation |
| `..._Cluster.ipynb` | scaling, dimensionality reduction and cluster evaluation |
| `..._Cluster_score_review.ipynb` | satisfaction score added to the behavioral representation |
| `..._simulation.ipynb` | temporal stability, cohort evolution and adjusted Rand monitoring |
| `..._essais.ipynb` | discarded alternatives and iterative experimentation |
| `connect_mariadb.ipynb` | original database access, replaced publicly by an injected data contract |

## Verified data scale

The prepared dataframe shown in the simulation notebook contained **111,151 rows**, 36 joined columns and **95,380 unique customers**. The work explicitly inspected missing values, duplicated order/customer relationships, cancelled or unavailable orders, timestamps, prices and review scores.

## RFM and business interpretation

The RFM notebook calculates:

- Recency from the last purchase to the maximum observable date;
- Frequency as order count;
- Monetary value as accumulated product price;
- review Score as a separate satisfaction signal.

Quintile scores are translated into ten named marketing segments rather than exposing anonymous cluster numbers to stakeholders.

## Temporal model monitoring

The simulation notebook is especially relevant to current ML practice. It:

1. builds two-week observation periods;
2. recalculates RFM+Score at each deadline;
3. fits a reference scaler and four-cluster KMeans model at time zero;
4. refits comparison models as new data arrives;
5. calculates adjusted Rand index between reference and new assignments;
6. repeats the analysis on both growing populations and fixed initial cohorts.

The first historical window begins on **30 April 2017** with 8,973 observed customers. Coverage grows to more than 63,000 during 2018 before the dataset collection tail declines. Alternative cohorts begin with 16,138 and 24,446 customers to test sensitivity to the initial period.

The historical plots do not expose their raw ARI coordinates as text outputs, so this public version documents the exact monitoring protocol rather than inventing numeric stability claims.

## Portfolio interpretation

This work demonstrates feature engineering, unsupervised learning, customer analytics, time-aware validation, drift monitoring and stakeholder-oriented segment naming. These are presented as current competencies even though the source project originated in a training programme.

