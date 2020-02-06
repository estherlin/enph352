POWERS2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
MAX_WAVENUMBER = 15802

class Interferogram:
    """Interferogram class for all data processing, plotting, and saving. 


    Attributes:
        dir: directory holding data file
        filename: filename holding data
        datestamp: datestamp recording when data was taken
        res: resolution of scan
        vel: mirror velocity of scan
        LP: low pass frequency of scan
        HP: high pass frequency of scan
        gain: gain of scan
        raw_data: parsed interferogram acquisitions of scan
        num_acq: number of acquisitions of scan
        num_pts: number of points of each acquistion in scan
        wavenumbers: wavenumber axis for each acquisiton
        spectra: fourier transformed spectra with mertz correction
    """
    
    def __init__(self, DIR, filename, sampling=1):
        self.dir = DIR
        self.filename = filename
        
        with open(DIR+filename) as f:
            data = f.read().splitlines() 
        
        # Read in params at the top of the file
        self.datestamp = data[0].replace("#","").strip()
        result = re.search(r'\d+', data[1])
        self.res = int(result.group())
        result = re.search(r'\d+', data[2])
        self.vel = int(result.group())
        result = re.search(r'\d+', data[3])
        self.LP = int(result.group())
        result = re.search(r'\d+', data[4])
        self.HP = int(result.group())
        result = re.search(r'\d+', data[5])
        self.gain = int(result.group())
        
        # Read in the raw spectrum data
        raw = list(filter(None, data[6:]))
        scan_idx = [i for i in range(0, len(raw)) if "#" in raw[i]] + [len(raw)]
        self.raw_data = np.array(
            [np.array(raw[scan_idx[i]+1:scan_idx[i+1]], dtype=np.float) for i in range(0, len(scan_idx)-1)]
        )
        self.num_acq = len(self.raw_data)
        
        # Find the wavenumbers
        self.num_pts = [len(self.raw_data[i]) for i in range(0, self.num_acq)]
        self.wavenumbers = np.array(
            [sampling*np.linspace(0, MAX_WAVENUMBER, num=int(self.num_pts[i])/2) for i in range(0, self.num_acq)]
        )

        # Find the spectra
        mean = np.mean(np.array([x for x in raw if "#" not in x], dtype=np.float))
        self.spectra = self.fft(mean)

    
    def fft(self, mean):
        """
        Calculates the spectra of the interferogram
        
        Args:
            interferogram2: The test sample spectrum, a np.array

        Returns:
            A numpy array of transmittances. 
        
        Raises:
            AssertionError: An error occurred if resolutions are different
        """
        new_data = []

        for line in self.raw_data:
            
            # Normalize data
            new_line = Interferogram.normalize_raw_data(line, mean)
            
            # Zero fill the data
            new_line = Interferogram.zero_fill(new_line)
            
            # Find the phase corrections
            phase, re_phase, im_phase = self.mertz(new_line)
            
            # fft the interferogram
            inter, re_inter, im_inter = Interferogram.fft_interferogram(line)
            
            # Record the spectra multiplied by correction
            new_data.append(np.absolute(np.multiply(inter, phase)))
        
        return np.array(new_data)
        

    def mertz(self, data):
        """
        Returns the phase correction data
        The real and imaginary data arrays are multiplied by the power spectrum

        Args: 
            data: interferogram to be filled
        Returns: 
            fft spectrum: A numpy array of data multiplied by the power spectrum 
            re spectrum: A real numpy array of data multiplied by the power spectrum 
            im spectrum: A imaginary numpy array of data multiplied by the power spectrum 
        """
        # find burtst location
        burst = np.argmax(data)
        
        # Add the apodization triangular phase correction
        copied_burst = np.zeros(len(data))
        copied_burst[burst-128:burst+128] = data[burst-128:burst+128]
        copied_burst = np.multiply(copied_burst, Interferogram.triangular_signal(burst, len(copied_burst)))
        
        # Slicing to rotate about ZPD
        copied_burst = np.concatenate((copied_burst[burst:], copied_burst[:burst]))
        
        # data is FFT'd, producing real and imaginary data arrays.
        ffted = np.fft.fft(copied_burst)
        im_data = ffted.imag
        re_data = ffted.real
        
        # Find power spectrum
        power = np.absolute(ffted)
        
        # The real and imaginary data arrays are multiplied by the power spectrum 
        return np.multiply(power, ffted), np.multiply(re_data, power), np.multiply(im_data, power)


    @staticmethod
    def fft_interferogram(data):
        """
        Do the fft for the interferogram, including the apodization, etc. 

        Args: 
            data: interferogram to be filled
        Returns: 
            fft spectrum: A numpy array of ffted data
            re spectrum: A real numpy array of ffted data
            im spectrum: A imaginary numpy array of ffted data
        """
        
        # find burst location
        burst = np.argmax(data)
        
        # Apodize the whole interferogram with triangular function
        data = np.multiply(data, Interferogram.triangular_signal(burst, len(data)))
        
        # zero fill
        data = Interferogram.zero_fill(data)
        
        # Slicing to rotate about ZPD
        data = np.concatenate((data[burst:], data[:burst]))
        
        # data is FFT'd, producing real and imaginary data arrays.
        ffted = np.fft.fft(data)
        return ffted, ffted.real, ffted.imag
    
    
    @staticmethod
    def zero_fill(data):
        """
        FFT requires number of points in the interferogram be a power of 2.
        If it is not, then the size of the array is increased to the next higher power of 2 
        and the added points are set to 0. 
        
        Args: 
            data: interferogram to be filled
        Returns: 
            A numpy array of filled interferogram
        """
        for i in range(10, len(POWERS2)):
            if POWERS2[i] >= len(data):
                break
        return np.concatenate((data, np.zeros(POWERS2[i]-len(data))))
    
    
    @staticmethod
    def normalize_raw_data(data, mean):
        """The mean of the data is subtracted from the data, brings baseline of data to 0"""
        return data - mean
    
    @staticmethod
    def apodize(burst, data):
        return np.multiply(data, Interferogram.triangular_signal(burst, len(data)))
    
    @staticmethod
    def triangular_signal(center, total_len):
        window = signal.triang(2*center-1)
        try:
            return np.concatenate((window, np.zeros(total_len-len(window))))
        except:
            return window[:total_len]
    
    @staticmethod
    def calc_transmittance(interferogram1, interferogram2):
        """
        Calculates the transmittance per wavenumber
        
        Args:
            interferogram1: The background spectrum, a np.array
            interferogram2: The test sample spectrum, a np.array

        Returns:
            A numpy array of transmittances. 
        
        Raises:
            AssertionError: An error occurred if resolutions are different
        """
        assert (len(interferogram1) == len(interferogram2)), 'Background spectrum has {} pts, sample spectrum has {} pts'.format(len(interferogram1), len(interferogram2))
        return np.divide(interferogram2, interferogram1)
    
        
    @staticmethod
    def calc_absorbance(transmittance):
        """
        Calculates the absorbance per wavenumber
        
        Args:
            transmittance: array of transmittances

        Returns:
            A numpy array of absorbances. 
        """
        return -np.log(transmittance)
    
    @staticmethod
    def calc_snr(interferogram1, interferogram2):
        """
        Calculates the signal to noise ratio
        
        Args:
            interferogram1: The background spectrum, a np.array
            interferogram2: The test sample spectrum, a np.array

        Returns:
            A signal to noise value
        """
        transmittance = Interferogram.calc_transmittance(interferogram1, interferogram2)
        noise_rms = np.sqrt(np.mean(np.square(transmittance)))
        return 100 / noise_rms       