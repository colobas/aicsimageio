#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List

###############################################################################

# The order of the readers in this impl dict is important.
#
# Example:
# if TiffReader was placed before OmeTiffReader,
# we would never hit the OmeTiffReader

# Additionally while so many formats can be read by base-imageio
# Our custom reader may be more well-suited for interactions
# Example:
# DefaultReader supports LSM, and all the similar "Tiff-Like"
# formats, but TiffReader does as well and it has better
# dask chunking + metadata parsing than DefaultReader for those formats

# BASE-IMAGEIO FORMATS (with tifffile + non-existant removals)
#
# Pulled using:
# from imageio import formats
# routes = {}
# for f in formats:
#   for ext in f.extensions:
#       routes[ext[1:]] = ["aicsimageio.readers.default_reader.DefaultReader"]

FORMAT_IMPLEMENTATIONS: Dict[str, List[str]] = {
    "1sc": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "2fl": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "3fr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "acff": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "acqp": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "afi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "afm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "aim": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "al3d": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ali": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "am": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "amiramesh": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ano": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "apl": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "arf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "array-like": ["aicsimageio.readers.array_like_reader.ArrayLikeReader"],
    "arw": ["aicsimageio.readers.default_reader.DefaultReader"],
    "avi": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "bay": ["aicsimageio.readers.default_reader.DefaultReader"],
    "bif": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "bin": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "bip": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "bmp": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "bmq": ["aicsimageio.readers.default_reader.DefaultReader"],
    "bsdf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "bufr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "bw": ["aicsimageio.readers.default_reader.DefaultReader"],
    "c01": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "cap": ["aicsimageio.readers.default_reader.DefaultReader"],
    "cat": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "cfg": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ch5": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "cif": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "cine": ["aicsimageio.readers.default_reader.DefaultReader"],
    "cr2": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "crw": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "cs1": ["aicsimageio.readers.default_reader.DefaultReader"],
    "csv": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ct": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ct.img": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "cur": ["aicsimageio.readers.default_reader.DefaultReader"],
    "cut": ["aicsimageio.readers.default_reader.DefaultReader"],
    "cxd": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "czi": [
        "aicsimageio.readers.czi_reader.CziReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "dat": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "db": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "dc2": ["aicsimageio.readers.default_reader.DefaultReader"],
    "dcm": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "dcr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "dcx": ["aicsimageio.readers.default_reader.DefaultReader"],
    "dds": ["aicsimageio.readers.default_reader.DefaultReader"],
    "df3": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "dicom": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "dm2": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "dm3": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "dng": ["aicsimageio.readers.default_reader.DefaultReader"],
    "drf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "dsc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "dti": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "dv": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ecw": ["aicsimageio.readers.default_reader.DefaultReader"],
    "emf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "eps": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "epsi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "erf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "exp": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "exr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "fake": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "fdf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "fff": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "ffr": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "fid": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "fit": ["aicsimageio.readers.default_reader.DefaultReader"],
    "fits": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "flc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "flex": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "fli": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "fpx": ["aicsimageio.readers.default_reader.DefaultReader"],
    "frm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ftc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "fts": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ftu": ["aicsimageio.readers.default_reader.DefaultReader"],
    "fz": ["aicsimageio.readers.default_reader.DefaultReader"],
    "g3": ["aicsimageio.readers.default_reader.DefaultReader"],
    "gbr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "gdcm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "gel": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "gif": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "gipl": ["aicsimageio.readers.default_reader.DefaultReader"],
    "grey": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "grib": ["aicsimageio.readers.default_reader.DefaultReader"],
    "h5": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "hdf": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "hdf5": ["aicsimageio.readers.default_reader.DefaultReader"],
    "hdp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "hdr": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "hed": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "his": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "htd": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "htm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "html": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "hx": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "i2i": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ia": ["aicsimageio.readers.default_reader.DefaultReader"],
    "icns": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ico": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ics": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ids": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "iff": ["aicsimageio.readers.default_reader.DefaultReader"],
    "iim": ["aicsimageio.readers.default_reader.DefaultReader"],
    "iiq": ["aicsimageio.readers.default_reader.DefaultReader"],
    "im": ["aicsimageio.readers.default_reader.DefaultReader"],
    "im3": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "img": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "imggz": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ims": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "inf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "inr": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ipl": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "ipm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ipw": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "j2c": ["aicsimageio.readers.default_reader.DefaultReader"],
    "j2k": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "jfif": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jif": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jng": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jp2": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "jpc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jpe": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jpeg": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "jpf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "jpg": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "jpk": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "jpx": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "jxr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "k25": ["aicsimageio.readers.default_reader.DefaultReader"],
    "kc2": ["aicsimageio.readers.default_reader.DefaultReader"],
    "kdc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "klb": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "koa": ["aicsimageio.readers.default_reader.DefaultReader"],
    "l2d": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "labels": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "lbm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "lei": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "lfp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "lfr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "lif": [
        "aicsimageio.readers.lif_reader.LifReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "liff": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "lim": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "lms": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "lsm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mdb": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mdc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mef": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mgh": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mha": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mhd": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mic": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mkv": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mnc": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "mnc2": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mng": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mod": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mos": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mov": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "mp4": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mpeg": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mpg": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mpo": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mrc": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mri": ["aicsimageio.readers.default_reader.DefaultReader"],
    "mrw": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "msp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "msr": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mtb": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "mvd2": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "naf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "nd": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "nd2": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ndpi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ndpis": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "nef": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "nhdr": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "nia": ["aicsimageio.readers.default_reader.DefaultReader"],
    "nii": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "nii.gz": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "niigz": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "npz": ["aicsimageio.readers.default_reader.DefaultReader"],
    "nrrd": [
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "nrw": ["aicsimageio.readers.default_reader.DefaultReader"],
    "obf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "oib": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "oif": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "oir": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ome": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ome.tif": [
        "aicsimageio.readers.ome_tiff_reader.OmeTiffReader",
        "aicsimageio.readers.tiff_reader.TiffReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "ome.tiff": [
        "aicsimageio.readers.ome_tiff_reader.OmeTiffReader",
        "aicsimageio.readers.tiff_reader.TiffReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "orf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "par": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "pbm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pcd": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pcoraw": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "pct": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "pcx": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "pef": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pfm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pgm": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "pic": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "pict": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "png": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "pnl": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ppm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pr3": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "ps": ["aicsimageio.readers.default_reader.DefaultReader"],
    "psd": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "ptx": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pxn": ["aicsimageio.readers.default_reader.DefaultReader"],
    "pxr": ["aicsimageio.readers.default_reader.DefaultReader"],
    "qptiff": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "qtk": ["aicsimageio.readers.default_reader.DefaultReader"],
    "r3d": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "raf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "ras": ["aicsimageio.readers.default_reader.DefaultReader"],
    "raw": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "rcpnl": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "rdc": ["aicsimageio.readers.default_reader.DefaultReader"],
    "rec": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "rgb": ["aicsimageio.readers.default_reader.DefaultReader"],
    "rgba": ["aicsimageio.readers.default_reader.DefaultReader"],
    "rw2": ["aicsimageio.readers.default_reader.DefaultReader"],
    "rwl": ["aicsimageio.readers.default_reader.DefaultReader"],
    "rwz": ["aicsimageio.readers.default_reader.DefaultReader"],
    "scan": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "scn": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sdt": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "seq": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sif": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sld": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sm2": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sm3": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "spc": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "spe": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "spi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sr2": ["aicsimageio.readers.default_reader.DefaultReader"],
    "srf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "srw": ["aicsimageio.readers.default_reader.DefaultReader"],
    "st": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "sti": ["aicsimageio.readers.default_reader.DefaultReader"],
    "stk": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "stp": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "svs": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "swf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "sxm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "targa": ["aicsimageio.readers.default_reader.DefaultReader"],
    "tfr": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "tga": [
        "aicsimageio.readers.default_reader.DefaultReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
    ],
    "thm": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "tif": [
        "aicsimageio.readers.ome_tiff_reader.OmeTiffReader",
        "aicsimageio.readers.tiff_reader.TiffReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "tiff": [
        "aicsimageio.readers.ome_tiff_reader.OmeTiffReader",
        "aicsimageio.readers.tiff_reader.TiffReader",
        "aicsimageio.readers.bioformats_reader.BioformatsReader",
        "aicsimageio.readers.default_reader.DefaultReader",
    ],
    "tim": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "tnb": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "top": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "txt": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "v": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "vff": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "vms": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "vsi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "vtk": ["aicsimageio.readers.default_reader.DefaultReader"],
    "vws": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "wap": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wat": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "wav": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "wbm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wbmp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wdp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "webp": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wlz": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "wmf": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wmv": ["aicsimageio.readers.default_reader.DefaultReader"],
    "wpi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xbm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "xdce": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xml": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xpm": ["aicsimageio.readers.default_reader.DefaultReader"],
    "xqd": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xqf": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xv": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "xys": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "zfp": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "zfr": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "zip": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "zpo": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
    "zvi": ["aicsimageio.readers.bioformats_reader.BioformatsReader"],
}

READER_TO_INSTALL: Dict[str, str] = {
    "aicsimageio.readers.bioformats_reader.BioformatsReader": "bioformats",
    "aicsimageio.readers.default_reader.DefaultReader": "base-imageio",
    "aicsimageio.readers.lif_reader.LifReader": "lif",
    "aicsimageio.readers.czi_reader.CziReader": "czi",
}