####### MODULES
import math
from numpy import *
from plyfile import PlyData, PlyElement

####### FUNCTIONS
def import_from_ply(fname):
	try:
		plydata = PlyData.read(fname)
	except:
		raise ValueError('Could not read file %s' %fname)
	pts=array([[x for x in b] for b in plydata.elements[0].data])
	return pts

def analyze_sphere(fname):
	pts_ply=import_from_ply(fname)
	(nr,nc)=pts_ply.shape
	pts=pts_ply[:,0:3]
	cen=mean(pts,0)
	# data centering
	pts=pts-ones((nr,1))*cen
	R=sqrt(mean(sum(pts**2,1)))
	return [R],["radius"]
