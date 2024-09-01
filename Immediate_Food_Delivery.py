import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    DF = delivery[(delivery['order_date'] == delivery['customer_pref_delivery_date'])]
    res = round((len(DF)/len(delivery))*100,2)

    return pd.DataFrame({"immediate_percentage": [res]})