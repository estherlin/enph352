# FITR Lab Logbook
The layout of this labbook is as follows: I have split this into 5 sections:

1.  **Theoretical Background**

    Background research + objectives + overview of lab procedure done prior to doing the lab.

2.  **Data Collection**

    This section is organized by the week of the lab. Dates and filenames are noted. 

3.  **Analysis**

    The section is organized by topics that were encountered. Dates are recorded for the duration of the problem.

4.  **Results**

    This section is organized by the procedure outlined in the lab manual. Questions in lab manual are answered here.

5.  **Conclusions**


A copy of this labbook can be found on my lab book site: [link](https://estherlin.github.io/enph352/lab1/lab1.html). All of the code I used for analysis, complete with documentation is also there. 

# Table of Contents

[TOC]

# Background

## Theory [Jan. 10, 2020]

Quick intro: 

Inthe mid-infrared region of the electromagnetic spectrum, molecules absorb lightthrough the interaction between the photons and the vibrating electric dipoles of the molecule. 

In FTIR, a beam carrying many frequencies irradiates a sample. We measure how muchof that beam is absorbed and transmitted by the sample.

Withthe transmission and absorbance spectra, we can identifythe molecules in the sample.

### Absorption Lines in Air and CO~2~

 In the *mid-infrared* (MIR) region of the electromagnetic spectrum, molecules absorb (or emit) light through the *interaction between the photons and the vibrating electric dipoles of the molecule*.

-   CO: C has 4 valence e^-^, O has e^-^. Hence, has a strong osciallting dipole moment. 
    -   Will absorb strongly (sharp line shapes) at specific energies. 
    -   Common for many organic molecules
-   O~2~ (non organic) has no dipole moment
    -   Shows up as transparent in MIR region. 

**The key factor in the MIR region is electric dipole**. 

### Vibrational Modes

E&M waves in the *infrared* (IR) region with wavelengths λ between *780 nm and 2000 µm*, (wavenumbers ν between 12800 cm^-1^ and 5 cm^-1^) can stimulate *molecular vibration and rotation modes*. However, light can only be absorbed if there is a net change of dipole moment dude to the vibrational motion of the molecule (*transition dipole moment*). 

In other words, **for a mode to be observed in the IR regime, changes must occur in the permanent dipole**. As a result, diatomic atoms like N~2~ and O~2~ will be transparent in IR absorption spectra. 

There are  [6 normal modes of vibration](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Spectroscopy/Vibrational_Spectroscopy/Vibrational_Modes/Number_of_Vibrational_Modes_in_a_Molecule) for polyatomic molecules.  To calculate the number of vibration modes of a molecule:

1.  Determine the total number of degrees of freedom in molecule. 

    -   for an atom in 3D, it has 3 degrees of freedom
    -   a molecule of N atoms will have 3N degrees of freedom

2.  Determine whether or not molecule is linear or non-linear

    -   Linear molecules have bond angles of 180°, so there are 3 degrees of freedom for translational motion and 2 degrees of freedom for rotational motion
    -   Nonlinear molecules have 3 degrees of freedom for translational motion and 3 degrees of freedom for rotational motion

3.  Find number of degrees of vibrational freedom 
    $$
    \text{# vibrational} = \text{# total } - \text{# translational} -  \text{# rotational}
    $$

    -   Linear molecules: 3N - 5
    -   Nonlinear molecules: 3N-6

Examples that I did to clarify my understanding (checked with librechemistry online):

1.  CH~4~ has $3(5)-6=9$ vibrational modes
2.  CO~2~ has $3(3)-5 = 4$ vibrational modes
3.  SO~2~ has $3(3)-6=5$ vibrational modes

The lab manual provided us with an IR absorption spectra of common atmospheric gases:

>   ![Screen Shot 2020-02-04 at 11.18.32 AM](/Users/linesther/Desktop/Screen Shot 2020-02-04 at 11.18.32 AM.png)
>
>   IR absorption spectra of common atmospheric gases, from Handbook of Geophysics and Space Enviroments by S.L. Valley, Ed. (1965)

We will be more interested in the 1000 - 600 cm^-1^ region. 

### Lineshape

In theory, absoption lines should be at specific frequencies, but in practice they are limited by:

1.  Natural broadening, ie. Heisenberg uncertainty principle, so small, can be ignored
2.  Doppler broadening, ie. temperature broadening
3.  Collision broadening, ie. pressure broadening

The gaussian shape of doppler broadening is more compact while the Lorentzian is narrow but doesn't decay as fast. 

**Doppler Broadening**

Caused by the random rapid translational motions of gas molecules. The spectral shape is a gaussian distribution about an average $\nu_0$:
$$
P(\nu) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(\nu-\nu_0)^2}{2\sigma^2}}
$$
where $FWHM = 2\sigma\sqrt{2\ln 2} = 2.35\sigma$

**Collision Broadening**

Caused by disturbances to the absorption process during molecular collisions. The spectral shape is a Lorentzian (Cauchy) lineshape:
$$
P(\nu) = \frac{1}{2\pi}\frac{\Gamma}{(\nu - \nu_0)^2 + (\frac{\Gamma}{2})^2}
$$
where $FWHM = \Gamma$. The Lorentzian distribution, is a continuous probability distribution that is the ratio of two independent normally distributed random variables if the denominator distribution has mean zero. 

### FTIR Overview

A beam carrying many frequencies is shone on sample. Measures how much of that beam is absorbed by sample. Then beam is modified to contain a different combo fo freqnecies, for a 2nd data point. Repeated over short timespan. Absorption at every wavelength is then back calculated. 

-   Technique used to obtain IR spectrum of absorption/emissin of matter
-   Collects data over a wide spectral range
-   Fourier transform is needed to convert raw data to spectrum. Converts displacement of the mirror (cm) to wavenumbers (cm^-1^)
-   The spectrum of wavelengths are created using a Michelson interferometer. By moving non-probing branch mirror back, different wavelengths are blocked. 
-   Ideally, we would be irradiating a window that is not affected my thermal radiation absorption, such as  microwave and IR: 3.5-5 and 8-12 $\mu m$.
-   Has a high signal to noise


Intensity spectra can be converted into transmission (T) or absorbance (A) spectra with the **Beer-Lambert law**, where the measured A or T is on the y-axis and wavenumbers are on the x:

-   $T = \frac{I}{I_0} = 10^{\epsilon cd}$
-   $A = -\log T = \epsilon cd$

where:

-   $\epsilon$: molar absorption coefficient
-   $c$: sample concentrations
-   $d$: sample thickness
-   $I$: intensity of the sample spectra
-   $I_0$: intensity of the background/reference spectra

Chemists  prefer absorbance spectra because sample concentrations (c) can be estimated by the Beer-Lambert law. 

## Questions [Jan. 10, 2020]

1.  Wave numbers [k or $\nu$] scale linearly with energy? 

    A: Oh that makes so much sense. LOL what a dumb question. 

2.  What is a vibrational mode?

    A: See notes above

3.  What is a transition dipole moment?

    A: the [electric dipole moment](https://en.wikipedia.org/wiki/Electric_dipole_moment) associated with the transition between the two states. 

    -   a complex vector quantity that includes the phase factors associated with the two states
    -   transitions to different orbitals
    -   useful for determining if transitions are allowed under the electric dipole interaction

4.  Isn't molar absorption coefficient dependent on wavenumber?

    A: Yes. It's the variable $\epsilon$ that we see in the lab manual. 

## Objectives for Lab [Jan. 10, 2020]

1. To understand and familiarize yourself with infrared spectroscopy as a measurement tool.
2. To measure and understand the absorption spectra of several gases.

[Jan. 22, 2020]: Addendum to objectives:

- [x] Learn how signal processing works for FTIR labs. The Mertz method is really cool, I can see this being applicable in many other places.
- [x] Review the Nyquist thm and how sampling works for constructing signals.

## Overview of Procedure for the Lab
>   ![ENPH352Poster-FTIR](/Users/linesther/Downloads/ENPH352Poster-FTIR.png)
>
>   System level diagram of experimental setup, drawn by me. The Michelson interferometer setup on the left, and the analysis is done by the user on the computer with Fourier transform magics.

The FTIR is based on the Michelson interferometer. A multimode laser transmits light on the beamsplitter, which splits the light into two beams. The first beam hits the stationary mirror and transmits to the detector through the gas cell. The second beam travels to the scanning mirror. By translating the scanning mirror, different wavelengths in the beam are selected to pass through the gas cell. The detector records the interaction of the beams with the molecules (interferogram) in the gas cell and sends the information to a computer for Fourier Transform analysis.

Here, I summarize a general procedure for this lab, a high level summary of what the lab manual provides:

1.  Familiarize self with equipement.
2.  Acquire centered interferogram. 
    1.  Write software to processing interferogram and find the spectrums. 
    2.  Investigate relation between resolution and interferogram. 
3.  Investigate effect of purging the FTIR with N~2~
4.  Determine the signal to noise ration of interferometer at different resolutions
5.  Acquire interferogram with the addtion of a N~2~ gas cell
6.  Acquire interferogram with the addition of a CO~2~ gas cell (don't breathe in the CO~2~)
7.  Acquire interferogram with the addition of a air gas cell
8.  Calculate the fraction of CO~2~ in air. 

Each section will have more detailed instructions.


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

Default parameters + notes for acquisition software:

| Param              | Default Value | Notes                                    |
| ------------------ | ------------- | ---------------------------------------- |
| Resolution         | 64 cm^-1^     | Is this how much the mirror moves per step inside the interferometer? |
| Velocity           | 3.16 mm/s     | Is this how fast the mirror moves inside the interferometer? |
| Low pass filter    | 3 kHz         |                                          |
| High pass filter   | 100 Hz        |                                          |
| Gain               | 1             | When do you change the gain?             |
| Offset             | 0             | The Offset field does not display numbers greater than 20. Look in the scanner value column for the actual offset value. When you apply new offsets, that's applied to the ones already existing. A postive value will move burst to the left. |
| No of acquisitions | 1             | max 32 scans                             |

**Acquisition Software Process**

1.  Set parameters to default
2.  Press write params to scanner
3.  Press Start ACQ
4.  After done, press copy text to clipboard
5.  Save data in a txt file. 
6.  Press gnuplot to plot data. Press a to refresh. 

**The highest intesity part of the interferogram is called the centre burst. Explain the general shape of the interferogram.**

The general shape looks like a sinc function. ~~It's the FT for the contour that it passes through, when no gas is applied.~~ I actually don't know what I'm saying here. 

**Why is the interferogram shifted? (it shouldn't be, consider playing with the offset)**

-   The centre of the scan, the burst is the zero optical path difference (ZOPD). If it's shift, that means the ZOPD is not located when the mirror is at position zero. 

-   Why do we want the offset to be zero? 

    -    A; X axis is number of points. We want to capture the full interferogram. So we do an initial step of centering with the default values. 
    -    **Set the burst to be at point 512.** 
    -    After entering your ZOPD, we're good for the remainder of the lab. 

-   Calibration Example: 

    file: ```week1_centering.txt```

    >   ![Picture1](/Users/linesther/Downloads/Picture1.png)Example of centering. The burst is at approx point 512, which means that the full bidirectional interferogram is captured. 


**What happens to interferogram at higher or lower resolutions?**

One acquisition was collected. Madnesss occurs at resolution of 4. Otherwise, more points are being collected. 

| Resolution | Timestamp                  | Filename                      | Graph                                    |
| ---------- | -------------------------- | ----------------------------- | ---------------------------------------- |
| 32         | 2019-09-1714:57:17.528495  | ``` week1_step2_res_32.txt``` | ![Picture2](/Users/linesther/Downloads/Picture2.png) |
| 16         | 2019-09-1714:59:33.954924  | ``` week1_step2_res_16.txt``` | ![Picture3](/Users/linesther/Downloads/Picture3.png) |
| 8          | 2019-09-1715:03:29.803103  | ``` week1_step2_res_8.txt```  | ![Picture4](/Users/linesther/Downloads/Picture4.png) |
| 4          | 2019-09-17 15:04:45.047499 | ``` week1_step2_res_4.tx```   | ![Picture5](/Users/linesther/Downloads/Picture5.png) |

#### Step 3

>   Instructions copied from the lab manual: 
>
>   At 4 cm-1 resolution, acquire a spectrum without nitrogen flow. You will want to average several spectra for better SNR (how many?). Now gently flow N2 gas through the FTIR and source units and let them purge for a while. Take a new spectrum after 5 min. of purge and another one 5 min. later (saving both, of course)… continue purging for the remainder of the lab.

Vary number of acquisitions. Task: acquire spectra without nitrogen flow at resolution of 4. You need to average several spectra for better SNR. How many? Conclusion: just do the max, 32 acquisitions. 

| Number of Acquisitions | Timestamp                 | Filename                            | Graph                                    |
| ---------------------- | ------------------------- | ----------------------------------- | ---------------------------------------- |
| 32                     | 2019-09-1715:08:18.145604 | ``` week1_step3_no_no2_32acq.txt``` | ![Picture7](/Users/linesther/Downloads/Picture7.png) |
| 16                     | 2019-09-1715:12:13.229219 | ``` week1_step3_no_no2_16acq.txt``` | ![Picture8](/Users/linesther/Downloads/Picture8.png) |
| 8                      | 2019-09-1715:15:17.012119 | ```week1_step3_no_no2_8acq.txt```   | ![Picture9](/Users/linesther/Downloads/Picture9.png) |

It can be hard to gather a spectra for the resolution of 4. Sometimes you get good spectra when everything in the FTIR lines up with the ADC, and sometimes, you get what you see above. 

FTIR N2 flow: Didn’t get data after 5 mins. 10 mins however. The flow rate was low, though, I would say it was half of what it should be. Hence, treat the 10 mins as the 5 mins. 
FTIR flow: 15. Cells set at 0. Read about FTIR flow rate. 

| Number of Minutes | Timestamp                  | Filename                         | Graph                                    |
| ----------------- | -------------------------- | -------------------------------- | ---------------------------------------- |
| 10                | 2019-09-17 15:29:24.814325 | ``` week1_step3_n2_10mins.txt``` | ![Picture11](/Users/linesther/Downloads/Picture11.png) |
| 20                | 2019-09-17 15:37:25.882325 | ``` week1_step3_n2_20mins.txt``` | ![Picture12](/Users/linesther/Downloads/Picture12.png) |

#### Step 4

>   Instructions copied from the lab manual: 
>
>   Acquire a signal at 4 cm-1 resolution (possibly averaged). Determine the Signal to Noise
>   (S/N) ratio over the useful spectral range. 

Signal to noise ratio acquisitions. 32 acquisitions for different resolutions.

| Resolution | Timestamp                 | Filename                         | Graph                                    |
| ---------- | ------------------------- | -------------------------------- | ---------------------------------------- |
| 4          | 2019-09-1715:39:58.526794 | ``` week1_step4_snr_res_4.txt``` | ![Picture13](/Users/linesther/Downloads/Picture13.png) |
| 8          | 2019-09-1715:42:03.916245 | ``` week1_step4_snr_res_8.txt``` | ![Picture14](/Users/linesther/Downloads/Picture14.png) |

#### Step 5

>   Copied from the lab manual:
>
>   Install the gas cell and purge it too with N2 making sure that the valve on the gas cell is open. Wait a sufficient amount of time for the system to be well purged. Acquire signal at 4 cm-1 resolution and use the throughput spectrum from the last step as your normalization spectrum. Measure the optical throughput of the gas cell (which corresponds largely to the transparency of the windows).

Flushing of the cell. After 15 mins of flushing: 

-   2019-09-17 16:02:19.182212
-   ```week1_step5_n2_flush.txt```

![Picture15](/Users/linesther/Downloads/Picture15.png)



### Notes

#### Next Time

Start with step 7 and work way back up. Need to recapture data for step 4. 

#### The MIR8000 uses a HeNe laser as reference. 

The HeNe also goes through the interferometer, with no interaction with the IR laser. It creates a trigger pulse as HeNe goes through its fringes. This triggers the ADC. This gets sent to IR detector, that the ADC has moved another fringe pattern. Overall, this results in a data point being taken. 

The points on the x-axis of the plots being acquired from the MIR8000 are the intesity points as the HeNe goes through zero. From this, we can find distance travelled precisely. Together, resolution + velocity will set the number of points being acquires. 

**TODO**: we know that there are 1024 points being acquired for the default parameters. Hence, we can convert to the time domain. This will allow us to take the fourier transform to move into the frequency domain. 

**Important**: For the offset, this needs to be calibrated each lab session. Set the peak to $\frac{1}{2}(\text{# pts})$, so 5122 for the default params. This only needs to be done at the beginning of each lab. After initial calibration, everything else is an integer multiple of the fringes anyways. We saw that skipping starts at resolution 8, becomes obvious at resolution 4. The resolution is in wavenumber units. 

#### Flushing of Cell and FTIR

You can stick one end of the tubing into a cup of water to check the flow rate. You can also check the lab manual for the flow rates to calculate how much time is needed to flush the cell. Anyways, I like the  tubing idea. Stic the free end into water to see how many bubbles are coming out. 

>   ![IMG_5485](/Users/linesther/Desktop/IMG_5485.png)
>
>   Tubing in cup of water setup. It was a good sanity check for me to see if gas was even being pumped through. In step 3, I thought I was flushing my cell when in reality nothing was happening. I'll use this in the future to check if something is happening. Thank you Dr. Reinsberg!

Make sure that the cell is locked in. The cell is made so that the ring is concentric around the output of the FTIR. Also make sure that the valve on the cell isn't shut!

>   ![IMG_5488](/Users/linesther/Desktop/IMG_5488.png)
>
>   How the gas cell should be assembled. If put together correctly, it should lock together pretty nicely. One of the tubes will have some sort of gas flowing through, and the other should be left free to equilibriate the pressure. 

## Week 2 [Jan. 21, 2020]

All data is store under the ```data/lab1/week2/``` directory. Conducted a portion of the experiment with Arthur. 

### Lab Procedures Conducted

#### Centering

Use resolution of 32 parameters to set center burst to 1024. Also need to check if baseline is at 0. Spectrums are really noisy. Realized that IR source was off. Done with the cell in place, 

-   Only graph was saved. 
-   Remember, positive sign in offset field means to move burst to left

>   ![Picture19](/Users/linesther/Downloads/Picture19.png)
>
>   An example of the alignment centering.

#### Step 7

>   Copied from the lab manual:
>
>   Let the cell fill with air and take data. Plot both air and CO2 data on the same graph

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

>   Copied from the lab manual: 
>
>   Replace the N2 flowing through the gas cell with CO2. Adjust the CO2 pressure to be no more than a few psi - just enough to make sure there is flow through the cell; let the gases exchange over a period of 1 minute. 

Started CO~2~ purging at 3:16pm. At 60. After one minute, take 32 acquisitions. We proceeded to take several rounds of data, each at different time points. Have to be careful about CO~2~. We only purged for 1 minute, and we fanned the area afterwards.

| Time after 1 min Purge [min] | Timestamp                  | Filename                               | Graph                                    |
| ---------------------------- | -------------------------- | -------------------------------------- | ---------------------------------------- |
| 1+4                          | 2019-09-1712:22:39.932372  | ```step6/co2_cell_4cm-1.txt```         | ![Picture25](/Users/linesther/Downloads/Picture25.png) |
| 3+4                          | 2019-09-17 12:25:28.394080 | ```step6/co2_cell_4cm-1 (3min).txt```  | ![Picture26](/Users/linesther/Downloads/Picture26.png) |
| 6+4                          | 2019-09-17 12:27:38.830395 | ```step6/co2_cell_4cm-1 (6 min).txt``` | ![Picture27](/Users/linesther/Downloads/Picture27.png) |

#### Step 4

Redid signal to noise measurements. Dr. Reinsberg suggested that we try the processing with more finer resolutions. I had let the FTIR purge with N~2~ for a while. I think I messed up the resolution of 8cm^-1^ measurement, I was really impatient and started clicking on random things. Not sure how good the data is. I guess I'll just compare the 4cm^-1^ and 16cm^-1^ resolutions then!

| Resolution [cm^-1^] | Timestamp                  | Filename                         | Graph                                    |
| ------------------- | -------------------------- | -------------------------------- | ---------------------------------------- |
| 4                   | 2019-09-17 13:27:49.674836 | ```week2_step4_snr_res_4.txt```  | ![Picture18](/Users/linesther/Downloads/Picture18.png) |
| 8                   | 2019-09-17 13:40:53.559685 | ```week2_step4_snr_res_8.txt```  | ![Picture17](/Users/linesther/Downloads/Picture17.png) |
| 16                  | 2019-09-17 13:41:55.179366 | ```week2_step4_snr_res_16.txt``` | ![Picture16](/Users/linesther/Downloads/Picture16.png) |

Why do we purge the FTIR in the first place? I guess the N~2~ displaces other gases, decreases the number of unwanted interactions and hence increases the signal to noise ratio. It's also a good normalization baseline to have, since N~2~ is transparent. 

### Notes

####Resolution discussion with Dr. Reinsberg cont.

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

To see if this thing is oversampling, we can do a positive control test where we FT a sinusoid with a known frequency, and determine the axis of wavenumbers from that. However, I'm pretty sure this thing is not oversampling, cause the graph lines up with the numbers given in Dr. Waltham's table at the end of the lab. 

### How does oversampling work? [Feb. 3, 2020]

The signal from the interfering beams of the HeNe are monitored by a detector. A high precision electronic circuit produces a voltage pulse when the signal reference sinusoid crosses the zero level. By using only positive zero crossings, the circuitry can develop one pulse per cecle of the reference interferogram (sampling). When we use all zero crossings for two pulses per cycle of the interferogram, it's oversampling. These pulses trigger an A/D converter which samples the main interferogram. 

## 2. Software Design [Jan. 18-26, 2020]

The lab says: "*The software does not provide even the most basic of data post processing. This is a left asan exercise to the student; consider the tutorial provided here:www.essentialftir.com/tTutorial.html and the references listed below. Investigate the optimal process of a bi-directional spectrum using forward and reverse mirror direction and theapplication of the appropriate phase correction (Mertz method).*"

OH NO. There is so much analysis work. I tried to find existing FTIR softwares, but they do not support the flexibility we need for our experimental procedure. DOES THIS MEAN I HAVE TO WRITE THE CODE FOR EVERYTHING??? [Jan. 18, 2020]. 

[Jan. 20, 2020] yes. Unfortunate. The requirements for this Python code:

-   Need to be able to handle more than 1 acquisitions as smoothly as one acquisition. 
-   code will be documented with pdocs and hosted on my site 

NOTE: The code I used for the analsis of this lab can be found [here](https://estherlin.github.io/enph352/lab1/lab1.html), complete with documentation.

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

>   ![steps4](/Users/linesther/Downloads/mertzcomparison.png)
>
>   The mertz method seems to do a lot of smoothing. 
>
>   -   Q: Not sure if this is what we want???
>   -   A: Dr. Reinsberg says it's fine

#### Ratio and Conversion to Transmission/Absorbance

1.  IR spectroscopy is a single-beam technique. The sample data must be ratioed against a background spectrum to produce a transmittance spectrum. 
2.  Usually the background spectrum is collected using a gas cell filled with N~2~
3.  Calculate the transmittance per wavenumber: $\frac{I}{I_0} \equiv T = 10^{-\epsilon c d}$
4.  Calculate the absorbance per wavenusmber: $A = -\log T = \epsilon c d$

Test results using the same spectra the transmittance and absorbance calculations:

>   ![trans](/Users/linesther/Downloads/trans.png)
>
>   ![abs](/Users/linesther/Downloads/abs.png)
>
>   Sanity check for my transmission and absorbance calculations. Transmission should be 1 (YES) since I'm dividing a spectrum by itself and so absorbance should be 0. Good! My code is all good to go!

## 3. Signal to Noise [S/N] Calculations and Code [Jan. 30, 2020]

According to [researchgate](https://www.researchgate.net/profile/Rafik_Karaman/post/How_can_I_calculate_S_R_ratio_for_IR_spectrum/attachment/59d625d779197b8077984286/AS%3A319381026869248%401453157778077/download/SNR+FTIR.pdf), S/R for FTIR is defined as:

-   Noise N: the standard deviation $\sigma$ of a signals measured values
-   Signal S: the average $\bar{x}$ of those measurements. 

Then, the signal to noise ratio is
$$
S/N = \bar{x}/\sigma
$$
But we can observe that this is just the invers of the relative standard deviation of the signal. So doing our regular mathematical asymptotic analysis and assuming that the noise is normally distributed, selecting a confidence level of 99%, then fall but 1% of of the signal measurements will be between $\pm 2.5 \sigma$. This allows us to approximate $\sigma$ as $\sigma \approx \frac{max - min}{5}$ and S/N will be $S/N \approx \frac{5 \bar{x}}{Max-Min}$. (I'm not sure how this will help me, I need digital methods)

:D This doesn't help with finding signal to noise...

[Feb. 3, 2020]: After much digging on the internet and reading forums, I think I have an understanding of how to find signal to noise. 

We're doing single beam experiments. The steps I should follow to find signal to noise (adapted from researchgate, same source above):

1.  Obtain a background spectrum. 
2.  Independently determine the sample spectrum. 
3.  Determine the transmission spectra. 

If nothing is in the sample cell (we have nothing), then the detector should always record a 100% transmittance. Because of instrumental noise, this is not the case. Hence, deviations from that 100% transmission is considered to be the instruments noise. We can determing the S/N ratio in percentage %
$$
S/N = 100 / (\text{root mean square noise})
$$
YAY. Now I need to write the code for this. Bless numpy for all of it's functions, I guess all I have to do is: ```np.sqrt(np.mean(np.square(transmittance)))``` :D

#### Investigation into whether or not I should average my spectra

So the real motivation here is that the analysis for this lab already is pretty heavy. I'm also applying for jobs right now so I really don't have the bandwidth for this. I've looked a bit into averaging techniques, and none of them seem trivial. I have summarized my findings here. Analysis taken/paraphrased from source above. 

##### Ensemble Averaging (name from quantum mechanics or stat mech?)

Ensemble average is a method for increasing the S/N ratio digitally post data collection. Suppose we take $n$ independent scans. Then, the added signal $S_{pt}$ at each fringe point in the scan is 
$$
S_{pt} = \frac{\sum_i^n S_i}{n} = \frac{S_{sum}}{n}
$$
where $S_{sum}$ is the signal that is the sum of the scans. In other words, we are finding averages of each point. However, if we take enough acquisitions, we will see that the individual signals at each point have noise in them, characterized by a normal distribution. Hence, we get $S_{sum} = n\bar{x}_{pt}$ for each point, and the summed spectrum is $\sigma^2_{sum} = \sum \sigma_i^2 = n\sigma^2$., where $\sigma$ is the variance associated with $S_i$. We can now relate this back to a S/N ratio. The S/N for the averaged spectra will be
$$
(S/N)_{avg} = \frac{(S_{sum}/n)}{(\sigma_{sum}/n)} = \frac{\bar{x}_i}{\sqrt{n}\sigma/n} = \sqrt{n}(S/N)
$$
where (S/N) is the original S/N. So we see that that the emsemble averaged signal to noise is related to the original by an order of $\sqrt{n}$, where n is the number of independent accquisitions. 

While it doesn't take too long for me to do each scan, doing 32 scans and going through this averaging process will only bump my signal to noise ratio by $\sqrt{32} \approx 5.7$ times. FTIR is already know for having good S/N. I don't know if this is improvement is enough for me to put the time into this.

***From the analysis, I conclude that while there is benefit to doing averaging, it is not worth it for the amount of work I am willing to put in.*** 

#### Inherent sources of noise in the instrument

TODO if I have the time. However, I think any instrumental error in the FTIR will be dominated by procedural error. Arthur performs his experiments before me, so unless I purge everything with air for 30+ mins before starting my experiments, I'm going to et some skewed results anyways. 

### 4. Normalization of Transmission and Absorbance Spectra [Jan. 29, 2020]

 During lab, I had a discussion with Dr. Reinsberg about normalizing the transmission and absorbance spectra. This is because it doesn't really make sense for the transmission (or absorbance) to be above 100% or be a negative value. Also, in order to find the fraction of CO2 in air, I need some sort of comparable measure between the absorbance spectra of CO2 and air. The conclusions of our discussion:

1.  It's fine. Although it doesn't really make sense to have some of the transmission values I have, there's no simple way to do the normalization. 
2.  For finding the fraction of CO2 in air, we divide the small peak of co2 in air with the co2 peak in co2, since the co2 peak in co2 has the max amplitude any co2 peak can get. This seems to be a bit of a hacked together solution, but I'm not complaining. 

# Results

I am pretty sure there is no oversampling. This is because if I assume no oversampling, my results line up with Dr. Waltham's table. Also all of the stuff I find online. 

### Step 2

**Explain the general shape of the interferogram. [Feb. 3, 2020]**

As we can see with the centered interferogram collected in the first lab session: 

>   ![Picture1](/Users/linesther/Downloads/Picture1.png)
>
>   Centering of interferogram. Resolution of 64cm^-1^, one scan, default parameters. The y-axis is the ~~voltages~~ some arbituray energy [derivative] unit collected from the detector. The x-axis is the data point, or the fringe count, since the ADC cycles are triggered by the HeNe interferences.

The interferogram consists of a series of oscillations, with the maximum oscillation amplitude somewhere near the center of the interferogram and the oscilations dying out on the edges. 

**Why is the interferogram shifted? [Feb. 3, 2020]**

The centre of the scan, the burst is the zero optical path difference (ZOPD). If it's shifted, that means the ZOPD is not located when the mirror is at position zero. 

We want the offset to be zero in order to capture the full interferogram. So we do an initial step of centering with the default values by changing the Offset parameter in the GUI. 

>   ![Picture1](/Users/linesther/Downloads/Picture1.png)
>
>   Example of centering (```week1_centering.txt```). There were a total of 1024 points, so we wanted the centre burst to be at point 512. This way, we capture both sides of the interferogram to their fullest extent. 

**What happens to interferogram at higher or lower resolutions?** [Feb. 3, 2020]

The following data is copied from lab results from week 1. 

>   | Resolution [cm ^-1^] | Graph                                    |
>   | -------------------- | ---------------------------------------- |
>   | 32                   | ![Picture2](/Users/linesther/Downloads/Picture2.png)```week1_step2_res_32.txt``` |
>   |                      | ![Picture3](/Users/linesther/Downloads/Picture3.png)```week1_step2_res_16.txt``` |
>   | 8                    | ![Picture4](/Users/linesther/Downloads/Picture4.png)```week1_step2_res_8.txt```: Idk why this one wasn't well centered. But we get the gist of things. |
>   | 4                    | ![Picture5](/Users/linesther/Downloads/Picture5.png)```week1_step2_res_4.txt``` |
>
>   As can be seen, as resolution goes down, we get more points. Visually, the interferograms become less noisy and there is less smearing. However, often at a resolution of 4 cm^-1^, we can just get noise because the resolution is too fine. 

**What is the general shape of the spectrum? What is the IR source? Why does this spectrum exhibit lower-intensity troughs?[Feb. 3, 2020]**

Suppose we have beam 1 (beam entering interferometer) and beam 2 (marginal beam) interacting to create the constructive and destructive behaviour at the detector. In a real life non ideal case where the source is finite and produces parallel beams, there will be a ZOPD points where both beams are at constructive intereference conditions and the whole detector will sense a high level of intensity. But when the scanning mirror moves away from the ZOPD position, the next condition of constructive interference will happen sooner for beam 2 than beam 1. As a result, different parts of the detector will see different phases of the interference. In fact, the detector will see some average level of intensity, which will result in smearing of the smearing. This is why some minimas are larger than others. Hence, the varying intensity troughs of the interferogram is caused by both the interference patterns and some contribution of the smearing. 

**What is the useful spectral range of this FTIR system with the current source and optics? [Feb. 3, 2020]**

Conclusions from reading the MIR8000 manual. From the discussion above, an optimal functioning of the FTIR requires certain restriction on the sizes of the detector and source, and other optical components. I found this equation in the manual :
$$
\alpha_{\text{max}} = \sqrt{\frac{\Delta \sigma}{\sigma_{\text{max}}}}
$$
where $\alpha$ is the half angle in radian, $\sigma_{\text{max}}$ is the higher wave number that is observed, and spectral resolution $\Delta \sigma$.

According to the manual, at lower resolutions (64), we can potentially pump into the system a lot more radiation without impacting the resolution performance. But this would limit our choices for a dtector diameter. So, we generally choose a resolution of 4cm^-1^ that has a reasonably high resolution, but not too high. See step 3 for useful spectral range. 

**What are the relationships between wavenumber, wavelength and energy? What are the relationships between the interferometer resolution in the different units? [Feb. 3, 2020]**

-   Wavenumber $\mu$ [$\frac{1}{m}$]: $\mu = \frac{1}{\lambda}$
-   Wavelength $\lambda$ [$m$]: $\lambda = \frac{1}{\mu}$
-   Energy E [$J$]: $E = \frac{hc}{\lambda} = hc\mu$

where $h$ is the Planck constant and $c$ is the speed of light in vacuum. Please refer to the section on what resolution means to find the relationship between interferometer resolution. 

### Step 3 [Feb. 4, 2020]

Looking at the graphs, a good spectral range would be **700 - 6000 cm^-1^**. My peaks look good, I see the co2 in the 2350 ish range, and water as a smear in the 1000 - 2000 range and the 3000+ range. 

### Step 4 [Feb. 4, 2020]

Signal to noise (S/N) ratio calculations were performed with resolutions of 4cm^-1^ and 16 cm^-1^, with the mathematics derived in the analysis section. I chose not to average, instead just performing these calculations on single acquisitions. My justification is also included in the analysis section. 

>   | Resolution [cm^-1^] | S/N ratio (%) | Transmittance Graph                      |
>   | ------------------- | ------------- | ---------------------------------------- |
>   | 4                   | 101.811       | ![snr4](/Users/linesther/Downloads/snr4.png) |
>   | 16                  | 104.927       | ![snr16](/Users/linesther/Downloads/snr16.png) |
>
>   Signal to noise ratio table, with transmittance graphs. There doesn't seem to be too much difference between signal to noise of these two. 

### Step 5 [Feb. 4, 2020]

Using data gathered in week 2:

>   ![s5-1](/Users/linesther/Downloads/s5-1.png)
>
>   Interferograms of the n2 and and normalization spectra. 
>
>   ![s5-2](/Users/linesther/Downloads/s5-2.png)
>
>   Single beam spectra of n2 and normalized. (I normalized them by dividing by their largest value just for plotting purposes)
>
>   ![s5-3](/Users/linesther/Downloads/s5-3.png)
>
>   Transmission spectra of n2 using normalization spectra. 
>
>   ![s5-4](/Users/linesther/Downloads/s5-4.png)
>
>   Absorbance spectra of n2 using normalization spectra.

For the transmission diagram, disregarding the noises at the higher and lower wavenumbers, we see that n2 is transparent to co2. There is even a little dip around the 2300 cm^-1^ range, showing that n2 is transparent around that region. There are no particular peaks in the water range, shich is also good. 

While I didn't fit to gaussians and lorentzians (talked to prof, this seems to be too strenuous of a problem), I can say that I think the line shapes are more lorentzians than gaussians. This is a guess based on both

-   visual: the peaks are sharper, but they don't really go to zero
-   physically: lorentzians are caused by disturbances to the absorption process during molecular collisions

Actually, scratch all of this, I don't know and it's really hard to say. 

### Step 6 [Feb. 4, 2020]

Using data gathered in week 2:

>   ![s6-1](/Users/linesther/Downloads/s6-1.png)
>
>   Interferograms of theco2 and and normalization spectra. 
>
>   ![s6-2](/Users/linesther/Downloads/s6-2.png)
>
>   Single beam spectra of co2 and normalized. (I normalized them by dividing by their largest value just for plotting purposes)
>
>   ![s6-3](/Users/linesther/Downloads/s6-3.png)
>
>   Transmission spectra of co2 using normalization spectra. 
>
>   ![s6-4](/Users/linesther/Downloads/s6-4.png)
>
>   Absorbance spectra of co2 using normalization spectra.

We see a significantly strong peak of co2 around the 2350 range as expected. We are able to identify the absorption peak of CO~2~ at 2352 $\pm$ 22 cm^-1^, which is quite similar to the  2360 cm^-1^ peak location for CO~2~ that is in Dr. Waltham's table. 

### Step 7 [Feb. 4, 2020]

Using data gathered in week 2:

>   ![s6-1](/Users/linesther/Downloads/s7-1.png)
>
>   Interferograms of the air and and normalization spectra. 
>
>   ![s6-2](/Users/linesther/Downloads/s7-2.png)
>
>   Single beam spectra of air and normalized. (I normalized them by dividing by their largest value just for plotting purposes)
>
>   ![s6-3](/Users/linesther/Downloads/s7-3.png)
>
>   Transmission spectra of air using normalization spectra. 
>
>   ![s6-4](/Users/linesther/Downloads/s7-4.png)
>
>   Absorbance spectra of air using normalization spectra.

We see a small peak of co2 around the 2300 range as expected. We see a weak peak around 2350 cm-1, which is where CO2 absorbs. Hence, the FTIR has identified the CO2 in our gas cell of air. We also see a large water signal from 100-2000 and 3000+, as we expect from the theory section of this lab. 

### Step 8 [Feb. 4, 2020]

I talked to Dr. Reinsberg, and apparently too find the fraction of CO2 in air, we divide the small peak of co2 in air with the co2 peak in co2, since the co2 peak in co2 has the max amplitude any co2 peak can get. With some point hovering in matplotlib, I find the fraction of CO2 in air to be **8% $\pm$ 1%.** 

Note that this value is several orders of magnitude larger than the CO2 percetage measured in Earth's atmosphere, which is 0.04%. I have several speculations as to why my measurement is so large:

1.  The cell is not completely purged of CO2. Arthur does his experiments before me. Although I can spend 30+ mins before all of my experiment sessions purging the gas cell, I didn't have the time for that. Due to the geometry of the cell, it could be that there is some residual CO2 trapped in the cell that will up the percentage. 
2.  The humidity in the cell is high. Maybe some CO2 is trapped in the cell due to the humidity and has a harder time being purged. 
3.  The lab air I'm pumping into the cell has a high percentage of CO2. I'm pumping air from my lab bench into the cell to purge it of CO2. But some of the CO2 could have been cycled back into the cell, since I'm pumping from within a radius of 1 m. 

Overall though, I'm quite thankful that the fraction I found was 8%. If it's anything lower, I'm pretty sure I wouldn't have been able to see it. It would have been swallowed up in the noise and I would have had to do some crazy data analysis acrobatics to tease it out. 

# Conclusions [Feb. 4, 2020]

1.  FTIR is a useful tool for the identification of molecules in gas samples. However, I can't say anything about using it for quantification. We can only use it to determine the relative ratios of gases.
2.  Measurements of gas cells are limited by the thoroughness of flushing. We also see that our spectra was a lot of influence from humidity (water) in the absorbance spectra. It would be nice to try this experiment again in a drier room.
3.  One can infer the type of molecular movements and interactions from the lineshapes of the spectrums. The spectral shape is a Lorentzian (Cauchy) lineshape is caused by disturbances to the absorption process during molecular collisions. The spectral shape is a gaussian distribution is caused by the random rapid translational motions of gas molecules. 

Besides these points, there is also critical value in the post-processing of data. Methods like the Mertz correction and ensemble average can increase the signal to noise ratio. 

Overall, I learned quite a bit from this lab!

## Abstract

In the mid-infrared region of the electromagnetic spectrum, molecules absorb light through the interaction between the photons and the vibrating electric dipoles of the molecule. Fourier Transform Infrared Spectroscopy (FTIR) is a tool that can be used to measure the absorption and transmission of the sample. With the transmission and absorbance spectra, we can identify the molecules in the sample. The objective of this experiment is to measure absorption spectra of several gases, N~2~ as our control sample, and CO~2~, and air for the measurement of CO~2~ fraction in air. We acquired interferograms of gas cells flushed with the gases above at 4 cm^-1^ resolution.. The Mertz correction method is applied to the Fourier Transform analysis to increase clarity of the signal. For results, we are able to identify the absorption peak of CO~2~ to be at 2352 $\pm$ 22 cm^-1^, which is similar to the value 2362 cm^-1^ in the HITRAN database. We were also able to find the fraction of CO~2~ in air for our setup to be 8 $\pm$ 1%. Uncertainties in our measurements are primarily due to the variable flushing of the gas cells. However, we see that FTIR is a promising and useful tool for the identification of molecules in gas samples. 