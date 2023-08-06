import sqlite3
from pathlib import Path

import xlwings as xw
import pandas as pd


# Set workbook variables
xl_app = xw.apps.active

wb: xw.Book = xw.Book.caller()
ws_input: xw.Sheet = wb.sheets['Input']
ws_short: xw.Sheet = wb.sheets['Shortpay']
ws_accepted: xw.Sheet = wb.sheets['Accepted']

db_path = Path(r'\\gvwac09\Public\Finance\AVA\Database')


def _sql_shortpay():
    conn = sqlite3.connect(db_path / 'Ava_All.db')
    df = pd.read_sql_query(
        """
        SELECT a.Supplier_Nr, a.Invoice_Number, a.Capture_Date, a.Invoice_Date, a.Purchase_Order, a.Item_Number,
            a.Qty_Shipped, a.UOM, a.Invoice_Unit_Price, a.Unit_Price_to_Pay
        FROM t_Ava a
        WHERE a.Shortpay=1;
        """,
        conn
    )
    conn.close()
    return df


def _sql_accepted():
    conn = sqlite3.connect(db_path / 'Ava_All.db')
    df = pd.read_sql_query(
        """
        SELECT a.Supplier_Nr, a.Invoice_Number, a.Capture_Date, a.Invoice_Date, a.Purchase_Order, a.Item_Number,
            a.Qty_Shipped, a.UOM, a.Invoice_Unit_Price, a.Unit_Price_to_Pay,
            CASE
                WHEN a.Pricelist_Unit_Price = "NO PL" THEN ROUND(a.PO_Unit_Price,2)
                ELSE ROUND(a.Pricelist_Unit_Price,2)
            END AS Pricelist_PO_Price
        FROM t_Ava a
        WHERE ROUND(a.Unit_Price_to_Pay,2) > Pricelist_PO_Price;
        """,
        conn
    )
    conn.close()
    return df


def button_refresh():
    df_short = _sql_shortpay()
    df_short['Shortpay_per_Item'] = df_short['Unit_Price_to_Pay'] - df_short['Invoice_Unit_Price']
    df_short['Extended_Shortpay'] = df_short['Shortpay_per_Item'] * df_short['Qty_Shipped']
    ws_short.tables['t_short'].update(df_short)

    df_accepted = _sql_accepted()
    df_accepted['Delta_per_Item'] = df_accepted['Pricelist_PO_Price'] - df_accepted['Unit_Price_to_Pay']
    df_accepted['Extended_Delta'] = df_accepted['Delta_per_Item'] * df_accepted['Qty_Shipped']
    ws_accepted.tables['t_accepted'].update(df_accepted)

    xl_app.alert('Complete', title='Complete', mode='info')


if __name__ == "__main__":
    # To debug:
    # ------------------------------------------------------------------
    # xw.Book('Ava Captured.xlsb').set_mock_caller()
    # wb: xw.Book = xw.Book.caller()
    # ws_input: xw.Sheet = wb.sheets['Input']
    # ws_data: xw.Sheet = wb.sheets['Data']
    # ------------------------------------------------------------------
    button_refresh()
