# Standard for Address Transparency: reference implementation for institutional-grade reporting over address-level Bitcoin holdings and transactional data.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/user_interface-built%20with%20streamlit-orange)](https://streamlit.io)
[![Blockchair API](https://img.shields.io/badge/data-Blockchair%20API-brightgreen)](https://blockchair.com/api/)

## 🎯 Application Purpose

Under IFRS, US GAAP, and GIPS, Bitcoin is relegated to a line item—often stripped of traceable context. This project is **not** about surface-level disclosures. It’s about institutional users who **require verifiable, auditable, and address-level Bitcoin reporting**.

> This is a local, reference application designed for public accounting, tax litigation, forensics, asset recovery, and institutional validation.

---

## 📦 Application Features

- 🔐 **Runs Locally Only** — Your data never leaves your machine.
- 📊 **Excel Report Generator** — Summary + transaction sheet, with numerical format for easy cell manipulation.
- 🧾 **Detailed On-Chain Context** — Address type, balance, transaction log, unspent outputs.
- 🧮 **Accurate USD Conversion** — Historical market price included in report.

---

## 📸 Demo

⚠️ **SAT-1 App Demo: Please click on the Image to start video** ⚠️

<a href="https://www.youtube.com/embed/3V8pw9TnYME?autoplay=1" target="_blank">
  <img src="https://github.com/user-attachments/assets/209e8368-6899-47aa-adc8-f5aeb80bddd6" width="1096"/>
</a>

---

## 🧠 Use Cases

Creating a fully-Bitcoin reporting standard is bloody difficult. IFRS and US GAAP have a place for Bitcoin: inventory or intangible assets. Under GIPS, Bitcoin would appear as a line item within portfolio composition. High-level disclousures suffice investors (some): "X amount of Bitcoin, valued at Y amount USD, is held at Custody Z." Address-level disclosures also come with security risks because publicly-disclosing wallet addresses increases the risk of: phishing attacks, exposure of vulnerabiluties (lack of multisig, for example), and tracking of internal financial flows. A framework for disclosing address-level detail seems a bit too much. So why would I still want to build it?

It's not about *"who like transaparency"*, but rather: *"who has strong enough incentives to pay for detailed, verifiable, and auditable address-level reporting?"*

(Not organized in any particular order)

1. Forensic accounting and litigation support firms

    > Tracing of funds between addresses, prove co-mingling of funds (or disprove), determine net holdings at a specific point in time.

2.  Public accounting firms

    > Compare reported balances and transactions with on-chain data.

3. Asset recovery professionals

    > In bankrupcies, such as FTX or Mt. Gox, professionals are appointed to locate, report and recover (if possible) assets (in this case digital). A detailed, court-ready report tracking movement before and after insolvency event comes in handy.

4. Tax lawyers and high-networth individuals

    > Support capital gains (or loss) calculations, provide regulators or courts with detailed audit trails, and/or proving long term holdings.

5. Institutional investors, hedge funds and family offices

    > A single address-level report is not directly actionable on its own, however, when aggregated and combined with other market data, it can provide valueble insights of Bitcoin market dynamics.

    **Fun fact: This is the work I enjoy doing the most.** For example, my most recent project involved creating a model that would calculate rolling CAGR assuming hypothetical weekly Bitcoin purchases at a predefined time. The data used was historical pricing, however, it can be applied at the address-level.

6. Bitcoin custodians (optional)

    > These business must show transparency to regulators, however, high level disclosures suffice. Optionally, the custodian could offer monthly holdings report as a value-add service to their users.

7. Government or regulatory agencies (eventually)

    > They are years behind, but eventually will want better forensics for compliance, fraud detection and/or investigating undeclared holdings.

---

## 🏃‍♂️ Running the application instructions

1. Install Python
    - Check the box that says "Add python.exe to PATH"

2. Install Git and Github CLI

3. Clone the repository:

```bash
gh repo clone madame-president/SAT-1
cd SAT-1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
streamlit run main.py
```

---

## 📄 Abstract

The Standard for Address Transparency *(SAT-1 for short)* is a new format that defines the structure and key components of a Bitcoin address statement. SAT-1 was built inspired by traditional financial practices. My goal is to introduce a clean, structured way to present Bitcoin address details, balances and historical transactions in an auditable format. SAT-1 ensures that Bitcoin holdings can be audited with the same precision as traditional financial statements. This will bridge the wide gap between Bitcoin's technical transparency and institutional-grade financial reporting needs.

The Bitcoin network contains hunderds of gigabytes of unstructured data. The data is public and transparent, but there is no standarized method for reporting this information in a financial context. Without a clear framework, reporting on Bitcoin addresses often becomes vulnerable to misinterpretation and inconsinsitency. The method I propose to solve this problem is the standard of address transparancy.


## ⚙️ SAT-1 components

SAT-1 reports are divided into two sections:

1. Address Summary
2. Transaction History

### Address Summary contains:

| Field                        | Description                                                                                   |
| :--------------------------- | :-------------------------------------------------------------------------------------------- |
| **Timestamp**                | The exact time when the report was generated in UTC.                                          |
| **Market Price (USD)**       | The market price of Bitcoin at the time when the report is generated.                         |
| **Address**                  | The Bitcoin address being audited.                                                            |
| **Address Type**             | The classification of the address (`p2pkh`, `p2sh`, `bech32`, `taproot`).                     |
| **First Seen Receiving**     | The timestamp when the address was first seen receiving Bitcoin.                              |
| **Last Seen Receiving**      | The most recent timestamp the address received Bitcoin.                                       |
| **First Seen Spending**      | The timestamp when the address was first seen spending Bitcoin (if any).                      |
| **Last Seen Spending**       | The most recent timestamp the address spent Bitcoin (if any).                                 |
| **Period Transaction Count** | The number of transactions involving the address during the reporting period.                 |
| **Unspent Output Count**     | The current number of UTXOs associated with the address.                                      |
| **Current Balance (BTC)**    | The current Bitcoin balance of the address.                                                   |
| **Current Balance (USD)**    | The USD equivalent of the current balance.                                                    |
| **Total Received (BTC)**     | The total Bitcoin ever received by the address during the reporting period.                   |
| **Total Received (USD)**     | The USD equivalent of the total amount received with the value at time of transaction.        |
| **Total Sent (BTC)**         | The total Bitcoin ever sent by the address during the reporting period.                       |
| **Total Sent (USD)**         | The USD equivalent of the total amount sent with the value at time of transaction.            |
| **Period Start**             | The starting date for the reporting period.                                                   |
| **Period End**               | The ending date for the reporting period.                                                     |

#### Each data field included helps with:

- Generating Bitoin reports at specific date ranges.
- Calculating the address P/L.
- Measuring overall Bitcoin volume transacted within the address.
- Converting Bitcoin to fiat.

### Transaction history contains:

| Field                | Description                                                                    |
| :------------------- | :----------------------------------------------------------------------------- |
| **Block Height**     | The block in which the transaction was confirmed.                              |
| **Transaction Time** | The time the transaction was confirmed in UTC.                                 |
| **Txid**             | The transaction hash.                                                          |
| **Amount (BTC)**     | The amount of Bitcoin transacted.                                              |
| **Direction**        | Whether the Bitcoin was received or sent.                                      |

#### Each data field included helps with (additional):

- Verifying the transactions have been confirmed.
- Categorizing each transaction as received or sent, to mimic the double-entry accounting system.

## ⚠️ Disclaimer

Any code I share is intended to run locally. If adapting for web or shared environments, ensure proper handling of addresses, keys, and API rate limits.
