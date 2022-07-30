# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

 #for i in range(0,4):
    #    dut.sel.value = i
    #    assert dut.out.value == inputLines[i].value, "SELECTED LINE MISMATCHES: sel={A} != {B}, expected value={EXP}".format(
    #        A=int(dut.sel.value), B=inputLines[i].value, EXP=inputLines[i].value)

@cocotb.test()
async def test_mux0(dut):
    dut.inp0.value = random.randint(0, 3)
    dut.sel.value = 0
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp0.value, f"SELECTED LINE MISMATCHES for sel = 0"

@cocotb.test()
async def test_mux1(dut):
    dut.inp1.value = random.randint(0, 3)
    dut.sel.value = 1
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp1.value, f"SELECTED LINE MISMATCHES for sel = 1" 

@cocotb.test()
async def test_mux2(dut):
    dut.inp2.value = random.randint(0, 3)
    dut.sel.value = 2
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp2.value, f"SELECTED LINE MISMATCHES for sel = 2"   
   
    
@cocotb.test()
async def test_mux3(dut):
    dut.inp3.value = random.randint(0, 3)
    dut.sel.value = 3
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp3.value, f"SELECTED LINE MISMATCHES for sel = 3"
   
@cocotb.test()
async def test_mux4(dut):
    dut.inp4.value = random.randint(0, 3)   
    dut.sel.value = 4
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp4.value, f"SELECTED LINE MISMATCHES for sel = 4"

@cocotb.test()
async def test_mux5(dut):
    dut.inp5.value = random.randint(0, 3)
    dut.sel.value = 5
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp5.value, f"SELECTED LINE MISMATCHES for sel = 5"

@cocotb.test()
async def test_mux6(dut):
    dut.inp6.value = random.randint(0, 3)   
    dut.sel.value = 6
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp6.value, f"SELECTED LINE MISMATCHES for sel = 6"

@cocotb.test()
async def test_mux7(dut):
    dut.inp7.value = random.randint(0, 3)   
    dut.sel.value = 7
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp7.value, f"SELECTED LINE MISMATCHES for sel = 7"

@cocotb.test()
async def test_mux8(dut):
    dut.inp8.value = random.randint(0, 3)
    dut.sel.value = 8
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp8.value, f"SELECTED LINE MISMATCHES for sel = 8"

@cocotb.test()
async def test_mux9(dut):
    dut.inp9.value = random.randint(0, 3) 
    dut.sel.value = 9
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp9.value, f"SELECTED LINE MISMATCHES for sel = 9"
    
@cocotb.test()
async def test_mux10(dut):
    dut.inp10.value = random.randint(0, 3)
    dut.sel.value = 10
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp10.value, f"SELECTED LINE MISMATCHES for sel = 10"

@cocotb.test()
async def test_mux11(dut):
    dut.inp11.value = random.randint(0, 3)   
    dut.sel.value = 11
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp11.value, f"SELECTED LINE MISMATCHES for sel = 11"
    
@cocotb.test()
async def test_mux12(dut):
    dut.inp12.value = random.randint(0, 3)  
    dut.sel.value = 12
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp12.value, f"SELECTED LINE MISMATCHES for sel = 12"
    
@cocotb.test()
async def test_mux13(dut):
    dut.inp13.value = random.randint(0, 3)    
    dut.sel.value = 13
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp13.value, f"SELECTED LINE MISMATCHES for sel = 13"
    
@cocotb.test()
async def test_mux14(dut):
    dut.inp14.value = random.randint(0, 3)    
    dut.sel.value = 14
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp14.value, f"SELECTED LINE MISMATCHES for sel = 14"
    
@cocotb.test()
async def test_mux15(dut):
    dut.inp15.value = random.randint(0, 3)
    dut.sel.value = 15
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp15.value, f"SELECTED LINE MISMATCHES for sel = 15"

@cocotb.test()
async def test_mux16(dut):
    dut.inp16.value = random.randint(0, 3)
    dut.sel.value = 16
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp16.value, f"SELECTED LINE MISMATCHES for sel = 16"

@cocotb.test()
async def test_mux17(dut):
    dut.inp17.value = random.randint(0, 3)
    dut.sel.value = 17
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp17.value, f"SELECTED LINE MISMATCHES for sel = 17"

@cocotb.test()
async def test_mux18(dut):
    dut.inp18.value = random.randint(0, 3)    
    dut.sel.value = 18
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp18.value, f"SELECTED LINE MISMATCHES for sel = 18"
    
@cocotb.test()
async def test_mux19(dut):
    dut.inp19.value = random.randint(0, 3)    
    dut.sel.value = 19
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp19.value, f"SELECTED LINE MISMATCHES for sel = 19"

@cocotb.test()
async def test_mux20(dut):
    dut.inp20.value = random.randint(0, 3)
    dut.sel.value = 20
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp20.value, f"SELECTED LINE MISMATCHES for sel = 20"

@cocotb.test()
async def test_mux21(dut):
    dut.inp21.value = random.randint(0, 3)
    dut.sel.value = 21
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp21.value, f"SELECTED LINE MISMATCHES for sel = 21"

@cocotb.test()
async def test_mux22(dut):
    dut.inp22.value = random.randint(0, 3)    
    dut.sel.value = 22
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp22.value, f"SELECTED LINE MISMATCHES for sel = 22"

@cocotb.test()
async def test_mux23(dut):
    dut.inp23.value = random.randint(0, 3)    
    dut.sel.value = 23
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp23.value, f"SELECTED LINE MISMATCHES for sel = 23"

@cocotb.test()
async def test_mux24(dut):
    dut.inp24.value = random.randint(0, 3)    
    dut.sel.value = 24
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp24.value, f"SELECTED LINE MISMATCHES for sel = 24"

@cocotb.test()
async def test_mux25(dut):
    dut.inp25.value = random.randint(0, 3)    
    dut.sel.value = 25
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp25.value, f"SELECTED LINE MISMATCHES for sel = 25"
    
@cocotb.test()
async def test_mux26(dut):
    dut.inp26.value = random.randint(0, 3)
    dut.sel.value = 26
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp26.value, f"SELECTED LINE MISMATCHES for sel = 26"
    
@cocotb.test()
async def test_mux27(dut):
    dut.inp27.value = random.randint(0, 3)
    dut.sel.value = 27
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp27.value, f"SELECTED LINE MISMATCHES for sel = 27"
    
@cocotb.test()
async def test_mux28(dut):
    dut.inp28.value = random.randint(0, 3)    
    dut.sel.value = 28
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp28.value, f"SELECTED LINE MISMATCHES for sel = 28"
    
@cocotb.test()
async def test_mux29(dut):
    dut.inp29.value = random.randint(0, 3)    
    dut.sel.value = 29
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp29.value, f"SELECTED LINE MISMATCHES for sel = 29"
    
@cocotb.test()
async def test_mux30(dut):
    dut.inp30.value = random.randint(0, 3)
    dut.sel.value = 30
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp30.value, f"SELECTED LINE MISMATCHES for sel = 30"
    