# yfinance 使用文档：https://www.wenvenn.com/20211215/shi-yong-python-bao-yfinance-du-qu-ya-hu-cai-jing-shang-de-gu-piao-shu-ju/
# akshare 使用文档：https://cloud.tencent.com/developer/article/1866258
# https://docs.python.org/zh-cn/3/library/sqlite3.html

import akshare as ak
import sqlite3
import pandas as pd
from datetime import datetime
from settings import * 


class ChinaeseStock:
    def __init__(self):
        self.conn = sqlite3.connect('stock_data.db')
        self.cursor = self.conn.cursor()

    def stock_yearly_data(self, stock_code):
        table_name = 'd_%s' % stock_code
        self.cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchone() is None:

            create_table_sql = '''    
                CREATE TABLE IF NOT EXISTS %s (
                id INTEGER PRIMARY KEY,
                date TEXT,
                open REAL,
                close REAL,
                high REAL,
                low REAL,
                volume INTEGER,
                turnover REAL,
                amplitude REAL,
                change_rate REAL,
                change_amount REAL,
                turnover_rate REAL
            )
            ''' % table_name
            self.cursor.execute(create_table_sql)
            self.conn.commit()

        current_year = datetime.now().year
        while current_year >= 2010:
            try:
                df_year = ak.stock_zh_a_hist(symbol=stock_code, adjust='qfq', start_date=f"{
                                             current_year}0101", end_date=f"{current_year}1231")
                df_year.rename(columns={'日期': 'date', '开盘': 'open', '收盘': 'close', '最高': 'high', '最低': 'low', '成交量': 'volume', '成交额': 'turnover', '振幅': 'amplitude', '涨跌幅': 'change_rate', '涨跌额': 'change_amount', '换手率': 'turnover_rate'}, inplace=True)
                if not df_year.empty:
                    logging.info("First row of data for year", current_year, ":")
                    logging.info(df_year.head(1))
                else:
                    break
                df_year.to_sql(table_name, self.conn,
                               if_exists='append', index=False)
                # 提交事务
                self.conn.commit()
                logging.info(f"Data for year {
                      current_year} has been saved to the database.")
            except Exception as e:
                logging.error(f"Error occurred when fetching data for year {
                      current_year}: {e}")
                break
            current_year -= 1
        logging.info("Stock yearly data has been saved to SQLite database.")

    def today_stock_info(self):
        today_stock_info = ak.stock_zh_a_spot_em()
        return today_stock_info

    def fetch_data_for_days(self,table_name, days=[1, 3, 5, 10, 30]):

        results = {}
        for day in days:
            query = f"SELECT * FROM {table_name} WHERE date >= date('now', '-{day} day')"
            df = pd.read_sql_query(query, self.conn)
            results[f'{day} days'] = df

        self.conn.close()

        return results



