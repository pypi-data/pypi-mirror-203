
class InclusionExclusion:

    def pos_data_quality_review(self
                                , username: str
                                , warehouse: str
                                , database: str
                                , role: str
                                , columns=None
                                , filters=None
                                , order_by=None
                                , polars: bool = False):

        from NikeCA import Snowflake
        import configparser

        config = configparser.ConfigParser()
        config.read('pip.ini')

        table = config['inclusion_exclusion_pos_data_quality_review'].get('table')

        # Ensure columns is a list
        if not (isinstance(columns, list) or columns is None):
            raise TypeError("columns must be a list")

        # Ensure filters is a list
        if not (isinstance(filters, list) or filters is None):
            raise TypeError("filters must be a list")

        # Ensure order_by is a list
        if not (isinstance(order_by, list) or order_by is None):
            raise TypeError("order_by must be a list")

        if columns is None:
            columns_str = config['inclusion_exclusion_pos_data_quality_review'].get('columns')
        else:
            columns_str = ', '.join(columns)

        if filters is None:
            filters = []
        # Join column filters into comma-separated string, if any
        if len(filters) > 0:
            filters_str = 'AND '.join(filters)
            filters_str = f'WHERE {filters_str}'
        else:
            filters_str = ''

        if order_by is None:
            order_by = config['inclusion_exclusion_pos_data_quality_review'].get('order_by')
        else:
            order_by = ', '.join(order_by)

        query = f"""
            SELECT
                {columns_str}
                
            FROM
                {table}
            {filters_str}
                
            ORDER BY
                {order_by}
                
            ;
        """

        return Snowflake(username=username, warehouse=warehouse, database=database,
                         role=role).snowflake_pull(query=query, polars=polars)

    def summary(self
                , username: str
                , warehouse: str
                , database: str
                , role: str
                , columns=None
                , filters=None
                , order_by=None
                , polars: bool = True):

        import polars as pl
        import pandas as pd

        df = pl.DataFrame(InclusionExclusion.pos_data_quality_review(self, username=username, warehouse=warehouse,
                                                                     database=database, role=role, columns=columns,
                                                                     filters=filters, order_by=order_by, polars=polars))

        df = df.filter(
            pl.col('ACTIVITY_END_DT') == pl.col('ACTIVITY_END_DT').max().alias('test')
        )

        df_pd = pd.DataFrame()

        df_pd['RETAILERS'] = df.select(pl.col('RETAILER_ID').count()).to_arrow()[0]

        df_pd['INCLUDED'] = df.select(df.filter(pl.col('DASHBOARD_REPORTING_IND') == 'Y').select(pl.col('RETAILER_ID').count())).to_arrow()[0]
        df_pd['PERCENT_INCLUDED'] = f"{str(round(df_pd['INCLUDED']/df_pd['RETAILERS']*100, 0))}%"
        df_pd['EXCLUDED'] = df.select(df.filter(pl.col('DASHBOARD_REPORTING_IND') == 'N').select(pl.col('RETAILER_ID').count())).to_arrow()[0]
        df_pd['PERCENT_EXCLUDED'] = f"{str(round(df_pd['EXCLUDED']/df_pd['RETAILERS'] * 100, 0))}%"

        if polars:
            return pl.DataFrame(df_pd)
        return df_pd

    # def retailer_flag_flip(self
    #             , username: str
    #             , warehouse: str
    #             , database: str
    #             , role: str
    #             , columns=None
    #             , filters=None
    #             , order_by=None
    #             , polars: bool = True):
    #
    #     pass


