# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:51:12 2020

@author: jrena
"""

"""
	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD

	• SQL y PL/SQL

	• Linux

	• Unix

	• Shell (Linux - Unix)

	• C++, Proc*C y Tuxedo V12 o anteriores

	• Visual Basic 6.0

	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)

"""

Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
}

print("¿Cuenta con experiencia de al menos 2 años en lo siguiente?\n"
         "\nEscriba SI o NO segun corresponda\n")

def candidato():
	D1 = input(" Oracle: ").upper()
	D2 = input(" SQL/PL: ").upper()
	D3 = input(" Linux: ").upper()
	D4 = input(" Unix: ").upper()
	D5 = input(" Shell: ").upper()
	D6 = input(" C++: ").upper()
	D7 = input(" Proc*C: ").upper()
	D8 = input(" TuxedoV12: ").upper()
	D9 = input(" VB6: ").upper()
	D10 = input(" Java: ").upper()
	D11 = input(" WebServices: ").upper()
	D12 = input(" MicroServicios: ").upper()
	ExperienciaCandidato = set()
	if D1 == "SI":
		ExperienciaCandidato.add("Oracle")
	if D2 == "SI":
		ExperienciaCandidato.add("SQL/PL")
	if D3 == "SI":
		ExperienciaCandidato.add("Linux")
	if D4 == "SI":
		ExperienciaCandidato.add("Unix")
	if D5 == "SI":
		ExperienciaCandidato.add("Shell")
	if D6 == "SI":
		ExperienciaCandidato.add("C++")
	if D7 == "SI":
		ExperienciaCandidato.add("Proc*C")
	if D8 == "SI":
		ExperienciaCandidato.add("TuxedoV12")
	if D9 == "SI":
		ExperienciaCandidato.add("VB6")
	if D10 == "SI":
		ExperienciaCandidato.add("Java")
	if D11 == "SI":
		ExperienciaCandidato.add("WebServices")
	if D12 == "SI":
		ExperienciaCandidato.add("MicroServicios")
	Dif= Requisitos - ExperienciaCandidato
	Inter = Requisitos & ExperienciaCandidato
	print("\nExperiencia del candidato ",ExperienciaCandidato)
	print("\nExperiencia faltante en el candidato",Dif)
	Minimos = len(Requisitos)
	Experiencia = len(Inter)
	RequisitosMinimos = Minimos - 4
	if Experiencia >= RequisitosMinimos:
		return "\nEs Candidato"
	else:
		return "\nNO Es Candidato"

print(candidato())
