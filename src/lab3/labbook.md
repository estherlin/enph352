# Electromagnetic Skin Depth of Metals Labbook

## Table of Contents

[TOC]

## Data Collection

### Week 1 [Mar. 10, 2020]

Data is saved in the folder ```data/lab3/week3/```.

**Step 1**

Opening up the Skin Depth LabView program, we follow the instructions on the screen to set the parameters for our equipment.

**Step 2**

We measure the inner and outer radii of the pipes. Oh nooo, there are 3 different pipes and its hard to tell which is aluminum and which is steel. Measurements made:

| Pipe     | $2R_1$ (inner) $\pm 0.01$ [mm] | $2R_2$ (outer) $\pm 0.20$ [mm] | Thickness $R_2 - R_1$ $\pm 0.01$ [mm] |
| -------- | ------------------------------ | ------------------------------ | ------------------------------------- |
| Aluminum | 22.25                          | 25.40                          | 1.60                                  |
| Copper   | 25.44                          | 28.62                          | 1.55                                  |

Measuring the outside diameter directly is the least accurate way to measure. It would be better to find $R_2$ from using the inner diameter and the thickness. However, in our calculations, we never need the radii separately… LOL I'm dumb. 

The high frequency approximation breaks down when $k_0(R_2 - R_1)\lessapprox 1$. Plugging in $k_0 = \sqrt{\frac{\omega \sigma \mu}{2}}$, we find that the frequency approximation breaks down for angular frequencies
$$
\omega \lessapprox \frac{2}{\sigma \mu}\bigg(\frac{1}{R_2-R_1}\bigg)^2
$$
Using values of conductivity from <<https://www.engineeringtoolbox.com/resistivity-conductivity-d_418.html>>, and using the approximation $\mu \approx \mu_0 = 4π \times10^{−7} (H/m) = 4π \times10^{−5} (H/cm)$, I find:

| Pipe     | Electrical Conductivity [$1/\Omega\cdot cm$] | Cutoff Frequency $\omega$ [rad/s] | Cutoff Frequency $f$ [Hz] |
| -------- | ---------------------------------------- | --------------------------------- | ------------------------- |
| Aluminum | 3.77 x 10^5^                             | 1.649 x 10^14^                    | 2.625 x 10^13^            |
| Copper   | 5.95 x 10^5^                             | 1.113 x 10^14^                    | 1.772 x 10^13^            |

These frequencies are crazy high. So unless the frequency generator can go up to these speeds, we're definitely going to have attenuation.

TODO: Calculate uncertainty in frequencies

**Step 3**

| Material | Filename                                 | Results |
| -------- | ---------------------------------------- | ------- |
| Air      | ```air-20200310.DAT```                   |         |
| Aluminum | ```al-20200310.DAT```, ```al-20200310-amp.DAT``` |         |
| Copper   | ```cu-20200310.DAT```, ```cu-20200310-amp.DAT``` |         |

For copper, in frequencies above 60kHz, everything degenerated into noise. Set Vpp to 8 now. 50-80kHz. I'll also just redo the aluminum. 