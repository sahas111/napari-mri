# -*- coding: utf-8 -*-
from napari_mri.nifty_reader import napari_get_reader


def test_get_reader_hit():
    reader = napari_get_reader('fake.nii.gz')
    assert reader is not None
    assert callable(reader)


def test_get_reader_pass():
    reader = napari_get_reader('fake.file')
    assert reader is None
