# Checklist for responsible deep learning modeling of medical images based on COVID-19 detection studies


<!-- DO NOT EDIT THIS SECTION -->
<!--START_SECTION:data-section-->
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bibliographyItem</th>
      <th>doi</th>
      <th>lowQuality</th>
      <th>transferLearning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>test1</td>
      <td>123</td>
      <td>yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>test2</td>
      <td>456</td>
      <td>no</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data resource / Checklist</th>
      <th>[D] Does the data and its associated information provide sufficient diagnostic quality?</th>
      <th>[R] Are the low quality images rejected?</th>
      <th>[D] Is the dataset balanced in terms of sex and age?</th>
      <th>[R] Does the dataset contain one type of images (CT or X -ray or the same projection)?</th>
      <th>[R] Are the lung structures visible (“lung” window) on CT images?</th>
      <th>[D] Are images of children and of adults labelled as such within the dataset?</th>
      <th>[R] Are images correctly categorized in relation to class of pathology?</th>
      <th>[D] Are AP/PA projections described for every X -ray image?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>template</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>2)</td>
      <td>Y?</td>
      <td>N</td>
      <td>Y?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>not all</td>
      <td>N?</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3)</td>
      <td>N?</td>
      <td>N</td>
      <td>?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>N</td>
      <td>N?</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4)</td>
      <td>N</td>
      <td>N</td>
      <td>?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>N</td>
      <td>Y?</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5)</td>
      <td>N?</td>
      <td>N</td>
      <td>Y?</td>
      <td>N (PA + lateral, CT)</td>
      <td>n/a</td>
      <td>Y?</td>
      <td>N</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6)</td>
      <td>N?</td>
      <td>N</td>
      <td>Y?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7)</td>
      <td>N</td>
      <td>N</td>
      <td>Y</td>
      <td>Y</td>
      <td>n/a</td>
      <td>Y</td>
      <td>not all</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8)</td>
      <td>N?</td>
      <td>N</td>
      <td>Y</td>
      <td>Y</td>
      <td>n/a</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9)</td>
      <td>N</td>
      <td></td>
      <td>?</td>
      <td></td>
      <td></td>
      <td>N</td>
      <td></td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10)</td>
      <td>N?</td>
      <td>N</td>
      <td>N</td>
      <td>Y</td>
      <td>n/a</td>
      <td>Y</td>
      <td>Y?</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11)</td>
      <td>N</td>
      <td>n/a</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
      <td>not all</td>
      <td>N?</td>
      <td>n/a</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12)</td>
      <td>N</td>
      <td>Y</td>
      <td>?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13)</td>
      <td>N</td>
      <td>N</td>
      <td>?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>N</td>
      <td>N</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14)</td>
      <td>Y</td>
      <td>N</td>
      <td>?</td>
      <td>N (PA + lateral)</td>
      <td>n/a</td>
      <td>N</td>
      <td>Y</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>14</th>
      <td>17)</td>
      <td>N?</td>
      <td>Y?</td>
      <td>Y?</td>
      <td>Y</td>
      <td>n/a</td>
      <td>N</td>
      <td>N?</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>15</th>
      <td>23)</td>
      <td>N</td>
      <td>N</td>
      <td></td>
      <td>N (include CT scanogram)</td>
      <td>n/a</td>
      <td>N</td>
      <td>N</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<!--END_SECTION:data-section-->
