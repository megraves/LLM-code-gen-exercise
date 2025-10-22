Let’s go through this systematically — planning, executing, critiquing, and refining.

---

## 🧩 Step 1: **Plan**

We need to find the **largest prime factor** of a given integer `n` where:

* `n > 1`
* `n` is **not prime**

We’ll break this problem into substeps:

1. **Initialize** a variable to store the largest factor.
2. **Divide out small factors first**:

   * Start with the smallest prime, 2.
   * While `n` is divisible by 2, divide it out and record 2 as the current largest prime factor.
3. **Move to odd factors**:

   * Use a loop from 3 up to √n (since a larger factor would have to multiply with something smaller).
   * For each odd number `i`:

     * While `n` is divisible by `i`, divide it out and record `i` as the current largest factor.
4. **If after the loop `n > 2`**, then `n` itself is prime and is the largest prime factor.
5. **Return** the largest factor.

This approach is efficient and uses trial division only up to √n.

---

## ⚙️ Step 2: **Execute (Implement the Plan)**

```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest = None

    # Step 1: Handle factor 2
    while n % 2 == 0:
        largest = 2
        n //= 2

    # Step 2: Handle odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2  # Only test odd numbers

    # Step 3: If n is now > 2, it’s a prime factor
    if n > 2:
        largest = n

    return largest
```

---

## 🧪 Step 3: **Test the Implementation**

### Example 1:

`largest_prime_factor(13195)`

* Factors: 5, 7, 13, 29 → Largest = 29 ✅

### Example 2:

`largest_prime_factor(2048)`

* 2048 = 2¹¹ → Largest = 2 ✅

### Example 3:

`largest_prime_factor(100)`

* Factors: 2, 5 → Largest = 5 ✅

### Example 4:

`largest_prime_factor(72)`

* Factors: 2, 3 → Largest = 3 ✅

All pass.

---

## 🔍 Step 4: **Critique**

✅ **Strengths**

* Handles both even and odd factors.
* Efficient (divides n down as it goes).
* Works for all composite n > 1.

⚠️ **Possible improvements**

* Could be more readable if we clearly separate logic for dividing and checking factors.
* Could add a guard against invalid inputs (though spec says assume n > 1).

---

## 🧠 Step 5: **Refine (Make Slightly Clearer)**

Here’s a cleaner, final version:

```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest = 1

    # Divide out all factors of 2
    while n % 2 == 0:
        largest = 2
        n //= 2

    # Divide out all odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2

    # If remaining n is prime and greater than 2
    if n > 2:
        largest = n

    return int(largest)
```

---

✅ **Final Answer (passes all tests):**

```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 1

    while n % 2 == 0:
        largest = 2
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2

    if n > 2:
        largest = n

    return int(largest)
```
