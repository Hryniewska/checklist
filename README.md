# Checklist for responsible deep learning modeling of medical images based on COVID-19 detection studies


<!-- DO NOT EDIT THIS SECTION -->
<!--START_SECTION:data-section-->
## Summary showing which points from the checklist are fulfilled by studies.
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

## Summary showing which points from the checklist are fulfilled by data resources.
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

## This table presents the data sources. The JPEG quality factor (QF) for most images has been set to 75, other cases are indicated.
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Institution</th>
      <th>Link to dataset</th>
      <th>Dynamic range of images</th>
      <th>Data processing</th>
      <th>Prepared for scientific experiments</th>
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
    </tr>
    <tr>
      <th>1</th>
      <td>University of Waterloo</td>
      <td>github.com/lindawangg/COVID-Net b29</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>University of Waterloo</td>
      <td>github.com/agchung/Figure1-COVID-chestxray-dataset</td>
      <td>8 bits, 48 cases</td>
      <td>JPG, PNG</td>
      <td>X-ray database for research purposes only, continuously growing; Metadata: offset, sex, age. finding, survival temperature, pO2, saturation, view, modality, artifacts/distortion, notes; Categories: covid, pneumonia, no finding</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of Waterloo</td>
      <td>github.com/agchung/Actualmed-COVID-chestxray-dataset</td>
      <td>8 bits, 237 cases</td>
      <td>PNG, BMP</td>
      <td>X-ray database for  research purposes only, continuously growing; Metadata: finding, view, modality, notes; Categories: covid, no finding</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Qatar &amp; Bangladesh Universities</td>
      <td>kaggle.com/tawsifurrahman/covid19-radiography-database Chowdhury2020</td>
      <td>8 bits, 21165 cases</td>
      <td>PNG, resized</td>
      <td>X-ray database; No metadata; Categories: COVID-19 positive cases (3616),  normal (10,192), lung opacity (Non-COVID lung infection - 6,012), viral pneumonia (1,345)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>University of Montreal</td>
      <td>github.com/ieee8023/covid-chestxray-dataset cohen2020covidProspective</td>
      <td>8 bits, 951 cases</td>
      <td>JPG, PNG, resized</td>
      <td>X-ray database; Metadata: covid severity scores, sex,age, finding, RT_PCR_positive, survival, intubated, intubation_present, went_icu, in_icu, needed_supplemental_O2, extubated, temperature, pO2_saturation, leukocyte_count, neutrophil_count, lymphocyte_count, clinical_notes, other_notes; Categories: covid, viral, bacterial, fungal, lipoid, aspiration, unknown</td>
    </tr>
    <tr>
      <th>6</th>
      <td>National Institutes  of Health</td>
      <td>kaggle.com/c/rsna-pneumonia-detection-challenge Wang2017</td>
      <td>8 bits, 30227 (training)+3000 (test) cases</td>
      <td>DICOM, resized</td>
      <td>X-ray database of Pneumonia Detection Challenge; No metadata; Categories: normal. lung opacity, no lung opacity/not normal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>National Institutes of Health</td>
      <td>nihcc.app.box.com/v/ChestXray-NIHCC Wang2017</td>
      <td>8bits, 112120 cases</td>
      <td>PNG, resized</td>
      <td>X-ray database of Common Thorax Disease; Metadata: finding ROI; Categories: no findings and 14 disease categories (Atelectasis, Cardiomegaly, Effusion, Infiltration, Mass, Nodule, Pneumonia, Pneumothorax, Consolidation, Edema, Emphysema, Fibrosis, Pleural_Thickening, Hernia)</td>
    </tr>
    <tr>
      <th>8</th>
      <td>National Institutes of Health</td>
      <td>kaggle.com/nih-chest-xrays/sample Wang2017</td>
      <td>8 bits, Random sample of 5606 from 112,120 images of 30,805 unique patients</td>
      <td>PNG, resized</td>
      <td>X-ray database; Metadata: finding labels, follow-up, age, gender, view; Categories: Atelectasis, Cardiomegaly, Effusion, Infiltration, Mass, Nodule, Pneumonia, Pleural_Thickening, Hernia, Pneumothorax, Consolidation, Edema, Emphysema, Fibrosis</td>
    </tr>
    <tr>
      <th>9</th>
      <td>University of Montreal</td>
      <td>kaggle.com/praveengovi/coronahack-chest-xraydataset cohen2020covidProspective</td>
      <td>8 bits, 5910 cases (normal-1576, covid 58, SARS-4, virus-1493, bacteria 2777, ARDS-2)</td>
      <td>JPG,PNG-resized</td>
      <td>Collection Chest X Ray (anterior-posterior) of Healthy vs Pneumonia (Corona) affected patients infected patients along with few other categories such as SARS (Severe Acute Respiratory Syndrome), Streptococcus &amp; ARDS (Acute Respiratory Distress Syndrome); No metadata</td>
    </tr>
    <tr>
      <th>10</th>
      <td>University of California San Diego</td>
      <td>kaggle.com/paultimothymooney/chest-xray-pneumonia</td>
      <td>8 bits, 5863 cases</td>
      <td>JPG</td>
      <td>Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.; Categories: normal and pneumonia; No metadata</td>
    </tr>
    <tr>
      <th>11</th>
      <td>University of California San Diego</td>
      <td>github.com/UCSD-AI4H/COVID-CT Kermany2018LabeledOC</td>
      <td>8 bits, 349 cases</td>
      <td>Images collected (scanned) from covid-related and medical papers in PNG (covid) or JPG (normal)</td>
      <td>This dataset has 349 CT images containing clinical findings of COVID-19 from 216 patients; Categories: covid and noncovid cases; Metadata: age, gender, location, medical history (unfortunately modest), time after the onset of illness, severity, other diseases</td>
    </tr>
    <tr>
      <th>12</th>
      <td>University of California San Diego</td>
      <td>data.mendeley.com/datasets/rscbjbr9sj/2 Chowdhury2020</td>
      <td>8 bits, 5233 cases</td>
      <td>JPG (QF=95 for normal and QF=75 for pneumonia)</td>
      <td>Collection Chest X Ray; Categories: normal (1349 cases) vs pneumonia (3884 cases) including subcategories of bacteria and virus; No metadata</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Elazig in Turkey</td>
      <td>github.com/muhammedtalo/COVID-19  b21</td>
      <td>8 bits, 1125 cases</td>
      <td>JPG (QF=90, subsampling2x2), PNG (resized)</td>
      <td>X-Ray Images collection; No metadata; Categories: covid (125 cases), no findings (500 cases), pneumonia (500 cases)</td>
    </tr>
    <tr>
      <th>14</th>
      <td>National Library of Medicine</td>
      <td>openi.nlm.nih.gov/gridquery?it=xg&amp;coll=cxr&amp;m=1&amp;n=100</td>
      <td>8 bits or full bits, 7470 cases</td>
      <td>PNG (resized), Full DICOM</td>
      <td>Chest X-rays collection with 3,955 radiology reports; Categories: 14 pulmonary categories; Metadata: time after the onset of illness, severity, other diseases, captions of symptoms as unstructured symptom description</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Stanford University School of Medicine</td>
      <td>stanfordmlgroup.github.io/competitions/chexpert Irvin_2019</td>
      <td>8 bits, 224,316 chest radiographs of 65,240 patients</td>
      <td>JPG</td>
      <td>Large dataset of chest X-rays which features uncertainty labels and radiologist-labeled reference standard evaluation sets; Categories: each report was labeled for the presence of 14 observations (no finding, enlarged cardiom., cardiomegaly, lesion, opacity, edema, consolidation, pneumonia, atelectasis, pneumothorax, pleural effusion, pleural other, fracture, support devices) as positive, negative, or uncertain; Metadata: related to above categories (blank for unmentioned, 0 for negative, -1 for uncertain, and 1 for positive)</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Hospital San Juan de Alicante - University of Alicante</td>
      <td>bimcv.cipf.es/bimcv-projects/padchest  BUSTOS2020101797</td>
      <td>8 bits, more than 160,000 images from 67,000 patients</td>
      <td>PNG</td>
      <td>PadChest: A large chest x-ray image dataset with multi-label annotated reports; the reports were labeled with 174 different radiographic findings, 19 differential diagnoses, and 104 anatomic locations; a 27% of the reports were manually annotated by trained physicians; Metadata: age, sex</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Hospital Universitario San Cecilio</td>
      <td>github.com/ari-dasci/OD-covidgr  b26</td>
      <td>8 bits, 852 images</td>
      <td>JPEG (QF=90)</td>
      <td>X-ray images: 426 positive covid cases and 426 negative cases; only the posterior-anterior view is considered; Categories: covid severity - normal-PCR+ (76), mild (100), moderate (171), severe (79); General metadata: positive images correspond to patients who have been tested positive with RT-PCR within a time span of at most 24h between the X-ray image and the test; every image has been taken using the same type of equipment and with the same format</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Beth Israel Deaconess Medical Center in Boston</td>
      <td>physionet.org/content/mimic-cxr/2.0.0 Johnson2019</td>
      <td>full bits, 227,835 imaging studies for 65,379 patients</td>
      <td>full DICOM</td>
      <td>Chest radiographs with metadata: electronic health record data, dicom metadata, free-text radiology reports Categories: 14 pulmonary observations with an additional “uncertain” category</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Società Italiana di Radiologia Medica e Interventistica</td>
      <td>sirm.org/category/senza-categoria/covid-19</td>
      <td>8 bits</td>
      <td>mostly JPG (QF=95, subsampling2x2)</td>
      <td>Chest radiographs with free-text radiology and clinical reports, covid confirmation; Metadata includes selected information from electronic health record (e.g. symptoms, lab exams, ARDS, ventilatory assistance, previous exams); Categories: covid confirmation or no with 14 pulmonary observations</td>
    </tr>
    <tr>
      <th>20</th>
      <td>National Cancer Institute</td>
      <td>wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI Armato2015</td>
      <td>full bits, 1308 cases</td>
      <td>full DICOM</td>
      <td>The Lung Image Database consists of diagnostic and lung cancer screening thoracic CT scans with marked-up annotated lesions (XML); it includes three categories ("nodule &gt; or =3 mm," "nodule &lt;3 mm," and "non-nodule &gt; or =3 mm");</td>
    </tr>
    <tr>
      <th>21</th>
      <td>{University of Brescia</td>
      <td>brixia.github.io/#dataset</td>
      <td>full bits, 4,707 cases</td>
      <td>full DICOM</td>
      <td>COVID-19 subjects, acquired with both CR and DX modalities, in AP or PA projection with highly expressive multi-zone COVID-19 severity score, fully annotated; Metadata: the multi-region 6-valued Brixia-score defined for six zones, sex, age</td>
    </tr>
    <tr>
      <th>22</th>
      <td>open-edit radiology resource</td>
      <td>radiopaedia.org</td>
      <td>8 bits, a significant number of cases, constantly updated</td>
      <td>JPG with different QF, resized</td>
      <td>Database of general radiological purposes; in selected cases free-text radiology and clinical reports, selected; generally, quantitatively and qualitatively differentiated case reports</td>
    </tr>
    <tr>
      <th>23</th>
      <td>generated using data augmentation</td>
      <td>kaggle.com/nabeelsajid917/covid-19-x-ray-10000-images</td>
      <td>8 bits, 104 cases</td>
      <td>JPEG with different QF, resized</td>
      <td>Corona Virus X-ray Dataset; Categories: covid and normal; No metadata</td>
    </tr>
  </tbody>
</table>
<!--END_SECTION:data-section-->
