# -*- coding: utf-8 -*-
"""Lab 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bAtQCW_p3FReNuNWo6oF6uqSMjbOOh5_

# Imports
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from scipy.io.wavfile import write

"""# Problem **1.1**"""

class ComplexExp(object):
  """
  Creates a discrete complex exponential of discrete frequency k and Duration N.
  Arguments:
  k: discrete frequency
  N: duration of the complex exponential
  """
  def __init__(self, k, N):
    self.k = k
    self.N = N
    # Create time indices [0,..,N-1]
    self.n = np.arange(N)
    # Vector containing elements of the complex exponential
    self.exp_kN = (1/(np.sqrt(N))) * np.exp(2j*cmath.pi*self.k*self.n/self.N)
    # Real and imaginary parts
    self.exp_kN_real = self.exp_kN.real
    self.exp_kN_imag = self.exp_kN.imag

exp = ComplexExp(2,10)
print(exp.exp_kN)

# Importing the class we just created (If it was saved in a different file)
#from cpx_exp import ComplexExp

def q_11(N, k_list):
  for k in k_list:
    # Creates complex exponential object with frequency k and duration N
    exp_k = ComplexExp(k, N)
    # Real and imaginary parts
    cpx_cos = exp_k.exp_kN_real
    cpx_sin = exp_k.exp_kN_imag
    # Plots real and imaginary parts
    cpx_plt = plt.figure()
    plt.stem(exp_k.n, cpx_cos, 'tab:blue', markerfmt='bo', label= 'Real part')
    plt.stem(exp_k.n, cpx_sin, 'tab:green', markerfmt='go', label= 'Imaginary part')
    plt.title('Complex exponential: k = ' + str(k) + ', N = ' + str(N), fontsize=10)
    plt.xlabel('n', fontsize=9)
    plt.ylabel('x[n]', fontsize=9)
    plt.legend()
    #fig_path_name = 'cpxexp_k' + str(k) + '.png'
    #plt.savefig(fig_path_name, dpi=150)
    plt.show()

if __name__ == '__main__':
  list_of_ks = [0, 2, 9, 16]
  duration_of_signal = 32
  q_11(duration_of_signal, list_of_ks)

"""# Problem **1.2**"""

if __name__ == '__main__':
  list_of_ks = [0, 2, 9, 16]
  list_of_positive_ls = [32, 34, 41, 48]
  list_of_negative_ls = [-32, -30, -23, -16]
  duration_of_signal = 32
  q_11(duration_of_signal, list_of_ks)
  q_11(duration_of_signal, list_of_positive_ls)
  q_11(duration_of_signal, list_of_negative_ls)

"""# Problem **1.3**"""

if __name__ == '__main__':
  list_of_positive_ks = [2, 3, 9, 16]
  list_of_negative_ks = [-2, -3, -9, -16]
  duration_of_signal = 32
  q_11(duration_of_signal, list_of_positive_ks)
  q_11(duration_of_signal, list_of_negative_ks)

"""# Problem **1.4**"""

if __name__ == '__main__':
  list_of_ks_upward = [1, 3, 9, 16]
  list_of_ks_downward = [31, 29, 23, 16]
  duration_of_signal = 32
  q_11(duration_of_signal, list_of_ks_upward)
  q_11(duration_of_signal, list_of_ks_downward)

"""# Problem **1.5**"""

def q_15(N):
  k_list = np.arange(N)
  l_list = np.arange(N)
  
  # define complex exponential
  cpx_exps = np.zeros((N,N), dtype=np.complex) 
  for k in k_list: 
    cpx_exp = ComplexExp(k, N)
    cpx_exps[:, k] = cpx_exp.exp_kN 

  # calculate conjugate 
  cpx_conjugate = np.conjugate(cpx_exps)

  # Multiply the two arrays (complex exponent and its conjugate)
  result = np.round(np.matmul(cpx_conjugate, cpx_exps).real) 
  print ("\n matrix of inner products: Mp = \n", result)

  return result

if __name__ == '__main__':
  q_15(16)

"""# Problem **3.1**"""

def cosgen(f, T, f_s): 
  N = math.floor(T*(f_s))
  k = N * f / f_s
  t = np.linspace(0, (N-1) / f_s, N) 
  # Complex Exponential 
  cpx_exp = ComplexExp(k, N) 
  x = np.sqrt(N) * cpx_exp.exp_kN 

  return t, x, N

def q_31(f, T, f_s): 
  cpxexp, num_samples = cosgen(f, T, f_s)
  cpxcos = cpxexp.real

"""# Problem **3.2**"""

def q_32(f_0, T, f_s):
  cpx_exp, num_samples = cosgen(f_0, T, f_s) 
  # A note (cos real part)
  Anote = cpx_exp.real
  #Play note 
  write("Anote.wav", f_s, Anote.astype(np.float32)) 

if __name__ == '__main__':
  note = 440
  T = 2 
  f_s = 44100
  q_32(note, T, f_s)

"""# Problem **3.3**"""

def q_33(key_num, T, f_s): 
  f = 440* (2**((key_num - 49)/12))
  cpxexp, num_samples = cosgen(f, T, f_s)
  newnote = cpxexp.real
  write("newnote.wav", f_s, newnote.astype(np.float32))

if __name__ == '__main__':
  note = 40
  T = 2 
  f_s = 44100
  q_33(note, T, f_s)

"""# Problem **3.4**"""

def q_34(notes, rhythms, f_s): 
  assert len(notes) == len(rhythms), "List of musical notes and musical times should have same length"
  song = []
  for note, note_time in zip(notes, rhythms):
    f_i = 2**((note - 49) / 12)*440
    x, N = cosgen(f_i, note_time, f_s)
    song = np.append(song, x.real)
    song = np.append(song, np.zeros(10))

  # Writing song
  write("q34_song.wav", f_s, song.astype(np.float32))

#notes 
D3 = 30 
E3 = 32 
F3 = 33 
G3 = 35 
A3 = 37 
B3 = 39 
C4 = 40 
D4 = 42 
E4 = 44
F4 = 45 
G4 = 47 
A4 = 49
B4 = 51
C5 = 52 

#Song (Heart and Soul) 
song_only_notes = [C4, C4, E4, E4, A3, A3, C4, C4, F3, F3, A3, A3, G3, G3, B3, 
                   B3, C4, C4, E4, E4, A3, A3, C4, C4, F3, F3, A3, A3, G3, G3, 
                   B3, B3, C4, C4, C4, C4, B3, A3, B3, C4, D4, E4, E4, E4, E4, 
                   D4, C4, D4, E4, F4, G4, C4, A4, G4, F4, E4, D4, C4, B3, A3, 
                   G3, F3, E3, D3, E3, F3, G3, A3, B3, C4, C4, E4, E4, A3, A3, 
                   C4, C4, F3, F3, A3, A3, G3, G3, B3, B3, C4, C4, C4, C4, B3, 
                   A3, B3, C4, D4, E4, E4, E4, E4, D4, C4, D4, E4, F4, G4, C4, 
                   A4, G4, F4, E4, D4, C4, C5, B4, A4, B4, A4, G4, F4, G4, F4, 
                   E4, D4, G4, C4] 
#half note base
rhythm = 1
#eighth note
e = rhythm * 0.5 
#quarter note
q = rhythm * 1.0 
#quarter note + double triplet 
qdt = rhythm * (1 + (2/3))
#half note 
h = rhythm * 2.0 
#half note + double triplet 
hdt = rhythm * (2 + (2/3)) 
#triplet
t = rhythm * (1/3) 
#double triplet
dt = rhythm * (2/3) 

song_rhythm = [dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, 
               dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, 
               q, q, hdt, t, dt, t, dt, t, q, q, q, hdt, t, dt, t, dt, t, q, h, 
               hdt, t, dt, t, q, q, qdt, t, qdt, t, dt, t, dt, t, dt, t, dt, t,
               dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, q, q, hdt, 
               t, dt, t, dt, t, q, q, q, 
               hdt, t, dt, t, dt, t, q, h, hdt, t, dt, t, q, q, q, dt, t, dt, 
               t, dt, t, dt, t, dt, t, q, q, h] 

q_34(song_only_notes, song_rhythm, f_s)



"""**bold text**# new

"""

def cosgen(f, T, f_s): 
  N = math.floor(T*(f_s))
  k = N * f / f_s
  t = np.linspace(0, (N-1) / f_s, N) 
  # Complex Exponential 
  cpx_exp = ComplexExp(k, N) 
  x = np.sqrt(N) * cpx_exp.exp_kN 

  return t, x, N

def generateA(f_0, T, f_s):
  cpx_exp, num_samples = cosgen(f_0, T, f_s) 
  # A note (cos real part)
  Anote = cpx_exp.real

import numpy as np
import cmath

class dft():
    """
    dft Discrete Fourier transform.
    solve1,solve2,solve3 are the discrete Fourier transform (DFT) of
    vector x. There are three different ways of obtaining the DFT.
    The most efficient way of obtaining the dft is method 3, but 1
    and 2 are included for educational purposes.
    X is a vector that contains the DFT coefficients and f is a
    vector that contains the real frequencies determined by sampling
    frequency fs. f are the frequencies starting at f=0 and X are the
    corresponding frequency components. f_c is a vector containing the
    frequencies such that f_c=0 is at the center, and X_c contains the
    frequency components corresponding to f_c. In essence, f_c and X_c
    are the centered counterparts of f and X. Frequency 0 is always
    present.
    If a parameter K is given, solve1,solve2, solve3 computes the DFT with
    only K coefficients. Recall that this periodizes signal x with period K.
    If the length of the signal x is less than K, then the signal will be
    padded with zeros. If the length of the signal x is greater than K,
    then there will be aliasing occured from periodizing singal x with
    period K. f_c and X_c are the centered counterparts of f and X
    """
    def __init__(self, x, fs, K=None):
        """
        :param x: Input vector x contains the discrete signal
        :param fs: Input integer fs contains the sample frequency
        :param K: Input positive integer that determines the number of coeffients
        used to calculate the DFT. If K is not provided, K=length(x).
        """
    # START: SANITY CHECK OF INPUTS.
        if (type(fs) != int) or (fs<=0):
            raise NameError('The frequency fs should be a positive integer.')
        if not isinstance(x, np. ndarray):
            raise NameError('The input signal x must be a numpy array.')
        if isinstance(x, np. ndarray):
            if x.ndim!=1:
                raise NameError('The input signal x must be a numpy vector array.')
        self.x=x
        self.fs=fs
        self.N=len(x)
        if K == None:
            K = len(self.x)
        # START: SANITY CHECK OF INPUTS.
        if (type(K) != int) or (K <= 0) or (K < 0):
            raise NameError('K should be a positive integer.')
        self.K=K
        self.f=np.arange(self.K)*self.fs/self.K # (0:K-1) just creates a vector from 0 to K by steps of 1.
        self.f_c=np.arange(-np.ceil(K/2)+1,np.floor(self.K/2)+1)*self.fs/self.K
        # This accounts for the frequencies
        # centered at zero. I want to be guaranteed that k=0 is always a
        # possible k. Then, I also have to account for both even and odd choices
        # of K, and that's why the floor() function appears to round down the
        # numbers.
    def changeK(self,K):
        """
        :param K: Input positive integer that determines the number of coeffients
        used to calculate the DFT. This function changes the attribute K of the class.
        """
        if (type(K) != int) or (K <= 0) or (K <  0):
            raise NameError('K should be a positive integer.')
        old_K=self.K
        self.K=K
        self.f=np.arange(self.K)*self.fs/self.K # (0:K-1) just creates a vector from 0 to K by steps of 1.
        self.f_c=np.arange(-np.ceil(K/2)+1,np.floor(self.K/2)+1)*self.fs/self.K
        # This accounts for the frequencies
        # centered at zero. I want to be guaranteed that k=0 is always a
        # possible k. Then, I also have to account for both even and odd choices
        # of K, and that's why the floor() function appears to round down the
        # numbers.
        print('The value of K was succefully change from %d to %d'%(old_K,self.K))
        pass

    def solve1(self):
        """
        \\\\\ METHOD 1: For loops
        By definition of DFT (eq. 1, lab 2) we have that
        X(k) = 1/sqrt(N) * sum_{n=0 to N-1} x(n) exp(-j 2 pi k n / N)
        where n is the discrete time index, k is the discrete time frequency and N is
        the length of the time signal x. Observe that this gives the DFT coefficient
        for a single coefficient k. We are trying to look for all coefficients
        k=0,1,...,K.
        This means that, for each value of k=0,1,...,K we will need to compute N
        multiplications x(n)*exp(-j 2 pi k n / N), for n=0,1,...,N-1, and sum the
        result.
        First thing we need is to create the variable X that we will output. This will
        be a vector of length K.
        """

        X=np.zeros(self.K,dtype=np.complex_)
        for k in range (self.K) :# For each time index k=0,1,...,K;
            for n in range (self.N):  # For each frequency n=0,1,...,N-1:
                X[k]=X[k]+1/np.sqrt(self.N)*self.x[n]*np.exp(-1j*2*cmath.pi*k*n/self.K)

        # Obs: in the case we have K different from N, then the
   		# signal will be periodized with period K. That is why the
        # exponential is divided by K instead of N.
        X_c=np.roll(X,np.int(np.ceil(self.K/2)-1)) # Circularly shift X to get it centered in f_c==0
        return [self.f,X,self.f_c,X_c]

    def solve2(self):
        """
        \\\\ METHOD 2: Matrix form
        Using for loops in python is rather expensive. Numpy is already optimized to
        work with vectors and matrices, so it's a good idea to take advantage of this,
        together with the built-in elementwise operators.
        Observe that we want a vector X=[X(0) X(1) ... X(K-1)]'=[X(k), k=0,...,K-1]'
        and that each element of the vector is computed as before:
        X(k) = 1/sqrt(N) * sum_{n=0 to N-1} x(n) exp(-j 2 pi k n / N)
        But, as mentioned in (eq. 2, lab. 2) this is nothing more than the inner
        product of x=[x(0) ... x(N-1)]'=[x(n), n=0,...,N-1]' with the complex
        exponential of frequency K and length N ekN=[ekN(0) ... ekN(N-1)]'=[ekN(n),
        n=0,...,N-1]', so that X(0)=<x,e0N>=e0N'*x, X(1)=<x,e1N>=e1N*x', ...,
        X(K-1)=<x,e(K-1)N>=e(K-1)N'*x. So we see that we have a bunch of vectors
        {ekN, k=0,...,K-1} that always multiply the same vector x. We can achieve
        this by creating a matrix where each of the ekN is a row, and then get
        the full vector X by multiplying this matrix by x. We will denote the
        matrix as WKN for future reference:
        WKN=[e0N'; e1N'; ... ; e(K-1)N'];
        Finally, observe that as we move from row to row, k grows from 0 to K-1.
        And as we move from column to column, it is n that grows from 0 to N-1.
        Also, observe that ekN is a function of (k,n) given by exp(-j 2 pi k n /K).
        So if we create a matrices of indices (k,n) then we can directly apply
        the exponential by making use of the elementwise nature of this operation
        in Numpy.
        """
        matrix_k=np.transpose(np.tile(np.arange(self.K),(self.N,1)))
        matrix_n=np.tile(np.transpose(np.arange(self.N)),(self.K,1))
        indices=np.multiply(matrix_k,matrix_n)
        WKN=1/np.sqrt(self.N)*np.exp(-1j*2*np.pi*indices/self.K)
        X=WKN@self.x

        X_c=np.roll(X,np.int(np.ceil(self.K/2)-1)) # Circularly shift X to get it centered in f_c==0
        return [self.f,X,self.f_c,X_c]

    def solve3(self):
        """
        \\\\\ METHOD 3: Built-in fft() function
        Even though the matrix form is fast, it is still not fast enough for large
        signals x. For that, it is better to use the built in fft() function which is
        the optimal way to compute a dft. Besides, it is really easy to code.
        """
        X=np.fft.fft(self.x,self.K)/np.sqrt(self.N);
        # \\\\\ CENTER FFT.
        X_c=np.roll(X,np.int(np.ceil(self.K/2-1))) # Circularly shift X to get it centered in f_c==0
        return [self.f,X,self.f_c,X_c]

def q_32(list_notes, list_times, fs):
    """
    Question 3.2: DFT of an song
    Arguments:
        list_notes: list of notes of the song (list)
        list_times: list of the times of each note (list)
        fs: sampling frequency (int)
    """
    assert len(list_notes) == len(list_times), "List of musical notes and musical times should have same length"
    song = []
    for note, note_time in zip(list_notes, list_times):
        fi = 2**((note - 49) / 12)*440
        _, x, N = cexpt(fi, note_time, fs)
        song = np.append(song, x.real)
        song = np.append(song, np.zeros(10))

    Anote_dft = dft(song, fs)
    [freqs, X, f_c, X_c] = Anote_dft.solve3()

    plt.figure()
    plt.plot(f_c, abs(X_c))
    plt.xlim((-2000,2000))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('DFT')
    plt.title('DFT of Heart and Soul')
    # plt.savefig('song_dft.png')
    plt.show()
    return song,f_c, X_c

def energy(f, X,  interval):
    """
    energy computes the energy of a signal in a frequency interval
    X: DFT of signal (array)
    f: frequency array of signal DFT
    interval: Frequency interval (list of len()=2 of int), interval[0]=<interval[1]
    :return: Energy of signal in interval (float)
    """
    aux=0
    for i,freq in enumerate(f):
        if freq>=interval[0] and freq<=interval[1]:
            aux=aux+abs(X[i]*np.conjugate(X[i]))

    return aux

def q_33(song, f_c, X_c,notes_freq, notes_repetitions, notes):
    """
    Energy of different tones of a musical piece
    :list song: List that contains the song
    :list f_c: List of frequencies of the DFT of the song (centered in 0)
    :list X_c: List of values of the DFT of the song (centered in 0
    :list notes_freq: List of frequencies of the notes used for the song
    :list notes_repetitions: List of repetitions of each note i song
    :list notes:
    """
    fig, axs = plt.subplots(2)
    axs[0].grid()
    axs[1].grid()
    fig.suptitle('Energy per note of Heart and Soul')
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)

    ener_X_c=[abs(X_c[i])**2 for i in range(len(X_c))]

    axs[0].plot(f_c, ener_X_c)
    axs[0].set_xlim((0,2000))
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('DFT')
    y_max=max(ener_X_c)*1.1
    axs[0].set_ylim((0, y_max))
    axs[1].bar(notes_freq,notes_repetitions, width=15)
    # axs[1].set_xticks(notes_freq)
    y_max = max(notes_repetitions) * 1.1
    axs[1].set_ylim((0, y_max))
    axs[1].set_xlim((0,2000))
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Number of time')
    # plt.savefig('EnergyPerNote.png')
    plt.show()

def q_34(f_0, T, f_s, instruments, names_of_instruments)

if __name__ == '__main__':
  fs = 44100 
  #notes 
  D3 = 30 
  E3 = 32 
  F3 = 33 
  G3 = 35 
  A3 = 37 
  B3 = 39 
  C4 = 40 
  D4 = 42 
  E4 = 44
  F4 = 45 
  G4 = 47 
  A4 = 49
  B4 = 51
  C5 = 52 

  #Song (Heart and Soul) 
  song_only_notes = [C4, C4, E4, E4, A3, A3, C4, C4, F3, F3, A3, A3, G3, G3, B3, 
                    B3, C4, C4, E4, E4, A3, A3, C4, C4, F3, F3, A3, A3, G3, G3, 
                    B3, B3, C4, C4, C4, C4, B3, A3, B3, C4, D4, E4, E4, E4, E4, 
                    D4, C4, D4, E4, F4, G4, C4, A4, G4, F4, E4, D4, C4, B3, A3, 
                    G3, F3, E3, D3, E3, F3, G3, A3, B3, C4, C4, E4, E4, A3, A3, 
                    C4, C4, F3, F3, A3, A3, G3, G3, B3, B3, C4, C4, C4, C4, B3, 
                    A3, B3, C4, D4, E4, E4, E4, E4, D4, C4, D4, E4, F4, G4, C4, 
                    A4, G4, F4, E4, D4, C4, C5, B4, A4, B4, A4, G4, F4, G4, F4, 
                    E4, D4, G4, C4] 
  #half note base
  rhythm = 1
  #eighth note
  e = rhythm * 0.5 
  #quarter note
  q = rhythm * 1.0 
  #quarter note + double triplet 
  qdt = rhythm * (1 + (2/3))
  #half note 
  h = rhythm * 2.0 
  #half note + double triplet 
  hdt = rhythm * (2 + (2/3)) 
  #triplet
  t = rhythm * (1/3) 
  #double triplet
  dt = rhythm * (2/3) 

  song_rhythm = [dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, 
                dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, 
                q, q, hdt, t, dt, t, dt, t, q, q, q, hdt, t, dt, t, dt, t, q, h, 
                hdt, t, dt, t, q, q, qdt, t, qdt, t, dt, t, dt, t, dt, t, dt, t,
                dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, dt, t, q, q, hdt, 
                t, dt, t, dt, t, q, q, q, 
                hdt, t, dt, t, dt, t, q, h, hdt, t, dt, t, q, q, q, dt, t, dt, 
                t, dt, t, dt, t, dt, t, q, q, h]  

  song,f_c, X_c=q_32(song_only_notes, song_rhythm, fs)


  #q_33 

  notes = [D3, E3, F3, G3, A3, B3, C4, D4, E4, F4, G4, A4, B4, C5]
  notes_freq = [2 ** ((note - 49) / 12) * 440 for note in notes]

  notes_repetitions=[0 for i in range(len(notes))]
  for i,note in enumerate(song_only_notes):
      notes_repetitions[notes.index(int(note))]=notes_repetitions[notes.index(int(note))]+song_rhythm[i]

  q_33(song, f_c, X_c, notes_freq,notes_repetitions,notes)


  #q_34 
  
  oboe = [1.386, 1.370, 0.360, 0.116, 0.106, 0.201, 0.037, 0.019] 
  flute = [0.260, 0.118, 0.085, 0.017, 0.014]
  trumpet = [1.167, 1.178, 0.611, 0.591, 0.344, 0.139, 0.090, 0.057, 0.035, 
              0.029, 0.022, 0.020, 0.014] 
  clarinet = [0.061, 0.628, 0.231, 1.161, 0.201, 0.328, 0.154, 0.072, 0.186, 
              0.133, 0.309, 0.071, 0.098, 0.114, 0.027, 0.057, 0.022, 0.042, 
              0.023]

  f_0 = 440
  T = 2 
  f_s = 44100 

  q_34(f_0,T,f_s,[oboe,flute,trumpet,clarinet],
       ['oboe','flute','trumpet','clarinet'])