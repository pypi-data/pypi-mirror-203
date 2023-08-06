I3D_Feature_Extraction
======================

Hello, I am Hao Vy Phan. I have develop this package using ResNet-50 to
convert a video into an extracted i3D features numpy file.

Overview
--------

**Input**: a directory which store 1 or more videos.

**Output**: 1 or many ``.npy`` files (extracted i3D features). Each
features file is shaped ``n/16 * 2048`` where ``n`` is the number of
frames in the video

If there is a problem installing or implementing this package, please do
not hesitate to contact me via my email. I am pleased to have people use
my product.

--------------

Usage
-----

Installation
~~~~~~~~~~~~

Before installing my package, please install these pakages:

\*
`Opencv-Python==4.5.5 <https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv>`__

\*
`torch==1.10.1+cu113 <https://download.pytorch.org/whl/cu113/torch-1.10.1%2Bcu113-cp38-cp38-win_amd64.whl>`__

\*
`torchaudio==0.10.1+cu113 <https://download.pytorch.org/whl/cu113/torchaudio-0.10.1%2Bcu113-cp38-cp38-win_amd64.whl>`__

\*
`torchvision==0.11.2+cu113 <https://download.pytorch.org/whl/cu113/torchvision-0.11.2%2Bcu113-cp38-cp38-win_amd64.whl>`__

\* Or find your own python OS version of torch from this link:
https://download.pytorch.org/whl/cu113/torch_stable.html

Installing them through ``pip install`` may raise errors. You can
download the wheel files from the above links and run this code:

.. code:: commandline

   pip install torchvision-0.11.2+cu113-cp38-cp38-win_amd64.whl
   pip install torchaudio-0.10.1+cu113-cp38-cp38-win_amd64.whl
   pip install torch-1.10.1+cu113-cp38-cp38-win_amd64.whl
   pip install opencv_python-4.5.5-cp38-cp38-win_amd64.whl


After 4 above packages, to install ``i3dFeatureExtraction`` package into
your Python environment, run this code on your terminal:

.. code:: commandline

   pip install i3dFeatureExtraction

Or install a specific version:

.. code:: commandline

   pip install i3dFeatureExtraction==x.x.x

Implementing
~~~~~~~~~~~~

The main function of this package is ``FeatureExtraction`` which
converts a directory of videos into numpy feature files.

.. code:: python

   from i3dFeatureExtraction import FeatureExtraction
   FeatureExtraction.generate(
       outputpath = "directory/to/store/output/numpy/files",
       datasetpath="directory/of/input/videos",
       pretrainedpath = "path/to/i3D/pretrained/weight",
       sample_mode = "oversample/center_crop"
   )

--------------
Structure
--------------

I am not good at drawing UML diagram but I hope this image helps illustrate the package's structure.

.. image:: https://vyhaoromanletters.s3.us-east-2.amazonaws.com/i3dExtract.png
   :alt: i3dFeatureExtraction - UML Diagram

Credits
-----------

This code is based on the following repositories:

\*
`pytorch-resnet3d <https://github.com/Tushar-N/pytorch-resnet3d>`__

\*
`pytorch-i3d-feature-extraction <https://github.com/Finspire13/pytorch-i3d-feature-extraction>`__

\*
`E2E-Action-Segmentation/feature_extraction/ <https://github.com/nguyenphwork/E2E-Action-Segmentation/tree/main/feature_extraction>`__

I would like to extend a special thank-you to the original authors of
these repositories for providing the foundation on which this
implementation is built.


