#!/usr/bin/env python
import pytest

from app.Calculator import ClassCalculator

def test_calculator_sum():
      calc = ClassCalculator
      assert calc.sum(2,4) = 5

def test_calculadora_subtraction():
      calc = ClassCalculator
      assert calc.subtration(5,3) = 2

def test_calculadora_multiplication():
      calc = ClassCalculator
      assert calc.multiplication(5,3) = 15
      
def test_calculadora_division():
      calc = ClassCalculator
      assert calc.division(6,3) = 2
      

