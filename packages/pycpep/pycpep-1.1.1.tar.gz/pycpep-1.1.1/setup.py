import setuptools

setuptools.setup(name='pycpep',
        version='1.1.1',
        license='MIT',
        url='https://github.com/nirmalparmarphd/PyCpep',
        description='Predicts deviation in the heat capacity measurement for microDSC Tian-Calvet', 
        long_description='README.md',
        author='Nirmal Parmar',
        author_email='nirmalparmarphd@gmail.com',
        packages=setuptools.find_packages(),
        include_package_data=True,
        package_data={'': ['mdl/*.h5', 'mdl/*.pkl','mdl/*.hdf5']},
        install_requires=['scikit-learn','numpy', 'h5py','keras', 'gitpython', 'pandas','h5py'],
        zip_safe=False)
