"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
            dat_file='2002FemResp.dat.gz',
               nrows=None):
    """This method is used to return data frame
    """
    dct=thinkstats2.ReadStataDct(dct_file)
    df=dct.ReadFixedWidth(dat_file,compression='gzip',nrows=nrows)
    
    return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    mydata=ReadFemResp()
    indexed_data=mydata["pregnum"].value_counts().sort_index()
    print(indexed_data)
    
    print(len(mydata))
    
    assert(len(mydata)==7643)
    assert(mydata.pregnum.value_counts()[1]==1267)
    assert(mydata.pregnum.value_counts()[3]=1110)
    assert(mydata.pregnum.value_counts()[5]==305)
    
    print('%s: All tests passed.' % script)


main("notebook script")