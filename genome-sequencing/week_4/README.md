# How do we sequence antibiotics

In the previous week, we worked with theoretical spetra, however in the experimental spectra, we might have false/missing masses from the spectrum generated from the mass spectrometer. In this situation, we need to generate a score for each peptide and then cut out peptides with scores below our threshold.

More annoyingly, many peptides sythensized by NTP-synthetase contain other different amino acids thant he 20 naturally occurring ones. I.e amino acids with masses ranging from 57-200 daltons.

To solve the problem of missing and false masses, we could use a scoring function that will select the peptide whose theoretical spectrum matches the given experimental spectrum the most closely.