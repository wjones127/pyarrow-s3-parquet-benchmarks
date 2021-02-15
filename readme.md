PyArrow Read S3 Parquet Benchmarks
================

![](readme_files/figure-gfm/load%20data-1.png)<!-- -->

    ## # A tibble: 9 x 6
    ##   num_files num_columns method            runtime  out_size throughput_mbps
    ##       <int> <fct>       <chr>               <dbl>     <int>           <dbl>
    ## 1         1 1           Local Filesystem     1.19 687650240          550.  
    ## 2         1 1           PyArrow s3fs       111.   687652368            5.91
    ## 3         1 1           AWS Data Wrangler   15.3  674510420           41.9 
    ## 4         1 4           Local Filesystem     1.29 687650240          507.  
    ## 5         1 4           PyArrow s3fs       111.   687652368            5.89
    ## 6         1 4           AWS Data Wrangler   14.7  674510420           43.7 
    ## 7         1 All         Local Filesystem     1.50 687650240          437.  
    ## 8         1 All         PyArrow s3fs       107.   687652368            6.10
    ## 9         1 All         AWS Data Wrangler   14.5  674510420           44.3

## Discussion

The performance issues with Parquet reads in S3 have been discussed
here:

  - <https://issues.apache.org/jira/browse/PARQUET-1698>

## Setup

Install requirements in virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Then run the setup script

``` bash
python cli init
```

Now you can run the benchmark:

``` bash
python cli run
```

When you are finished, cleanup with:

``` bash
python cli cleanup
```
