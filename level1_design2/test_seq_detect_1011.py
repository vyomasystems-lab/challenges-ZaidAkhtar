# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    sequence = [1,0,1,1]
    seqBit = [0,0,0,1,0,1,1,0,0,0,0,0]
    result = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    for i in range(3):
        seqBit[i] = random.randint(0, 1)
    
    for i in range(7,12):
        seqBit[i] = random.randint(0, 1)
        
    cocotb.log.info('random sequence bits = ',seqBit)

    for i in range(len(seqBit)):
        dut.inp_bit.value = seqBit[i]

    index = []
    for i in range(len(seqBit)):
        if seqBit[i:i+len(sequence)] == sequence:
           index.append(i+len(sequence))
           result[i+len(sequence)] = 1

    cocotb.log.info('result : ',result)

    for i in range(len(seqBit)):
        
        dut.inp_bit.value = seqBit[i]
        await RisingEdge(dut.clk)
        try:
            assert dut.seq_seen.value == result[i]
        except AssertionError as e:
            print("RESULT MISMATCH FOR INDEX = {A}, EXPECTING :{B}, GOT: {C}".format(A=i, B=seqBit[i+1], C=int(dut.seq_seen.value)))
        