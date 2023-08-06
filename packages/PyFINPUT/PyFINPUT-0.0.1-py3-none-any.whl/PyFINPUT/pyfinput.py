"""
PyFINPUT
Benedict Saunders (c) 2023
Licensed under the GNU General Public License v3.0


Module for adding a simple input file. It's in the style of argparse:

First, initiliase the input file class with the following arguments:

    filename: str (required)
        The filename of the input file
    case_sensitive: bool (optional, def.: False)
        Whether the keywords are case sensitive of not
    assigner: str (optional, def.: "=")
        Character(s) to divide the keywords from their
        values: str
    comment: str (optional, def.: "#")
        Character(s) to identify the beginning of
        comment strings

Keywords can be added to the input_file object with the "add_keyword()"
function:

    name: str (required)
        Name of keyword
    kw_type: type (optional, def.: str)
        Type of the keyword value(s)
    nkws: int (optional, def.: 1)
        Number of values in keyword
        Can also be "*" or "+"
    required: bool (optional, def.: False)
        Raise an exception if True, but
        keyword not in file.
    default: any (optional, def.: "")
        The default value for the keyword

Finally, parse the file with the parse_file() function on the input_file
object:
    returns:
        dict
        The returned dict contains the keywords as keys as strings,
        and their values as the dictionary values, with the defined
        type.

"""
from typing import Any, Type
from src.PyFINPUT.utils import *

class keyword:
    def __init__(self,        
        name = None,
        kw_type = any,
        nkws = 1,
        req = False,
        default = None) -> None:
        self.name = name,
        self.type = kw_type,
        self.nkws = nkws
        self.required = req
        self.handled = False
        self.default = default

class input_file:
    def __init__(self, name: str, case_sensitive: bool = False, assigner: str = ":", comment: str = "#") -> None:
        self.filename = name
        self.kws = []
        self.cs = case_sensitive
        self.assigner = assigner
        self.cmt_id = comment

    def add_keyword(
        self,
        name: str,
        kw_type = str,
        default = None,
        nkws: int = 1,
        required: bool = False,
    ) -> None:
        self.kws.append(keyword(name, kw_type=kw_type, nkws=nkws, req=required, default=default))

    def parse_file(self) -> dict:
        with open(self.filename, "r") as f:
            # First we need to remove comments
            lines = [l.strip() for l in f.readlines() if not l.strip().startswith(self.cmt_id)]
            lines = [l.split(self.cmt_id)[0] for l in lines]

        # Set params dict to contain defaults
        params = dict([(kw.name[0], kw.default) for kw in self.kws if kw.required == False])
        unhandled = [keyword.name[0] for keyword in self.kws]
        required = [keyword.name[0] for keyword in self.kws if any([keyword.required == True, keyword.nkws == "+"])]

        # Iterate through the lines witout comments
        for line in lines:
            k, v = [l.strip() for l in line.split(self.assigner)][:2]
            for kw in self.kws:
                if kw.name[0] == k and k in unhandled:
                    if k in required:
                        required.remove(k)
                    unhandled.remove(k)

                    # Doing stuff with keywords of multiple members
                    if kw.nkws in ["*", "+"]:
                        kw.nkws = len(v.split())
                    if kw.nkws > 1:
                        v = v.split()
                        if kw.nkws > 1 and kw.nkws not in ["*", "+"]:
                            if kw.nkws != len(v):
                                raise LookupError(f"\n\tInsufficient number of members for keyword: {k}\n\t{len(v)} found, but {kw.nkws} expected")
                    v = self._set_type(v, kw.type[0])
                    params[k] = v
                    break
                else:
                    raise LookupError(f"\n\tMultiple occurences of keyword {k} ")
                
        # If a keyword is set as required, make sure it is actually provided.
        if len(required) > 0:
            print("\tMissing required keyword(s):")
            _ = [print(f"\n\t{mkw}") for mkw in required]
            exit()
        return params     

    def _set_type(self, v, t):
        if t == bool:
            if v.casefold() not in ["0".casefold(), "F".casefold(), "FALSE".casefold()]:
                v = 1
            else:
                v = 0
        if isinstance(v, list):
            v = [t(x) for x in v]
        else:
            v = t(v)
        return v
