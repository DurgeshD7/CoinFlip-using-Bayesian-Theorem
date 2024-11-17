# Given data: 7 heads and 3 tails
heads = 7
tails = 3
total_flips = heads + tails

# Prior probability for a fair coin (50% chance for heads or tails)
prior_heads = 0.5
prior_tails = 0.5

# Likelihood of the observed data given the coin is fair
# P(D|H) and P(D|T) where D is the data (7 heads, 3 tails)
likelihood_heads = (0.5 ** heads) * (0.5 ** tails)
likelihood_tails = (0.5 ** tails) * (0.5 ** heads)

# Posterior probability
posterior_heads = likelihood_heads * prior_heads
posterior_tails = likelihood_tails * prior_tails

# Normalize to get the probability
total_posterior = posterior_heads + posterior_tails
posterior_heads = posterior_heads/total_posterior
posterior_tails = posterior_tails/total_posterior

# Adding more realistic priors for bias estimation
biased_prior_heads = 0.7
biased_prior_tails = 0.3

# Update posterior with biased prior
posterior_biased_heads = likelihood_heads * biased_prior_heads
posterior_biased_tails = likelihood_tails * biased_prior_tails

# Normalize to get the probability
total_posterior_biased = posterior_biased_heads + posterior_biased_tails
posterior_biased_heads /= total_posterior_biased
posterior_biased_tails /= total_posterior_biased

print(f"Posterior probability of heads (biased prior): {posterior_biased_heads:.2f}")
print(f"Posterior probability of tails (biased prior): {posterior_biased_tails:.2f}")

# Determine if the coin is biased
if posterior_biased_heads > 0.5:
    print("The coin is likely biased towards heads.")
elif posterior_biased_heads < 0.5:
    print("The coin is likely biased towards tails.")
else:
    print("The coin is likely fair.")
