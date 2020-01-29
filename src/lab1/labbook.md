# FITR Lab Logbook
The layout of this labbook is as follows: I have split this into 3 sections:

1.  **Data Collection**

    This section is organized by the week of the lab. Dates and filenames are noted. 

2.  **Analysis**

    The section is organized by topics that were encountered. Dates are recorded for the duration of the problem.

3.  **Results**

    This section is organized by the procedure outlined in the lab manual. Questions in lab manual are answered here.

4.  **Conclusions**


# Table of Contents

[TOC]

# Data Collection

##Week 1 [Jan. 14, 2020]

All data is stored under the ```data/lab1/week1/``` directory. 

### Knowledge Transfer from Arthur [Jan. 18, 2020]

-   Check that canisters to the left of NO~2~ and CO~2~ are set at around 14.7 psi. 
    -   NO~2~: 14.7 psi
    -   CO~2~: 15.7 psi
-   Made a folder on the lab computer, called ```2020_enph352_esther``` to store my data temporarily. 
-   Apparently the lab manual is super out of date with how to use the software. 
    -   MUST bring a USB to the lab. 
    -   The computer is a linux machine. 
-   To change the pressure levels of the benchtop gas source, turn the knobs to the right (cw) to turn off. 



### Lab Procedures Conducted

#### Step 1

Just a note on how expensive the equipment is. 

#### Step 2

Default Parameters for Acquisition Software:

| Param              | Default Value | Notes                                    |
| ------------------ | ------------- | ---------------------------------------- |
| Resolution         | 64 cm^-1^     | Is this how much the mirror moves per step inside the interferometer? |
| Velocity           | 3.16 mm/s     | Is this how fast the mirror moves inside the interferometer? |
| Low pass filter    | 3 kHz         |                                          |
| High pass filter   | 100 Hz        |                                          |
| Gain               | 1             | When do you change the gain?             |
| Offset             | 0             | The Offset field does not display numbers greater than 20. Look in the scanner value column for the actual offset value. When you apply new offsets, that's applied to the ones already existing. |
| No of acquisitions | 1             | max 32 scans                             |

**Acquisition Software Process**

1.  Set parameters to default
2.  Press write params to scanner
3.  Press Start ACQ
4.  After done, press copy text to clipboard
5.  Save data in a txt file. 
6.  Press gnuplot to plot data. Press a to refresh. 

**The highest intesity part of the interferogram is called the centre burst. Explain the general shape of the interferogram.**

The general shape looks like a sinc function. It's the FT for the contour that it passes through, when no gas is applied. 

**Why is the interferogram shifted? (it shouldn't be, consider playing with the offset)**

-   The centre of the scan, the burst is the zero optical path difference (ZOPD). If it's shift, that means the ZOPD is not located when the mirror is at position zero. 

-   Why do we want the offset to be zero? 

    -    X axis is number of points. We want to capture the full interferogram. So we do an initial step of centering with the default values. 
    -    Set the burst to be at point 512. 

-   Calibration Example: 

    file: ```week1_centering.txt```

    ![Picture1](/Users/linesther/Downloads/Picture1.png)


**What happens to interferogram at higher or lower resolutions?**

One acquisition was collected. Madnesss occurs at resolution of 4. 

| Resolution | Timestamp                  | Filename                      | Graph                                    |
| ---------- | -------------------------- | ----------------------------- | ---------------------------------------- |
| 32         | 2019-09-1714:57:17.528495  | ``` week1_step2_res_32.txt``` | ![Picture2](/Users/linesther/Downloads/Picture2.png) |
| 16         | 2019-09-1714:59:33.954924  | ``` week1_step2_res_16.txt``` | ![Picture3](/Users/linesther/Downloads/Picture3.png) |
| 8          | 2019-09-1715:03:29.803103  | ``` week1_step2_res_8.txt```  | ![Picture4](/Users/linesther/Downloads/Picture4.png) |
| 4          | 2019-09-17 15:04:45.047499 | ``` week1_step2_res_4.tx```   | ![Picture5](/Users/linesther/Downloads/Picture5.png) |

#### Step 3

Vary number of acquisitions. Task: acquire spectra without nitrogen flow at resolution of 4. You need to average several spectra for better SNR. How many? Conclusion: just do the max, 32 acquisitions. 

| Number of Acquisitions | Timestamp                 | Filename                            | Graph                                    |
| ---------------------- | ------------------------- | ----------------------------------- | ---------------------------------------- |
| 32                     | 2019-09-1715:08:18.145604 | ``` week1_step3_no_no2_32acq.txt``` | ![Picture7](/Users/linesther/Downloads/Picture7.png) |
| 16                     | 2019-09-1715:12:13.229219 | ``` week1_step3_no_no2_16acq.txt``` | ![Picture8](/Users/linesther/Downloads/Picture8.png) |
| 8                      | 2019-09-1715:15:17.012119 | ```week1_step3_no_no2_8acq.txt```   | ![Picture9](/Users/linesther/Downloads/Picture9.png) |

FTIR N2 flow: Didn’t get data after 5 mins. 10 mis however.
FTIR flow: 15. Cells set at 0. Read about FTIR flow rate. 

| Number of Minutes | Timestamp                  | Filename                         | Graph                                    |
| ----------------- | -------------------------- | -------------------------------- | ---------------------------------------- |
| 10                | 2019-09-17 15:29:24.814325 | ``` week1_step3_n2_10mins.txt``` | ![Picture11](/Users/linesther/Downloads/Picture11.png) |
| 20                | 2019-09-17 15:37:25.882325 | ``` week1_step3_n2_20mins.txt``` | ![Picture12](/Users/linesther/Downloads/Picture12.png) |



#### Step 4

Signal to noise ratio. 32 acquisitions for resolutions.

| Resolution | Timestamp                 | Filename                         | Graph                                    |
| ---------- | ------------------------- | -------------------------------- | ---------------------------------------- |
| 4          | 2019-09-1715:39:58.526794 | ``` week1_step4_snr_res_4.txt``` | ![Picture13](/Users/linesther/Downloads/Picture13.png) |
| 8          | 2019-09-1715:42:03.916245 | ``` week1_step4_snr_res_8.txt``` | ![Picture14](/Users/linesther/Downloads/Picture14.png) |



#### Step 5

Flushing of the cell. After 15 mins of flushing: 

-   2019-09-17 16:02:19.182212
-   ```week1_step5_n2_flush.txt```

![Picture15](/Users/linesther/Downloads/Picture15.png)



### Notes

#### The MIR8000 uses a HeNe laser as reference. 

The HeNe also goes through the interferometer, with no interaction with the IR laser. It creates a trigger pulse as HeNe goes through its fringes. This triggers the ADC. This gets sent to IR detector, that the ADC has moved another fringe pattern. Overall, this results in a data point being taken. 

The points on the x-axis of the plots being acquired from the MIR8000 are the intesity points as the HeNe goes through zero. From this, we can find distance travelled precisely. Together, resolution + velocity will set the number of points being acquires. 

**TODO**: we know that there are 1024 points being acquired for the default parameters. Hence, we can convert to the time domain. This will allow us to take the fourier transform to move into the frequency domain. 

**Important**: For the offset, this needs to be calibrated each lab session. Set the peak to $\frac{1}{2}(\text{# pts})$, so 5122 for the default params. This only needs to be done at the beginning of each lab. After initial calibration, everything else is an integer multiple of the fringes anyways. We saw that skipping starts at resolution 8, becomes obvious at resolution 4. The resolution is in wavenumber units. 

#### Flushing of Cell and FTIR

You can stick one end of the tubing to check the flow rate. Can also check the lab manual for the flow rates to calculate how much time is needed to flush the cell. 



## Week 2 [Jan. 21, 2020]

All data is store under the ```data/lab1/week2/``` directory. Conducted a portion of the experiment with Arthur. 

### Lab Procedures Conducted

#### Centering

Use resolution of 32 parameters to set center burst to 1024. Also need to check if baseline is at 0. Spectrums are really noisy. Realized that IR source was off. Done with the cell in place, 

-   Only graph was saved. 
-   Remember, positive sign in offset field means to move burst to left

![Picture19](/Users/linesther/Downloads/Picture19.png)

#### Step 7

Absorption of air. Flushed cell with air, hooked up by TA. Acquire a signal at 4cm^-1^ resolution. Worked with Arthur to purge the cell with air. Collect data with Arthur. Tried one acquisition, also wanted to see the forwards and backwards motion. so did it with 32. 

| Num Acquisitions                         | Timestamp                  | Filename                               | Graph                                    |
| ---------------------------------------- | -------------------------- | -------------------------------------- | ---------------------------------------- |
| 1                                        | 2019-09-1711:36:59.072198  | ```step7/air_cell_4cm-1.txt```         | ![Picture20](/Users/linesther/Downloads/Picture20.png) |
| 32 (wanted to see backwards and forwards) | 2019-09-17 11:43:26.764214 | ```step7/air_cell_4cm-1(32 acq).txt``` | ![Picture21](/Users/linesther/Downloads/Picture21.png) |

#### Step 5

Flush cell with N2. Did after step 7, since air is mostly N~2~. Flow rate on this is pretty pathetic. Should flush for 20 mins. Flushing rate at max 60. Having arduino problems. On the bright side, we have been flushing since 2:45pm. Got data after purging for 25 mins. All data were taken with 32 acquisitions

| Trial # | Timestamp                  | Filename                                 | Graph                                    |
| ------- | -------------------------- | ---------------------------------------- | ---------------------------------------- |
| 1       | 2019-09-1712:12:17.068642  | ```step5/n2_cell_4cm-1 (32 ac).txt```    | ![Picture22](/Users/linesther/Downloads/Picture22.png) |
| 2       | 2019-09-17 12:17:33.931597 | ```step5/n2_cell_4cm-1 (arthur 32ac).txt``` | ![Picture23](/Users/linesther/Downloads/Picture23.png) |

Spoke to prof. Will need to filter off the acquisitions that have no prominent peak. They will only increase the S/N. 

#### Step 6

Started CO~2~ purging at 3:16pm. At 60. After one minute, take 32 acquisitions. We proceeded to take several rounds of data, each at different time points. Have to be careful about CO~2~. We only purged for 1 minute, and we fanned the area afterwards.

| Time after 1 min Purge [min] | Timestamp                  | Filename                               | Graph                                    |
| ---------------------------- | -------------------------- | -------------------------------------- | ---------------------------------------- |
| 1+4                          | 2019-09-1712:22:39.932372  | ```step6/co2_cell_4cm-1.txt```         | ![Picture25](/Users/linesther/Downloads/Picture25.png) |
| 3+4                          | 2019-09-17 12:25:28.394080 | ```step6/co2_cell_4cm-1 (3min).txt```  | ![Picture26](/Users/linesther/Downloads/Picture26.png) |
| 6+4                          | 2019-09-17 12:27:38.830395 | ```step6/co2_cell_4cm-1 (6 min).txt``` | ![Picture27](/Users/linesther/Downloads/Picture27.png) |

#### Step 4

Redid signal to noise measurements. Dr. Reinsberg suggested that we try the processing with more finer resolutions. I had let the FTIR purge with N~2~ for a while. 

| Resolution [cm^-1^] | Timestamp                  | Filename                         | Graph                                    |
| ------------------- | -------------------------- | -------------------------------- | ---------------------------------------- |
| 4                   | 2019-09-17 13:27:49.674836 | ```week2_step4_snr_res_4.txt```  | ![Picture18](/Users/linesther/Downloads/Picture18.png) |
| 8                   | 2019-09-17 13:40:53.559685 | ```week2_step4_snr_res_8.txt```  | ![Picture17](/Users/linesther/Downloads/Picture17.png) |
| 16                  | 2019-09-17 13:41:55.179366 | ```week2_step4_snr_res_16.txt``` | ![Picture16](/Users/linesther/Downloads/Picture16.png) |

### Notes

####Resolution discussion with Dr. Reinsberg

Had a discussion with Dr. Reinsberg as to how to check if the MIR8000 is oversampling or not. Performing the calculations, we see that it might be oversampling. Need to use a positive control to determine for sure though. See section in analysis.



# Analysis

## 1. Figuring out what Resolution Means [Jan. 18-20, 2020]

From the notes, we know that the Nyquist frequency of the FTIR depends on the HeNe laser and can be calculated from the equation of the [Nyquist frequency](Nyquist frequency) $f_{\text{Nyquist}} = \frac{1}{2}f_s$:
$$
f_{\text{Nyquist}} = \frac{c}{2\lambda_{\text{HeNe}}}
$$
We can convert this to an upper limit on *wavenumber* corresponding to the positive frequencies:
$$
\nu_{\text{Nyquist}} = \frac{2f_\text{Nyquist}}{c} = 15804 \text{ cm}^{-1}
$$
This allows us to determine the wavenumber spacing $\Delta \nu$ for the frequency domain spectrum by dividing $\nu_{\text{Nyquist}}$by the number of points on the positive half of the frequency domain. This is because the Fourier transform will give a symmetric spectrum, and we are only interested in the positive half. So, 
$$
\Delta \nu = \frac{\nu_{\text{Nyquist}}}{\frac{N}{2}}
$$
where $N$ is the total number of points collected by the spectrometer. This allows us to construct a table of resolutions and their corresponding wavenumber spacings $\Delta \nu$ using the number of points as collected in the part 2 of the lab procedure (sampling):

| Resolution [cm^-1^] | \# of points | \# of points (power of 2) | $\Delta \nu_\text{sampling}$ [cm^-1^] | $\Delta \nu_\text{over sampling}$ [cm^-1^] |
| ------------------- | ------------ | ------------------------- | ------------------------------------- | ---------------------------------------- |
| 64                  | 1024         | 2^10^                     | 30.86                                 | 61.72                                    |
| 32                  | 2048         | 2^11^                     | 15.43                                 | 30.86                                    |
| 16                  | 4096         | 2^12^                     | 7.72                                  | 15.44                                    |
| 8                   | 8192         | 2^13^                     | 3.86                                  | 7.72                                     |
| 4                   | 16384        | 2^14^                     | 1.93                                  | 3.86                                     |

 OR. I can just do ```np.linspace(start=0, stop=15802, num=int(num_points/2))```. Since the number of points actually fluctuates for the lower resolutions. 

### Positive Control Test to see if MIR8000 is Oversampling [Jan. 23 2020]

But is this thing oversampling???

Note: Try the positive control

Also, peaks for water: 

## 2. Software Design [Jan. 18-23, 2020]

The lab says: "*The software does not provide even the most basic of data post processing. This is a left asan exercise to the student; consider the tutorial provided here:www.essentialftir.com/tTutorial.html and the references listed below. Investigate the optimal process of a bi-directional spectrum using forward and reverse mirror direction and theapplication of the appropriate phase correction (Mertz method).*"

OH NO. There is so much analysis work. I tried to find existing FTIR softwares, but they do not support the flexibility we need for our experimental procedure. DOES THIS MEAN I HAVE TO WRITE THE CODE FOR EVERYTHING??? [Jan. 18, 2020]. 

[Jan. 20, 2020] yes. Unfortunate. The requirements for this Python code:

-   Need to be able to handle more than 1 acquisitions as smoothly as one acquisition. 
-   code will be documented with pdocs and hosted on my site 

#### Mertz Method

You follow the steps outlined in [FFT applied to FTIR](https://web.archive.org/web/20180816190611/http://essentialftir.com/fftTutorial.html). All graphs shown below are done with ```week1_centering.txt```

I feel like I gave this a pretty good shot. 

#####Step 1: Normalize data 

Required prior to zero filling.

-   Subtract mean of data from the data, setting the baseline to zero. 
-   If data file has multiple acquisitions, use mean of the entire datafile over all acquisitions for continuity. 

##### Step 2: Zero fill the interferogram

The FFT requires that the number of points in the interferogram be a power of 2. If it is not, then the size of the array is increased to the next higher power of two and the added points are set to 0.

***The FFT requires that the number of points in the interferogram be a power of 2. If it is not, then the size of the array is increased to the next higher power of two and the added points are set to 0.***

##### Step 3: Prepare phase corrected data with the mertz method

1.  An array of the same size as the zero-filled interferogram is prepared and filled with zeros.
2.  The 256 points centered around ZPD are copied from the interferogram into the new array, but are scaled by a ramp function that is 1 at the ZPD and 0 at the beginning and end. 
    -   Q: **What do we do with this new array?**
    -   A: *Ah so the rest of the processing steps are done on this array* (Dr. Reinsberg)
3.  The interferogram data is rotated so that the right side of the data after the ZPD, including the ZPD point, is moved to the front of the array. The data to the left of the ZPD is reversed and placed at the end of the array.
4.  The data is FFT'd, producing real and imaginary data arrays
5.  The power spectrum is derived from the real and imaginary data from the previous step. The power spectrum is the square root of the sum of the squares of the real and imaginary data. 
    -   Q: **Do we normalize???**
    -   A: *No*(Dr. Reinsberg)
6.  The real and imaginary data arrays are multiplied by the power spectrum (Figure 8). This is the end of the preparation of the phase correction data.

##### Step 4: The sample data is FFT's and phase corrected

1.  The original interferogram is apodized using a triangular function, with the value of 0 at the left side, a value of 1 at 2 times the ZPD location, and ramping back down to 0 at the right side.
    -   Q: **a value of 1 at 2 times the ZPD location? Isn't this problematic for bursts that are centered?**
    -   A: *Dr. Reinsberg (and other sources) say that we should just do the ramp function centered at the burst.* (Dr. Reinsberg)
2.  The apodized interferogram is zero-filled.
3.  The interferogram is rotated 
4.  The interferogram is FFT'd
5.  The complex (real and imaginary) data are multiplied by the complex phase correction data from step 3. 
    -   Q: **Do you multiply imaginary with imaginary, vice versa with real?**
    -   A: *No you multiply complex with complex* (Dr. Reinsberg)

![steps4](/Users/linesther/Downloads/mertzcomparison.png)

The mertz method seems to do a lot of smoothing. Not sure if this is what we want???

#### Ratio and Conversion to Transmission/Absorbance

1.  IR spectroscopy is a single-beam technique. The sample data must be ratioed against a background spectrum to produce a transmittance spectrum. 
2.  Usually the background spectrum is collected using a gas cell filled with N~2~
3.  Calculate the transmittance per wavenumber: $\frac{I}{I_0} \equiv T = 10^{-\epsilon c d}$
4.  Calculate the absorbance per wavenusmber: $A = -\log T = \epsilon c d$

Test results using the same spectra the transmittance and absorbance calculations:

![trans](/Users/linesther/Downloads/trans.png)

![abs](/Users/linesther/Downloads/abs.png)



# Results





