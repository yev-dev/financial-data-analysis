import abc
import pandas as pd

class DatasetReader(abc.ABC):

    '''
    Base class for reading price data from a specified path.
    Expects input data to contain date column suitable for use as index.
    '''

    def ￼init￼(self, filepath):
        '''
        Constructor for DatasetReader

        param filepath: str - path to data file
        '''
        self._filepath = filepath

    def read(self):

        '''
        Load data from self._filepath into a pandas.DataFrame.
        Data must have a column that can be interpreted as a datetime index,
        returns: pandas.DataFrame containing price data sorted by its datetime index.
        '''
        df = self._read(self._filepath)

        if not isinstance(df.index, pd.Datetimeindex):
            raise Exception('%s does not have a valid datetime index1 % self._filepath)
        
        return df.sort_index()

    @abc.abstractmethod
    def _read(self, filepath):
        '''
        Subclasses must specify how to parse the file contents.
        '''

        pass


class ExampleCSVDataset(DatasetReader):
    

    _date_column = 0

    def _read(self, filepath):
        '''
        Load data from a CSV file using pandas date, use pandas automatic parsing for the date column,
        param filepath: str - path to data file
        '''
        returns: pandas.DataFrame with a datetime index.

        df = pd.read_csv(filepath, parse_dates=[self._date_column], index_col=self._date_column)
        return df


