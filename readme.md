PyArrow Read S3 Parquet Benchmarks
================

![](readme_files/figure-gfm/load%20data-1.png)<!-- -->![](readme_files/figure-gfm/load%20data-2.png)<!-- -->

    ## # A tibble: 9 x 6
    ##   num_files num_columns method            runtime  out_size throughput_mbps
    ##       <int> <fct>       <chr>               <dbl>     <int>           <dbl>
    ## 1         1 1           Local Filesystem    0.437  43799374           95.6 
    ## 2         1 1           PyArrow s3fs        8.64   43799906            4.83
    ## 3         1 1           AWS Data Wrangler  15.5    43799374            2.70
    ## 4         1 4           Local Filesystem    0.357 194907202          521.  
    ## 5         1 4           PyArrow s3fs       28.6   194907734            6.50
    ## 6         1 4           AWS Data Wrangler  49.2   192717232            3.73
    ## 7         1 All         Local Filesystem    1.28  687650240          513.  
    ## 8         1 All         PyArrow s3fs      116.    687652368            5.66
    ## 9         1 All         AWS Data Wrangler  15.7   674510420           41.0

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
