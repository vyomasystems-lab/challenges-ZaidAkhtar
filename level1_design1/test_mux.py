# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    inputLines = [dut.inp0, dut.inp1, dut.inp2, dut.inp3, dut.inp4, dut.inp5, dut.inp6, dut.inp7, 
    dut.inp8, dut.inp9, dut.inp10, dut.inp11, dut.inp12, dut.inp13, dut.inp14, dut.inp15, dut.inp16, 
    dut.inp17, dut.inp18, dut.inp19, dut.inp20, dut.inp21, dut.inp22, dut.inp23, dut.inp24, dut.inp25,
    dut.inp26, dut.inp27, dut.inp28, dut.inp29, dut.inp30]

    for i in range(0,32):
        dut.sel.value = i
        assert dut.out.value == inputLines[i], "SELECTED LINE MISMATCHES: sel={A} != {B}, expected value={EXP}".format(
            A=int(dut.sel.value), B=inputLines[i], EXP=inputLines[i])
