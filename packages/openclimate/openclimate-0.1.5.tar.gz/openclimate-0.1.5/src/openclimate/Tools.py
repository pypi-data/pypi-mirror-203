from dataclasses import dataclass
import pandas as pd


@pd.api.extensions.register_dataframe_accessor("analysis")
class Tools:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj):
        # Validate that the necessary columns exist in the DataFrame
        if not all(col in obj.columns for col in ['actor_id', 'year', 'total_emissions']):
            raise AttributeError("Must have 'actor_id', 'year', and 'emissions' columns")

    def cumulative_emissions(self,
                             sort_by: list=['actor_id', 'year'],
                             groupby: str='actor_id',
                             input_var: str='total_emissions',
                             output_var: str='cumulative_emissions'):
        """
        Calculates the cumulative emissions for each actor_id in the dataframe.
        """
        self._obj.sort_values(sort_by, inplace=True)
        self._obj[output_var] = self._obj.groupby(groupby)[input_var].cumsum()
        return self._obj

    def per_capita(self, variable: str='total_emissions', population_var: str='population'):
        self._obj[f'{variable}_per_capita'] = self._obj[variable] / self._obj[population_var]
        return self._obj
