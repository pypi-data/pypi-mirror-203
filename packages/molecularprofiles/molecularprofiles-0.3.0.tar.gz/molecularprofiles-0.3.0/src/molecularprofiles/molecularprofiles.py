"""
This is a class that offers a set of functions to work with meteorological data
in ecsv or grib(2) format.

Created by Pere Munar-Adrover
email: pere.munaradrover@gmail.com
Further developed and mainted by
Mykhailo Dalchenko (mykhailo.dalchenko@unige.ch) and
Georgios Voutsinas (georgios.voutsinas@unige.ch)
"""

import os
import logging

import astropy.units as u
from astropy.table import Table
import numpy as np
from scipy.interpolate import interp1d

from molecularprofiles.utils.grib_utils import get_grib_file_data, extend_grib_data
from molecularprofiles.utils.constants import (
    DENSITY_SCALE_HEIGHT,
    N0_AIR,
    STD_GRAVITATIONAL_ACCELERATION,
    STD_AIR_DENSITY,
)

from molecularprofiles.utils.humidity import (
    compressibility,
    density_moist_air,
    molar_fraction_water_vapor,
    partial_pressure_water_vapor,
)
from molecularprofiles.utils.rayleigh import Rayleigh

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
log_config_file = f"{ROOTDIR}/utils/mdps_log.conf"
logging.config.fileConfig(fname=log_config_file, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class MolecularProfile:
    """
    This class provides a series of functions to analyze the quality of the data for both
    CTA-North and CTA-South.

    Methods within this class:

    get_data:                   it retrieves the data from the input file. If the input file
                                is a grib file and there is no file in the working directory
                                with the same name but with .txt extension the program extracts
                                the data from the grib file through the grib_utils program. If
                                there is such a txt file, it reads it directly
    write_corsika:              prints the data into a txt file which format is compliant with the input card
                                for the CORSIKA air shower simulation software
    create_mdp:                 creates an altitude profile of the molecular number density
    rayleigh_extinction:        creates a file, in format to be directly fed to simtel simulation, with the
                                extinction per altitude bin for wavelengths from 200 to 1000 nm
    """

    def __init__(self, data_file, data_server="server", observatory="north"):
        """
        Constructor

        :param data_file: txt file containing the data (string)
        :param data_server: label to be put in some of the output plots (string)
        :param observatory: valid options are: "north", "south", "other"

        """

        self.data_file = data_file
        self.data_server = data_server
        self.observatory = observatory

    # =============================================================================================================
    # Private functions
    # =============================================================================================================
    def _interpolate_cubic(self, x_param, y_param, new_x_param):
        func = interp1d(x_param, y_param, kind="cubic", fill_value="extrapolate")
        return func(new_x_param)

    def _interpolate_param_to_h(self, param, height):
        logger.error("Not implemented")
        raise NotImplementedError
        # interpolated_param = []
        # group_mjd = self.dataframe.groupby("MJD")

        # logger.info("Computing the extrapolation of the values of density:")
        # logger.info("(This is to make it easier to compare ECMWF and GDAS, or any other")
        # logger.info("weather model)")

        # for mjd in self.dataframe.MJD.unique():
        #     h_at_mjd = group_mjd.get_group(mjd)["h"].tolist()
        #     param_at_mjd = group_mjd.get_group(mjd)[param].tolist()
        #     func = interp1d(h_at_mjd, param_at_mjd, kind="cubic", fill_value="extrapolate")

        #     if isinstance(height, int) or isinstance(height, float):
        #         interpolated_param.append(np.float(func(height)))
        #     else:
        #         interpolated_param.append(func(height))
        # interpolated_param = np.array(interpolated_param)
        # if isinstance(height, float) or isinstance(height, int):
        #     interpolated_param = np.array(interpolated_param)
        #     return interpolated_param
        # else:
        #     interpolated_param_avgs = compute_averages_std(interpolated_param)
        #     return (
        #         interpolated_param,
        #         interpolated_param_avgs[0],
        #         interpolated_param_avgs[1],
        #         interpolated_param_avgs[2],
        #         interpolated_param_avgs[3],
        #     )

    def _compute_mass_density(self, air="moist", co2_concentration=415):
        """
        Computes regular and exponential mass density of air.

        Adds to data the following columns:
        - 'Xw': molar fraction of water vapor (0 if air is dry)
        - 'Compressibility'
        - 'Mass Density'
        - 'Exponential Mass Density'

        Parameters
        ----------
        air : str
            Type of air, can be 'moist' or 'dry'
        co2_concentration : float
            CO2 volume concentration in ppmv
        """

        if air == "moist":
            self.data["Xw"] = molar_fraction_water_vapor(
                self.data["Pressure"], self.data["Temperature"], self.data["Relative humidity"]
            )
        elif air == "dry":
            self.data["Xw"] = 0.0
        else:
            raise ValueError("Wrong air condition. It must be 'moist' or 'dry'.")

        self.data["Compressibility"] = compressibility(
            self.data["Pressure"], self.data["Temperature"], self.data["Xw"]
        )
        self.data["Mass Density"] = density_moist_air(
            self.data["Pressure"],
            self.data["Temperature"],
            self.data["Compressibility"],
            self.data["Xw"],
            co2_concentration,
        )
        self.data["Exponential Mass Density"] = (
            self.data["Mass Density"] / STD_AIR_DENSITY
        ).decompose() * np.exp((self.data["Altitude"] / DENSITY_SCALE_HEIGHT).decompose())

    # =============================================================================================================
    # Main get data function
    # =============================================================================================================
    def get_data(self):
        """
        Reads ECMWF or GDAS data in ecsv or grib(2) format
        and computes statistical description of the data
        """
        file_ext = os.path.splitext(self.data_file)[1]
        if file_ext == ".grib" or file_ext == ".grib2":
            self.data = get_grib_file_data(self.data_file)
            self.data = extend_grib_data(self.data)
        elif file_ext == ".ecsv":
            self.data = Table.read(self.data_file, format="ascii.ecsv")
        else:
            raise NotImplementedError(
                f"Only grib (1,2) and ecsv formats are supported at the moment. Requested format: {file_ext}"
            )
        self.stat_columns = [
            "Pressure",
            "Altitude",
            "Density",
            "Temperature",
            "Wind Speed",
            "Wind Direction",
            "Relative humidity",
            "Exponential Density",
        ]
        self.stat_data = self.data[self.stat_columns].group_by("Pressure")
        self.stat_description = {
            "avg": self.stat_data.groups.aggregate(np.mean),
            "std": self.stat_data.groups.aggregate(np.std),
            "mad": self.stat_data.groups.aggregate(lambda x: np.mean(np.absolute(x - np.mean(x)))),
            "p2p_max": self.stat_data.groups.aggregate(lambda x: np.max(x) - np.mean(x)),
            "p2p_min": self.stat_data.groups.aggregate(lambda x: np.mean(x) - np.min(x)),
        }

    def _refractive_index(self, P, T, RH, wavelength, C):
        """Wrapper for Rayleigh.calculate_n()."""
        rayleigh = Rayleigh(wavelength, C, P, T, RH)
        return rayleigh.refractive_index

    # =======================================================================================================
    # printing functions:
    # =======================================================================================================

    def write_corsika(self, outfile, co2_concentration):
        """
        Write an output file in the style of a CORSIKA atmospheric configuration file:

        alt (km)     rho (g/cm^3)   thick (g/cm^2)   (n-1)
        """
        height = np.arange(0.0, 27000.0, 1000) * u.m
        temperature = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Temperature"],
                height,
            )
            * self.stat_description["avg"]["Temperature"].unit
        )
        relative_humidity = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Relative humidity"],
                height,
            )
            * self.stat_description["avg"]["Relative humidity"].unit
        )
        pressure = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Pressure"],
                height,
            )
            * self.stat_description["avg"]["Pressure"].unit
        )
        thickness = pressure / STD_GRAVITATIONAL_ACCELERATION
        density = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Density"],
                height,
            )
            * self.stat_description["avg"]["Density"].unit
            / N0_AIR
        )
        rel_water_vapor_pressure = (
            partial_pressure_water_vapor(temperature, relative_humidity) / pressure
        ).decompose()
        rel_refractive_index = (
            self._refractive_index(
                pressure, temperature, relative_humidity, 350.0 * u.nm, co2_concentration
            )
            - 1.0
        )

        with open(outfile, "w") as f:

            f.write("# Atmospheric Model ECMWF year/month/day   hour h\n")  # .format(**datedict))
            f.write(
                "#Col. #1          #2           #3            #4        [ #5 ]        [ #6 ]       [ # 7 ]\n"
            )
            f.write(
                "# Alt [km]    rho [g/cm^3] thick [g/cm^2]    n-1        T [k]       p [mbar]      pw / p\n"
            )

            for i in np.arange(len(height)):

                outdict = {
                    "height": height[i].to_value(u.km),
                    "rho": density[i].to_value(u.g / u.cm**3),
                    "thick": thickness[i].to_value(u.g / u.cm**2),
                    "nm1": rel_refractive_index[i],
                    "T": temperature[i].to_value(u.K),
                    "p": pressure[i].to_value(u.mbar),
                    "pw/p": rel_water_vapor_pressure[i],
                }
                f.write(
                    "  {height:7.3f}     {rho:5.5E}  {thick:5.5E}  {nm1:5.5E}  {T:5.5E}  {p:5.5E}  {pw/p:5.5E}\n".format(
                        **outdict
                    )
                )

            # concatenate the dummy values of MagicWinter starting from 50.0 km
            f.write(
                "   27.000     2.96567e-05  1.96754e+01  6.84513e-06  223.70  1.90428e+01  0.00000e+00\n"
            )

            f.write(
                "   28.000     2.52913e-05  1.69341e+01  5.83752e-06  225.69  1.63842e+01  0.00000e+00\n"
            )

            f.write(
                "   29.000     2.15935e-05  1.45949e+01  4.98403e-06  227.75  1.41164e+01  0.00000e+00\n"
            )

            f.write(
                "   30.000     1.84554e-05  1.25967e+01  4.25972e-06  229.92  1.21798e+01  0.00000e+00\n"
            )

            f.write(
                "   32.000     1.35171e-05  9.42594e+00  3.11990e-06  234.75  9.10824e+00  0.00000e+00\n"
            )

            f.write(
                "   34.000     9.93769e-06  7.09977e+00  2.29374e-06  240.36  6.85638e+00  0.00000e+00\n"
            )

            f.write(
                "   36.000     7.35111e-06  5.38483e+00  1.69672e-06  246.30  5.19717e+00  0.00000e+00\n"
            )

            f.write(
                "   38.000     5.47808e-06  4.11190e+00  1.26441e-06  252.24  3.96630e+00  0.00000e+00\n"
            )

            f.write(
                "   40.000     4.11643e-06  3.15961e+00  9.50121e-07  257.79  3.04599e+00  0.00000e+00\n"
            )

            f.write(
                "   42.000     3.12126e-06  2.44097e+00  7.20424e-07  262.51  2.35189e+00  0.00000e+00\n"
            )

            f.write(
                "   44.000     2.38908e-06  1.89362e+00  5.51429e-07  265.91  1.82354e+00  0.00000e+00\n"
            )

            f.write(
                "   46.000     1.84598e-06  1.47276e+00  4.26075e-07  267.52  1.41753e+00  0.00000e+00\n"
            )

            f.write(
                "   48.000     1.43779e-06  1.14626e+00  3.31858e-07  267.20  1.10275e+00  0.00000e+00\n"
            )

            f.write(
                "   50.000     1.09738e-06  8.72656e-01   2.53289e-07   266.34   8.38955e-01  0.00000e+00\n"
            )
            f.write(
                "   55.000     5.99974e-07  4.61036e-01   1.38481e-07   257.19   4.42930e-01  0.00000e+00\n"
            )
            f.write(
                "   60.000     3.25544e-07  2.36175e-01   7.51395e-08   242.81   2.26896e-01  0.00000e+00\n"
            )
            f.write(
                "   65.000     1.70152e-07  1.15918e-01   3.92732e-08   227.93   1.11324e-01  0.00000e+00\n"
            )
            f.write(
                "   70.000     8.43368e-08  5.45084e-02   1.94660e-08   215.90   5.22651e-02  0.00000e+00\n"
            )
            f.write(
                "   75.000     3.95973e-08  2.48012e-02   9.13953e-09   208.66   2.37169e-02  0.00000e+00\n"
            )
            f.write(
                "   80.000     1.79635e-08  1.10899e-02   4.14618e-09   205.11   1.05760e-02  0.00000e+00\n"
            )
            f.write(
                "   85.000     8.03691e-09  4.91583e-03   1.85502e-09   202.12   4.66284e-03  0.00000e+00\n"
            )
            f.write(
                "   90.000     3.59602e-09  2.15599e-03   8.30003e-10   196.26   2.02583e-03  0.00000e+00\n"
            )
            f.write(
                "   95.000     1.59871e-09  9.21029e-04   3.69000e-10   187.55   8.60656e-04  0.00000e+00\n"
            )
            f.write(
                "  100.000     6.73608e-10  3.82814e-04   1.55477e-10   185.38   3.58448e-04  0.00000e+00\n"
            )
            f.write(
                "  105.000     2.69097e-10  1.61973e-04   6.21108e-11   197.19   1.52311e-04  0.00000e+00\n"
            )
            f.write(
                "  110.000     1.09021e-10  7.37110e-05   2.51634e-11   224.14   7.01416e-05  0.00000e+00\n"
            )
            f.write(
                "  115.000     4.71300e-11  3.70559e-05   1.08782e-11   268.51   3.63251e-05  0.00000e+00\n"
            )
            f.write(
                "  120.000     2.23479e-11  2.05900e-05   5.15817e-12   333.43   2.13890e-05  0.00000e+00\n"
            )

    def create_mdp(self, mdp_file):
        """
        Write an output file with the molecular number density per height
        """

        heights = (
            np.arange(0.0, 27000.0, 1000) * u.m
        )  # FIXME: The hardcoded value 27 reflects the current ceiling of GDAS data (26km a.s.l.). Shouldn't be hardcoded and in general the binning and limits should be considered.
        with open(mdp_file, "w") as f:

            number_density = (
                self._interpolate_cubic(
                    self.stat_description["avg"]["Altitude"],
                    self.stat_description["avg"]["Density"],
                    heights,
                )
                * self.stat_description["avg"]["Density"].unit
            )
            for i, height in enumerate(heights):
                file_line = [str(height), "\t", str(number_density[i]), "\n"]
                f.writelines(file_line)

    def rayleigh_extinction(self, rayleigh_extinction_file, co2_concentration):
        """
        Calculates the integral optical depth due to Rayleigh scattering
        per altitude bins as a function of wavelength.
        The optical depth (AOD) for an altitude h over the observatory will be given by
        the integral of the monochromatic volume coefficient beta, with integration limits
        h_obs up to h.

        returns:
        --------
            File with integral optical depth per height bin per wavelength bin. The format is the same with MODTRAN files.
        """

        # For now we work for La Palma site. We will most probably have to find an average
        # altitude for each site. h_obs should become an attribute of observatory class.
        height_obs = 2158
        height = (
            np.array(
                [
                    height_obs,
                    2258,
                    2358,
                    2458,
                    2658,
                    2858,
                    3158,
                    3658,
                    4158,
                    4500,
                    5000,
                    5500,
                    6000,
                    7000,
                    8000,
                    9000,
                    10000,
                    11000,
                    12000,
                    13000,
                    14000,
                    15000,
                    16000,
                    18000,
                    20000,
                    22000,
                    24000,
                    26000,
                ]
            )
            * u.m
        )
        # and here's the big question, still unanswered. What do we do with the altitudes that DAS values do not exist?
        # , 28.000, 30.000, 32.500, 35.000, 37.500, 40.000, 45.000, 50.000, 60.000, 70.000, 80.000, 100.000 ]
        bin_widths = np.diff(height)
        bin_centers = (height[:-1] + height[1:]) / 2

        temperature = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Temperature"],
                bin_centers,
            )
            * self.stat_description["avg"]["Temperature"].unit
        )
        relative_humidity = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Relative humidity"],
                bin_centers,
            )
            * self.stat_description["avg"]["Relative humidity"].unit
        )
        pressure = (
            self._interpolate_cubic(
                self.stat_description["avg"]["Altitude"],
                self.stat_description["avg"]["Pressure"],
                bin_centers,
            )
            * self.stat_description["avg"]["Pressure"].unit
        )
        wavelength_range = np.arange(200, 1001, 1) * u.nm

        # Here is a schoolkid's, homemade numerical integration. Though it gives reasonable results.
        with open(rayleigh_extinction_file, "w") as f:
            for wavelength in wavelength_range:
                aod = 0
                file_line = [str(wavelength.to(u.nm)).split(" ")[0], "\t"]
                for P, T, RH, dh in zip(pressure, temperature, relative_humidity, bin_widths):
                    rayleigh = Rayleigh(wavelength, co2_concentration, P, T, RH)
                    beta = rayleigh.beta
                    aod += dh * beta
                    file_line += [f"{aod:.6f}", "\t"]
                file_line += ["\n"]
                f.writelines(file_line)

        return rayleigh_extinction_file
