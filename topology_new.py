import sys
import os
def controller():
	"Input ip address of controller"
	ip_controller =str(raw_input('What address ip of controller ? \n ' ))
	"port_controller =str(raw_input('What address port of controller ? \n ' ))"
	return ip_controller
def linear_network():
	"Input number of switches"
	k1=int(raw_input('How many switch in linear network ? \n'))
	control=controller()
	os.system('sudo mn --switch ovsk --controller=remote,ip=%s,port=6633 --topo linear,%s --protocol OpenFlow13'%control %k1)
def tree_network():
	"Input number deepth for tree network "
	depth1 =int(raw_input('How many depth in tree network? \n '))
	"Input number fanout for tree network "
	fanout1 =int(raw_input('How many fanout in tree network? \n '))
	control=controller()
	os.system('sudo mn --switch ovsk --controller=remote,ip=%s,port=6633 --topo tree,depth=%s,fanout=%s --protocol OpenFlow13'%control %depth1 %fanout1)
	def single_network():
		k2=int(raw_input('How many host connect in switch ? \n'))
		control=controller()
		os.system('sudo mn --switch ovsk --controller=remote,ip=%s,port=6633 --topo single,%s --protocol OpenFlow13'%control %k1)
def choose_type ():
	print('Do you use topology network for mininet ? \n')
	type_topo=int(raw_input('Press number for choose type network have: 1(tree network) | 2(linear network) | 3(single network) '))
	if type_topo ==1:
		print('You have to choose tree network ' )
	elif type_topo ==2:
		print('You have to choose linear network ')
	elif type_topo ==3:
		print('You have to choose single network ')
		
	return type_topo
def clear():
	os.system('sudo mn -c')
def main():
	clear()
	type =choose_type()
	if type ==1:
		tree_network()
	elif type==2:
		linear_network()
	elif type==3:
		single_network()
main()
	