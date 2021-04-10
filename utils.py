# Utility functions for getting data, plotting, and stuff
from urllib import request
from collections import namedtuple
from astropy.table import Table
import shutil
import tarfile
import tempfile
import os

data_url="https://storage.googleapis.com/ahw2019/for_malz_and_lanusse.tar.gz"
colors = ["k", "#2ca02c", "tomato", "cornflowerblue", "plum", "gold"]

def load_data(output_dir='dataset'):
  """Retrieves opsim data from the internets if not already available locally
  """
  if not os.path.exists(output_dir):
    # Create a temporary work directory
    temp_path = tempfile.mktemp()
    tar_filename = os.path.join(temp_path, 'archive.tar.gz')

    # Download the archive from the cloud
    request.urlretrieve(data_url, tar_filename)

    # Extract archive
    my_tar = tarfile.open(tar_filename)
    my_tar.extractall(temp_path)

    # Move directory
    shutil.move(os.path.join(temp_path, 'for_malz_and_lanusse'),
                output_dir)

  # Now we can load the data
  all_readme = open(os.path.join(output_dir,'readme.txt')).read().split('\n')
  in_metadata = []
  for i, line in enumerate(all_readme[0:6]):
    descr = all_readme[i+1].split()
    in_metadata.append(descr)

  names_z=('ID', 'z_true', 'z_phot', 'dz_phot', 'NN', 'N_train')
  names_phot=('ID', 'z_true',
    'u', 'err_u', 'g', 'err_g', 'r', 'err_r', 'i', 'err_i', 'z', 'err_z', 'y', 'err_y',
    'u-g', 'err_u-g', 'g-r', 'err_g-r', 'r-i', 'err_r-i', 'i-z', 'err_i-z', 'z-y', 'err_z-y')

  available_os = list(metadata.keys())
  names = [metadata[runid].OpSimName for runid in available_os]
  os_names = dict(zip(available_os, names))
  os_colors = dict(zip(available_os, colors))

  phot_cats, z_cats = {}, {}
  for an_os in available_os:
    one_os = 'run_'+an_os
    test_cat = Table.read(os.path.join(output_dir,one_os+'/test.cat'),
                          format='ascii')

    z_cat = Table.read(os.path.join(output_dir,one_os+'/zphot.cat'),
                         format='ascii',
                         names=names_z)

    phot_cat = Table.read(os.path.join(output_dir,one_os+'/test.cat')
                         format='ascii',
                         names=names_phot)
    phot_cat = Table.from_pandas(phot_cat.to_pandas().dropna())
    phot_cats[an_os] = phot_cat
    limmags = []
    for band in ['u', 'g', 'r', 'i', 'z', 'y']:
      limmags.append(max(phot_cat[band]))
    limmag = metadatum(an_os, os_names[an_os], *limmags)
    z_cats[an_os] = z_cat

  return z_cats, phot_cats, os_names, os_colors
