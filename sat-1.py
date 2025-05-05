import requests
import pandas as pd

satsBtc = lambda s: s / 100_000_000

def blockchairRequest(address, startDate, endDate, apiKey):
    staticUrl = "https://api.blockchair.com/bitcoin/dashboards/address/"
    queryUrl = f"{staticUrl}{address}?transaction_details=true&q=time({startDate}..{endDate})&key={apiKey}"

    try:
        response = requests.get(queryUrl, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def getSummary(data, address):
    try:
        addressData = data["data"][address]["address"]
        periodData = data["data"][address]["period"]
        contextData = data["context"]

        def clean(value, nullPlaceholder="Not yet spent"):
            return nullPlaceholder if value in [None, "2000-01-01 00:00:00"] else value

        summary = {
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
        return summary
    except KeyError as e:
        print(f"Data field missing: {e}")
        return None

    
def getTransactions(data, address):
    try:
        txs = data["data"][address].get("transactions", [])
        if not txs:
            print("No transactions found for this period.")
            return pd.DataFrame(columns=["Block Height", "Transaction Time", "Txid", "Amount", "Direction"])
        
        transactionHistory = []
        for tx in txs:
            balanceChange = tx.get("balance_change", 0)
            direction = "Received" if balanceChange > 0 else "Sent"
            transactionHistory.append({
                "Block Height": tx["block_id"],
                "Transaction Time": tx["time"],
                "Txid": tx["hash"],
                "Amount": satsBtc(balanceChange),
                "Direction": direction
            })

        df = pd.DataFrame(transactionHistory)
        return df

    except KeyError as e:
        print(f"Transaction error: {e}")
        return pd.DataFrame()


def excelReport(summaryDataframe, transactionsDataframe, filename):
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        summaryDataframe.to_excel(writer, sheet_name="Summary", index=False)
        transactionsDataframe.to_excel(writer, sheet_name="Transactions", index=False)

def main():
    print("SAT-1 Reporting Tool")
    address = ""
    startDate = ""
    endDate = ""
    apiKey = ""

    data = blockchairRequest(address, startDate, endDate, apiKey)
    if not data:
        print("No data was retrieved. Please check the address or API key.")
        return

    summary = getSummary(data, address)
    if not summary:
        print("Summary could not be extracted.")
        return

    transactionsDataframe = getTransactions(data, address)
    summaryDataframe = pd.DataFrame(summary.items(), columns=["Field", "Value"])

    filename = f"verified_sat_report_{address}.xlsx"
    excelReport(summaryDataframe=summaryDataframe, transactionsDataframe=transactionsDataframe, filename=filename)

    print(f"Bitcoin address report saved as '{filename}'")


if __name__ == "__main__":
    main()
