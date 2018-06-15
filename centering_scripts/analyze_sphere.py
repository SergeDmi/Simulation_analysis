# -*- coding: utf-8 -*-
#!/usr/bin/env python

####### Modules
import math
from numpy import *

####### Custom utilitary package
from tools import *
####### Specialize analysis package
import ply_analysis as pa

####### MAIN
if __name__=="__main__":
	# declaration of file names
	file_base="simulated_cell_"
	config_file="config.cym"
	export_file="sphere_res.txt"

	# export files
	oop=open(export_file,'w')
	eop=open('end_%s' %export_file,'w')

	## First we load the data
	plyfiles=make_ordered_file_list(file_base,'.ply')

	# We make a dictionary of simulation properties from the config file
	prodic=make_prop_dict(config_file,"set_prop")
	keys=prodic.keys()

	# Results analysis and export
	for i,item in enumerate(plyfiles):
		# Analysis is outsourced !
		(list_res,list_names)=pa.analyze_sphere(item[1])
		# Making header for export file
		if i==0:
			header="#time "
			header=header+''.join([' %s' %name for name in list_names])
			header=header+''.join([' %s' %key for key in keys])+'\n'
			oop.write(header)
		# Export
		oop.write('%s' %item[0])
		[oop.write(' %s' %res) for res in list_res]
		[oop.write(' %s' %prodic[key]) for key in keys]
		oop.write(' \n')

	# Also saving just last point
	eop.write('%s' %item[0])
	[eop.write(' %s' %res) for res in list_res]
	[eop.write(' %s' %prodic[key]) for key in prodic.keys()]

	# Closing here
	oop.close()
	eop.close()

	# Great job chaps !
