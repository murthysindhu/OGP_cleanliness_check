# OGP_cleanliness_check
Process OGP teflon/tooling images to check for impurities.
- Check for contaminants with `getSpeckScore.py`.
- Testing of different techniques can be found in the Jupyter Notebook `speck_score.ipynb`.


## Check for contaminants in an image:

```
py getSpeckScore.py -f path_to_file/image.png -m 2 -s 0.3
```
`-m`: Method for finding contaminant. \
`-m = 1` --> Cut on grayscale distribution. Specks tend to have darker pixels than the Teflon surface. \
`-m = 2` --> Cluster gray values into three clusters and find the percentage of pixels in the darkest cluster.\
\
`-s`: Percentage below which sample is flagged for contamination.

If the percentage of dark pixels > 0.5 implies the presence of contaminants.

## Install Pillow for reading in images
`pip install Pillow`

## Install OpenCV for k-means clustering
`pip install opencv-python`
- Documentation can be found here: https://docs.opencv.org/3.4/d1/d5c/tutorial_py_kmeans_opencv.html
