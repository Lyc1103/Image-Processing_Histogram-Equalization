# Histogram Equalization

> Author : Ya Chan<br>
> Date : 2021 / 4 / 6<br>
> List :
>
> > <a href = "#description">Description</a><br>
> > <a href = "#example">Example In-Output</a><br>
> > <a href = "#reference">Reference</a>

<br>
<div id = "description">

## Description

1. Develop a histogram equalization ( HE ) program;
2. Apply the HE to i) gray, ii) color images;
3. For each input image, print out the input/output images and their histograms.

For a color image C,<br>
( i ) Convert it into a gray image G;<br>
( ii ) Apply HE to G to get G’;<br>
( iii ) For each pixel of C, modify its color ( r , g , b ) by ( r’ , g’ , b’ ) = ( r , g , b ) X G’ / G.

</div>
<br>
<br>
<div id = "example">

## Example In-Outputs

### Inputs :

- Original Image:<br>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <img src = "https://i.imgur.com/J6rnVlT.jpg" width = "150">

### Outputs :

- Color image <b>without</b> Histogram-Equalization:<br>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <img src = "https://i.imgur.com/J6rnVlT.jpg" width = "150">

- Gray image <b>without</b> Histogram-Equalization:<br>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <img src = "https://i.imgur.com/Agat6pJ.jpg" width = "150">

- Color image <b>with</b> Histogram-Equalization:<br>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <img src = "https://i.imgur.com/FLwYszi.jpg" width = "150">

- Gray image <b>with</b> Histogram-Equalization:<br>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <img src = "https://i.imgur.com/5p5yBg2.jpg" width = "150">

</div>
<br>
<br>
<div id = "reference">

## Reference

<a href = "https://iter01.com/519791.html">Python 影像處理 OpenCV （16）：影像直方圖</a>
