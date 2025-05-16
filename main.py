import streamlit as st
import pandas as pd
import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()
apiKey = os.getenv("BLOCKCHAIR_API_KEY")

satsBtc = lambda s: s / 100_000_000

def blockchairRequest(address, startDate, endDate):
    staticUrl = "https://api.blockchair.com/bitcoin/dashboards/address/"
    queryUrl = f"{staticUrl}{address}?transaction_details=true&q=time({startDate}..{endDate})&key={apiKey}"
    try:
        response = requests.get(queryUrl, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Request error: {e}")
        return None

def getSummary(data, address):
    try:
        addressData = data["data"][address]["address"]
        periodData = data["data"][address]["period"]
        contextData = data["context"]

        def clean(value, nullPlaceholder="Not yet spent"):
            return nullPlaceholder if value in [None, "2000-01-01 00:00:00"] else value

        return {
            "Timestamp": contextData["cache"]["since"],
            "Market Price (USD)": float(contextData["market_price_usd"]),
            "Address": str(address),
            "Address Type": str(addressData["type"]),
            "First Seen Receiving": str(clean(addressData["first_seen_receiving"])),
            "Last Seen Receiving": str(clean(addressData["last_seen_receiving"])),
            "First Seen Spending": str(clean(addressData["first_seen_spending"])),
            "Last Seen Spending": str(clean(addressData["last_seen_spending"])),
            "Period Transaction Count": int(periodData["transaction_count"]),
            "Unspent Output Count": int(addressData["unspent_output_count"]),
            "Current Balance (BTC)": satsBtc(addressData["balance"]),
            "Current Balance (USD)": float(addressData["balance_usd"]),
            "Total Received (BTC)": satsBtc(addressData["received"]),
            "Total Received (USD)": float(addressData["received_usd"]),
            "Total Sent (BTC)": satsBtc(addressData["spent"]),
            "Total Sent (USD)": float(addressData["spent_usd"]),
            "Period Start": str(periodData["period_start"]),
            "Period End": str(periodData["period_end"])
        }
    except KeyError as e:
        st.error(f"Missing data field: {e}")
        return None

def getTransactions(data, address):
    try:
        txs = data["data"][address].get("transactions", [])
        if not txs:
            st.warning("No transactions found for this period.")
            return pd.DataFrame(columns=["Block Height", "Transaction Time", "Txid", "Amount", "Direction"])

        return pd.DataFrame([{
            "Block Height": tx["block_id"],
            "Transaction Time": tx["time"],
            "Txid": tx["hash"],
            "Amount": satsBtc(tx.get("balance_change", 0)),
            "Direction": "Received" if tx.get("balance_change", 0) > 0 else "Sent"
        } for tx in txs])

    except KeyError as e:
        st.error(f"Transaction error: {e}")
        return pd.DataFrame()

def toExcel(summaryDf, transactionsDf):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        summaryDf.to_excel(writer, sheet_name="Summary", index=False)
        transactionsDf.to_excel(writer, sheet_name="Transactions", index=False)
    return output.getvalue()

st.title("SAT-1 Bitcoin Address Report")

address = st.text_input("Bitcoin Address")
startDate = st.date_input("Start Date")
endDate = st.date_input("End Date")

if st.button("Generate Report"):
    if not all([address, startDate, endDate, apiKey]):
        st.error("Please fill out all fields and ensure API key is set in .env file.")
    else:
        data = blockchairRequest(address, startDate, endDate)
        if data:
            summary = getSummary(data, address)
            if summary:
                summaryDf = pd.DataFrame(summary.items(), columns=["Field", "Value"])
                transactionsDf = getTransactions(data, address)

                st.subheader("Summary")
                st.dataframe(summaryDf, use_container_width=True)

                st.subheader("Transactions")
                st.dataframe(transactionsDf, use_container_width=True)

                excelBytes = toExcel(summaryDf, transactionsDf)
                st.download_button(
                    label="Download Excel Report",
                    data=excelBytes,
                    file_name=f"verified_sat_report_{address}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )