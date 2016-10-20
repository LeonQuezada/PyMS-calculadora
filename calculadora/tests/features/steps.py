# -*- coding: utf-8 -*-
from lettuce import step,world
from calculadora import calculadora

@step(u'dado que tengo el numero "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group1(step, num1, num2):
    cal = calculadora()
    world.resultado = cal.suma(float(num1),float(num2))

@step(u'dado que tengo el numero para dividir "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_para_dividir_group1_y_group1(step, num1, num2):
    cal = calculadora()
    world.resultado = cal.divicion(float(num1),float(num2))

@step(u'cuando realizo  la suma')
def cuando_realizo_la_suma(step):
    pass

@step(u'cuando realizo  la resta')
def cuando_realizo_la_resta(step):
    pass

@step(u'cuando realizo  la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
    pass

@step(u'cuando realizo la divicion')
def cuando_realizo_la_divicion(step):
	pass
    

@step(u'entoces el resultado que obtengo en "([^"]*)"')
def entoces_el_resultado_que_obtengo_en_group1(step, esperado):
    assert float(esperado)==world.resultado,world.resultado
