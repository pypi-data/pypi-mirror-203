"""
Alpha月报
"""
import os
import numpy as np
import pandas as pd
import hbshare as hbs
import datetime
import math
from sqlalchemy import create_engine
from hbshare.quant.Kevin.rm_associated.config import engine_params, style_names
from hbshare.quant.Kevin.quant_room.MyUtil.data_loader import get_fund_nav_from_sql, get_trading_day_list
from periodic_config import index_name_dict, industry_name_dict
from hbshare.quant.CChen.cons import sql_write_path_hb
from hbshare.quant.CChen.fut import wind_stk_index_basis
from WindPy import w

w.start()


class MonthlyReporter:
    def __init__(self, trade_date):
        self.trade_date = trade_date
        self._date_preprocess()

    def _date_preprocess(self):
        trade_dt = datetime.datetime.strptime(self.trade_date, '%Y%m%d')
        range_start = (trade_dt - datetime.timedelta(days=500)).strftime('%Y%m%d')
        month_list = get_trading_day_list(range_start, self.trade_date, frequency="month")
        self.pre_date = month_list[month_list.index(self.trade_date) - 1]
        self.start_date = [x for x in month_list if x[4:6] == "12"][-1]
        self.trading_day_list_tm = get_trading_day_list(self.pre_date, self.trade_date)
        self.trading_day_list_ty = get_trading_day_list(self.start_date, self.trade_date)

    def _calc_market_index_ret(self):
        """
        指数收益
        """
        index_list = list(index_name_dict.keys())
        res = w.wsd(','.join(index_list), "close", self.start_date, self.trade_date)
        if res.ErrorCode != 0:
            data = pd.DataFrame()
            print("fetch market index data error: start_date = {}, end_date = {}".format(
                self.pre_date, self.trade_date))
        else:
            data = pd.DataFrame(res.Data, index=res.Codes, columns=res.Times).T
            data.index.name = 'trade_date'
            data.reset_index(inplace=True)
            data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
            data = data.set_index('trade_date').rename(columns=index_name_dict).sort_index().dropna()
            data /= data.iloc[0]
            assert (data.shape[0] == len(self.trading_day_list_ty))

        return data

    def _calc_industry_ret(self):
        """
        行业收益及成交情况
        """
        industry_list = list(industry_name_dict.keys())
        # 行业指数收益
        res = w.wsd(','.join(industry_list), "close", self.pre_date, self.trade_date)
        if res.ErrorCode != 0:
            data = pd.DataFrame()
            print("fetch industry return data error: start_date = {}, end_date = {}".format(
                self.pre_date, self.trade_date))
        else:
            data = pd.DataFrame(res.Data, index=res.Codes, columns=res.Times).T
            data.index.name = 'trade_date'
            data.reset_index(inplace=True)
            data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
            data = data.set_index('trade_date').rename(columns=industry_name_dict).sort_index().dropna()
            data /= data.iloc[0]
            assert (data.shape[0] == len(self.trading_day_list_tm))
        industry_ret = data.loc[self.trade_date].sort_values() - 1
        # 行业成交额
        res = w.wsd(','.join(industry_list), "amt", self.pre_date, self.trade_date)
        if res.ErrorCode != 0:
            data = pd.DataFrame()
            print("fetch industry amt data error: start_date = {}, end_date = {}".format(
                self.pre_date, self.trade_date))
        else:
            data = pd.DataFrame(res.Data, index=res.Codes, columns=res.Times).T
            data.index.name = 'trade_date'
            data.reset_index(inplace=True)
            data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
            data = data.set_index('trade_date').rename(columns=industry_name_dict).sort_index().dropna()
            assert (data.shape[0] == len(self.trading_day_list_tm))
        industry_amt = (data.sum() / data.sum().sum()).sort_values()

        industry_data = industry_ret.to_frame('月度涨跌幅').merge(
            industry_amt.to_frame('月度成交占比'), left_index=True, right_index=True)

        return industry_data

    def _calc_style_factor_ret(self):
        """
        风格因子收益
        """
        sql_script = "SELECT * FROM factor_return where " \
                     "TRADE_DATE > {} and TRADE_DATE <= {}".format(self.pre_date, self.trade_date)
        engine = create_engine(engine_params)
        factor_return = pd.read_sql(sql_script, engine)
        factor_return['trade_date'] = factor_return['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
        factor_return = pd.pivot_table(
            factor_return, index='trade_date', columns='factor_name', values='factor_ret').sort_index()[style_names]
        assert (factor_return.shape[0] == len(self.trading_day_list_tm) - 1)

        return factor_return

    def _calc_trading_liquidity(self):
        """
        指数成交活跃度
        """
        # TODO
        start_date = "20211231"
        sql_script = "SELECT * FROM mac_stock_trading WHERE TRADE_DATE > {} and TRADE_DATE <= {}".format(
            start_date, self.trade_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
        amt_data = data.set_index('trade_date')[['amt_300', 'amt_500', 'amt_1000', 'amt_other']]
        amt_ratio = amt_data.div(amt_data.sum(axis=1), axis=0)

        return amt_ratio

    def _calc_valuation(self):
        """
        指数估值数据
        """
        trade_dt = datetime.datetime.strptime(self.trade_date, '%Y%m%d')
        range_start = (trade_dt - datetime.timedelta(days=365*10)).strftime('%Y%m%d')
        sql_script = "SELECT * FROM mac_stock_pe_ttm where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            range_start, self.trade_date)
        engine = create_engine(engine_params)
        pe_ttm = pd.read_sql(sql_script, engine)
        pe_ttm['trade_date'] = pe_ttm['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
        pe_ttm = pe_ttm.set_index('trade_date').rename(
            columns={"SZ50": "上证50", "HS300": "沪深300", "ZZ500": "中证500", "ZZ1000": "中证1000"})
        pe_ttm = pe_ttm[['上证50', '沪深300', '中证500', '中证1000']]
        pe_quantile = pe_ttm.apply(lambda x: x.dropna().rank(pct=True).iloc[-1])

        return pe_ttm, pe_quantile

    @staticmethod
    def _calc_stock_bond_premium(benchmark_name):
        # 宽基指数股息率
        sql_script = "SELECT trade_date, {} FROM mac_stock_dividend".format(benchmark_name)
        engine = create_engine(engine_params)
        dividend = pd.read_sql(sql_script, engine).dropna()
        # 国债收益率数据
        sql_script = "SELECT trade_date, ytm_10y FROM mac_treasury_yield"
        treasury_data = pd.read_sql(sql_script, engine)
        data = pd.merge(dividend, treasury_data, on='trade_date').dropna()
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.datetime.strftime(x, '%Y%m%d'))
        # 指数行情数据
        map_dict = {"SZZS": "000001", "SZ50": "000016", "HS300": "000300", "ZZ500": "000905", "ZZ1000": "000852"}
        sql_script = "SELECT JYRQ, ZQDM, SPJG FROM funddb.ZSJY where ZQDM = '{}' and JYRQ >= '20080101'".format(
            map_dict[benchmark_name])
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        index_df = pd.DataFrame(res['data']).rename(columns={"JYRQ": "trade_date", "SPJG": "benchmark"})
        data = pd.merge(data, index_df[['trade_date', 'benchmark']], on='trade_date').sort_values(by='trade_date')

        return data

    def _calc_index_basis(self):
        start_date = datetime.datetime.strptime("20210101", '%Y%m%d').date()
        end_date = datetime.datetime.strptime(self.trade_date, '%Y%m%d').date()
        sql_path = sql_write_path_hb['daily']
        a = wind_stk_index_basis(
            code='IC', start_date=start_date, end_date=end_date, sql_path=sql_path, table="futures_wind")

    def run(self):
        # market_index_ret = self._calc_market_index_ret()
        # industry_data = self._calc_industry_ret()
        # style_ret = self._calc_style_factor_ret()
        # trading_liquidity = self._calc_trading_liquidity()
        # pe_ttm, pe_quantile = self._calc_valuation()
        # premium_300 = self._calc_stock_bond_premium("HS300")
        # premium_500 = self._calc_stock_bond_premium("ZZ500")
        index_basis = self._calc_index_basis()


if __name__ == '__main__':
    MonthlyReporter(trade_date="20230331").run()