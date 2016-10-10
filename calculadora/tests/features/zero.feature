Feature: sumar de dos numeros
    yo como usuario de la app calculadora 
	quiero realizar una suma de dos numeros
	para poder tener un resultado confibale.

    Scenario: sumar 2 mas 2
		dado que tengo el numero "2" y "2"
		cuando realizo  la suma 
		entoces el resultado que obtengo en "4"

    Scenario: sumar -2 mas 2
		dado que tengo el numero "-2" y "2"
		cuando realizo  la suma 
		entoces el resultado que obtengo en "0"

    Scenario: sumar 1000 mas 2000
		dado que tengo el numero "1000" y "2000"
		cuando realizo  la suma 
		entoces el resultado que obtengo en "3000"

    Scenario: sumar -2 mas -3
		dado que tengo el numero "-2" y "-3"
		cuando realizo  la suma 
		entoces el resultado que obtengo en "-5"