import os
from rpy2.robjects import r, numpy2ri, pandas2ri
from rpy2.robjects.packages import importr
numpy2ri.activate()
pandas2ri.activate()
importr('WhiteStripe')

neurobase = importr('neurobase')

def readnii(file):
	return neurobase.readnii(file)
def writenii(data, file):
	import nibabel as nib
	import numpy as np
	if type(data) is np.ndarray:
		new_image = nib.Nifti1Image(data, affine=np.eye(4))
		return new_image.to_filename(file)
	else:
		return neurobase.writenii(data, file)


def download_img_data(lib_loc = r('NULL')):
	r.assign('lib.loc', lib_loc)
	return r('download_img_data(lib.loc=lib.loc)')

def get_deriv_smooth_hist(x = r('NA'), coefs = r('NA'), knots = r('NA'), deg = 4, deriv_deg = 1):
	r.assign('x', x)
	r.assign('coefs', coefs)
	r.assign('knots', knots)
	r.assign('deg', deg)
	r.assign('deriv.deg', deriv_deg)
	return r('get.deriv.smooth.hist(x=x, coefs=coefs, knots=knots, deg=deg, deriv.deg=deriv.deg)')

def get_first_mode(x = r('NA'), y = r('NA'), rare_prop = None, verbose = True, remove_tail = True):
	r.assign('x', x)
	r.assign('y', y)
	r.assign('verbose', verbose)
	r.assign('remove.tail', remove_tail)
	if rare_prop is None:
		rare_prop = r('1/5')
	r.assign('rare.prop', rare_prop)
	return r('get.first.mode(x=x, y=y, rare.prop=rare.prop, verbose=verbose, remove.tail=remove.tail)')

def get_largest_mode(x = r('NA'), y = r('NA'), verbose = True):
	r.assign('x', x)
	r.assign('y', y)
	r.assign('verbose', verbose)
	return r('get.largest.mode(x=x, y=y, verbose=verbose)')

def get_last_mode(x = r('NA'), y = r('NA'), rare_prop = None, verbose = True, remove_tail = True):
	r.assign('x', x)
	r.assign('y', y)
	r.assign('verbose', verbose)
	r.assign('remove.tail', remove_tail)
	if rare_prop is None:
		rare_prop = r('1/5')
	r.assign('rare.prop', rare_prop)
	return r('get.last.mode(x=x, y=y, rare.prop=rare.prop, verbose=verbose, remove.tail=remove.tail)')

def make_img_voi(img = r('NA'), slices = None, na_rm = True):
	r.assign('img', img)
	r.assign('na.rm', na_rm)
	if slices is None:
		slices = r('80:120')
	r.assign('slices', slices)
	return r('make_img_voi(img=img, slices=slices, na.rm=na.rm)')

def s_hist():
	return r('s.hist')

def smooth_hist(x = r('NA'), y = r('NA'), deg = 4, k = None, method = "REML"):
	r.assign('x', x)
	r.assign('y', y)
	r.assign('deg', deg)
	r.assign('method', method)
	if k is None:
		k = r('floor(min(250, length(x)/2))')
	r.assign('k', k)
	return r('smooth_hist(x=x, y=y, deg=deg, k=k, method=method)')

def t1_voi_hist():
	return r('t1.voi.hist')

def t2_voi_hist():
	return r('t2.voi.hist')

def whitestripe(img = r('NA'), type = None, breaks = 2000, whitestripe_width = 0.05, whitestripe_width_l = None, whitestripe_width_u = None, arr_ind = False, verbose = True, stripped = False, slices = r('NULL')):
	r.assign('img', img)
	r.assign('breaks', breaks)
	r.assign('whitestripe.width', whitestripe_width)
	r.assign('arr.ind', arr_ind)
	r.assign('verbose', verbose)
	r.assign('stripped', stripped)
	r.assign('slices', slices)
	if type is None:
		type = r('c("T1", "T2", "FA", "MD", "first", "last", "largest")')
	r.assign('type', type)
	if whitestripe_width_l is None:
		whitestripe_width_l = r('whitestripe.width')
	r.assign('whitestripe.width.l', whitestripe_width_l)
	if whitestripe_width_u is None:
		whitestripe_width_u = r('whitestripe.width')
	r.assign('whitestripe.width.u', whitestripe_width_u)
	return r('whitestripe(img=img, type=type, breaks=breaks, whitestripe.width=whitestripe.width, whitestripe.width.l=whitestripe.width.l, whitestripe.width.u=whitestripe.width.u, arr.ind=arr.ind, verbose=verbose, stripped=stripped, slices=slices)')

def whitestripe_hybrid(t1 = r('NA'), t2 = r('NA')):
	r.assign('t1', t1)
	r.assign('t2', t2)
	return r('whitestripe_hybrid(t1=t1, t2=t2)')

def whitestripe_ind_to_mask(img = r('NA'), indices = r('NA'), writeimg = False):
	r.assign('img', img)
	r.assign('indices', indices)
	r.assign('writeimg', writeimg)
	return r('whitestripe_ind_to_mask(img=img, indices=indices, writeimg=writeimg)')

def whitestripe_norm(img = r('NA'), indices = r('NA')):
	r.assign('img', img)
	r.assign('indices', indices)
	return r('whitestripe_norm(img=img, indices=indices)')

def ws_img_data(lib_loc = r('NULL'), warn = True):
	r.assign('lib.loc', lib_loc)
	r.assign('warn', warn)
	return r('ws_img_data(lib.loc=lib.loc, warn=warn)')

def xvals():
	return r('xvals')
