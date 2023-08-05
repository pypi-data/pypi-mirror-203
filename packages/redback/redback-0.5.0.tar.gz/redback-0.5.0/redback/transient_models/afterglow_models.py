from astropy.cosmology import Planck18 as cosmo  # noqa
from inspect import isfunction
from redback.utils import logger, citation_wrapper, calc_ABmag_from_flux_density, lambda_to_nu
from redback.constants import day_to_s
from redback.sed import get_correct_output_format_from_spectra
import astropy.units as uu
import numpy as np
from collections import namedtuple
try:
    import afterglowpy as afterglow

    jettype_dict = {'tophat': afterglow.jet.TopHat, 'gaussian': afterglow.jet.Gaussian,
                    'powerlaw_w_core': afterglow.jet.PowerLawCore, 'gaussian_w_core': afterglow.jet.GaussianCore,
                    'cocoon': afterglow.Spherical, 'smooth_power_law': afterglow.jet.PowerLaw,
                    'cone': afterglow.jet.Cone}
    spectype_dict = {'no_inverse_compton': 0, 'inverse_compton': 1}
except ModuleNotFoundError as e:
    logger.warning(e)
    afterglow = None

jet_spreading_models = ['tophat', 'cocoon', 'gaussian',
                          'kn_afterglow', 'cone_afterglow',
                          'gaussiancore', 'gaussian',
                          'smoothpowerlaw', 'powerlawcore',
                          'tophat']

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def cocoon(time, redshift, umax, umin, loge0, k, mej, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A cocoon afterglow model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param umax: initial outflow 4 velocity maximum
    :param umin: minimum outflow 4 velocity
    :param loge0: log10 fidicial energy in velocity distribution E(>u) = E0u^-k in erg
    :param k: power law index of energy velocity distribution
    :param mej: mass of material at umax in solar masses
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['cocoon']
    frequency = kwargs['frequency']
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'uMax': umax, 'Er': e0,
         'uMin': umin, 'k': k, 'MFast_solar': mej, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def kilonova_afterglow(time, redshift, umax, umin, loge0, k, mej, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A kilonova afterglow model from afterglowpy, similar to cocoon but with constraints.

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param umax: initial outflow 4 velocity maximum
    :param umin: minimum outflow 4 velocity
    :param loge0: log10 fidicial energy in velocity distribution E(>u) = E0u^-k in erg
    :param k: power law index of energy velocity distribution
    :param mej: mass of material at umax in solar masses
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    output = cocoon(time=time, redshift=redshift, umax=umax, umin=umin, loge0=loge0,
                    k=k, mej=mej, logn0=logn0,p=p,logepse=logepse,logepsb=logepsb,
                    ksin=ksin, g0=g0, **kwargs)
    return output

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def cone_afterglow(time, redshift, thv, loge0, thw, thc, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A cone afterglow model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thw: wing truncation angle of jet thw = thw*thc
    :param thc: half width of jet core in radians
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :param base_model: A string to indicate the type of jet model to use.
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['cone']
    frequency = kwargs['frequency']
    thw = thw * thc
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres, 'thetaWing': thw}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def gaussiancore(time, redshift, thv, loge0, thc, thw, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A gaussiancore model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thw: wing truncation angle of jet thw = thw*thc
    :param thc: half width of jet core in radians
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['gaussian_w_core']
    frequency = kwargs['frequency']

    thw = thw * thc
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres, 'thetaWing': thw}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def gaussian(time, redshift, thv, loge0, thw, thc, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A gaussian structured jet model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thw: wing truncation angle of jet thw = thw*thc
    :param thc: half width of jet core in radians
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['gaussian']
    frequency = kwargs['frequency']
    thw = thw * thc
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres, 'thetaWing': thw}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def smoothpowerlaw(time, redshift, thv, loge0, thw, thc, beta, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A smoothpowerlaw structured jet model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thw: wing truncation angle of jet thw = thw*thc
    :param thc: half width of jet core in radians
    :param beta: index for power-law structure, theta^-b
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['smooth_power_law']
    frequency = kwargs['frequency']
    thw = thw * thc
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres, 'thetaWing': thw, 'b': beta}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def powerlawcore(time, redshift, thv, loge0, thw, thc, beta, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A power law with core structured jet model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thw: wing truncation angle of jet thw = thw*thc
    :param thc: half width of jet core in radians
    :param beta: index for power-law structure, theta^-b
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['powerlaw_w_core']
    frequency = kwargs['frequency']
    thw = thw * thc
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb

    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres, 'thetaWing': thw, 'b': beta}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def tophat(time, redshift, thv, loge0, thc, logn0, p, logepse, logepsb, ksin, g0, **kwargs):
    """
    A tophat jet model from afterglowpy

    :param time: time in days in observer frame
    :param redshift: source redshift
    :param thv: viewing angle in radians
    :param loge0: log10 on axis isotropic equivalent energy
    :param thc: half width of jet core/jet opening angle in radians
    :param beta: index for power-law structure, theta^-b
    :param logn0: log10 number density of ISM in cm^-3
    :param p: electron distribution power law index. Must be greater than 2.
    :param logepse: log10 fraction of thermal energy in electrons
    :param logepsb: log10 fraction of thermal energy in magnetic field
    :param ksin: fraction of electrons that get accelerated
    :param g0: initial lorentz factor
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models. assuming a monochromatic
    """
    time = time * day_to_s
    dl = cosmo.luminosity_distance(redshift).cgs.value
    spread = kwargs.get('spread', False)
    latres = kwargs.get('latres', 2)
    tres = kwargs.get('tres', 100)
    spectype = kwargs.get('spectype', 0)
    l0 = kwargs.get('L0', 0)
    q = kwargs.get('q', 0)
    ts = kwargs.get('ts', 0)
    jettype = jettype_dict['tophat']
    frequency = kwargs['frequency']
    e0 = 10 ** loge0
    n0 = 10 ** logn0
    epse = 10 ** logepse
    epsb = 10 ** logepsb
    Z = {'jetType': jettype, 'specType': spectype, 'thetaObs': thv, 'E0': e0,
         'thetaCore': thc, 'n0': n0, 'p': p, 'epsilon_e': epse, 'epsilon_B': epsb,
         'xi_N': ksin, 'd_L': dl, 'z': redshift, 'L0': l0, 'q': q, 'ts': ts, 'g0': g0,
         'spread': spread, 'latRes': latres, 'tRes': tres}
    flux_density = afterglow.fluxDensity(time, frequency, **Z)
    if kwargs['output_format'] == 'flux_density':
        return flux_density
    elif kwargs['output_format'] == 'magnitude':
        return calc_ABmag_from_flux_density(flux_density).value

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def afterglow_models_with_energy_injection(time, **kwargs):
    """
    A base class for afterglowpy models with energy injection.
    :param time: time in days in observer frame
    :param kwargs: Additional keyword arguments
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :param base_model: A string to indicate the type of jet model to use.
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    from redback.model_library import modules_dict  # import model library in function to avoid circular dependency
    base_model = kwargs['base_model']
    if isfunction(base_model):
        function = base_model
    elif base_model not in jet_spreading_models:
        logger.warning('{} is not implemented as a base model'.format(base_model))
        raise ValueError('Please choose a different base model')
    elif isinstance(base_model, str):
        function = modules_dict['afterglow_models'][base_model]
    else:
        raise ValueError("Not a valid base model.")
    kwargs['ts'] = kwargs['ts'] * day_to_s
    kwargs['spread'] = True
    output = function(time, **kwargs)
    return output

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def afterglow_models_with_jet_spread(time, **kwargs):
    """
    A base class for afterglow models with jet spreading. Note, with these models you cannot sample in g0.

    :param time: time in days in observer frame
    :param kwargs: Additional keyword arguments
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param l0, ts, q: energy injection parameters, defaults to 0
    :param output_format: Whether to output flux density or AB mag
    :param base_model: A string to indicate the type of jet model to use.
    :return: flux density or AB mag. Note this is going to give the monochromatic magnitude at the effective frequency for the band.
    For a proper calculation of the magntitude use the sed variant models.
    """
    from redback.model_library import modules_dict  # import model library in function to avoid circular dependency
    base_model = kwargs['base_model']
    if isfunction(base_model):
        function = base_model
    elif base_model not in jet_spreading_models:
        logger.warning('{} is not implemented as a base model'.format(base_model))
        raise ValueError('Please choose a different base model')
    elif isinstance(base_model, str):
        function = modules_dict['afterglow_models'][base_model]
    else:
        raise ValueError("Not a valid base model.")
    kwargs['spread'] = True
    kwargs.pop('g0')
    output = function(time, **kwargs)
    return output

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020ApJ...896..166R/abstract')
def afterglow_models_sed(time, **kwargs):
    """
    A base class for afterglowpy models for bandpass magnitudes/flux/spectra/sncosmo source.

    :param time: time in days in observer frame
    :param kwargs: Additional keyword arguments, must be all parameters required by the base model and the following:
    :param base_model: A string to indicate the type of jet model to use.
    :param spread: whether jet can spread, defaults to False
    :param latres: latitudinal resolution for structured jets, defaults to 2
    :param tres: time resolution of shock evolution, defaults to 100
    :param spectype: whether to have inverse compton, defaults to 0, i.e., no inverse compton.
    Change to 1 for including inverse compton emission.
    :param bands: Required if output_format is 'magnitude' or 'flux'.
    :param output_format: 'magnitude', 'spectra', 'flux', 'sncosmo_source'
    :param lambda_array: Optional argument to set your desired wavelength array (in Angstroms) to evaluate the SED on.
    :return: set by output format - 'magnitude', 'spectra', 'flux', 'sncosmo_source'
    """
    from redback.model_library import modules_dict  # import model library in function to avoid circular dependency
    base_model = kwargs['base_model']
    if isfunction(base_model):
        function = base_model
    elif base_model not in jet_spreading_models:
        logger.warning('{} is not implemented as a base model'.format(base_model))
        raise ValueError('Please choose a different base model')
    elif isinstance(base_model, str):
        function = modules_dict['afterglow_models'][base_model]
    else:
        raise ValueError("Not a valid base model.")
    temp_kwargs = kwargs.copy()
    temp_kwargs['spread'] = kwargs.get('spread', False)
    lambda_observer_frame = kwargs.get('lambda_array', np.geomspace(100, 60000, 200))
    frequency = lambda_to_nu(lambda_observer_frame)
    time_observer_frame = np.linspace(0, np.max(time), 300)
    times_mesh, frequency_mesh = np.meshgrid(time_observer_frame, frequency)
    temp_kwargs['frequency'] = frequency_mesh
    temp_kwargs['output_format'] = 'flux_density'
    output = function(times_mesh, **temp_kwargs).T
    fmjy = output * uu.mJy
    spectra = fmjy.to(uu.mJy).to(uu.erg / uu.cm ** 2 / uu.s / uu.Angstrom,
                                 equivalencies=uu.spectral_density(wav=lambda_observer_frame * uu.Angstrom))
    if kwargs['output_format'] == 'spectra':
        return namedtuple('output', ['time', 'lambdas', 'spectra'])(time=time_observer_frame,
                                                                    lambdas=lambda_observer_frame,
                                                                    spectra=spectra)
    else:
        return get_correct_output_format_from_spectra(time=time, time_eval=time_observer_frame,
                                                      spectra=spectra, lambda_array=lambda_observer_frame,
                                                      **kwargs)


