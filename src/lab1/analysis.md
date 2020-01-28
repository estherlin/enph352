# FTIR Lab Analysis

##Table of Contents

[TOC]

## Figuring out what Resolution Means [Jan. 18-20, 2020]

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

## Software Design [Jan. 18-23, 2020]

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
    -   A: *Ah so the rest of the processing steps are done on this array*
3.  The interferogram data is rotated so that the right side of the data after the ZPD, including the ZPD point, is moved to the front of the array. The data to the left of the ZPD is reversed and placed at the end of the array.
4.  The data is FFT'd, producing real and imaginary data arrays
5.  The power spectrum is derived from the real and imaginary data from the previous step. The power spectrum is the square root of the sum of the squares of the real and imaginary data. 
    -   Q: **Do we normalize???**
    -   A: *No*
6.  The real and imaginary data arrays are multiplied by the power spectrum (Figure 8). This is the end of the preparation of the phase correction data.

##### Step 4: The sample data is FFT's and phase corrected

1.  The original interferogram is apodized using a triangular function, with the value of 0 at the left side, a value of 1 at 2 times the ZPD location, and ramping back down to 0 at the right side.
    -   Q: **a value of 1 at 2 times the ZPD location? Isn't this problematic for bursts that are centered?**
    -   A: Dr. Reinsberg (and other sources) say that we should just do the ramp function centered at the burst. 
2.  The apodized interferogram is zero-filled.
3.  The interferogram is rotated 
4.  The interferogram is FFT'd
5.  The complex (real and imaginary) data are multiplied by the complex phase correction data from step 3. 
    -   Q: **Do you multiply imaginary with imaginary, vice versa with real?**
    -   A: *No you multiply complex with complex*

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



## Positive Control Test to see if MIR8000 is Oversampling [Jan. 23 2020]

But is this thing oversampling???

Note: Try the positive control

Also, peaks for water: 