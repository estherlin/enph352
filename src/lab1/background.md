# Background for Fourier Transform Infrared Spectroscopy of Air and CO~2~ Lab

[TOC]

## Theory

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

Examples:

1.  CH~4~ has $3(5)-6=9$ vibrational modes
2.  CO~2~ has $3(3)-5 = 4$ vibrational modes
3.  SO~2~ has $3(3)-6=5$ vibrational modes

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
-   Has a high signal to noise, 

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

## Questions

1.  Wave numbers [k or $\nu$] scale linearly with energy? Oh that makes so much sense. 

2.  What is a vibrational mode?

3.  What is a transition dipole moment?

    Answer: the [electric dipole moment](https://en.wikipedia.org/wiki/Electric_dipole_moment) associated with the transition between the two states. 

    -   a complex vector quantity that includes the phase factors associated with the two states
    -   transitions to different orbitals
    -   useful for determining if transitions are allowed under the electric dipole interaction

4.  Isn't molar absorption coefficient dependent on wavenumber?