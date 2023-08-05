from typing import Type
import math
from enum import Enum


class Unit(Enum):
    """
    A common parent class representing different units of measurement.

    Attributes:
        None
    """

    def __repr__(self):
        """
        Returns a string representation of the enum member.

        Returns:
            str: A string representation of the enum member.
        """
        return f'<{self.__class__.__name__}.{self.name}: {self.value}>'

    def __str__(self):
        """
        Returns a string representation of the enum member.

        Returns:
            str: A string representation of the enum member.
        """
        return self.value

    @classmethod
    def from_string(cls, s):
        """
        Returns the enum member corresponding to the given string value.

        Args:
            s (str): The string value to look up.

        Returns:
            Unit: The enum member corresponding to the given string value.

        Raises:
            ValueError: If the given string value does not correspond to any
                enum member.
        """
        for unit in cls:
            if unit.value == s:
                return unit
        raise ValueError('Unknown unit')

    @classmethod
    def get_conversion_factor(cls, from_unit, to_unit):
        """
        Returns the conversion factor between two units.

        Args:
            from_unit (Unit): The unit to convert from.
            to_unit (Unit): The unit to convert to.

        Returns:
            float: The conversion factor between the two units.

        Raises:
            KeyError: If either from_unit or to_unit is not a valid enum member.
        """
        conversion_factors = cls.conversion_factors()
        return conversion_factors[from_unit] / conversion_factors[to_unit]


class SpaceUnit(Unit):
    """
    An enum class representing different space units.

    This enum class defines the members representing different space units,
    and also overrides the conversion_factors method to provide the specific
    conversion factors for space units.

    Attributes:
        NM (str): Nanometers.
        UM (str): Micrometers.
        MM (str): Millimeters.
        CM (str): Centimeters.
        M (str): Meters.
    """
    NM = 'nm'
    UM = 'um'
    MM = 'mm'
    CM = 'cm'
    M = 'm'

    @classmethod
    def conversion_factors(cls):
        """
        Returns a dictionary containing the conversion factors for space units.

        This method returns a dictionary containing the conversion factors for
        space units. The keys are the space units themselves, and the values
        are the conversion factors from the unit to meters.

        Returns:
            dict: A dictionary containing the conversion factors for space units.
        """
        return {
            cls.NM: 1e-9,
            cls.UM: 1e-6,
            cls.MM: 1e-3,
            cls.CM: 1e-2,
            cls.M: 1.0,
        }


class TimeUnit(Unit):
    """
    An enum class representing different space units.

    This enum class defines the members representing different space units,
    and also overrides the conversion_factors method to provide the specific
    conversion factors for space units.

    Attributes:
        NS (str): Nanoseconds.
        US (str): Microseconds.
        MS (str): Milliseconds.
        S (str): Seconds.
    """
    NS = 'ns'
    US = 'us'
    MS = 'ms'
    S = 'S'

    @classmethod
    def conversion_factors(cls):
        """
        Returns a dictionary containing the conversion factors for space units.

        This method returns a dictionary containing the conversion factors for
        space units. The keys are the space units themselves, and the values
        are the conversion factors from the unit to meters.

        Returns:
            dict: A dictionary containing the conversion factors for space units.
        """
        return {
            cls.NS: 1e-9,
            cls.US: 1e-6,
            cls.MS: 1e-3,
            cls.S: 1.0,
        }


# Create an empty class to represent a quantity with no units
class NoUnit(Unit):
    """
    A class representing a unit with no units.

    This class is used to represent a unit with no units. It is used as the
    denominator unit in quantities with no denominator unit.

    Attributes:
        UNIT (str): The string representation of the unit.
    """
    UNIT = 'unit'

    @classmethod
    def conversion_factors(cls):
        """
        Returns a dictionary containing the conversion factors for space units.

        This method returns a dictionary containing a conversion factor of 1

        Returns:
            dict: A dictionary containing a conversion factor of 1
        """
        return {
            cls.UNIT: 1.0,
        }


class Quantity:
    """
    A class representing a quantity with a value, a numerator unit, and a
    denominator unit.

    Attributes:
        value (float): The value of the quantity.
        numerator_unit (Unit): The numerator unit of the quantity.
        denominator_unit (Unit): The denominator unit of the quantity.
    """

    def __init__(self, value, numerator_unit, denominator_unit=NoUnit):
        """
        Initializes a Quantity object.

        Args:
            value (float): The value of the quantity.
            numerator_unit (Unit): The numerator unit of the quantity.
            denominator_unit (Unit): The denominator unit of the quantity.
        """
        self.value = value
        self.numerator_unit = numerator_unit
        self.denominator_unit = denominator_unit

    def __repr__(self):
        """
        Returns a string representation of the quantity.

        Returns:
            str: A string representation of the quantity.
        """
        if self.denominator_unit is None:
            return f'<{self.__class__.__name__}: {self.value} {self.numerator_unit}>'
        else:
            return f'<{self.__class__.__name__}: {self.value} {self.numerator_unit}/{self.denominator_unit}>'

    def __str__(self):
        """
        Returns a string representation of the quantity.

        Returns:
            str: A string representation of the quantity.
        """
        if self.denominator_unit is None:
            return f'{self.value} {self.numerator_unit}'
        else:
            return f'{self.value} {self.numerator_unit}/{self.denominator_unit}'

    def convert_numerator(self, to_unit):
        """
        Converts the numerator unit of the quantity to the given unit.

        Args:
            to_unit (Unit): The unit to convert to.

        Returns:
            Quantity: The converted quantity.
        """
        if not isinstance(to_unit, type(self.numerator_unit)):
            raise TypeError(f'Cannot convert {self.numerator_unit} to {to_unit}')
        return Quantity(
            self.value * self.numerator_unit.get_conversion_factor(self.numerator_unit, to_unit),
            to_unit,
            self.denominator_unit
        )

    def convert_denominator(self, to_unit):
        """
        Converts the denominator unit of the quantity to the given unit.

        Args:
            to_unit (Unit): The unit to convert to.

        Returns:
            Quantity: The converted quantity.
        """
        if not isinstance(to_unit, type(self.denominator_unit)):
            raise TypeError(f'Cannot convert {self.denominator_unit} to {to_unit}')
        return Quantity(
            self.value / self.denominator_unit.get_conversion_factor(self.denominator_unit, to_unit),
            self.numerator_unit,
            to_unit
        )

    def convert(self, to_numerator_unit, to_denominator_unit=None):
        """
        Converts the numerator and denominator units of the quantity to the given units.

        Args:
            to_numerator_unit (Unit): The numerator unit to convert to.
            to_denominator_unit (Unit): The denominator unit to convert to.

        Returns:
            Quantity: The converted quantity.
        """
        if to_denominator_unit is None:
            return self.convert_numerator(to_numerator_unit)
        else:
            return self.convert_numerator(to_numerator_unit).convert_denominator(to_denominator_unit)


g_C_water = Quantity(299.792458/1.33, SpaceUnit.MM, TimeUnit.NS)


class CoordSys(Enum):
    """
    An enumeration representing different types of coordinate systems.

    Attributes:
        CART (int): The Cartesian coordinate system.
        CYL (int): The cylindrical coordinate system.
        SPH (int): The spherical coordinate system.
    """
    CART = 1
    CYL = 2
    SPH = 3

    def __repr__(self):
        return f'<{self.__class__.__name__}.{self.name}>'

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def from_string(s):
        if s == 'cartesian':
            return CoordSys.CART
        elif s == 'cylindrical':
            return CoordSys.CYL
        elif s == 'spherical':
            return CoordSys.SPH
        else:
            raise ValueError('Unknown coordinate system')

    def cartesian_to_cylindrical(self, x, y, z):
        if self == CoordSys.CART:
            r = math.sqrt(x ** 2 + y ** 2)
            phi = math.atan2(y, x)
            return r, phi, z
        else:
            raise ValueError('Unknown coordinate system')

    def cartesian_to_spherical(self, x, y, z):
        if self == CoordSys.CART:
            r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
            phi = math.atan2(y, x)
            theta = math.acos(z / r)
            return r, phi, theta
        else:
            raise ValueError('Unknown coordinate system')

    def cylindrical_to_cartesian(self, r, phi, z):
        if self == CoordSys.CYL:
            x = r * math.cos(phi)
            y = r * math.sin(phi)
            return x, y, z
        else:
            raise ValueError('Unknown coordinate system')

    def cylindrical_to_spherical(self, r, phi, z):
        if self == CoordSys.CYL:
            x, y, z = self.cylindrical_to_cartesian(r, phi, z)
            return self.cartesian_to_spherical(x, y, z)
        else:
            raise ValueError('Unknown coordinate system')

    def spherical_to_cartesian(self, r, phi, theta):
        if self == CoordSys.SPH:
            x = r * math.sin(theta) * math.cos(phi)
            y = r * math.sin(theta) * math.sin(phi)
            z = r * math.cos(theta)
            return x, y, z
        else:
            raise ValueError('Unknown coordinate system')

    def spherical_to_cylindrical(self, r, phi, theta):
        if self == CoordSys.SPH:
            x, y, z = self.spherical_to_cartesian(r, phi, theta)
            return self.cartesian_to_cylindrical(x, y, z)
        else:
            raise ValueError('Unknown coordinate system')


class Coord:
    def __init__(self, x, y, z,
                 coordsys: Type[CoordSys] = CoordSys.CART,
                 space_unit: Type[SpaceUnit] = SpaceUnit.MM):
        """
        Initializes a new Coordinate object with the specified x, y, and z (or rho, theta, and phi) values,
        coordinate system, and unit.

        Args:
            x (float): The x, rho, or R coordinate value.
            y (float): The y or phi coordinate value.
            z (float): The z or theta coordinate value.
            coordsys (CoordSys, optional): The coordinate system in which the coordz are specified.
                Defaults to CoordSys.CART.
            space_unit (Unit, optional): The unit of measurement for the coordinate values. Defaults to Unit.MM.
        """
        self.space_unit = space_unit
        self.system = coordsys
        if coordsys == CoordSys.CART:
            self.x = x
            self.y = y
            self.z = z
            self.perp = math.sqrt(x ** 2 + y ** 2)
            self.R = math.sqrt(x ** 2 + y ** 2 + z ** 2)
            self.phi = math.atan2(y, x)
            # Calculate theta considering the case where x and y are both zero
            if x == 0 and y == 0:
                self.theta = math.copysign(math.pi / 2, z)
            else:
                self.theta = math.acos(z / self.R)
        elif coordsys == CoordSys.CYL:
            self.perp = x
            self.phi = y
            self.z = z
            self.x = x * math.cos(y)
            self.y = x * math.sin(y)
            self.R = math.sqrt(x ** 2 + z ** 2)
            # Calculate theta considering the case where x and y are both zero
            if x == 0 and y == 0:
                self.theta = math.copysign(math.pi / 2, z)
            else:
                self.theta = math.acos(z / self.R)
        elif coordsys == CoordSys.SPH:
            self.R = x
            self.phi = y
            self.theta = z
            self.x = x * math.sin(z) * math.cos(y)
            self.y = x * math.sin(z) * math.sin(y)
            self.z = x * math.cos(z)
            self.perp = math.sqrt(self.x ** 2 + self.y ** 2)
        else:
            raise ValueError('Unknown coordinate system')

    def __str__(self):
        """
        Returns a string representation of the Coordinate object.
        """
        if self.system == CoordSys.CART:
            return f"({self.x} {self.space_unit.value}, {self.y} {self.space_unit.value}, {self.z} {self.space_unit.value})"
        elif self.system == CoordSys.CYL:
            return f"({self.perp} {self.space_unit.value}, {self.phi} rad, {self.z} {self.space_unit.value})"
        elif self.system == CoordSys.SPH:
            return f"({self.R} {self.space_unit.value}, {self.theta} rad, {self.phi} rad)"
        else:
            return "Unknown coordinate system"

    def __repr__(self):
        """
        Returns a string representation of the Coordinate object that can be used to recreate the object.
        """
        return f"Coordinate({self.x}, {self.y}, {self.z}, coordinate_system={self.system}, unit={self.space_unit})"

    # Convert to another unit
    def convert_unit(self, new_unit: Type[SpaceUnit]):
        conversion_factor = SpaceUnit.get_conversion_factor(self.space_unit, new_unit)

        self.x *= conversion_factor
        self.y *= conversion_factor
        self.z *= conversion_factor

        self.perp *= conversion_factor
        self.R *= conversion_factor

        self.space_unit = new_unit

    # Calculate the distance between two coordz
    def distance(self, other):
        if self.system == other.system:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
        else:
            # Convert other to this coordinate system
            other = other.convert(self.system)
            return self.distance(other)


class TimeCoord(Coord):
    def __init__(self, x, y, z, t,
                 coordsys=CoordSys.CART,
                 space_unit: Type[SpaceUnit] = SpaceUnit.MM, time_unit: Type[TimeUnit] = TimeUnit.NS):
        """
        Initializes a new TimeCoord object with the specified x, y, and z (or rho, theta, and phi) values,
        time value, coordinate system, and units.

        Args:
            x (float): The x, rho, or R coordinate value.
            y (float): The y or phi coordinate value.
            z (float): The z or theta coordinate value.
            t (float): The time coordinate value.
            coordsys (CoordSys, optional): The coordinate system in which the coordz are specified.
                Defaults to CoordSys.CART.
            space_unit (Unit, optional): The unit of measurement for the space coordinate values. Defaults to Unit.MM.
            time_unit (Unit, optional): The unit of measurement for the time coordinate value. Defaults to Unit.NS.
        """
        super().__init__(x, y, z, coordsys=coordsys, space_unit=space_unit)
        self.t = t
        self.time_unit = time_unit

    def convert_space_unit(self, new_unit):
        super().convert_unit(new_unit)

    def convert_time_unit(self, new_unit):
        conversion_factor = TimeUnit.get_conversion_factor(self.time_unit, new_unit)
        self.t *= conversion_factor
        self.time_unit = new_unit

    def __str__(self):
        """
        Returns a string representation of the TimeCoord object.
        """
        return f"{super().__str__()}, {self.t} {self.time_unit.value}"

    def __repr__(self):
        """
        Returns a string representation of the TimeCoord object that can be used to recreate the object.
        """
        return f"TimeCoord({self.x}, {self.y}, {self.z}, {self.t}, coordinate_system={self.system}, space_unit={self.space_unit}, time_unit={self.time_unit})"
