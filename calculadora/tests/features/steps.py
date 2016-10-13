# -*- coding: utf-8 -*-
from lettuce import step,world
from calculadora import calculadora

@step(u'dado que tengo el numero "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group1(step, num1, num2):
    cal = calculadora()
    world.resultado = cal.suma(int(num1),int(num2))

@step(u'cuando realizo  la suma')
def cuando_realizo_la_suma(step):
    pass

@step(u'cuando realizo  la resta')
def cuando_realizo_la_resta(step):
    pass

@step(u'cuando realizo  la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
    pass

@step(u'entoces el resultado que obtengo en "([^"]*)"')
def entoces_el_resultado_que_obtengo_en_group1(step, esperado):
    assert int(esperado)==world.resultado, 'El resultado esperado no es el mismo'+' error:'+esperado+' '+world.resultado
