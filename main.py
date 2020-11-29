import SamplePreprocessor
import SamplesToDistributionCalculator
import TheoreticalDistributionCalculator
import ChiSquareCalculator
import IsNormalDistributionDefiner

import matplotlib.pyplot as plt

if __name__ == '__main__':
    h = 0.001
    significance = 0.05
    path = '/media/sf_virtualbox/Chi_v07b.txt'

    preprocessor = SamplePreprocessor.SamplePreprocessor(path_=path, h_=h)
    samples, degree = preprocessor.samples, preprocessor.degree
    print('Degrees of freedom: ', degree)

    actual_calculator = SamplesToDistributionCalculator.SamplesToDistributionCalculator(samples)
    average, sd = actual_calculator.calculate_normal_distribution_parameters()
    print('Average: ', average)
    print('SD: ', sd)

    expected_calculator = \
        TheoreticalDistributionCalculator.TheoreticalDistributionCalculator(n_=actual_calculator.n,
                                                                            frequencies_=actual_calculator.frequencies,
                                                                            average_=average, sd_=sd, h_=h)
    expected_frequencies = expected_calculator.calculate_expected_frequencies()
    #
    chi_square_calculator = \
        ChiSquareCalculator.ChiSquareCalculator(actual_frequencies_=actual_calculator.frequencies,
                                                expected_frequencies_=expected_frequencies)
    chi_square = chi_square_calculator.calculate_chi_square()
    print('Chi_Square: ', chi_square)

    definer = IsNormalDistributionDefiner.IsNormalDistributionDefiner(degrees_=degree, significance_=significance)
    if definer.is_normal_distribution(chi_square):
        print('Distribution is normal')
    else:
        print('Distribution is not normal')

    plt.hist(actual_calculator.samples)
    plt.show()
