import argparse

from requests_prediction import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis', type=bool)
    parser.add_argument('--nn', type=bool)
    parser.add_argument('--lstm', type=bool)

    args = parser.parse_args()

    main(show_analysis=args.analysis, use_lstm=args.lstm, use_nn=args.nn)
