# This function will return either 'bull' or 'bear' if a corresponding Marubozu is formed; else it returns False
# The threshold in the peak differences is flexible(to maintain flexibility in stock markets) and set at 0.25%


def marubozu(opn, high, low, close):
    if opn < close:  # Bullish Marubozu Check
        open_low_difference = abs(opn - low) / opn * 100
        print("Open low diff percentage = ", open_low_difference)
        close_high_difference = abs(close - high) / close * 100
        print("Close high diff percentage = ", close_high_difference)
        if open_low_difference < 0.0025 and close_high_difference < 0.25:  # Definition of marubozu
            return 'Bull'
    elif close < opn:  # Bearish Marubozu Check
        open_high_difference = abs(opn - high) / opn * 100
        print("Open high diff percentage = ", open_high_difference)
        close_low_difference = abs(close - low) / close * 100
        print("Close low diff percentage = ", close_low_difference)
        if open_high_difference < 0.0025 and close_low_difference < 0.25:  # Definition of marubozu
            return 'Bear'
    else:
        return False


if __name__ == '__main__':
    print(marubozu(12430, 12430, 12216, 12224))  # Test
