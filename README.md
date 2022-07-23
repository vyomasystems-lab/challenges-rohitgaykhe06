# challenges-rohitgaykhe06
challenges-rohitgaykhe06 created by GitHub Classroom
final Report 
# Mux Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![Capture1](https://user-images.githubusercontent.com/96008151/180605367-f088d5b7-2d04-430c-a845-7a9ee1f7ea97.PNG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit input as *sel* and 2-bit inputs as *inp13* and *inp12* gives 2-bit output as *out*.

The values are assigned to the input port using 
```
dut.sel.value = 13
dut.inp13.value=2
dut.inp12.value=1
```

The assert statement is used for comparing the mux outut to the expected value.

The following error is seen:
```
assert dut.out.value ==dut.inp13.value, "Mux result is incorrect: {out} != {inp13}, expected value={inp13}".format(
                     AssertionError: Mux result is incorrect: 01 != 10, expected value=10
```
## Test Scenario **(Important)**
- Test Inputs: sel=13 inp13=2 inp12=1
- Expected Output: out=inp13
- Observed Output in the DUT dut.out=inp12

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 case(sel) 
 
    5'b01101: out = inp12; ====> BUG It should be 5'b1100.
    5'b01101: out = inp13;   
 endcase
```
For the Mux design, sel=13 is added 2 times.This is the reason,for sel=13, it gives output as *inp12* instead of *inp13*.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/96008151/180606033-241b2e41-e751-437f-b1a9-2e67518f083e.png)


The updated design is checked in as mux_fix.v

## Verification Strategy

## Is the verification complete ?


