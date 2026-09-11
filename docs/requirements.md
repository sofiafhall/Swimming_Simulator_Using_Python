# Functional Requirements

## Input Handling

**R-01** The system accepts swim times in the format of either 'SS.hh' and 'M:SS.hh' and converts them to float seconds.
*Verification:* Test

**R-02** The system rejects incorrectly formated times with a message and does not terminate.
*Verification:* Test

**R-03** The system flags year over year time change exceeding 25% as implausible, and requires confirmation.
*Verification:* Test

## Model

**R-04** The system computes improvement based on event, gender, division, and career transition.
*Verification:* Test

**R-05** The system combines an individual's observed improvement rate toward the population mean.
*Verification:* Test

**R-06** The system will generate a fourth year predicition from no more than 10,000 Monte Carlo samples. 
*Verification:* Test

**R-07** The system will give 80% and 95% predicition intervals. 
*Verification:* Test

## Reproduce

**R-08** The system will produce identical output for identical input when a random seed is given. 
*Verification:* Test

**R-09** The system fit model parameters so predictions are reproducible without adjusting. 
*Verification:* Test

**R-10** The system will report predicition intervals based upon a standard. 
*Verification:* Test
