"""Monte Carlo prediction of a swimmer's fourth year time."""

import numpy as np


def predict_dist(yr_3_time, mean_rate, std_dev_rate, n=10_000, seed=None):
    """
    yr_3_time   : float, third year time in seconds
    mean_rate   : float, expected percent improvement (pos = faster)
    std_dev_rate: float, standard deviation of rate
    n           : int, number of samples
    seed        : int or None, for reproducibility (outlined in reqs)
    return      : np.ndarray of n simulated fourth year times.
    """

    rng = np.random.default_rng(seed)

    rates = rng.normal(mean_rate, std_dev_rate, n) # improvement rates from a normal distribution
    times = yr_3_time * (1 - (rates / 100)) # converting each rate 

    return times

def summarize(samples, yr_3_time):

    return {
        "median":       np.percentile(samples, 50),   # 50th percentile of samples
        "p10":          np.percentile(samples, 10),   # 10th perentile
        "p90":          np.percentile(samples, 90),    # 90th percentile
        "p2_5":         np.percentile(samples, 2.5),   # 2.5th percentile
        "p97_5":        np.percentile(samples, 97.5),   # 97.5th percentile
        "prob_faster":  (samples < yr_3_time).mean(),   # fraction of samples below yr_3_time
    }

if __name__ == "__main__":
    samples = predict_dist(53.10, mean_rate=1.5, std_dev_rate=1.2, seed=42)
    result = summarize(samples, 53.10)

    print(f"Year 3 time: {53.10:.2f}")
    print(f"Median: {result['median']:.2f}")
    print(f"80% interval: {result['p10']:.2f} - {result['p90']:.2f}")
    print(f"95% interval: {result['p2_5']:.2f} - {result['p97_5']:.2f}")
    print(f"P(faster): {result['prob_faster']:.0%}")


    