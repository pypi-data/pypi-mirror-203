Project daskcheck
=================

Help with a simple use of the **dask**

The idea
--------

1.  define properly the *core function* (*xcorefunc* in the example)
    with **THE return**
2.  `daskcheck` then will take care about:
    -   sending the parameters
    -   collecting results and saving them to **local json file**

Instalation of daskcheck
------------------------

``` {.bash org-language="sh"}
pip install daskcheck
```

Installation of dask
--------------------

See <https://docs.dask.org/en/stable/install.html>

``` {.bash org-language="sh"}
pip install "dask[complete]"
```

Launching dask scheduler/workers
--------------------------------

*Pay attention to correct/compatible libraries on different workers*

### Environment needed

    export PATH=$PATH:$HOME/.local/bin

    export PYTHONPATH=$HOME/root/lib/
    export ROOTSYS=$HOME/root
    export PATH=$ROOTSYS/bin:~/bin:$PATH
    export LD_LIBRARY_PATH=$ROOTSYS/lib:$ROOTSYS/lib/root:$LD_LIBRARY_PATH

    source $HOME/root/bin/thisroot.sh

    export DISPLAY=:0
    export DS=$HOME/.dask_server
    export DSER=`cat $DS`
    export HOST=`hostname`

    cd /tmp

    if [ -f  "$DS" ]; then
        echo ... OK $DS exists
    else
        echo ... NO $DS exists
        sleep 5
        echo ...
        exit 1
    fi

    export workers=2

    echo ... I am on $HOST and trying to connect to /$DSER/ one thread per worker
    dask worker ${DSER}:8786      --nworkers $workers --nthreads 1

### Launching scheduler

``` {.bash org-language="sh"}
#dask scheduler --port 8786
export PATH=$PATH:$HOME/.local/bin

export HOST=`hostname`

cd /tmp

if [ "$HOST" = "core6a" ]; then
    echo ... starting scheduler
    dask scheduler   --port 8786 #  --bokeh-port 8787
fi
sleep 5
exit 0
```

### Launching worker

``` {.bash org-language="sh"}
dask     worker 127.0.0.1:8786 --nworkers 5 --nthreads 1
```

Testing dask
------------

*IN DEVELOPMENT...*

This runs (sched and workers are ON) 40x get~cpuinfo~

``` {.bash org-language="sh"}
./daskcheck.py test
```

**In progress ... this worked only inside git project folder with actual
files...**

This is solved .... possible to load (unload first). See `tesmod.py`

``` {.bash org-language="sh"}
./daskcheck.py dask py_file_with_main  1,3
./daskcheck.py dask py_file_with_main  11..33
```

Monitoring dask
---------------

    xdg-open http://localhost:8787

Recollection the data from json
-------------------------------

Usage
-----

``` {.python}
from daskcheck import daskcheck

from fire import Fire
import time
import platform
import datetime as dt
import json

def main( parlist ):
    parameters = daskcheck.prepare_params( parlist )

    if type(parameters)==list:
        print("i... viable for DASK ....")
        daskcheck.submit( daskcheck.get_cpu_info , parameters)
    else:
        print("i... running only locally")
        my_results = xcorefunc( 1 , parameters )
        # Write LOG file.
        now = dt.datetime.now()
        stamp = now.strftime("%Y%m%d_%H%M%S")
        with open(f"dask_results_log_{stamp}.json", "w") as fp:
            json.dump( my_results , fp, sort_keys=True, indent='\t', separators=(',', ': '))
    return

def xcorefunc( order, param):
    """
    Function to be sent to dask server with order# + parameter
    """
    import ROOT # I need to avoid breaking pickle
    start_time = time.perf_counter()

    return order, [platform.node(),  f"{time.perf_counter() - start_time:.1f} s" , ni]


if __name__=="__main__":
    Fire(main)

```
