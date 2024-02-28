# https://www.wenvenn.com/20211215/shi-yong-python-bao-yfinance-du-qu-ya-hu-cai-jing-shang-de-gu-piao-shu-ju/
import yfinance as yf

aapl = yf.Ticker('AAPL')
aapl_info = aapl.info

# 调用Ticker对象的info函数可以获取该股票的所有信息，返回一个dictionary结构数据，里面包含比如该公司所属sector，员工数，所在城市，和各种财务表现等。由于整个dictionary比较大，下面只选择打印了几个信息。
print('AAPL sector: ', aapl_info['sector'])
print('AAPL EBITA Margins: ', aapl_info['ebitdaMargins'])
print('AAPL Profit Margins: ', aapl_info['profitMargins'])
print('AAPL Gross Margins: ', aapl_info['grossMargins'])
print('AAPL Day High: ', aapl_info['dayHigh'])
# 获取AAPL所有的历史数据，并打印最开始5天的记录
aapl_history_max = aapl.history(period='max')
aapl_history_max.head()

# 获取AAPL从2021年12月1日到2021年12月15日精度为2分钟的历史数据，并打印最开始的5条记录。
aapl_history_1m = aapl.history(start="2021-12-01", end="2021-12-15", interval="2m")
aapl_history_1m.head()

# 获取股票的分红和扩股数据 - actions
aapl_actions = aapl.actions

aapl_actions.head()

# 获取股票的分红数据 - dividends
aapl_dividends = aapl.dividends

aapl_dividends.head()

# actions函数的返回结果同时记录了分红和扩股信息，如果只想看扩股信息，可以直接使用splits。
aapl_splits = aapl.splits

aapl_splits.head()