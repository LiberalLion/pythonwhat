import inspect
import pythonwhat


def get_manual_converters():

    return {
        "pandas.io.excel.ExcelFile": lambda x: x.io,
        "builtins.dict_keys": lambda x: sorted(x),
        "builtins.dict_items": lambda x: sorted(x),
        "bs4.BeautifulSoup": lambda x: str(x),
        "bs4.element.Tag": lambda x: str(x),
        "bs4.element.NavigableString": lambda x: str(x),
        "bs4.element.ResultSet": lambda x: [str(res) for res in x],
        "h5py._hl.files.File": lambda x: x.file.filename,
        "h5py._hl.group.Group": lambda x: f"{x.file.filename}_{list(x.keys())}",
        "sqlalchemy.engine.base.Engine": lambda x: x.url.database,
    }
