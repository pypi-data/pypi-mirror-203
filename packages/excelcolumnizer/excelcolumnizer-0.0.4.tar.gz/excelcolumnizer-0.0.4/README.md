# excelcolumnizer

## What is it?

A package that helps you recover columns of Excel data converted from PDF files.

## Where to get it

<pre lang=sh>pip install excelcolumnizer</pre>

## Dependencies

<ul><li><a href="https://openpyxl.readthedocs.io/en/stable/">openpyxl</a></li>
<li><a href="https://github.com/ragardner/tksheet">tksheet</a></li></ul>

## Changes
<ul>
<li>Version 0.0.4</li>

```python

import excelcolumnizer as xl

xlpath='<full name of your excel file including extension>'
xl.sheet(xlpath)

```

<ul><li>A GUI with tksheet will be opened with the contents of excel file.</li>
<li>Here is a recommending set of actions to try:</li>
<ol><li>Remove unwanted rows (F7)</li>
<li>Remove unwanted columns (F7) or combine columns (F5)</li>
  <li>Click a cell to insert (F1) or delete the cell (F3)</li></ol>
<br>

<li>All action is repeated if the same kind of selected rows/columns is found at other locations.</li>
  <ul><li>Thus, try one action at the top</li></ul>
<li>After every action, the contents will be saved to a file that is the original name with a string "_cleaned".</li>
<li>When a cell is inserted, all the cells at right will be shifted to the right</li>
<li>When a cell is deleted, all the cells at right will be shifted to the left and the cell at the last column will be empty.</li>
  <li>If the action is done by mistake, press function-key F12 to restore the last action</li></ul>
  <br>
<ul><li>To aid your step, some highlights take places</li>
  <ul><li>Some rows will be highlighted in redish, indicating that the rows are least occurance among "patterns". It does not mean you need to delete the rows, but it might be one of them you want to delete.</li>
    <li>When columns are highlighted, the columns are all empty. Thus, you can certainly delete the columns</li></ul>
    
</ul>
<br>