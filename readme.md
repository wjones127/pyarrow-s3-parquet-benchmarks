PyArrow Read S3 Parquet Benchmarks
================

![](readme_files/figure-gfm/load%20data-1.png)<!-- -->![](readme_files/figure-gfm/load%20data-2.png)<!-- -->

<!--html_preserve-->

<style>html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
}

#wfsttwbkef .gt_table {
  display: table;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#wfsttwbkef .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#wfsttwbkef .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#wfsttwbkef .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 0;
  padding-bottom: 4px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#wfsttwbkef .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wfsttwbkef .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#wfsttwbkef .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#wfsttwbkef .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#wfsttwbkef .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#wfsttwbkef .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#wfsttwbkef .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#wfsttwbkef .gt_group_heading {
  padding: 8px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
}

#wfsttwbkef .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#wfsttwbkef .gt_from_md > :first-child {
  margin-top: 0;
}

#wfsttwbkef .gt_from_md > :last-child {
  margin-bottom: 0;
}

#wfsttwbkef .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#wfsttwbkef .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 12px;
}

#wfsttwbkef .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wfsttwbkef .gt_first_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
}

#wfsttwbkef .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wfsttwbkef .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#wfsttwbkef .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#wfsttwbkef .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wfsttwbkef .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#wfsttwbkef .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding: 4px;
}

#wfsttwbkef .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#wfsttwbkef .gt_sourcenote {
  font-size: 90%;
  padding: 4px;
}

#wfsttwbkef .gt_left {
  text-align: left;
}

#wfsttwbkef .gt_center {
  text-align: center;
}

#wfsttwbkef .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#wfsttwbkef .gt_font_normal {
  font-weight: normal;
}

#wfsttwbkef .gt_font_bold {
  font-weight: bold;
}

#wfsttwbkef .gt_font_italic {
  font-style: italic;
}

#wfsttwbkef .gt_super {
  font-size: 65%;
}

#wfsttwbkef .gt_footnote_marks {
  font-style: italic;
  font-size: 65%;
}
</style>

<div id="wfsttwbkef" style="overflow-x:auto;overflow-y:auto;width:auto;height:auto;">

<table class="gt_table">

<thead class="gt_header">

<tr>

<th colspan="4" class="gt_heading gt_title gt_font_normal" style>

S3 Parquet Read Benchmark Results

</th>

</tr>

<tr>

<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style>

</th>

</tr>

</thead>

<thead class="gt_col_headings">

<tr>

<th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1">

Num Columns Read

</th>

<th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">

Result Size (MB)

</th>

<th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">

Runtime (s)

</th>

<th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">

Throughput (MBps)

</th>

</tr>

</thead>

<tbody class="gt_table_body">

<tr class="gt_group_heading_row">

<td colspan="4" class="gt_group_heading">

Local Filesystem

</td>

</tr>

<tr>

<td class="gt_row gt_center">

1

</td>

<td class="gt_row gt_right">

41.77

</td>

<td class="gt_row gt_right">

0.44

</td>

<td class="gt_row gt_right">

95.63

</td>

</tr>

<tr>

<td class="gt_row gt_center">

4

</td>

<td class="gt_row gt_right">

185.88

</td>

<td class="gt_row gt_right">

0.36

</td>

<td class="gt_row gt_right">

521.01

</td>

</tr>

<tr>

<td class="gt_row gt_center">

All

</td>

<td class="gt_row gt_right">

655.79

</td>

<td class="gt_row gt_right">

1.28

</td>

<td class="gt_row gt_right">

512.53

</td>

</tr>

<tr class="gt_group_heading_row">

<td colspan="4" class="gt_group_heading">

PyArrow s3fs

</td>

</tr>

<tr>

<td class="gt_row gt_center">

1

</td>

<td class="gt_row gt_right">

41.77

</td>

<td class="gt_row gt_right">

8.64

</td>

<td class="gt_row gt_right">

4.83

</td>

</tr>

<tr>

<td class="gt_row gt_center">

4

</td>

<td class="gt_row gt_right">

185.88

</td>

<td class="gt_row gt_right">

28.60

</td>

<td class="gt_row gt_right">

6.50

</td>

</tr>

<tr>

<td class="gt_row gt_center">

All

</td>

<td class="gt_row gt_right">

655.80

</td>

<td class="gt_row gt_right">

115.78

</td>

<td class="gt_row gt_right">

5.66

</td>

</tr>

<tr class="gt_group_heading_row">

<td colspan="4" class="gt_group_heading">

AWS Data Wrangler

</td>

</tr>

<tr>

<td class="gt_row gt_center">

1

</td>

<td class="gt_row gt_right">

41.77

</td>

<td class="gt_row gt_right">

15.46

</td>

<td class="gt_row gt_right">

2.70

</td>

</tr>

<tr>

<td class="gt_row gt_center">

4

</td>

<td class="gt_row gt_right">

183.79

</td>

<td class="gt_row gt_right">

49.22

</td>

<td class="gt_row gt_right">

3.73

</td>

</tr>

<tr>

<td class="gt_row gt_center">

All

</td>

<td class="gt_row gt_right">

643.26

</td>

<td class="gt_row gt_right">

15.68

</td>

<td class="gt_row gt_right">

41.03

</td>

</tr>

</tbody>

</table>

</div>

<!--/html_preserve-->

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
