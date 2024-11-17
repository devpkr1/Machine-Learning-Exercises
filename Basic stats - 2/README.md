# Estimation And Confidence Intervals

## Background
In quality control processes, especially when dealing with high-value items, destructive sampling is a necessary but costly method to ensure product quality. The test to determine whether an item meets the quality standards destroys the item, leading to the requirement of small sample sizes due to cost constraints.

## Scenario
A manufacturer of print-heads for personal computers is interested in estimating the mean durability of their print-heads in terms of the number of characters printed before failure. To assess this, the manufacturer conducts a study on a small sample of print-heads due to the destructive nature of the testing process.

## Data
A total of 15 print-heads were randomly selected and tested until failure. The durability of each print-head (in millions of characters) was recorded as follows:
- 1.13
- 1.55
- 1.43
- 0.92
- 1.25
- 1.36
- 1.32
- 0.85
- 1.07
- 1.48
- 1.20
- 1.33
- 1.18
- 1.22
- 1.29

## Assignment Tasks

### a. Build 99% Confidence Interval Using Sample Standard Deviation
Assuming the sample is representative of the population, construct a 99% confidence interval for the mean number of characters printed before the print-head fails using the sample standard deviation. 

**Steps:**
1. **Calculate the Sample Mean ($\bar{x}$)**:
   $$
   \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
   $$
   where $n$ is the sample size and $x_i$ are the sample values.

2. **Calculate the Sample Standard Deviation ($s$)**:
   $$
   s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}
   $$

3. **Determine the t-Score**:
   For a 99% confidence level and $n-1$ degrees of freedom, find the critical t-value from the t-distribution table.

4. **Calculate the Margin of Error (ME)**:
   $$
   ME = t \times \frac{s}{\sqrt{n}}
   $$

5. **Construct the Confidence Interval**:
   $$
   \text{Confidence Interval} = \left( \bar{x} - ME, \bar{x} + ME \right)
   $$

**Rationale**: The t-distribution is used because the sample size is small ($n < 30$) and the population standard deviation is unknown.

### b. Build 99% Confidence Interval Using Known Population Standard Deviation
If it were known that the population standard deviation is 0.2 million characters, construct a 99% confidence interval for the mean number of characters printed before failure.

**Steps:**
1. **Calculate the Sample Mean ($\bar{x}$)** (same as above).

2. **Determine the Z-Score**:
   For a 99% confidence level, find the critical z-value from the standard normal distribution table.

3. **Calculate the Margin of Error (ME)**:
   $$
   ME = z \times \frac{\sigma}{\sqrt{n}}
   $$
   where $\sigma$ is the known population standard deviation.

4. **Construct the Confidence Interval**:
   $$
   \text{Confidence Interval} = \left( \bar{x} - ME, \bar{x} + ME \right)
   $$