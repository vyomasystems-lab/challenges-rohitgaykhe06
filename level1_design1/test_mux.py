# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.sel.value=13
    dut.inp13.value=2
    dut.inp12.value=1

    await Timer(2, units='ns')
    
    assert dut.out.value ==dut.inp13.value, "Mux result is incorrect: {out} != {inp12}, expected value={inp13}".format(
            out=dut.out.value,inp12=dut.inp12.value,inp13=dut.inp13.value)





