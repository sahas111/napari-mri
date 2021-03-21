"""
This is a simple napari plugin for 3D-viewing of nifty files
(.nii.gz) - a common MRI file format.
"""

from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_reader(path):
    if isinstance(path, list):
        path = path[0]
    if not path.endswith(".nii.gz"):
        return None
    return MRI_reader


def MRI_reader(path):
    """Given a single path, returns a tuple [(data, metadata)]"""
    import numpy as np
    import nibabel as nib
    # Read a .nii file and header info including voxel spacing
    img_file = nib.load(path)
    img_data = img_file.get_fdata()
    # sagittal view
    img_sag_reversed = (img_data[:, :, ::-1])
    img_sag_final = (np.transpose(img_sag_reversed, (0, 2, 1)))
    # save the sagittal MRI file and view other planes (coronal and axial)
    # by the roll-dimension button
    data = img_sag_final
    # Read and store the image header information
    metadata = {
        name: img_file.header[name]
        for name in img_file.header.keys()
    }
    params = {
        "metadata": metadata,
    }
    return [(data, params)]
