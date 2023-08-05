# -*- coding: utf-8 -*-

__author__ = "Giovani Hidalgo Ceotto, Franz Masatoshi Yuri, Mateus Stano Junqueira, Kaleb Ramos Wanderley, Calebe Gomes Teles, Matheus Doretto"
__copyright__ = "Copyright 20XX, RocketPy Team"
__license__ = "MIT"

import warnings
from inspect import getsourcelines
from collections import namedtuple
from inspect import getsourcelines

import numpy as np

from .Function import Function
from .Parachute import Parachute
from .AeroSurfaces import NoseCone, TrapezoidalFins, EllipticalFins, Tail


class Rocket:

    """Keeps all rocket and parachute information.

    Attributes
    ----------
        Geometrical attributes:
        Rocket.radius : float
            Rocket's largest radius in meters.
        Rocket.area : float
            Rocket's circular cross section largest frontal area in squared
            meters.
        Rocket.distanceRocketNozzle : float
            Distance between rocket's center of mass, without propellant,
            to the exit face of the nozzle, in meters. Always positive.
        Rocket.distanceRocketPropellant : float
            Distance between rocket's center of mass, without propellant,
            to the motor reference point, which for solid and hybrid motors
            is the center of mass of solid propellant, in meters. Always positive.

        Mass and Inertia attributes:
        Rocket.mass : float
            Rocket's mass without propellant in kg.
        Rocket.inertiaI : float
            Rocket's moment of inertia, without propellant, with respect to
            to an axis perpendicular to the rocket's axis of cylindrical
            symmetry, in kg*m^2.
        Rocket.inertiaZ : float
            Rocket's moment of inertia, without propellant, with respect to
            the rocket's axis of cylindrical symmetry, in kg*m^2.
        Rocket.centerOfMass : Function
            Distance of the rocket's center of mass, including propellant,
            to rocket's center of mass without propellant, in meters.
            Expressed as a function of time.
        Rocket.reducedMass : Function
            Function of time expressing the reduced mass of the rocket,
            defined as the product of the propellant mass and the mass
            of the rocket without propellant, divided by the sum of the
            propellant mass and the rocket mass.
        Rocket.totalMass : Function
            Function of time expressing the total mass of the rocket,
            defined as the sum of the propellant mass and the rocket
            mass without propellant.
        Rocket.thrustToWeight : Function
            Function of time expressing the motor thrust force divided by rocket
            weight. The gravitational acceleration is assumed as 9.80665 m/s^2.

        Eccentricity attributes:
        Rocket.cpEccentricityX : float
            Center of pressure position relative to center of mass in the x
            axis, perpendicular to axis of cylindrical symmetry, in meters.
        Rocket.cpEccentricityY : float
            Center of pressure position relative to center of mass in the y
            axis, perpendicular to axis of cylindrical symmetry, in meters.
        Rocket.thrustEccentricityY : float
            Thrust vector position relative to center of mass in the y
            axis, perpendicular to axis of cylindrical symmetry, in meters.
        Rocket.thrustEccentricityX : float
            Thrust vector position relative to center of mass in the x
            axis, perpendicular to axis of cylindrical symmetry, in meters.

        Aerodynamic attributes
        Rocket.aerodynamicSurfaces : list
            List of aerodynamic surfaces of the rocket.
        Rocket.staticMargin : float
            Float value corresponding to rocket static margin when
            loaded with propellant in units of rocket diameter or
            calibers.
        Rocket.powerOffDrag : Function
            Rocket's drag coefficient as a function of Mach number when the
            motor is off.
        Rocket.powerOnDrag : Function
            Rocket's drag coefficient as a function of Mach number when the
            motor is on.

        Motor attributes:
        Rocket.motor : Motor
            Rocket's motor. See Motor class for more details.
    """

    def __init__(
        self,
        motor,
        mass,
        inertiaI,
        inertiaZ,
        radius,
        distanceRocketNozzle,
        distanceRocketPropellant,
        powerOffDrag,
        powerOnDrag,
    ):
        """Initializes Rocket class, process inertial, geometrical and
        aerodynamic parameters.

        Parameters
        ----------
        motor : Motor
            Motor used in the rocket. See Motor class for more information.
        mass : int, float
            Unloaded rocket total mass (without propellant) in kg.
        inertiaI : int, float
            Unloaded rocket lateral (perpendicular to axis of symmetry)
            moment of inertia (without propellant) in kg m^2.
        inertiaZ : int, float
            Unloaded rocket axial moment of inertia (without propellant)
            in kg m^2.
        radius : int, float
            Rocket largest outer radius in meters.
        distanceRocketNozzle : int, float
            Distance from rocket's unloaded center of mass to nozzle outlet,
            in meters. Generally negative, meaning a negative position in the
            z axis which has an origin in the rocket's center of mass (without
            propellant) and points towards the nose cone.
        distanceRocketPropellant : int, float
            Distance from rocket's unloaded center of mass to the motor reference
            point, which for solid and hybrid motor the is the center of mass of
            solid propellant, in meters. Generally negative, meaning a negative
            position in the z axis which has an origin in the rocket's center of
            mass (with out propellant) and points towards the nose cone.
        powerOffDrag : int, float, callable, string, array
            Rocket's drag coefficient when the motor is off. Can be given as an
            entry to the Function class. See help(Function) for more
            information. If int or float is given, it is assumed constant. If
            callable, string or array is given, it must be a function of Mach
            number only.
        powerOnDrag : int, float, callable, string, array
            Rocket's drag coefficient when the motor is on. Can be given as an
            entry to the Function class. See help(Function) for more
            information. If int or float is given, it is assumed constant. If
            callable, string or array is given, it must be a function of Mach
            number only.

        Returns
        -------
        None
        """
        # Define rocket inertia attributes in SI units
        self.mass = mass
        self.inertiaI = inertiaI
        self.inertiaZ = inertiaZ
        self.centerOfMass = (
            (distanceRocketPropellant - motor.zCM) * motor.mass / (mass + motor.mass)
        )

        # Define rocket geometrical parameters in SI units
        self.radius = radius
        self.area = np.pi * self.radius**2

        # Center of mass distance to points of interest
        self.distanceRocketNozzle = distanceRocketNozzle
        self.distanceRocketPropellant = distanceRocketPropellant

        # Eccentricity data initialization
        self.cpEccentricityX = 0
        self.cpEccentricityY = 0
        self.thrustEccentricityY = 0
        self.thrustEccentricityX = 0

        # Parachute data initialization
        self.parachutes = []

        # Rail button data initialization
        self.railButtons = None

        # Aerodynamic data initialization
        self.aerodynamicSurfaces = []
        self.cpPosition = 0
        self.staticMargin = Function(
            lambda x: 0, inputs="Time (s)", outputs="Static Margin (c)"
        )

        # Define aerodynamic drag coefficients
        self.powerOffDrag = Function(
            powerOffDrag,
            "Mach Number",
            "Drag Coefficient with Power Off",
            "linear",
            "constant",
        )
        self.powerOnDrag = Function(
            powerOnDrag,
            "Mach Number",
            "Drag Coefficient with Power On",
            "linear",
            "constant",
        )

        # Define motor to be used
        self.motor = motor

        # Important dynamic inertial quantities
        self.reducedMass = None
        self.totalMass = None

        # Calculate dynamic inertial quantities
        self.evaluateReducedMass()
        self.evaluateTotalMass()
        self.thrustToWeight = self.motor.thrust / (9.80665 * self.totalMass)
        self.thrustToWeight.setInputs("Time (s)")
        self.thrustToWeight.setOutputs("Thrust/Weight")

        # Evaluate static margin (even though no aerodynamic surfaces are present yet)
        self.evaluateStaticMargin()

        return None

    def evaluateReducedMass(self):
        """Calculates and returns the rocket's total reduced mass. The
        reduced mass is defined as the product of the propellant mass
        and the mass of the rocket without propellant, divided by the
        sum of the propellant mass and the rocket mass. The function
        returns an object of the Function class and is defined as a
        function of time.

        Parameters
        ----------
        None

        Returns
        -------
        self.reducedMass : Function
            Function of time expressing the reduced mass of the rocket,
            defined as the product of the propellant mass and the mass
            of the rocket without propellant, divided by the sum of the
            propellant mass and the rocket mass.
        """
        # Make sure there is a motor associated with the rocket
        if self.motor is None:
            print("Please associate this rocket with a motor!")
            return False

        # Retrieve propellant mass as a function of time
        motorMass = self.motor.mass

        # Retrieve constant rocket mass without propellant
        mass = self.mass

        # Calculate reduced mass
        self.reducedMass = motorMass * mass / (motorMass + mass)
        self.reducedMass.setOutputs("Reduced Mass (kg)")

        # Return reduced mass
        return self.reducedMass

    def evaluateTotalMass(self):
        """Calculates and returns the rocket's total mass. The total
        mass is defined as the sum of the propellant mass and the
        rocket mass without propellant. The function returns an object
        of the Function class and is defined as a function of time.

        Parameters
        ----------
        None

        Returns
        -------
        self.totalMass : Function
            Function of time expressing the total mass of the rocket,
            defined as the sum of the propellant mass and the rocket
            mass without propellant.
        """
        # Make sure there is a motor associated with the rocket
        if self.motor is None:
            print("Please associate this rocket with a motor!")
            return False

        # Calculate total mass by summing up propellant and dry mass
        self.totalMass = self.mass + self.motor.mass
        self.totalMass.setOutputs("Total Mass (Rocket + Propellant) (kg)")

        # Return total mass
        return self.totalMass

    def evaluateStaticMargin(self):
        """Calculates and returns the rocket's static margin when
        loaded with propellant. The static margin is saved and returned
        in units of rocket diameter or calibers. This function also calculates
        the rocket center of pressure and total lift coefficients.

        Parameters
        ----------
        None

        Returns
        -------
        self.staticMargin : float
            Float value corresponding to rocket static margin when
            loaded with propellant in units of rocket diameter or
            calibers.
        """
        # Initialize total lift coefficient derivative and center of pressure
        self.totalLiftCoeffDer = 0
        self.cpPosition = 0

        # Calculate total lift coefficient derivative and center of pressure
        if len(self.aerodynamicSurfaces) > 0:
            for aerodynamicSurface in self.aerodynamicSurfaces:
                self.totalLiftCoeffDer += Function(
                    lambda alpha: aerodynamicSurface.cl(alpha, 0)
                ).differentiate(x=1e-2, dx=1e-3)
                self.cpPosition += (
                    Function(
                        lambda alpha: aerodynamicSurface.cl(alpha, 0)
                    ).differentiate(x=1e-2, dx=1e-3)
                    * aerodynamicSurface.cp[2]
                )
            self.cpPosition /= self.totalLiftCoeffDer

        # Calculate static margin
        self.staticMargin = (self.centerOfMass - self.cpPosition) / (2 * self.radius)
        self.staticMargin.setInputs("Time (s)")
        self.staticMargin.setOutputs("Static Margin (c)")
        self.staticMargin.setDiscrete(
            lower=0, upper=self.motor.burnOutTime, samples=200
        )

        # Return self
        return self

    def addTail(
        self, topRadius, bottomRadius, length, distanceToCM, radius=None, name="Tail"
    ):
        """Create a new tail or rocket diameter change, storing its
        parameters as part of the aerodynamicSurfaces list. Its
        parameters are the axial position along the rocket and its
        derivative of the coefficient of lift in respect to angle of
        attack.
        Parameters
        ----------
        topRadius : int, float
            Tail top radius in meters, considering positive direction
            from center of mass to nose cone.
        bottomRadius : int, float
            Tail bottom radius in meters, considering positive direction
            from center of mass to nose cone.
        length : int, float
            Tail length or height in meters. Must be a positive value.
        distanceToCM : int, float
            Tail position relative to rocket unloaded center of mass,
            considering positive direction from center of mass to nose
            cone. Consider the point belonging to the tail which is
            closest to the unloaded center of mass to calculate
            distance.
        Returns
        -------
        cl : Function
            Function of the angle of attack (Alpha) and the mach number
            (Mach) expressing the tail's lift coefficient. The inputs
            are the angle of attack (in radians) and the mach number.
            The output is the tail's lift coefficient. In the current
            implementation, the tail's lift coefficient does not vary
            with mach.
        self : Rocket
            Object of the Rocket class.
        """

        # Modify reference radius if not provided
        radius = self.radius if radius is None else radius

        # Create new tail as an object of the Tail class
        tail = Tail(topRadius, bottomRadius, length, distanceToCM, radius, name)

        # Add tail to aerodynamic surfaces list
        self.aerodynamicSurfaces.append(tail)

        # Refresh static margin calculation
        self.evaluateStaticMargin()

        # Return self
        return self.aerodynamicSurfaces[-1]

    def addNose(self, length, kind, distanceToCM, name="Nose Cone"):
        """Creates a nose cone, storing its parameters as part of the
        aerodynamicSurfaces list. Its parameters are the axial position
        along the rocket and its derivative of the coefficient of lift
        in respect to angle of attack.


        Parameters
        ----------
        length : int, float
            Nose cone length or height in meters. Must be a positive
            value.
        kind : string
            Nose cone type. Von Karman, conical, ogive, and lvhaack are
            supported.
        distanceToCM : int, float
            Nose cone position relative to rocket unloaded center of
            mass, considering positive direction from center of mass to
            nose cone. Consider the center point belonging to the nose
            cone base to calculate distance.
        name : string
            Nose cone name. Default is "Nose Cone".

        Returns
        -------
        cl : Function
            Function of the angle of attack (Alpha) and the mach number
            (Mach) expressing the nose cone's lift coefficient. The inputs
            are the angle of attack (in radians) and the mach number.
            The output is the nose cone's lift coefficient. In the current
            implementation, the nose cone's lift coefficient does not vary
            with mach
        self : Rocket
            Object of the Rocket class.
        """
        # Create a nose as an object of NoseCone class
        nose = NoseCone(length, kind, distanceToCM, self.radius, name)
        # Add nose to the list of aerodynamic surfaces
        self.aerodynamicSurfaces.append(nose)

        # Refresh static margin calculation
        self.evaluateStaticMargin()

        # Return self
        return self.aerodynamicSurfaces[-1]

    def addFins(self, *args, **kwargs):
        """See Rocket.addTrapezoidalFins for documentation.
        This method is set to be deprecated in version 1.0.0 and fully removed
        by version 2.0.0. Use Rocket.addTrapezoidalFins instead. It keeps the
        same arguments and signature."""
        warnings.warn(
            "This method is set to be deprecated in version 1.0.0 and fully "
            "removed by version 2.0.0. Use Rocket.addTrapezoidalFins instead",
            PendingDeprecationWarning,
        )
        return self.addTrapezoidalFins(*args, **kwargs)

    def addTrapezoidalFins(
        self,
        n,
        rootChord,
        tipChord,
        span,
        distanceToCM,
        cantAngle=0,
        sweepLength=None,
        sweepAngle=None,
        radius=None,
        airfoil=None,
        name="Fins",
    ):
        """Create a trapezoidal fin set, storing its parameters as part of the
        aerodynamicSurfaces list. Its parameters are the axial position
        along the rocket and its derivative of the coefficient of lift
        in respect to angle of attack.
        Parameters
        ----------
        n : int
            Number of fins, from 2 to infinity.
        span : int, float
            Fin span in meters.
        rootChord : int, float
            Fin root chord in meters.
        tipChord : int, float
            Fin tip chord in meters.
        distanceToCM : int, float
            Fin set position relative to rocket unloaded center of
            mass, considering positive direction from center of mass to
            nose cone. Consider the center point belonging to the top
            of the fins to calculate distance.
        cantAngle : int, float, optional
            Fins cant angle with respect to the rocket centerline. Must
            be given in degrees.
        sweepLength : int, float, optional
            Fins sweep length in meters. By sweep length, understand the axial distance
            between the fin root leading edge and the fin tip leading edge measured
            parallel to the rocket centerline. If not given, the sweep length is
            assumed to be equal the root chord minus the tip chord, in which case the
            fin is a right trapezoid with its base perpendicular to the rocket's axis.
            Cannot be used in conjunction with sweepAngle.
        sweepAngle : int, float, optional
            Fins sweep angle with respect to the rocket centerline. Must
            be given in degrees. If not given, the sweep angle is automatically
            calculated, in which case the fin is assumed to be a right trapezoid with
            its base perpendicular to the rocket's axis.
            Cannot be used in conjunction with sweepLength.
        radius : int, float, optional
            Reference radius to calculate lift coefficient. If None, which
            is default, use rocket radius. Otherwise, enter the radius
            of the rocket in the section of the fins, as this impacts
            its lift coefficient.
        airfoil : tuple, optional
            Default is null, in which case fins will be treated as flat plates.
            Otherwise, if tuple, fins will be considered as airfoils. The
            tuple's first item specifies the airfoil's lift coefficient
            by angle of attack and must be either a .csv, .txt, ndarray
            or callable. The .csv and .txt files must contain no headers
            and the first column must specify the angle of attack, while
            the second column must specify the lift coefficient. The
            ndarray should be as [(x0, y0), (x1, y1), (x2, y2), ...]
            where x0 is the angle of attack and y0 is the lift coefficient.
            If callable, it should take an angle of attack as input and
            return the lift coefficient at that angle of attack.
            The tuple's second item is the unit of the angle of attack,
            accepting either "radians" or "degrees".
        Returns
        -------
        cl : Function
            Function of the angle of attack (Alpha) and the mach number
            (Mach) expressing the fin's lift coefficient. The inputs
            are the angle of attack (in radians) and the mach number.
            The output is the fin's lift coefficient.
        self : Rocket
            Object of the Rocket class.
        """

        # Modify radius if not given, use rocket radius, otherwise use given.
        radius = radius if radius is not None else self.radius

        # Create a fin set as an object of TrapezoidalFins class
        finSet = TrapezoidalFins(
            n,
            rootChord,
            tipChord,
            span,
            distanceToCM,
            radius,
            cantAngle,
            sweepLength,
            sweepAngle,
            airfoil,
            name,
        )

        # Add fin set to the list of aerodynamic surfaces
        self.aerodynamicSurfaces.append(finSet)

        # Refresh static margin calculation
        self.evaluateStaticMargin()

        # Return the created aerodynamic surface
        return self.aerodynamicSurfaces[-1]

    def addEllipticalFins(
        self,
        n,
        rootChord,
        span,
        distanceToCM,
        cantAngle=0,
        radius=None,
        airfoil=None,
        name="Fins",
    ):
        """Create an elliptical fin set, storing its parameters as part of the
        aerodynamicSurfaces list. Its parameters are the axial position
        along the rocket and its derivative of the coefficient of lift
        in respect to angle of attack.
        Parameters
        ----------
        type: string
            Type of fin selected to the rocket. Must be either "trapezoid"
            or "elliptical".
        span : int, float
            Fin span in meters.
        rootChord : int, float
            Fin root chord in meters.
        n : int
            Number of fins, from 2 to infinity.
        distanceToCM : int, float
            Fin set position relative to rocket unloaded center of
            mass, considering positive direction from center of mass to
            nose cone. Consider the center point belonging to the top
            of the fins to calculate distance.
        cantAngle : int, float, optional
            Fins cant angle with respect to the rocket centerline. Must
            be given in degrees.
        radius : int, float, optional
            Reference radius to calculate lift coefficient. If None, which
            is default, use rocket radius. Otherwise, enter the radius
            of the rocket in the section of the fins, as this impacts
            its lift coefficient.
        airfoil : tuple, optional
            Default is null, in which case fins will be treated as flat plates.
            Otherwise, if tuple, fins will be considered as airfoils. The
            tuple's first item specifies the airfoil's lift coefficient
            by angle of attack and must be either a .csv, .txt, ndarray
            or callable. The .csv and .txt files must contain no headers
            and the first column must specify the angle of attack, while
            the second column must specify the lift coefficient. The
            ndarray should be as [(x0, y0), (x1, y1), (x2, y2), ...]
            where x0 is the angle of attack and y0 is the lift coefficient.
            If callable, it should take an angle of attack as input and
            return the lift coefficient at that angle of attack.
            The tuple's second item is the unit of the angle of attack,
            accepting either "radians" or "degrees".
        Returns
        -------
        cl : Function
            Function of the angle of attack (Alpha) and the mach number
            (Mach) expressing the fin's lift coefficient. The inputs
            are the angle of attack (in radians) and the mach number.
            The output is the fin's lift coefficient.
        self : Rocket
            Object of the Rocket class.
        """

        # Modify radius if not given, use rocket radius, otherwise use given.
        radius = radius if radius is not None else self.radius

        # Create a fin set as an object of EllipticalFins class
        finSet = EllipticalFins(
            n, rootChord, span, distanceToCM, radius, cantAngle, airfoil, name
        )

        # Add fin set to the list of aerodynamic surfaces
        self.aerodynamicSurfaces.append(finSet)

        # Refresh static margin calculation
        self.evaluateStaticMargin()

        # Return self
        return self.aerodynamicSurfaces[-1]

    def addParachute(
        self, name, CdS, trigger, samplingRate=100, lag=0, noise=(0, 0, 0)
    ):
        """Creates a new parachute, storing its parameters such as
        opening delay, drag coefficients and trigger function.

        Parameters
        ----------
        name : string
            Parachute name, such as drogue and main. Has no impact in
            simulation, as it is only used to display data in a more
            organized matter.
        CdS : float
            Drag coefficient times reference area for parachute. It is
            used to compute the drag force exerted on the parachute by
            the equation F = ((1/2)*rho*V^2)*CdS, that is, the drag
            force is the dynamic pressure computed on the parachute
            times its CdS coefficient. Has units of area and must be
            given in squared meters.
        trigger : function
            Function which defines if the parachute ejection system is
            to be triggered. It must take as input the freestream
            pressure in pascal and the state vector of the simulation,
            which is defined by [x, y, z, vx, vy, vz, e0, e1, e2, e3, wx, wy, wz].
            It will be called according to the sampling rate given next.
            It should return True if the parachute ejection system is
            to be triggered and False otherwise.
        samplingRate : float, optional
            Sampling rate in which the trigger function works. It is used to
            simulate the refresh rate of onboard sensors such as barometers.
            Default value is 100. Value must be given in hertz.
        lag : float, optional
            Time between the parachute ejection system is triggered and the
            parachute is fully opened. During this time, the simulation will
            consider the rocket as flying without a parachute. Default value
            is 0. Must be given in seconds.
        noise : tuple, list, optional
            List in the format (mean, standard deviation, time-correlation).
            The values are used to add noise to the pressure signal which is
            passed to the trigger function. Default value is (0, 0, 0). Units
            are in pascal.

        Returns
        -------
        parachute : Parachute
            Parachute  containing trigger, samplingRate, lag, CdS, noise
            and name. Furthermore, it stores cleanPressureSignal,
            noiseSignal and noisyPressureSignal which are filled in during
            Flight simulation.
        """
        # Create a parachute
        parachute = Parachute(name, CdS, trigger, samplingRate, lag, noise)

        # Add parachute to list of parachutes
        self.parachutes.append(parachute)

        # Return self
        return self.parachutes[-1]

    def setRailButtons(self, distanceToCM, angularPosition=45):
        """Adds rail buttons to the rocket, allowing for the
        calculation of forces exerted by them when the rocket is
        sliding in the launch rail. Furthermore, rail buttons are
        also needed for the simulation of the planar flight phase,
        when the rocket experiences 3 degrees of freedom motion while
        only one rail button is still in the launch rail.

        Parameters
        ----------
        distanceToCM : tuple, list, array
            Two values organized in a tuple, list or array which
            represent the distance of each of the two rail buttons
            to the center of mass of the rocket without propellant.
            If the rail button is positioned above the center of mass,
            its distance should be a positive value. If it is below,
            its distance should be a negative value. The order does
            not matter. All values should be in meters.
        angularPosition : float
            Angular position of the rail buttons in degrees measured
            as the rotation around the symmetry axis of the rocket
            relative to one of the other principal axis.
            Default value is 45 degrees, generally used in rockets with
            4 fins.

        Returns
        -------
        None
        """
        # Order distance to CM
        if distanceToCM[0] < distanceToCM[1]:
            distanceToCM.reverse()
        # Save important attributes
        self.railButtons = self.railButtonPair(distanceToCM, angularPosition)

        return None

    def addCMEccentricity(self, x, y):
        """Moves line of action of aerodynamic and thrust forces by
        equal translation amount to simulate an eccentricity in the
        position of the center of mass of the rocket relative to its
        geometrical center line. Should not be used together with
        addCPEccentricity and addThrustEccentricity.

        Parameters
        ----------
        x : float
            Distance in meters by which the CM is to be translated in
            the x direction relative to geometrical center line.
        y : float
            Distance in meters by which the CM is to be translated in
            the y direction relative to geometrical center line.

        Returns
        -------
        self : Rocket
            Object of the Rocket class.
        """
        # Move center of pressure to -x and -y
        self.cpEccentricityX = -x
        self.cpEccentricityY = -y

        # Move thrust center by -x and -y
        self.thrustEccentricityY = -x
        self.thrustEccentricityX = -y

        # Return self
        return self

    def addCPEccentricity(self, x, y):
        """Moves line of action of aerodynamic forces to simulate an
        eccentricity in the position of the center of pressure relative
        to the center of mass of the rocket.

        Parameters
        ----------
        x : float
            Distance in meters by which the CP is to be translated in
            the x direction relative to the center of mass axial line.
        y : float
            Distance in meters by which the CP is to be translated in
            the y direction relative to the center of mass axial line.

        Returns
        -------
        self : Rocket
            Object of the Rocket class.
        """
        # Move center of pressure by x and y
        self.cpEccentricityX = x
        self.cpEccentricityY = y

        # Return self
        return self

    def addThrustEccentricity(self, x, y):
        """Moves line of action of thrust forces to simulate a
        misalignment of the thrust vector and the center of mass.

        Parameters
        ----------
        x : float
            Distance in meters by which the line of action of the
            thrust force is to be translated in the x direction
            relative to the center of mass axial line.
        y : float
            Distance in meters by which the line of action of the
            thrust force is to be translated in the x direction
            relative to the center of mass axial line.

        Returns
        -------
        self : Rocket
            Object of the Rocket class.
        """
        # Move thrust line by x and y
        self.thrustEccentricityY = x
        self.thrustEccentricityX = y

        # Return self
        return self

    def info(self):
        """Prints out a summary of the data and graphs available about
        the Rocket.

        Parameters
        ----------
        None

        Return
        ------
        None
        """
        # Print inertia details
        print("Inertia Details")
        print("Rocket Dry Mass: " + str(self.mass) + " kg (No Propellant)")
        print("Rocket Total Mass: " + str(self.totalMass(0)) + " kg (With Propellant)")

        # Print rocket geometrical parameters
        print("\nGeometrical Parameters")
        print("Rocket Radius: " + str(self.radius) + " m")

        # Print rocket aerodynamics quantities
        print("\nAerodynamics Stability")
        print("Initial Static Margin: " + "{:.3f}".format(self.staticMargin(0)) + " c")
        print(
            "Final Static Margin: "
            + "{:.3f}".format(self.staticMargin(self.motor.burnOutTime))
            + " c"
        )

        # Print parachute data
        for chute in self.parachutes:
            print("\n" + chute.name.title() + " Parachute")
            print("CdS Coefficient: " + str(chute.CdS) + " m2")

        # Show plots
        print("\nAerodynamics Plots")
        self.powerOnDrag()

        # Return None
        return None

    def allInfo(self):
        """Prints out all data and graphs available about the Rocket.

        Parameters
        ----------
        None

        Return
        ------
        None
        """
        # Print inertia details
        print("Inertia Details")
        print("Rocket Mass: {:.3f} kg (No Propellant)".format(self.mass))
        print("Rocket Mass: {:.3f} kg (With Propellant)".format(self.totalMass(0)))
        print("Rocket Inertia I: {:.3f} kg*m2".format(self.inertiaI))
        print("Rocket Inertia Z: {:.3f} kg*m2".format(self.inertiaZ))

        # Print rocket geometrical parameters
        print("\nGeometrical Parameters")
        print("Rocket Maximum Radius: " + str(self.radius) + " m")
        print("Rocket Frontal Area: " + "{:.6f}".format(self.area) + " m2")
        print("\nRocket Distances")
        print(
            "Rocket Center of Mass - Nozzle Exit Distance: "
            + str(self.distanceRocketNozzle)
            + " m"
        )
        print(
            "Rocket Center of Mass - Motor reference point: "
            + str(self.distanceRocketPropellant)
            + " m"
        )
        print(
            "Rocket Center of Mass - Rocket Loaded Center of Mass: "
            + "{:.3f}".format(self.centerOfMass(0))
            + " m"
        )
        print("\nAerodynamic Components Parameters")
        print("Currently not implemented.")

        # Print rocket aerodynamics quantities
        print("\nAerodynamics Lift Coefficient Derivatives")
        for aerodynamicSurface in self.aerodynamicSurfaces:
            name = aerodynamicSurface.name
            clalpha = Function(
                lambda alpha: aerodynamicSurface.cl(alpha, 0),
            ).differentiate(x=1e-2, dx=1e-3)
            print(
                name + " Lift Coefficient Derivative: {:.3f}".format(clalpha) + "/rad"
            )

        print("\nAerodynamics Center of Pressure")
        for aerodynamicSurface in self.aerodynamicSurfaces:
            name = aerodynamicSurface.name
            cpz = aerodynamicSurface.cp[2]
            print(name + " Center of Pressure to CM: {:.3f}".format(cpz) + " m")
        print(
            "Distance - Center of Pressure to CM: "
            + "{:.3f}".format(self.cpPosition)
            + " m"
        )
        print("Initial Static Margin: " + "{:.3f}".format(self.staticMargin(0)) + " c")
        print(
            "Final Static Margin: "
            + "{:.3f}".format(self.staticMargin(self.motor.burnOutTime))
            + " c"
        )

        # Print parachute data
        for chute in self.parachutes:
            print("\n" + chute.name.title() + " Parachute")
            print("CdS Coefficient: " + str(chute.CdS) + " m2")
            if chute.trigger.__name__ == "<lambda>":
                line = getsourcelines(chute.trigger)[0][0]
                print(
                    "Ejection signal trigger: "
                    + line.split("lambda ")[1].split(",")[0].split("\n")[0]
                )
            else:
                print("Ejection signal trigger: " + chute.trigger.__name__)
            print("Ejection system refresh rate: " + str(chute.samplingRate) + " Hz.")
            print(
                "Time between ejection signal is triggered and the "
                "parachute is fully opened: " + str(chute.lag) + " s"
            )

        # Show plots
        print("\nMass Plots")
        self.totalMass()
        self.reducedMass()
        print("\nAerodynamics Plots")
        self.staticMargin()
        self.powerOnDrag()
        self.powerOffDrag()
        self.thrustToWeight.plot(lower=0, upper=self.motor.burnOutTime)

        # ax = plt.subplot(415)
        # ax.plot(  , self.rocket.motor.thrust()/(self.env.g() * self.rocket.totalMass()))
        # ax.set_xlim(0, self.rocket.motor.burnOutTime)
        # ax.set_xlabel("Time (s)")
        # ax.set_ylabel("Thrust/Weight")
        # ax.set_title("Thrust-Weight Ratio")

        # Return None
        return None

    def addFin(
        self,
        numberOfFins=4,
        cl=2 * np.pi,
        cpr=1,
        cpz=1,
        gammas=[0, 0, 0, 0],
        angularPositions=None,
    ):
        "Hey! I will document this function later"
        self.aerodynamicSurfaces = []
        pi = np.pi
        # Calculate angular positions if not given
        if angularPositions is None:
            angularPositions = np.array(range(numberOfFins)) * 2 * pi / numberOfFins
        else:
            angularPositions = np.array(angularPositions) * pi / 180
        # Convert gammas to degree
        if isinstance(gammas, (int, float)):
            gammas = [(pi / 180) * gammas for i in range(numberOfFins)]
        else:
            gammas = [(pi / 180) * gamma for gamma in gammas]
        for i in range(numberOfFins):
            # Get angular position and inclination for current fin
            angularPosition = angularPositions[i]
            gamma = gammas[i]
            # Calculate position vector
            cpx = cpr * np.cos(angularPosition)
            cpy = cpr * np.sin(angularPosition)
            positionVector = np.array([cpx, cpy, cpz])
            # Calculate chord vector
            auxVector = np.array([cpy, -cpx, 0]) / (cpr)
            chordVector = (
                np.cos(gamma) * np.array([0, 0, 1]) - np.sin(gamma) * auxVector
            )
            self.aerodynamicSurfaces.append([positionVector, chordVector])
        return None

    # Variables
    railButtonPair = namedtuple("railButtonPair", "distanceToCM angularPosition")
