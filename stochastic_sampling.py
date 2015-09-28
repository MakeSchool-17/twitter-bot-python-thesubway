import sys
import word_frequency


def histogram_word(input_histogram):
    print(input_histogram.keys())

if __name__ == '__main__':
    my_file = str(sys.argv[1])
    my_histogram = word_frequency.histogram(my_file)
    histogram_word(my_histogram)
