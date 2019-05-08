import pytest
import calculator as student

def testSum1():
    assert student.sum(1,2)==3
def testSum2():
    assert student.sum(6,4)==10
def testSub1():
    assert student.sub(1,2)==-1
def testSub2():
    assert student.sub(6,4)==2
def testDiv1():
    assert student.div(1,2)==0.5
def testDiv2():
    assert student.div(6,3)==2
def testMul1():
    assert student.mul(1,2)==2
def tustMul2():
    assert student.mul(4,6)==24
