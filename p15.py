# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

import random

#Reservoir sampling
def main():
  def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

main()