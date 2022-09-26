'''
Created on Sep 23, 2022

@author: mireia
'''
import argparse

parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b') #run the parser and parse the arguments. By itself it only contains help --h
parser.add_argument('-a', '--numero_a', type=int, help='Parámetro a') # indicamos el nombre de la variable al introducir el valor 
parser.add_argument('-b', '--numero_b', type=int, help='Parámetro b') #With -- the arguments changes from positional to optional
parser.add_argument('-o', '--operacion',
                    type=str,
                    choices=['suma', 'resta', 'multiplicacion'], #si se introduce otra operación dará error
                    default='suma', required=False, 
                    help='Operación a realizar con a y b')

args = parser.parse_args()


if args.operacion == 'suma':
    print(args.numero_a + args.numero_b)
elif args.operacion == 'resta':
    print(args.numero_a - args.numero_b)
elif args.operacion == 'multiplicacion':
    print(args.numero_a * args.numero_b)