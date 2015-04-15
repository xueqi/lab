
from EMAN2_cppwrap import *
from global_def import *


ref_ali2d_counter = -1
	
def helical3c( ref_data ):
	from utilities      import print_msg
	from filter         import fit_tanh, filt_tanl
	from morphology     import threshold
	from utilities import sym_vol
	#  Prepare the reference in helical refinement, i.e., low-pass filter .
	#  Input: list ref_data
	#   0 - raw volume
	#  Output: filtered, and masked reference image

	global  ref_ali2d_counter
	ref_ali2d_counter += 1
	print_msg("helical   #%6d\n"%(ref_ali2d_counter))
	stat = Util.infomask(ref_data[0], None, True)
	volf = ref_data[0] #- stat[0]
	fl = 0.4
	aa = 0.11
	volf = filt_tanl(volf, fl, aa)
	
	return  volf

