#!/usr/bin/env python3
import hashlib
import math

import numpy as np

import artistools as at

modelpath = at.get_config()["path_testartismodel"]
outputpath = at.get_config()["path_testoutput"]


def test_commands():
    import importlib

    # ensure that the commands are pointing to valid submodule.function() targets
    for _command, (submodulename, funcname) in sorted(at.commands.get_commandlist().items()):
        submodule = importlib.import_module(submodulename, package="artistools")
        assert hasattr(submodule, funcname)


def test_timestep_times():
    timestartarray = at.get_timestep_times_float(modelpath, loc="start")
    timedeltarray = at.get_timestep_times_float(modelpath, loc="delta")
    timemidarray = at.get_timestep_times_float(modelpath, loc="mid")
    assert len(timestartarray) == 100
    assert math.isclose(float(timemidarray[0]), 250.421, abs_tol=1e-3)
    assert math.isclose(float(timemidarray[-1]), 349.412, abs_tol=1e-3)

    assert all(
        tstart < tmid < (tstart + tdelta) for tstart, tdelta, tmid in zip(timestartarray, timedeltarray, timemidarray)
    )


def test_deposition():
    at.deposition.main(argsraw=[], modelpath=modelpath)


def test_estimator_snapshot():
    at.estimators.plot(argsraw=[], modelpath=modelpath, outputfile=outputpath, timedays=300)


def test_estimator_timeevolution():
    at.estimators.plot(argsraw=[], modelpath=modelpath, outputfile=outputpath, modelgridindex=0, x="time")


def test_get_inputparams():
    inputparams = at.get_inputparams(modelpath)
    dicthash = hashlib.sha256(str(sorted(inputparams.items())).encode("utf-8")).hexdigest()
    assert dicthash == "ce7d04d6944207673a105cba8d2430055d0b53b7f3e92db3964d2dca285a3adb"


def test_get_levels():
    at.atomic.get_levels(modelpath, get_transitions=True, get_photoionisations=True)


def test_get_modeldata_tuple():
    dfmodel, t_model_init_days, vmax_cmps = at.inputmodel.get_modeldata_tuple(modelpath, get_elemabundances=True)
    assert np.isclose(t_model_init_days, 0.00115740740741, rtol=0.0001)
    assert np.isclose(vmax_cmps, 800000000.0, rtol=0.0001)

    # assert (
    #     hashlib.sha256(pd.util.hash_pandas_object(dfmodel, index=True).values).hexdigest() ==
    #     '40a02dfa933f6b28671d42f3cf69a182955a5a89dc93bbcd22c894192375fe9b')


def test_macroatom():
    at.macroatom.main(argsraw=[], modelpath=modelpath, outputfile=outputpath, timestep=10)


def test_nltepops():
    # at.nltepops.plot(modelpath=modelpath, outputfile=outputpath, timedays=300),
    #                    **benchargs)
    at.nltepops.plot(argsraw=[], modelpath=modelpath, outputfile=outputpath, timestep=40)


def test_nonthermal():
    at.nonthermal.plot(argsraw=[], modelpath=modelpath, outputfile=outputpath, timestep=70)


def test_radfield():
    at.radfield.main(argsraw=[], modelpath=modelpath, modelgridindex=0, outputfile=outputpath)


def test_get_ionrecombratecalibration():
    at.atomic.get_ionrecombratecalibration(modelpath=modelpath)


def test_spencerfano():
    at.nonthermal.solvespencerfanocmd.main(
        argsraw=[], modelpath=modelpath, timedays=300, makeplot=True, npts=200, noexcitation=True, outputfile=outputpath
    )


def test_transitions():
    at.transitions.main(argsraw=[], modelpath=modelpath, outputfile=outputpath, timedays=300)
