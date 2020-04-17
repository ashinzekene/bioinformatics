def SpectrumConvolution(spectrum):
    spectrum.sort()
    convolution = []
    for i, current_mass in enumerate(spectrum[:-1]):
        for mass in spectrum[i+1:]:
            if mass == current_mass:
                continue
            convolution.append(mass - current_mass)
    convolution.sort()
    return convolution


if __name__ == "__main__":
    spectrum = []
    with open('./datasets/dataset_104_4.txt') as f:
        spectrum = f.read().strip().split(' ')
        spectrum = [int(mass) for mass in spectrum]

    result = SpectrumConvolution(spectrum)
    with open('./results/spectrum_convolution.txt', 'w') as f:
        f.write(' '.join([str(mass) for mass in result]))
    