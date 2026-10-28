from scipy.stats import poisson

# Given expected number of rainy days (mean, lambda)
lambda_val = 10

# 1. Probability of observing 12 or more days of rain: P(X >= 12) = 1 - P(X <= 11)
prob_12_or_more = 1 - poisson.cdf(11, lambda_val)

# 2. Probability of observing between 12 and 18 days of rain: P(12 <= X <= 18)
prob_between_12_and_18 = poisson.cdf(18, lambda_val) - poisson.cdf(11, lambda_val)

# Displaying the results
print(f"Probability of observing 12 or more days of rain: {prob_12_or_more:.4f}")
print(f"Probability of observing between 12 and 18 days of rain: {prob_between_12_and_18:.4f}")