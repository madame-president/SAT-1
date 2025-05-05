# Standard for Address Transparency (SAT-1): institutional-grade reporting for Bitcoin addresses

## Abstract

The Standard for Address Transparency *(SAT-1 for short)* is a new format that defines the structure and key components of a Bitcoin address statement. SAT-1 was built inspired by traditional financial practices. My goal is to introduce a clean, structured way to present Bitcoin address details, balances and historical transactions in an auditable format. SAT-1 ensures that Bitcoin holdings can be audited with the same precision as traditional financial statements. This will bridge the wide gap between Bitcoin's technical transparency and institutional-grade financial reporting needs.

## Introduction

The Bitcoin network contains hunderds of gigabytes of unstructured data. The data is public and transparent, but there is no standarized method for reporting this information in a financial context. Without a clear framework, reporting on Bitcoin addresses often becomes vulnerable to misinterpretation and inconsinsitency. The method I propose to solve this problem is the standard of address transparancy.

## SAT-1 components

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

## Why does this matter?

SAT-1 goes beyond a report formatting. It is the first attempt at the institutional level to reconcile Bitcoin's technical transparency and traditional financial accountability. The standardized fields ensure clear comparisons across addresses. It is designed to satisfy internal audits, external audits, tax preparation and compliance needs. The values are recorded in UTC for universal time accuracy. And most importantly, every data point is backed by on-chain evidence.

As Bitcoin adoption continues amoung institutions and wealth funds, auditable Bitcoin address reporting will become a requirement. SAT-1 establishes a strong foundation for this inevitable future.
