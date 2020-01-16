

# Week 1

[TOC]

## Knowledge Transfer from Arthur

-   Check that canisters to the left of NO~2~ and CO~2~ are set at around 14.7 psi. 
    -   NO~2~: 14.7 psi
    -   CO~2~: 15.7 psi
-   Made a folder on the lab computer, called ```2020_enph352_esther``` to store my data temporarily. 
-   Apparently the lab manual is super out of date with how to use the software. 
    -   MUST bring a USB to the lab. 
    -   The computer is a linux machine. 
-   To change the pressure levels of the benchtop gas source, turn the knobs to the right (cw) to turn off. 



## Procedure

### Step 1

Just a note on how expensive the equipment is. 

### Step 2

#### Default Parameters for Acquisition Software:

| Param              | Default Value | Notes                                    |
| ------------------ | ------------- | ---------------------------------------- |
| Resolution         | 64 cm^-1^     | Is this how much the mirror moves per step inside the interferometer? |
| Velocity           | 3.16 mm/s     | Is this how fast the mirror moves inside the interferometer? |
| Low pass filter    | 3 kHz         |                                          |
| High pass filter   | 100 Hz        |                                          |
| Gain               | 1             | When do you change the gain?             |
| Offset             | 0             | The Offset field does not display numbers greater than 20. Look in the scanner value column for the actual offset value. When you apply new offsets, that's applied to the ones already existing. |
| No of acquisitions | 1             | max 32 scans                             |

#### Acquisition Software Process

1.  Set parameters to default
2.  Press write params to scanner
3.  Press Start ACQ
4.  After done, press copy text to clipboard
5.  Save data in a txt file. 
6.  Press gnuplot to plot data. Press a to refresh. 

#### The highest intesity part of the interferogram is called the centre burst. Explain the general shape of the interferogram. 

The general shape looks like a sinc function. It's the FT for the contour that it passes through, when no gas is applied. 

#### Why is the interferogram shifted? (it shouldn't be, consider playing with the offset)

-   The centre of the scan, the burst is the zero optical path difference (ZOPD). If it's shift, that means the ZOPD is not located when the mirror is at position zero. 

-   Why do we want the offset to be zero? 

    -    X axis is number of points. We want to capture the full interferogram. So we do an initial step of centering with the default values. 
    -   Set the burst to be at point 512. 

-   Calibration Example: 

    file: ```week1_centering.txt```

    ![Picture1](/Users/linesther/Downloads/Picture1.png)



#### What happens to interferogram at higher or lower resolutions?

One acquisition was collected. Madnesss occurs at resolution of 4. 

| Resolution | Timestamp                  | Filename                      | Graph                                    |
| ---------- | -------------------------- | ----------------------------- | ---------------------------------------- |
| 32         | 2019-09-1714:57:17.528495  | ``` week1_step2_res_32.txt``` | ![Picture2](/Users/linesther/Downloads/Picture2.png) |
| 16         | 2019-09-1714:59:33.954924  | ``` week1_step2_res_16.txt``` | ![Picture3](/Users/linesther/Downloads/Picture3.png) |
| 8          | 2019-09-1715:03:29.803103  | ``` week1_step2_res_8.txt```  | ![Picture4](/Users/linesther/Downloads/Picture4.png) |
| 4          | 2019-09-17 15:04:45.047499 | ``` week1_step2_res_4.tx```   | ![Picture5](/Users/linesther/Downloads/Picture5.png) |

### Step 3

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



### Step 4

Signal to noise ratio. 32 acquisitions for resolutions.

| Resolution | Timestamp                 | Filename                         | Graph                                    |
| ---------- | ------------------------- | -------------------------------- | ---------------------------------------- |
| 4          | 2019-09-1715:39:58.526794 | ``` week1_step4_snr_res_4.txt``` | ![Picture13](/Users/linesther/Downloads/Picture13.png) |
| 8          | 2019-09-1715:42:03.916245 | ``` week1_step4_snr_res_8.txt``` | ![Picture14](/Users/linesther/Downloads/Picture14.png) |



### Step 5

Flushing of the cell. After 15 mins of flushing: 

-   2019-09-17 16:02:19.182212
-   ```week1_step5_n2_flush.txt```

![Picture15](/Users/linesther/Downloads/Picture15.png)



## Notes

### The MIR8000 uses a HeNe laser as reference. 

The HeNe also goes through the interferometer, with no interaction with the IR laser. It creates a trigger pulse as HeNe goes through its fringes. This triggers the ADC. This gets sent to IR detector, that the ADC has moved another fringe pattern. Overall, this results in a data point being taken. 

The points on the x-axis of the plots being acquired from the MIR8000 are the intesity points as the HeNe goes through zero. From this, we can find distance travelled precisely. Together, resolution + velocity will set the number of points being acquires. 

**TODO**: we know that there are 1024 points being acquired for the default parameters. Hence, we can convert to the time domain. This will allow us to take the fourier transform to move into the frequency domain. 

**Important**: For the offset, this needs to be calibrated each lab session. Set the peak to $\frac{1}{2}(\text{# pts})$, so 5122 for the default params. This only needs to be done at the beginning of each lab. After initial calibration, everything else is an integer multiple of the fringes anyways. We saw that skipping starts at resolution 8, becomes obvious at resolution 4. The resolution is in wavenumber units. 

### Flushing of Cell and FTIR

You can stick one end of the tubing to check the flow rate. Can also check the lab manual for the flow rates to calculate how much time is needed to flush the cell. 